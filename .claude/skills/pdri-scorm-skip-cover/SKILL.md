---
name: pdri-scorm-skip-cover
description: Make a PDRI single-chapter SCORM zip (dist/pdri/chNN-scorm12.zip / -scorm2004.zip) open straight on the lesson, without the title cover ("Buka Buku") and the chapter-picking screen, then verify it. Use when the user asks to remove/skip/hide the cover or chapter-selection screen of the SCORM packages, or after rebuilding a chapter's zip when the cover must stay removed. NOT part of build_outputs.py: run it only on request.
---

# Skip the cover and chapter list in a PDRI SCORM zip

`build_outputs.py` (skill `pdri-build-chapter`) makes zips that open on the book cover, then the chapter list, then the
lesson. This skill patches finished zips so the LMS opens the lesson directly. It is a separate, on-request step:
**a rebuild recreates the cover, so run this again after every rebuild** of a zip you want without it.

## 1. Patch (in place, idempotent)

Run from the repo root, `PYTHONUTF8=1`:
```
python .claude/skills/pdri-scorm-skip-cover/scripts/skip_cover.py dist/pdri/ch01-scorm12.zip dist/pdri/ch01-scorm2004.zip
```
Several zips per call are fine. It refuses a zip with more than one chapter. Two edits:
- `scorm-host.js`: `start()` loads `book/chNN/index.html` (NN = the package's only chapter) instead of `book/index.html`.
- `book/chNN/index.html`: a `<style id="skip-cover">` hides the lesson's "Semua bab" icon (`#bHome`) and finish-card link
  (`.finwrap a.btn.quiet`), which pointed back at the cover. `imsmanifest.xml`, `launch.html` and every other file are
  untouched; `book/index.html` stays in the zip, unused and unreachable.

Tracking is unaffected: scoring, `cmi.interactions`, completion and resume live in `scorm-host.js` and the lesson page.
Audio still starts from the lesson's own "Mulai pelajaran" button or Space (that click is the autoplay gesture).

## 2. Verify

The Papermorph checks click through the cover by default; `DIRECT=1` makes them open the lesson directly
(resume is checked as "the lesson sees its saved progress"). Chromium headless may crash on this machine: set
`PW_CHANNEL=chrome` (see `pdri-build-chapter`).
```
export PYTHONUTF8=1 PW_CHANNEL=chrome
T=Papermorph/.claude/skills/papermorph/assets/scorm/test
DIRECT=1 python $T/check_scorm.py dist/pdri/ch01-scorm12.zip          # 5 PASS lines
DIRECT=1 python $T/check_interactions.py dist/pdri/ch01-scorm12.zip   # onInteraction, records, ids, no refused SetValue
```
Repeat for `-scorm2004.zip`. Optionally unzip, open `launch.html` in Chrome and look at the first screen (should be the
lesson cover) and the finish card (only "Tonton lagi").

## 3. Editing a zip by hand

Possible but fragile: scene text and quiz are JS strings in `book/chNN/index.html`; subtitles and animation timing follow the
audio in `book/chNN/audio/id/timings.js`, so changing narration needs the timings updated. After editing, re-zip with
`imsmanifest.xml` at the **root** of the archive (zip from inside the folder; not a wrapper folder). No manifest change is
needed while no file is added or removed. Safer: edit `site/pdri-mck/chNN/` and rebuild with `pdri-build-chapter`, then re-run
this skill.
