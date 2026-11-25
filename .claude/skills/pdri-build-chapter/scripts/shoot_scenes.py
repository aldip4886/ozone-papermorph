"""Python port of tools/pdri/scenes/shoot_scenes.js: final-state screenshot of every WORK/html/NN-*.html into WORK/png/."""
import sys, pathlib
from playwright.sync_api import sync_playwright

W = pathlib.Path(sys.argv[1]).resolve()
(W / 'png').mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(channel=__import__("os").environ.get("PW_CHANNEL") or None)
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1.5)
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    for f in sorted((W / 'html').glob('[0-9]*.html')):
        if f.name.startswith('00-'):
            continue
        errs.clear()
        pg.goto(f.as_uri() + '?beat=0&t=999')
        pg.wait_for_timeout(1500)
        pg.evaluate('document.fonts.ready')
        pg.locator('#stage').screenshot(path=str(W / 'png' / f.name.replace('.html', '.png')))
        print(f.name, ' | '.join(errs) if errs else 'ok', flush=True)
    b.close()
