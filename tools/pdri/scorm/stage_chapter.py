#!/usr/bin/env python3
"""Stage a single PDRI chapter as its own standalone Papermorph book, so the Skill's scripts/scorm.py
(which packages a whole site/<book>/ folder) can build a SCORM zip for just that one chapter.

Copies site/pdri-mck/ into a scratch folder, keeps only lib/, unit-art.js and the target ch0N/ folder,
deletes every other chapter, and rewrites the cover's Contents.book() call to list just that chapter
(so the cover's table of contents never links to a chapter the package doesn't contain).

    python3 tools/pdri/scorm/stage_chapter.py site/pdri-mck 1 dist/pdri/stage/ch01

The site folder itself is never modified.
"""
import os
import re
import shutil
import stat
import sys
from pathlib import Path


def _rm_readonly(func, path, exc_info):
    # Windows (and OneDrive-synced folders especially) sometimes copies files as read-only.
    os.chmod(path, stat.S_IWRITE)
    func(path)


def _rmtree(path):
    # shutil.rmtree's `onexc` exists only from Python 3.12; older versions take `onerror` (same callback shape here).
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=_rm_readonly)
    else:
        shutil.rmtree(path, onerror=_rm_readonly)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    site = Path(sys.argv[1]).resolve()
    n = int(sys.argv[2])
    out = Path(sys.argv[3]).resolve()

    chdir = f'ch{n:02d}'
    page = site / chdir / 'index.html'
    if not page.is_file():
        sys.exit(f'{page}: not found')
    html = page.read_text(encoding='utf-8')
    m = re.search(r'const CHAPTER\s*=\s*\{[^}]*?title:\s*(["\'])(.*?)(?<!\\)\1[^}]*?minutes:\s*(\d+)', html)
    if not m:
        m2 = re.search(r'const CHAPTER\s*=\s*\{[^}]*?minutes:\s*(\d+)[^}]*?title:\s*(["\'])(.*?)(?<!\\)\2', html)
        if not m2:
            sys.exit(f'{page}: no CHAPTER constant with title and minutes')
        title, minutes = m2.group(3), int(m2.group(1))
    else:
        title, minutes = m.group(2), int(m.group(3))
    title = title.replace("\\'", "'").replace('\\"', '"')

    if out.exists():
        _rmtree(out)
    shutil.copytree(site, out)

    for d in sorted(out.glob('ch[0-9][0-9]')):
        if d.name != chdir:
            _rmtree(d)

    cover = out / 'index.html'
    cover_html = cover.read_text(encoding='utf-8')
    call = re.search(r'Contents\.book\(\{.*?\n\}\);', cover_html, re.S)
    if not call:
        sys.exit(f'{cover}: no Contents.book({{...}}) call found')
    js_title = title.replace('\\', '\\\\').replace("'", "\\'")
    new_call = (
        "Contents.book({\n"
        f"  start: {{ unit: 1, chapter: {n} }},\n"
        "  units: [   // trimmed to this chapter alone by tools/pdri/scorm/stage_chapter.py\n"
        f"    ['Bab {n}', [['{js_title}', {minutes}]]],\n"
        "  ],\n"
        "  hues: ['#F5B324', '#3A9BE1'],\n"
        "});"
    )
    cover_html = cover_html[:call.start()] + new_call + cover_html[call.end():]
    cover.write_text(cover_html, encoding='utf-8')

    print(out)


if __name__ == '__main__':
    main()
