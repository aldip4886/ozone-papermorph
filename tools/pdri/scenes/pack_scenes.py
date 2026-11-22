# usage: pack_scenes.py WORKDIR N 'Judul bab' pdf-name.pdf  -> WORKDIR/<pdf>, WORKDIR/html/00-daftar-adegan.html
import pymupdf, glob, io, re, html, sys
from PIL import Image
W, N, TITLE, PDF = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
doc = pymupdf.open()
for f in sorted(glob.glob(f'{W}/png/*.png')):
    im = Image.open(f).convert('RGB'); b = io.BytesIO(); im.save(b, 'JPEG', quality=90)
    w, h = im.size; pg = doc.new_page(width=w/2.7, height=h/2.7); pg.insert_image(pg.rect, stream=b.getvalue())
doc.set_metadata({'title': f'Bab {N} · {TITLE} (PDRI)'})
cat = doc.pdf_catalog(); doc.xref_set_key(cat, 'PageMode', '/FullScreen'); doc.xref_set_key(cat, 'PageLayout', '/SinglePage')
doc.save(f'{W}/{PDF}', garbage=4, deflate=True)
rows = []
for f in sorted(glob.glob(f'{W}/html/[0-9]*.html')):
    if f.endswith('00-daftar-adegan.html'): continue
    t = re.search(r'<title>Bab \d+ · (Adegan \d+): (.*?)</title>', open(f).read()).groups()
    rows.append(f'<li><a href="{f.split("/")[-1]}"><b>{t[0]}</b> {html.escape(t[1])}</a></li>')
open(f'{W}/html/00-daftar-adegan.html', 'w').write(f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Bab {N} · Daftar Adegan</title>
<style>:root{{color-scheme:light}}body{{margin:0;background:#0A2A5C;color:#fff;font-family:Poppins,system-ui,sans-serif;padding:40px 16px}}main{{max-width:640px;margin:auto}}h1{{font-size:28px;margin:0 0 4px}}p{{color:#D5E2F5;margin:0 0 24px}}ol{{list-style:none;padding:0;margin:0}}li a{{display:block;padding:12px 16px;margin:6px 0;border-radius:10px;background:#fff;color:#0A2A5C;text-decoration:none}}li a b{{color:#B07A00;margin-right:8px}}li a:hover{{background:#F5B324}}</style></head>
<body><main><h1>Bab {N} · {html.escape(TITLE)}</h1><p>Satu file per adegan. Setiap file berdiri sendiri (suara, font, gambar sudah di dalamnya) dan tombol Lanjut membuka adegan berikutnya.</p><ol>''' + '\n'.join(rows) + '</ol></main></body></html>')
print(len(doc), 'pages,', len(rows), 'scenes')
