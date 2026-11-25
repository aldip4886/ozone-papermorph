"""Answer every quiz in a chapter page and list each window.onInteraction call (qid, result) the engine makes."""
import sys, asyncio
from playwright.async_api import async_playwright

URL = sys.argv[1]
FILL = sys.argv[2] if len(sys.argv) > 2 else '0'

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1600, 'height': 900})
        await pg.add_init_script("window.__ix = []; window.onInteraction = (q, e, d, l) => window.__ix.push([q, e && (e.result ?? e.r ?? JSON.stringify(e)).toString().slice(0, 40)]);")
        await pg.goto(URL); await pg.wait_for_timeout(800)
        if await pg.locator('#cover').count(): await pg.click('#cover'); await pg.wait_for_timeout(500)
        n = await pg.evaluate('BEATS.length')
        for i in range(n):
            if not await pg.evaluate(f'!!BEATS[{i}].ask && BEATS[{i}].ask !== finishCard'):
                continue
            await pg.evaluate(f'seek({i}, false)'); await pg.wait_for_timeout(200)
            if await pg.locator('#ui .quiz').count() == 0:
                await pg.evaluate(f'BEATS[{i}].ask(() => {{}})'); await pg.wait_for_timeout(200)
            for _ in range(20):
                if await pg.locator('#ui .quiz').count() == 0: break
                rows = pg.locator('#ui .quiz .row'); boxes = pg.locator('#ui .quiz input.box'); opts = pg.locator('#ui .quiz .opts > button.opt')
                if await rows.count():
                    for r in range(await rows.count()):
                        o = rows.nth(r).locator('.opts button')
                        if await o.count(): await o.first.click()
                elif await boxes.count():
                    for k in range(await boxes.count()): await boxes.nth(k).fill(FILL)
                elif await opts.count():
                    await opts.first.click()
                await pg.wait_for_timeout(150)
                for label in ['Periksa', 'Cek', 'Check']:
                    btn = pg.locator(f'#ui .quiz .btn:not([hidden]):has-text("{label}")')
                    if await btn.count(): await btn.first.click(); await pg.wait_for_timeout(150)
                # a wrong answer offers retry / "Lihat jawaban" first; reveal so the next question opens
                for _ in range(3):
                    if await pg.locator('#ui .quiz .btn:not([hidden])').filter(has_text='berikutnya').count(): break
                    show = pg.locator('#ui .quiz .btn:not([hidden])').filter(has_text='Lihat jawaban')
                    if not await show.count(): break
                    await show.first.click(); await pg.wait_for_timeout(200)
                nxt = pg.locator('#ui .quiz .btn:not([hidden])').filter(has_text='berikutnya')
                if await nxt.count(): await nxt.first.click(); await pg.wait_for_timeout(250)
                else:
                    fin = pg.locator('#ui .quiz .btn:not([hidden])').filter(has_text='Lanjutkan')
                    if await fin.count(): await fin.first.click(); await pg.wait_for_timeout(250)
                    break
        for row in await pg.evaluate('window.__ix'): print(row)
        await b.close()

asyncio.run(main())
