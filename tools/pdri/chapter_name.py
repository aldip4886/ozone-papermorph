"""How a PDRI lesson is named in its outputs. A numbered bab (ch01-ch08) is "Bab N"; a lesson that sets
CHAPTER.label in its index.html (KB 4 · Estafet PPN lives in ch41 with label 'KB 4') is named by that label instead.

    name   'Bab 3' | 'KB 4'           shown in titles and the scene list
    prefix 'bab3'  | 'kb4'            dist/pdri/html/<prefix>/, the PDF name
    zip    'ch03'  | 'kb4'            dist/pdri/<zip>-scorm12.zip
    title, slug                       CHAPTER.title and its slug
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def meta(n):
    html = (ROOT / f'site/pdri-mck/ch{n:02d}/index.html').read_text(encoding='utf-8')
    chap = re.search(r"^const CHAPTER = \{.*\};$", html, re.M).group(0)
    title = re.search(r"title: '([^']*)'", chap).group(1)
    label = re.search(r"label: '([^']*)'", chap)
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    if label:
        name = label.group(1); prefix = re.sub(r'[^a-z0-9]', '', name.lower())
        return {'name': name, 'prefix': prefix, 'zip': prefix, 'title': title, 'slug': slug, 'label': True}
    return {'name': f'Bab {n}', 'prefix': f'bab{n}', 'zip': f'ch{n:02d}', 'title': title, 'slug': slug, 'label': False}
