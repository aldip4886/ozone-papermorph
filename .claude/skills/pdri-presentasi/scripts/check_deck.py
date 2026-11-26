"""Play every slide of a PDRI presentation to its end and report it; save a contact sheet of the end frames.

    python check_deck.py dist/pdri/presentasi/babN-*.html [OUTDIR]

Per slide: hash, end (s, compressed timing), state [t, done, waiting]. waiting=True means a question is open (normal for
'Cek pemahaman', 'Latihan bab', the finish card). Fails (exit 1) on any page error, console error, missing thumbnail,
a slide that never loads, or the hash not following the slide. Sheet: OUTDIR/<name>-sheet.jpg (end frame of each slide).
"""
import json, os, sys, pathlib, io
from playwright.sync_api import sync_playwright
from PIL import Image

deck = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else deck.parent / '_check'); out.mkdir(parents=True, exist_ok=True)
bad = []
with sync_playwright() as p:
    b = p.chromium.launch(channel=os.environ.get('PW_CHANNEL') or None)
    pg = b.new_page(viewport={'width': 1440, 'height': 860})
    pg.on('pageerror', lambda e: bad.append('pageerror ' + str(e)))
    pg.on('console', lambda m: bad.append('console ' + m.text) if m.type == 'error' else None)
    pg.goto(deck.as_uri()); pg.wait_for_timeout(800)
    n = pg.evaluate('SLIDES.length')
    if pg.evaluate('SLIDES.filter(s => !s.thumb).length'): bad.append('missing thumbnails')
    shots = []
    for i in range(n):
        if i: pg.evaluate('deck.go(1)')
        fr = None
        for _ in range(60):
            pg.wait_for_timeout(100)
            fr = next((f for f in pg.frames if f.url == 'about:srcdoc'), None)
            try:
                if fr and fr.evaluate(f'typeof P !== "undefined" && P.started && CHAPTER.label.includes("Adegan {i + 1} dari")'): break
            except Exception: pass
        else:
            bad.append(f'slide {i + 1} did not start'); continue
        end = fr.evaluate('P.end')
        pg.wait_for_timeout(int(end * 1000) + 600)
        st = fr.evaluate('[+P.t.toFixed(1), P.done, P.waiting]')
        h = pg.evaluate('location.hash')
        if h != f'#{i + 1}': bad.append(f'slide {i + 1}: hash {h}')
        title = pg.evaluate(f'SLIDES[{i}].title')
        print(f'{i + 1:2d} {h:4s} end {end:5.1f}  t/done/waiting {st}  {title}', flush=True)
        shots.append(Image.open(io.BytesIO(pg.locator('#screen').screenshot())).convert('RGB'))
    b.close()
if shots:
    W, H, cols = 480, 280, 4
    rows = (len(shots) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * W, rows * H), '#071A3A')
    for k, im in enumerate(shots):
        im.thumbnail((W - 8, H - 8)); sheet.paste(im, ((k % cols) * W + 4, (k // cols) * H + 4))
    f = out / (deck.stem + '-sheet.jpg'); sheet.save(f, quality=80); print('sheet', f)
print('\n'.join(bad) if bad else 'OK: no errors')
sys.exit(1 if bad else 0)
