#!/usr/bin/env python3
"""End-to-end check that a SCORM package reports cmi.interactions correctly, in the mock LMS, in a
headless browser -- the companion to check_scorm.py's completion/resume check.

    uv run --with playwright SKILL/assets/scorm/test/check_interactions.py dist/<book>-scorm12.zip
    uv run --with playwright SKILL/assets/scorm/test/check_interactions.py dist/<book>-scorm2004.zip

No server is needed: the check answers every request itself from the zip and mock-lms.html, exactly
like check_scorm.py. It opens the first chapter and answers every quiz question it finds, generically
(it has no knowledge of any book's actual questions or correct answers): a grouping/matching question's
rows each get their first column clicked, a fill-in/numeric row gets "0" typed into every box, and a
plain choice question gets its first option clicked. That mix of right and wrong answers is enough to
exercise both "correct" and "wrong"/"incorrect" results without the test needing to know a single
right answer.

This guards specifically against two regressions found in the field:
  - window.onInteraction never getting installed because the bridge checked for CHAPTER (set by the
    chapter's own inline script) before that script had run, instead of finishCard (set by engine.js,
    which has already run by the time the bridge loads).
  - The LMS briefly seeing "failed" (no score yet) right before "passed" (with the real score), because
    finishCard's own progress() call reported before the chapter's score had been recorded.
"""
import asyncio
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse, unquote

from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent
ORIGIN = "http://lms.papermorph.test"
ID_RE = re.compile(r"^cmi\.interactions\.\d+\.id$")


async def answer_every_quiz(frame, max_questions=60):
    """Seeks through every beat, answering whatever quiz UI appears along the way, generically."""
    n = await frame.evaluate("BEATS.length")
    for i in range(n):
        await frame.evaluate(f"seek({i}, false)")
        await frame.wait_for_timeout(150)
        if await frame.locator("#ui .quiz").count() == 0:
            has_ask = await frame.evaluate(f"!!BEATS[{i}].ask")
            if has_ask:
                await frame.evaluate(f"BEATS[{i}].ask(() => {{}})")
                await frame.wait_for_timeout(150)
        asked = 0
        while await frame.locator("#ui .quiz").count() and asked < max_questions:
            asked += 1
            rows = frame.locator("#ui .quiz .row")
            boxes = frame.locator("#ui .quiz input.box")
            opts = frame.locator("#ui .quiz .opts > button.opt")
            n_rows = await rows.count()
            if n_rows:
                for r in range(n_rows):
                    row_opts = rows.nth(r).locator(".opts button")
                    if await row_opts.count():
                        await row_opts.first.click()
            elif await boxes.count():
                for b in range(await boxes.count()):
                    await boxes.nth(b).fill("0")
            elif await opts.count():
                await opts.first.click()
            else:
                break   # an interactive type this script doesn't know how to drive (e.g. a stage-tap question)
            check_btn = frame.locator("#ui .quiz button.btn:has-text('Periksa'), #ui .quiz button.btn:has-text('Check')")
            if await check_btn.count() and await check_btn.is_visible():
                await check_btn.click()
            await frame.wait_for_timeout(150)
            go_btn = frame.locator("#ui .quiz button.btn.go")
            if await go_btn.count() and await go_btn.is_visible():
                await go_btn.click()
                await frame.wait_for_timeout(150)
            else:
                break   # still stuck (e.g. a question type this script can't drive); stop this beat's quiz
        await frame.wait_for_timeout(100)


