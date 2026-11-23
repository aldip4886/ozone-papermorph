# Merender halaman modul PDF layar penuh (dist/pdri/pdf) menjadi WebP + thumbnail
# Pakai: python tools/pdri-deck/render_pages.py
import fitz, glob, os, io
from PIL import Image
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
out = os.path.join(os.path.dirname(__file__), 'pages')
os.makedirs(out, exist_ok=True)
for f in sorted(glob.glob(os.path.join(root, 'dist', 'pdri', 'pdf', 'bab*-fullscreen.pdf'))):
    b = int(os.path.basename(f)[3])
    d = fitz.open(f)
    for i, pg in enumerate(d):
        pix = pg.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))  # 1440 x 811
        im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        im.save(os.path.join(out, f'b{b}p{i+1:02d}.webp'), 'WEBP', quality=80, method=6)
        th = im.resize((240, round(240 * im.height / im.width)), Image.LANCZOS)
        th.save(os.path.join(out, f't{b}p{i+1:02d}.webp'), 'WEBP', quality=60, method=6)
    print('bab', b, len(d), 'halaman')
