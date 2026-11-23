"""Naskah bab tanpa rekaman -> narration.id.json (dengan penanda [[nama]]) dan audio/id/timings.js (silent).
Baca teks per adegan dari docs/naskah-voiceover/babN-naskah-voiceover.md dan letak penanda dari
content/pdri-mck/chNN/marks.json ({adegan: [[nama, "awal kalimat"], ...]}). Waktu diperkirakan (140 kata per menit)
karena belum ada rekaman; animasi tetap disinkronkan dari penanda ini dan dipadatkan saat dipakai tanpa suara.
Pakai: python tools/pdri/vo/make_timings.py N"""
import sys, re, json, pathlib
N = int(sys.argv[1]); ROOT = pathlib.Path(__file__).resolve().parents[3]
nar = {}
for l in (ROOT / f'docs/naskah-voiceover/bab{N}-naskah-voiceover.md').read_text(encoding='utf-8').splitlines():
    if re.match(r'^\|\s*\d+\s*\|', l):
        c = [x.strip() for x in l.split('|')[1:-1]]
        nar[c[1].strip('`')] = c[-1]
marks = json.loads((ROOT / f'content/pdri-mck/ch{N:02d}/marks.json').read_text(encoding='utf-8'))
WPS = 140 / 60
def clock(text, wanted):
    """waktu mulai tiap kata; penanda diletakkan pada kata pertama potongan teks yang diminta"""
    words = text.split(); t = 0.1; times = []
    for w in words:
        times.append(t); t += 1 / WPS * (0.8 + 0.06 * len(w) / 2)
        if w.endswith(('.', '?', '!')): t += 0.45
        elif w.endswith((',', ':', ';')): t += 0.2
    return times, t
beats, tims = {}, {}
for bid, text in nar.items():
    times, end = clock(text, None)
    pos = {}; ins = text
    for name, snip in marks.get(bid, []):
        i = text.find(snip)
        assert i >= 0, f'{bid}: "{snip}" tidak ada di naskah'
        pos[name] = i
    for name, i in sorted(pos.items(), key=lambda kv: -kv[1]):
        ins = ins[:i] + f'[[{name}]]' + ins[i:]
    beats[bid] = ins
    mk = {}
    for name, i in pos.items():
        mk[name] = round(times[len(text[:i].split()) if text[:i].endswith(' ') or i == 0 else len(text[:i].split()) - 1], 3)
    sents = re.split(r'(?<=[.?!])\s+', text); k = 0; cues = []
    for s in sents:
        cues.append([round(times[min(k, len(times) - 1)], 3), s]); k += len(s.split())
    tims[bid] = {'dur': round(end + 0.4, 3), 'marks': dict(sorted(mk.items(), key=lambda kv: kv[1])), 'cues': cues, 'silent': True}
cdir = ROOT / f'content/pdri-mck/ch{N:02d}'
(cdir / 'narration.id.json').write_text(json.dumps({'voice': None, 'note': 'Belum direkam. Naskah dari docs/naskah-voiceover; waktu diperkirakan 140 kata per menit.', 'beats': beats}, ensure_ascii=False, indent=1), encoding='utf-8')
adir = ROOT / f'site/pdri-mck/ch{N:02d}/audio/id'; adir.mkdir(parents=True, exist_ok=True)
(adir / 'timings.js').write_text('window.TIMINGS = ' + json.dumps(tims, ensure_ascii=False, indent=1) + ';\n', encoding='utf-8')
print(N, len(tims), 'adegan', {k: len(v['marks']) for k, v in tims.items()})
