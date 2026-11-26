"""Placeholder timings for a chapter that has a narration but no recording yet.

    python tools/pdri/vo/silent_timings.py 41

Reads content/pdri-mck/chNN/narration.id.json (text with [[mark]]s) and writes site/pdri-mck/chNN/audio/id/timings.js
with every beat "silent": true, its marks and caption cues placed at an estimated 150 words a minute (numbers count as
the words they are read as). The engine then plays the lesson on wall time with captions. Replace each beat with real
timing once its clip is recorded (skill pdri-voiceover, align_beat.py), which drops the silent flag.
"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
N = int(sys.argv[1]); C = f'ch{N:02d}'
nar = json.loads((ROOT / f'content/pdri-mck/{C}/narration.id.json').read_text(encoding='utf-8-sig'))['beats']
out = ROOT / f'site/pdri-mck/{C}/audio/id/timings.js'
old = {}
if out.exists():
    t = out.read_text(encoding='utf-8'); old = json.loads(t[t.index('{'):t.rindex('}') + 1])
WPS = 150 / 60

def spoken(w):  # rough count of the words a token is read as
    d = re.sub(r'\D', '', w)
    return 1 if not d else max(1, min(8, len(d) // 2 + 1))

res = {}
for bid, text in nar.items():
    if bid in old and not old[bid].get('silent'):
        res[bid] = old[bid]; continue          # keep a beat that already has real, aligned timing
    t, marks, words, pend = 0.15, {}, [], None
    for m in re.finditer(r'\[\[(\w+)\]\]|(\S+)', text):
        if m.group(1): pend = m.group(1); continue
        w = m.group(2)
        if pend: marks[pend] = round(t, 2); pend = None
        words.append((t, w))
        t += spoken(w) / WPS
        if w.endswith(('.', '?', '!')): t += .45
        elif w.endswith((',', ':', ';')): t += .2
    cues, cur, st = [], [], None
    for s, w in words:
        if not cur: st = s
        cur.append(w)
        if w.endswith(('.', '?', '!')) or (len(' '.join(cur)) > 70 and w.endswith((',', ':'))):
            cues.append([round(max(.05, st - .05), 2), ' '.join(cur)]); cur = []
    if cur: cues.append([round(max(.05, st - .05), 2), ' '.join(cur)])
    res[bid] = {'dur': round(t + .4, 2), 'marks': marks, 'cues': cues, 'silent': True}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text('window.TIMINGS = ' + json.dumps(res, ensure_ascii=False, indent=1) + ';\n', encoding='utf-8')
print(out, {k: v['dur'] for k, v in res.items()}, 'total', round(sum(v['dur'] for v in res.values())), 's')
