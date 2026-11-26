"""One self-contained HTML presentation per PDRI chapter: every scene of site/pdri-mck/chNN as a slide.

    python tools/pdri/scenes/build_deck.py N [--no-thumbs]

Writes dist/pdri/presentasi/babN-<slug>.html. The scenes are the ones build_scenes.py makes (one beat each, with its
animation and questions) but WITHOUT the voice-over: each beat runs silent on wall time, with its marks pulled together
so no step waits more than GAP s for the one before (compress()). The engine's cover, control bar and captions are
hidden. The shared parts (CSS, fonts, engine, chapter script, pictures) are stored once, and each slide's document is
put together in the browser when the slide opens. A slide plays its animation as soon as it opens. The deck adds
slide navigation (arrows, PageUp/PageDown, a presenter clicker), a sidebar of thumbnails and full screen.
Thumbnails are final-frame screenshots taken with Playwright (PW_CHANNEL=chrome on this machine).
"""
import base64, io, json, os, re, sys, pathlib, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
R = ROOT / 'site/pdri-mck'; L = R / 'lib'
N = int(sys.argv[1]); C = R / f'ch{N:02d}'
THUMBS = '--no-thumbs' not in sys.argv
OUTDIR = ROOT / 'dist/pdri/presentasi'; OUTDIR.mkdir(parents=True, exist_ok=True)

b64 = lambda p, mt: f'data:{mt};base64,' + base64.b64encode(p.read_bytes()).decode()
def css(name):
    s = (L / name).read_text(encoding='utf-8')
    s = re.sub(r'@import url\(([\w.]+)\);', lambda m: css(m.group(1)), s)
    return re.sub(r'url\("fonts/([\w-]+\.woff2)"\)', lambda m: f'url("{b64(L / "fonts" / m.group(1), "font/woff2")}")', s)
def must(s, old, new):
    assert old in s, old
    return s.replace(old, new)

CSS = css('engine.css')
eng = (L / 'engine.js').read_text(encoding='utf-8')
eng = must(eng, "document.head.append(Object.assign(document.createElement('script'), { src: new URL('volume.js', document.currentScript.src) }));", '')
# a slide lives in an about:srcdoc frame: there is no '../' to resolve
eng = must(eng, "new URL('../', location.href).pathname", "'pdri-deck'")
vol = (L / 'volume.js').read_text(encoding='utf-8')
mck = (L / 'mck.js').read_text(encoding='utf-8').replace("IMG + 'logos.png'", repr(b64(L / 'img/logos.png', 'image/png')))

# no voice: every beat is silent (wall clock); its marks keep their order, but no step waits more than GAP s for the
# one before (FIRST s for the first one), and the beat holds at most TAIL s after its last mark
GAP, FIRST, TAIL = 1.0, .6, 1.2
def compress(t):
    new, prev, at = {}, 0.0, 0.0
    for v in sorted(set(t['marks'].values())):
        at += min(v - prev, GAP if new else FIRST); new[v] = round(at, 2); prev = v
    dur = at + min(max(0.0, t['dur'] - prev), TAIL)
    return {'dur': round(max(dur, 1.0), 2), 'marks': {k: new[v] for k, v in t['marks'].items()}, 'cues': [], 'silent': True}
eng = must(eng, "if (!(k in tm.marks)) throw new Error(`${b.id}: missing mark ${k}`);",
           f"if (!(k in tm.marks)) {{ if (!tm.auto) throw new Error(`${{b.id}}: missing mark ${{k}}`); tm.marks[k] = {FIRST} + {GAP} * Object.keys(tm.marks).length; }}")
raw = (C / 'audio/id/timings.js').read_text(encoding='utf-8')
TIM = {k: compress(v) for k, v in json.loads(raw[raw.index('{'):raw.rindex('}') + 1]).items()}

html = (C / 'index.html').read_text(encoding='utf-8')
head, body = html.split('<script>\n', 1)
script = body.rsplit('</script>', 1)[0]
for im in set(re.findall(r"IMG \+ '([\w.-]+)'", script)):
    script = script.replace(f"IMG + '{im}'", repr(b64(L / 'img' / im, 'image/png' if im.endswith('png') else 'image/jpeg')))
ids = re.findall(r"^  \['([A-Za-z0-9]+)', '([^']*)'", script, re.M)
chap = re.search(r"^const CHAPTER = \{.*\};$", script, re.M)
TITLE = re.search(r"title: '([^']*)'", chap.group(0)).group(1)
script = script.replace(chap.group(0), '/*@CHAPTER@*/')
# a beat that timings.js lacks (stale timings, e.g. ch03 syarat/rina) starts with no marks: the patched engine gives each
# mark, the first time the beat's code asks for it, the next step FIRST + GAP * n (see the m() patch above)
for bid, _ in ids:
    if bid not in TIM:
        TIM[bid] = {'dur': FIRST + TAIL, 'marks': {}, 'cues': [], 'silent': True, 'auto': True}
        print(f'warning: timings.js has no beat {bid!r}; its marks are spaced {GAP} s apart in the order the code uses them', flush=True)
tim = 'window.TIMINGS = ' + json.dumps(TIM) + ';'
script = must(script, '\nmkBoot();', '\n/*@PICK@*/\nmkBoot();')

