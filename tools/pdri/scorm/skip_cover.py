#!/usr/bin/env python3
"""Patch a single-chapter PDRI SCORM zip so it opens straight on the lesson: no title cover ("Buka Buku") and no
chapter-picking screen. The zip is rewritten in place (imsmanifest.xml, launch.html and every other file are untouched).

    python tools/pdri/scorm/skip_cover.py dist/pdri/ch01-scorm12.zip dist/pdri/ch01-scorm2004.zip

Two edits, both idempotent:
  scorm-host.js          start() loads book/chNN/index.html instead of book/index.html (NN = the package's only chapter)
  book/chNN/index.html   a <style> hides the chapter's "All chapters" icon and finish-card link, which pointed at the cover
book/index.html (cover + contents) stays in the zip, unused and unreachable.
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

HOST_OLD = "frame.src = 'book/index.html';"
HOST_NEW = "frame.src = 'book/ch' + String(CFG.chapters[0].n).padStart(2, '0') + '/index.html';   // skip-cover: single chapter, no cover or contents"
STYLE = '<style id="skip-cover">#bHome{display:none!important}.finwrap a.btn.quiet{display:none!important}</style>'


def patch(path: Path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    chapters = sorted(n for n in names if re.fullmatch(r'book/ch\d\d/index\.html', n))
    if len(chapters) != 1:
        sys.exit(f'{path}: expected exactly one chapter, found {chapters}')
    chap = chapters[0]
    out = []
    for info, data in items:
        if info.filename == 'scorm-host.js':
            s = data.decode('utf-8')
            if HOST_OLD in s:
                s = s.replace(HOST_OLD, HOST_NEW)
            elif HOST_NEW not in s:
                sys.exit(f'{path}: scorm-host.js start() not recognised')
            data = s.encode('utf-8')
        elif info.filename == chap:
            s = data.decode('utf-8')
            if 'id="skip-cover"' not in s:
                s = s.replace('</head>', STYLE + '\n</head>', 1)
            data = s.encode('utf-8')
        out.append((info, data))
    tmp = Path(tempfile.mkdtemp()) / path.name
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as z:
        for info, data in out:   # imsmanifest.xml stays first
            z.writestr(info.filename, data)
    shutil.move(str(tmp), path)
    print(f'{path}: opens on {chap}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        patch(Path(p))
