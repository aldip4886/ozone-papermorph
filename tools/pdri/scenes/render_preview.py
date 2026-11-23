"""Render pratinjau MP4 tanpa voice over dari satu bab buku PDRI (site/pdri-mck/chNN) plus PNG keadaan akhir tiap adegan.
Mesin pelajaran dibuka di browser, timeline tiap beat dijalankan dengan seek() dan evalTo(t) per frame, jadi hasilnya
deterministik dan tidak bergantung pada kecepatan komputer. Titik sinkron animasi dipadatkan seperti di presentasi v4
(jeda antar titik 0,7-1,6 detik), karena tanpa narasi tidak perlu menunggu tempo suara.
Pakai:  python tools/pdri/scenes/render_preview.py N OUTDIR [fps]
Hasil:  OUTDIR/chNN.mp4  dan  OUTDIR/png/NN-<id>.png   (butuh playwright, Edge atau Chrome, ffmpeg)"""
import sys, os, subprocess, pathlib, json
from playwright.sync_api import sync_playwright

N = int(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); FPS = int(sys.argv[3]) if len(sys.argv) > 3 else 25
ROOT = pathlib.Path(__file__).resolve().parents[3]
URL = (ROOT / f'site/pdri-mck/ch{N:02d}/index.html').as_uri()
(OUT / 'png').mkdir(parents=True, exist_ok=True)
MP4 = OUT / f'ch{N:02d}.mp4'

RESYNC = """() => {
  for (const id in TIMINGS) {
    const tm = TIMINGS[id]; tm.silent = true;
    const marks = tm.marks || {}, vals = [];
    for (const k in marks) if (typeof marks[k] === 'number' && !vals.includes(marks[k])) vals.push(marks[k]);
    vals.sort((a, b) => a - b);
    const map = {}; let at = 0.7, prev = vals[0];
    vals.forEach((t, i) => { if (i) { at += Math.min(1.6, Math.max(0.7, (t - prev) * 0.25)); prev = t; } map[t] = at; });
    for (const k in marks) if (typeof marks[k] === 'number') marks[k] = map[marks[k]];
    tm.dur = Math.max(3, (vals.length ? map[vals[vals.length - 1]] : 1) + 2.4);
  }
  window.CLIP = {};
  const css = document.createElement('style');
  css.textContent = '#bar,#cover,.sound-note,.paused-mark,.caption{display:none!important}html,body{background:#fff!important}#frame{border-radius:0!important;box-shadow:none!important}';
  document.head.append(css);
  try { hideCover(); } catch (e) {}
  return BEATS.map(b => [b.id, !!b.ask]);
}"""

with sync_playwright() as p:
    try: br = p.chromium.launch(channel='msedge')
    except Exception: br = p.chromium.launch()
    pg = br.new_page(viewport={'width': 1640, 'height': 1000})
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL); pg.wait_for_timeout(800)
    beats = pg.evaluate(RESYNC)
    pg.evaluate("document.fonts.ready")
    pg.evaluate("setPlaying(false)")
    fr = pg.query_selector('#frame')
    box = fr.bounding_box(); clip = {'x': box['x'], 'y': box['y'], 'width': 1600, 'height': 900}; print('frame', box, 'beats', len(beats))
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                           '-vf', 'scale=1600:900:flags=lanczos,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '22',
                           '-movflags', '+faststart', '-an', str(MP4)], stdin=subprocess.PIPE)
    shot = lambda: pg.screenshot(type='jpeg', quality=92, clip=clip)
    total = 0; log = []
    for i, (bid, ask) in enumerate(beats):
        pg.evaluate(f"seek({i}, false)")
        pg.wait_for_timeout(150)
        end = pg.evaluate("P.end")
        dur = min(end, 5.0) if ask else end          # kartu kuis ditampilkan sebentar saja
        n = max(1, round(dur * FPS))
        for f in range(n + 1):
            t = min(dur, f / FPS)
            pg.evaluate(f"P.t = {t}; evalTo({t})")
            ff.stdin.write(shot()); total += 1
        if ask:                                       # tahan 1 detik pada kartu soal
            last = shot()
            for _ in range(FPS): ff.stdin.write(last); total += 1
        else:
            pg.evaluate("evalTo(Infinity)")
        (OUT / 'png' / f'{i+1:02d}-{bid}.png').write_bytes(pg.screenshot(type='png', clip=clip))
        log.append((i + 1, bid, round(dur, 1), ask)); print(i + 1, bid, round(dur, 1), 'ask' if ask else '', flush=True)
    ff.stdin.close(); ff.wait(); br.close()
print('frames', total, 'detik', round(total / FPS, 1), 'errors', errs[:3])
json.dump(log, open(OUT / f'ch{N:02d}-beats.json', 'w'))