# inside every slide: the stage alone fills the frame, deck keys go to the parent, the animation starts by itself
DECK_CSS = """
html,body{background:#071A3A}
#frame{height:var(--sh,900px)!important;border-radius:0!important;box-shadow:none!important}
#bar,#caption,#soundNote,#cover,#bHome,.finwrap a.btn.quiet{display:none!important}
"""
DECK_JS = r"""
(() => {
  const SW = 1600, SH = 900, root = document.documentElement;
  const fit = () => root.style.setProperty('--k', Math.min(innerWidth / SW, innerHeight / SH));
  addEventListener('resize', fit); fit(); setTimeout(fit, 0);
  const held = () => { try { return !!(P.keys && !P.done); } catch { return false; } };
  addEventListener('keydown', e => {
    if (e.altKey || e.metaKey || e.ctrlKey) return;
    if (e.target.matches?.('input, textarea')) return;
    const k = e.key;
    let act = null;
    if (k === 'PageDown') act = ['go', 1];
    else if (k === 'PageUp') act = ['go', -1];
    else if (k === 'ArrowRight' && !held()) act = ['go', 1];
    else if (k === 'ArrowLeft' && !held()) act = ['go', -1];
    else if (/^[gGfF]$/.test(k) || k === 'Escape') act = ['key', k.toLowerCase()];
    if (!act) return;
    e.preventDefault(); e.stopImmediatePropagation();
    act[0] === 'go' ? parent.deck?.go(act[1]) : parent.deck?.key(act[1]);
  }, true);
  // start once boot() has run (fonts loaded, beat built): the cover's click is the engine's own "play"
  let n = 0;
  const t = setInterval(() => {
    const c = document.getElementById('cover'), k = document.getElementById('coverK');
    if (c && k && k.textContent) { clearInterval(t); c.click(); parent.deck?.ready(window); }
    else if (++n > 200) clearInterval(t);
  }, 30);
})();
"""

esc = lambda s: s.replace('</script', '<\\/script')
jsstr = lambda s: json.dumps(s, ensure_ascii=False).replace('</', '<\\/')

slides = []
for k, (bid, title) in enumerate(ids):
    pick = (f"{{ let s = {k}; while (s > 0 && BEATS[s].lead === false) s--; if (s < {k}) {{ const pre = BEATS.slice(s, {k}), r = BEATS[{k}].run; "
            f"BEATS[{k}].run = (m, D) => {{ pre.forEach(b => b.run(() => -60, 0)); r(m, D); }}; }} }}\nBEATS.splice(0, BEATS.length, BEATS[{k}]);")
    chapter = f"const CHAPTER = {{ number: {N}, label: '{N} · Adegan {k + 1} dari {len(ids)}', title: {json.dumps(title)}, minutes: 1, language: 'id' }};"
    slides.append({'id': bid, 'title': title, 'chapter': chapter, 'pick': pick})

def slide_doc(s):
    sc = script.replace('/*@CHAPTER@*/', s['chapter']).replace('/*@PICK@*/', s['pick'])
    return (f'<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<style>{CSS}{DECK_CSS}</style></head><body><script>{esc(eng)}</script><script>{esc(vol)}</script><script>{esc(mck)}</script>'
            f'<script>{esc(tim)}</script><script>\n{esc(sc)}</script><script>{esc(DECK_JS)}</script></body></html>')

# thumbnails: each slide's last frame
thumbs = [None] * len(slides)
if THUMBS:
    from playwright.sync_api import sync_playwright
    from PIL import Image
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='deck'))
    with sync_playwright() as p:
        br = p.chromium.launch(channel=os.environ.get('PW_CHANNEL') or None)
        pg = br.new_page(viewport={'width': 1600, 'height': 900})
        for k, s in enumerate(slides):
            f = tmp / f'{k:02d}.html'; f.write_text(slide_doc(s), encoding='utf-8')
            pg.goto(f.as_uri() + '?beat=0&t=999'); pg.wait_for_timeout(1200); pg.evaluate('document.fonts.ready')
            im = Image.open(io.BytesIO(pg.locator('#stage').screenshot())).convert('RGB'); im.thumbnail((480, 270))
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=74)
            thumbs[k] = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
            print('thumb', k + 1, s['id'], flush=True)
        br.close()

shared = {'css': CSS + DECK_CSS, 'eng': esc(eng), 'vol': esc(vol), 'mck': esc(mck), 'tim': esc(tim), 'script': esc(script), 'deck': esc(DECK_JS)}
meta = [{'id': s['id'], 'title': s['title'], 'thumb': thumbs[k]} for k, s in enumerate(slides)]
js = lambda v: json.dumps(v, ensure_ascii=False).replace('</', '<\\/')
data = ''.join([
    f"const DECK = {js({'n': N, 'title': TITLE, 'count': len(slides)})};\n",
    f'const SLIDES = {js(meta)};\n',
    'const SHARED = {' + ', '.join(f'{k}: {jsstr(v)}' for k, v in shared.items()) + '};\n',
    f"const CHAPTERS = {js([s['chapter'] for s in slides])};\n",
    f"const PICKS = {js([s['pick'] for s in slides])};\n"])

shell = (pathlib.Path(__file__).parent / 'deck_shell.html').read_text(encoding='utf-8')
fonts = '\n'.join(re.findall(r'@font-face\s*\{[^}]*\}', CSS))
page = shell.replace('@FONTS@', fonts).replace('/*@DATA@*/', data).replace('@TITLE@', f'Bab {N} · {TITLE}')
slug = re.sub(r'[^a-z0-9]+', '-', TITLE.lower()).strip('-')
out = OUTDIR / f'bab{N}-{slug}.html'
out.write_text(page, encoding='utf-8')
print(out.relative_to(ROOT), f'{len(page) / 1e6:.1f} MB', len(slides), 'slides')
