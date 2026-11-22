import base64, re, json, sys, pathlib
R = pathlib.Path(__file__).resolve().parents[3]/'site/pdri-mck'; L = R/'lib'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1; C = R/f'ch{N:02d}'
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
b64 = lambda p, mt: f'data:{mt};base64,' + base64.b64encode(p.read_bytes()).decode()
def css(name):
    s = (L/name).read_text()
    s = re.sub(r'@import url\(([\w.]+)\);', lambda m: css(m.group(1)), s)
    return re.sub(r'url\("fonts/([\w-]+\.woff2)"\)', lambda m: f'url("{b64(L/"fonts"/m.group(1), "font/woff2")}")', s)
CSS = css('engine.css')
eng = (L/'engine.js').read_text()
old = "const src = `audio/${CHAPTER.language || 'en'}/${BEATS[i].id}.mp3?v=${TIMINGS[BEATS[i].id]?.dur ?? ''}`;"
assert old in eng; eng = eng.replace(old, "const src = window.CLIP?.[BEATS[i].id] ?? " + old[12:])
vline = "document.head.append(Object.assign(document.createElement('script'), { src: new URL('volume.js', document.currentScript.src) }));"
assert vline in eng; eng = eng.replace(vline, '')
vol = (L/'volume.js').read_text()
mck = (L/'mck.js').read_text().replace("IMG + 'logos.png'", repr(b64(L/'img/logos.png', 'image/png')))
tim = (C/'audio/id/timings.js').read_text()
html = (C/'index.html').read_text()
head, body = html.split('<script>\n', 1)
script = body.rsplit('</script>', 1)[0]
for im in set(re.findall(r"IMG \+ '([\w.-]+)'", script)):
    script = script.replace(f"IMG + '{im}'", repr(b64(L/'img'/im, 'image/png' if im.endswith('png') else 'image/jpeg')))
ids = re.findall(r"^  \['([a-z0-9]+)', '([^']*)'", script, re.M)
oldc = re.search(r"^const CHAPTER = \{.*\};$", script, re.M).group(0)
esc = lambda s: s.replace('</script', '<\\/script')
names = [f'{k+1:02d}-{bid}.html' for k, (bid, _) in enumerate(ids)]
for k, (bid, title) in enumerate(ids):
    nxt = f", next: '{names[k+1]}'" if k + 1 < len(ids) else ''
    sc = script.replace(oldc, f"const CHAPTER = {{ number: {N}, label: '{N} · Adegan {k+1} dari {len(ids)}', title: {json.dumps(title)}, minutes: 1, language: 'id'{nxt} }};")
    sc = sc.replace('\nmkBoot();', f"\n{{ let s = {k}; while (s > 0 && BEATS[s].lead === false) s--; if (s < {k}) {{ const pre = BEATS.slice(s, {k}), r = BEATS[{k}].run; BEATS[{k}].run = (m, D) => {{ pre.forEach(b => b.run(() => -60, 0)); r(m, D); }}; }} }}\nBEATS.splice(0, BEATS.length, BEATS[{k}]);\nmkBoot();")
    clip = C/f'audio/id/{bid}.mp3'
    pre = f"window.CLIP = {{ {json.dumps(bid)}: '{b64(clip, 'audio/mpeg')}' }};" if clip.exists() else ''
    page = f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bab {N} · Adegan {k+1}: {title}</title>
<style>{CSS}</style>
</head>
<body>
<script>{esc(eng)}</script>
<script>{esc(vol)}</script>
<script>{esc(mck)}</script>
<script>{esc(tim)}\n{pre}</script>
<script>
{esc(sc)}</script>
</body>
</html>
'''
    (OUT/names[k]).write_text(page)
    print(names[k], len(page)//1024, 'KB', title)
