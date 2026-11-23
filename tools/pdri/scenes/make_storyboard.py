"""Storyboard satu bab: lembar kontak (JPG) dari PNG keadaan akhir tiap adegan dan tabel storyboard (Markdown).
Pakai:  python tools/pdri/scenes/make_storyboard.py N WORKDIR "Judul bab" slug
        WORKDIR berisi png/NN-<id>.png dan chNN-beats.json dari render_preview.py
Hasil:  books/pdri/review/chNN-mck/storyboard-adegan.jpg  dan  docs/storyboard-pdri/babN-storyboard.md"""
import sys, json, pathlib, re
from PIL import Image, ImageDraw, ImageFont

N = int(sys.argv[1]); W = pathlib.Path(sys.argv[2]); TITLE = sys.argv[3]; SLUG = sys.argv[4]
ROOT = pathlib.Path(__file__).resolve().parents[3]
beats = json.load(open(W / f'ch{N:02d}-beats.json'))                       # [no, id, detik, ask]
html = (ROOT / f'site/pdri-mck/ch{N:02d}/index.html').read_text(encoding='utf-8')
titles = dict(re.findall(r"^  \['([A-Za-z0-9]+)', '([^']*)'", html, re.M))
nar = {}
for l in (ROOT / f'docs/naskah-voiceover/bab{N}-naskah-voiceover.md').read_text(encoding='utf-8').splitlines():
    if re.match(r'^\|\s*\d+\s*\|', l):
        c = [x.strip() for x in l.split('|')[1:-1]]
        nar[int(c[0])] = dict(dur=c[2], screen=c[3], text=c[-1])

# lembar kontak: 3 kolom
cols, tw, th, pad, cap = 3, 640, 360, 16, 34
rows = (len(beats) + cols - 1) // cols
sheet = Image.new('RGB', (cols * (tw + pad) + pad, rows * (th + cap + pad) + pad), '#0A2A5C')
d = ImageDraw.Draw(sheet)
try: font = ImageFont.truetype('arial.ttf', 20)
except Exception: font = ImageFont.load_default()
for k, (no, bid, dur, ask) in enumerate(beats):
    im = Image.open(W / 'png' / f'{no:02d}-{bid}.png').convert('RGB').resize((tw, th), Image.LANCZOS)
    x = pad + (k % cols) * (tw + pad); y = pad + (k // cols) * (th + cap + pad)
    sheet.paste(im, (x, y + cap))
    d.text((x, y + 4), f'{no:02d} · {titles.get(bid, bid)}' + ('  [interaktif]' if ask else ''), fill='#F5B324', font=font)
out = ROOT / f'books/pdri/review/ch{N:02d}-mck/storyboard-adegan.jpg'
sheet.save(out, quality=88); print(out, sheet.size)

# tabel storyboard
md = [f'# Storyboard Bab {N} · {TITLE}', '',
      f'Lembar kontak: `books/pdri/review/ch{N:02d}-mck/storyboard-adegan.jpg` (keadaan akhir tiap adegan). '
      f'Pratinjau gerak tanpa suara: `dist/pdri/mp4/bab{N}-{SLUG}.mp4`. HTML per adegan: `dist/pdri/html/bab{N}/`. '
      f'Naskah dan prompt suara: `docs/naskah-voiceover/bab{N}-naskah-voiceover.md`.', '',
      '| No | Kode | Judul adegan | Jenis | Durasi pratinjau | Layar | Narasi |', '| --- | --- | --- | --- | --- | --- | --- |']
for no, bid, dur, ask in beats:
    n = nar.get(no, {})
    md.append(f"| {no} | {bid} | {titles.get(bid, bid)} | {'Interaktif (kuis)' if ask else 'Materi'} | {dur:g} dtk | {n.get('screen', '')} | {n.get('text', '')} |")
md += ['', 'Catatan: pratinjau MP4 memakai tempo animasi tanpa narasi (jeda antar langkah 0,7 sampai 1,6 detik). Adegan interaktif ditampilkan 4 sampai 5 detik sebagai kartu soal.']
dst = ROOT / 'docs/storyboard-pdri'; dst.mkdir(exist_ok=True)
(dst / f'bab{N}-storyboard.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(dst / f'bab{N}-storyboard.md')