async def main(zpath, mastery_hint=None):
    z = zipfile.ZipFile(zpath)
    names = set(z.namelist())
    version = "1.2" if "adlcp_rootv1p2" in z.read("imsmanifest.xml").decode() else "2004"
    cfg = json.loads(z.read("launch.html").decode().split("PAPERMORPH_SCORM_CONFIG = ", 1)[1].split(";\n", 1)[0])
    first = cfg["chapters"][0]["n"]
    mastery = cfg.get("mastery")
    errors, warnings = [], []

    async def answer(route):
        path = unquote(urlparse(route.request.url).path)
        if path == "/mock-lms.html":
            return await route.fulfill(path=HERE / "mock-lms.html")
        name = path.removeprefix("/pkg/")
        if path.startswith("/pkg/") and name in names:
            kind = {".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".mp3": "audio/mpeg",
                    ".json": "application/json", ".png": "image/png", ".webp": "image/webp", ".svg": "image/svg+xml"}
            return await route.fulfill(body=z.read(name), content_type=kind.get(Path(name).suffix, "application/octet-stream"))
        await route.fulfill(status=404, body="")

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(channel=__import__("os").environ.get("PW_CHANNEL") or None, args=["--autoplay-policy=no-user-gesture-required"])
        page = await browser.new_page(viewport={"width": 1600, "height": 960})
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: m.type == "error" and not m.text.startswith("Failed to load resource") and errors.append(m.text))
        page.on("console", lambda m: m.type == "warning" and "[scorm]" in m.text and warnings.append(m.text))
        await page.route(f"{ORIGIN}/**", answer)
        await page.goto(f"{ORIGIN}/mock-lms.html?pkg=pkg&v={version}&reset")

        book = lambda: page.frame_locator("#sco").frame_locator("#book")
        await book().locator(".ch").first.wait_for(state="attached")
        await book().locator("#cover .btn.go").click()
        await book().locator(f"#ch{first:02d}").click()
        lesson = None
        for _ in range(100):
            lesson = page.frame(url=lambda u: f"/ch{first:02d}/index.html" in u)
            if lesson and await lesson.evaluate("typeof P === 'object' && typeof BEATS === 'object'"):
                break
            await page.wait_for_timeout(100)
        assert lesson, "the chapter did not open"

        has_hook = await lesson.evaluate("typeof window.onInteraction === 'function'")
        assert has_hook, "REGRESSION: window.onInteraction was not installed in the chapter frame"
        print("PASS window.onInteraction is installed")

        await lesson.click("#cover")
        await lesson.wait_for_timeout(200)
        await answer_every_quiz(lesson)

        log = await page.evaluate("LOG.join('\\n')")
        cmi = await page.evaluate("CMI")

        ids = sorted(v for k, v in cmi.items() if ID_RE.match(k))
        assert ids, "REGRESSION: no cmi.interactions.*.id was ever written, even after answering every quiz question"
        print(f"PASS {len(ids)} cmi.interactions record(s) written: {ids[:6]}{' ...' if len(ids) > 6 else ''}")

        bad_ids = [i for i in ids if not re.match(r"^ch\d{2}\.[A-Za-z0-9._-]+$", i) or len(i) > 64]
        assert not bad_ids, f"REGRESSION: id(s) don't match ch<NN>.<id>[.<key>], [A-Za-z0-9._-] only, <=64 chars: {bad_ids}"
        print("PASS every interaction id matches ch<NN>.<id-soal>[.<key-baris>], [A-Za-z0-9._-], <=64 chars")

        resp_key = "learner_response" if version == "2004" else "student_response"
        numeric_ids = {k.rsplit(".", 1)[0] for k, v in cmi.items() if k.endswith(".type") and v == "numeric"}
        for base in numeric_ids:
            resp = cmi.get(f"{base}.{resp_key}", "")
            assert re.fullmatch(r"-?\d+(\.\d+)?", resp), f"REGRESSION: numeric response {resp!r} at {base} is not a plain number (thousands grouping leaked through?)"
        if numeric_ids:
            print(f"PASS {len(numeric_ids)} numeric interaction(s) carry plain, ungrouped numbers")

        sd = json.loads(cmi.get("cmi.suspend_data", "{}") or "{}")
        assert sd.get("q"), f"REGRESSION: suspend_data.q is empty even though questions were answered: {cmi.get('cmi.suspend_data')!r}"
        limit = 4096 if version == "1.2" else 64000
        assert len(cmi.get("cmi.suspend_data", "")) < limit, f"suspend_data is {len(cmi['cmi.suspend_data'])} chars, over the {limit}-char limit for SCORM {version}"
        print(f"PASS suspend_data.q holds {len(sd['q'])} question group(s), {len(cmi['cmi.suspend_data'])} chars (< {limit})")

        # Drive to the finish card and check the status-setting calls never commit a failing status once a
        # passing score is already on record (the "failed-then-passed" race).
        n = await lesson.evaluate("BEATS.length")
        await lesson.evaluate(f"seek({n - 1}, false)")
        await lesson.wait_for_timeout(200)
        if await lesson.locator("#ui .fin").count() == 0:
            has_ask = await lesson.evaluate(f"!!BEATS[{n - 1}].ask")
            if has_ask:
                await lesson.evaluate(f"BEATS[{n - 1}].ask(() => {{}})")
        await lesson.wait_for_timeout(300)

        status_key = "cmi.success_status" if version == "2004" else "cmi.core.lesson_status"
        score_key = "cmi.score.raw" if version == "2004" else "cmi.core.score.raw"
        set_re = re.compile(r'(?:LMS)?SetValue\(\["' + re.escape(status_key) + r'",\s*"(\w+)"\]\)')
        score_re = re.compile(r'(?:LMS)?SetValue\(\["' + re.escape(score_key) + r'",\s*"?(\d+)"?\]\)')
        last_score = None
        bad = []
        for line in log.splitlines():
            sm, scm = set_re.search(line), score_re.search(line)
            if scm:
                last_score = int(scm.group(1))
            if sm and sm.group(1) == "failed" and mastery is not None and last_score is not None and last_score >= mastery:
                bad.append(line)
        assert not bad, "REGRESSION: a 'failed' status was committed after a passing score was already on record:\n" + "\n".join(bad)
        print("PASS no 'failed'/'incorrect' status committed once the score already met mastery")

        refused = [l for l in log.splitlines() if "refused" in l]
        assert not refused, f"saw a '... refused' line in the SCORM call log: {refused}"
        print("PASS no SetValue calls were refused by the mock LMS")

        await browser.close()
    assert not errors, errors
    assert not warnings, f"unexpected [scorm] warnings: {warnings}"
    print("PASS no page errors or [scorm] warnings")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    asyncio.run(main(sys.argv[1]))
