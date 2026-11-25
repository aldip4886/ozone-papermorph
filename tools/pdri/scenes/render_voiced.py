"""MP4 penuh satu bab dengan suara dan subtitle, dari mesin pelajaran (site/pdri-mck/chNN) dan rekaman di audio/id.
Timeline tiap beat dijalankan dengan seek() dan evalTo(t) per frame (deterministik); suara tiap beat dipasang pada
detik mulai beat + pre. Kartu kuis ditahan EXTRA detik setelah narasinya.
Pakai:  python tools/pdri/scenes/render_voiced.py N OUT.mp4 [fps] [extra_detik_kuis]   (butuh playwright, Edge atau Chrome, ffmpeg)"""
import sys, pathlib, subprocess, json
from playwright.sync_api import sync_playwright
N = int(sys.argv[1]); MP4 = pathlib.Path(sys.argv[2]); FPS = int(sys.argv[3]) if len(sys.argv) > 3 else 25
EXTRA = float(sys.argv[4]) if len(sys.argv) > 4 else 2.5
ROOT = pathlib.Path(__file__).resolve().parents[3]
CH = ROOT / f'site/pdri-mck/ch{N:02d}'
CSS = ("#bar,#cover,.sound-note,.paused-mark{display:none!important}"
       "html,body{background:#fff!important}#frame{border-radius:0!important;box-shadow:none!important}")
with sync_playwright() as p:
    try: br = p.chromium.launch(channel='msedge')
    except Exception: br = p.chromium.launch()
    pg = br.new_page(viewport={'width': 1640, 'height': 1000})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.add_init_script("try{localStorage.setItem('captions','1')}catch(e){}")
    pg.goto(CH.joinpath('index.html').as_uri()); pg.wait_for_timeout(800)
    pg.evaluate("(css)=>{const s=document.createElement('style');s.textContent=css;document.head.append(s);captions=true;try{hideCover()}catch(e){};setPlaying(false)}", CSS)
    beats = pg.evaluate("BEATS.map(b=>[b.id,!!b.ask,b.pre||0])")
    pg.evaluate("document.fonts.ready")
    box = pg.query_selector('#frame').bounding_box()
    clip = {'x': box['x'], 'y': box['y'], 'width': 1600, 'height': 900}
    tmp = MP4.with_suffix('.video.mp4')
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                           '-vf', 'scale=1600:900:flags=lanczos,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '22',
                           '-movflags', '+faststart', '-an', str(tmp)], stdin=subprocess.PIPE)
    shot = lambda: pg.screenshot(type='jpeg', quality=92, clip=clip)
    frames = 0; starts = []
    for i, (bid, ask, pre) in enumerate(beats):
        pg.evaluate(f"seek({i}, false); P.started = true")
        pg.wait_for_timeout(150)
        end = pg.evaluate("P.end")
        n = round(end * FPS)
        starts.append(frames / FPS)
        for f in range(n + 1):
            t = min(end, f / FPS)
            pg.evaluate(f"P.t = {t}; evalTo({t}); new Promise(r => requestAnimationFrame(() => r()))")
            ff.stdin.write(shot()); frames += 1
        if ask:
            last = shot()
            for _ in range(round(EXTRA * FPS)): ff.stdin.write(last); frames += 1
        else:
            pg.evaluate("evalTo(Infinity)")
        print(i + 1, bid, round(end, 1), flush=True)
    ff.stdin.close(); ff.wait(); br.close()
# audio: tiap klip pada detik mulai beat + pre
inputs, filt = [], []
for k, ((bid, ask, pre), st) in enumerate(zip(beats, starts)):
    f = CH / f'audio/id/{bid}.mp3'
    if not f.exists(): continue
    inputs += ['-i', str(f)]
    filt.append(f'[{len(filt)+1}:a]adelay={int((st + pre) * 1000)}|{int((st + pre) * 1000)}[a{len(filt)}]')
mix = ''.join(f'[a{i}]' for i in range(len(filt))) + f'amix=inputs={len(filt)}:normalize=0[out]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(tmp), *inputs, '-filter_complex', ';'.join(filt) + ';' + mix,
                '-map', '0:v', '-map', '[out]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', str(MP4)], check=True)
tmp.unlink()
print('selesai', MP4, round(frames / FPS, 1), 'detik', 'errors', errs[:3])
