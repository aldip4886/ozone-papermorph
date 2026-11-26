"""Build every deliverable for one PDRI chapter and verify it: SCORM 1.2 + 2004 (with cmi.interactions),
standalone HTML per scene, and the fullscreen PDF.

    python .claude/skills/pdri-build-chapter/scripts/build_outputs.py N [--only scorm,scenes] [--mastery 70]

Run from the repo root. Needs: playwright (Python), uv (for pymupdf), ffmpeg, and the local Papermorph clone at
Papermorph/.claude/skills/papermorph (its scorm.py + scorm-bridge.js carry the interaction tracking).
Exits non-zero on the first failed step or check.
"""
import argparse, os, re, shutil, subprocess, sys, pathlib, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
PM = ROOT / 'Papermorph/.claude/skills/papermorph'
ENV = dict(os.environ, PYTHONUTF8='1')   # project scripts read/write files without an explicit encoding
sys.path.insert(0, str(ROOT / 'tools/pdri'))
from chapter_name import meta           # 'Bab N', or the lesson's CHAPTER.label (KB 4 in ch41)


def run(*cmd, check_out=None, env=None):
    print('$', ' '.join(str(c) for c in cmd), flush=True)
    r = subprocess.run([str(c) for c in cmd], cwd=ROOT, env=dict(ENV, **(env or {})), capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(l for l in out.splitlines() if 'LF will be replaced' not in l and 'hardlink' not in l.lower())[-3000:])
    if r.returncode != 0:
        sys.exit(f'FAILED ({r.returncode}): {cmd[1] if len(cmd) > 1 else cmd[0]}')
    if check_out and re.search(check_out, out):
        sys.exit(f'FAILED check: output matched {check_out!r}')
    return out


def scorm(n, mastery, skip_cover=False):
    if not (PM / 'scripts/scorm.py').exists():
        sys.exit(f'Papermorph skill not found at {PM}')
    stage = ROOT / f'dist/pdri/stage/ch{n:02d}'
    run(sys.executable, 'tools/pdri/scorm/stage_chapter.py', 'site/pdri-mck', n, stage)
    me = meta(n)
    title = f"PDRI: Pajak dalam Rangka Impor ({me['name'] + ': ' + me['title'] if me['label'] else me['name']})"
    zips = []
    for v in ('1.2', '2004'):
        run(sys.executable, PM / 'scripts/scorm.py', stage, '--version', v, '--mastery', mastery,
            '--title', title, '--out', 'dist/pdri')
        made = ROOT / f'dist/pdri/ch{n:02d}-scorm{v.replace(".", "")}.zip'
        z = made.with_name(f"{me['zip']}-scorm{v.replace('.', '')}.zip")
        if z != made: shutil.move(made, z)
        zips.append(z)
    if skip_cover:   # open straight on the lesson (skill pdri-scorm-skip-cover)
        run(sys.executable, ROOT / '.claude/skills/pdri-scorm-skip-cover/scripts/skip_cover.py', *zips)
    env = {'DIRECT': '1'} if skip_cover else {}
    for z in zips:
        run(sys.executable, PM / 'assets/scorm/test/check_scorm.py', z, check_out=r'^FAIL|\nFAIL', env=env)
        run(sys.executable, PM / 'assets/scorm/test/check_interactions.py', z, check_out=r'^FAIL|\nFAIL', env=env)


def scenes(n):
    me = meta(n); title, slug = me['title'], me['slug']
    work = pathlib.Path(tempfile.mkdtemp(prefix=f'pdri-bab{n}-'))
    run(sys.executable, 'tools/pdri/scenes/build_scenes.py', work / 'html', n)
    out = run(sys.executable, HERE / 'shoot_scenes.py', work)
    bad = [l for l in out.splitlines() if l.endswith('.html') is False and '.html ' in l and not l.endswith(' ok')]
    if bad:
        sys.exit('Console/page errors while shooting scenes:\n' + '\n'.join(bad))
    pdf = f"{me['prefix']}-{slug}-fullscreen.pdf"
    run('uv', 'run', '--with', 'pymupdf', '--with', 'pillow', 'python', 'tools/pdri/scenes/pack_scenes.py', work, n, title, pdf)
    dst = ROOT / f"dist/pdri/html/{me['prefix']}"
    dst.mkdir(parents=True, exist_ok=True)
    for f in dst.glob('*.html'):
        f.unlink()                       # scene numbering shifts when beats are added; drop stale files
    for f in (work / 'html').glob('*.html'):
        shutil.copy2(f, dst / f.name)
    (ROOT / 'dist/pdri/pdf').mkdir(parents=True, exist_ok=True)
    shutil.copy2(work / pdf, ROOT / 'dist/pdri/pdf' / pdf)
    print(f'scene screenshots kept in {work / "png"} (check them visually)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter', type=int)
    ap.add_argument('--only', default='scorm,scenes')
    ap.add_argument('--mastery', default='70')
    ap.add_argument('--skip-cover', action='store_true', help='make the zips open straight on the lesson (pdri-scorm-skip-cover)')
    a = ap.parse_args()
    steps = a.only.split(',')
    if 'scorm' in steps: scorm(a.chapter, a.mastery, a.skip_cover)
    if 'scenes' in steps: scenes(a.chapter)
    print('\nDONE chapter', a.chapter)


if __name__ == '__main__':
    main()
