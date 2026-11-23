// Membangun docs/presentasi-pdri.html dari docs/outline-slide-pdri-v2.md + template.html
// Pakai: node tools/pdri-deck/build.js
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..', '..');
const md = fs.readFileSync(path.join(root, 'docs', 'outline-slide-pdri-v2.md'), 'utf8');
const tpl = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8');

const body = md.split('## Bagian B. Rincian Slide')[1].split('### Slide Cadangan')[0];
const lines = body.split(/\r?\n/);
const groups = [];
let g = null, s = null;
for (const raw of lines) {
  const line = raw.trimEnd();
  let m;
  if ((m = line.match(/^### (.+)$/))) {
    g = { name: m[1].trim(), slides: [] };
    groups.push(g);
    continue;
  }
  if ((m = line.match(/^\*\*(\d+) · ([A-Z]{3}) · (.+)\*\*$/))) {
    s = { n: +m[1], type: m[2], title: m[3].trim(), isi: '', sumber: '', catatan: '', layout: '', visual: '' };
    g.slides.push(s);
    continue;
  }
  if (s && (m = line.match(/^- (Isi|Layout|Visual|Sumber|Catatan): (.*)$/))) {
    s[{ Isi: 'isi', Layout: 'layout', Visual: 'visual', Sumber: 'sumber', Catatan: 'catatan' }[m[1]]] = m[2].trim();
  }
}
// bersihkan markup markdown ringan
const clean = (t) => t.replace(/\*\*/g, '').replace(/`/g, '');
groups.forEach((gr) => gr.slides.forEach((x) => { x.title = clean(x.title); x.isi = clean(x.isi); x.catatan = clean(x.catatan); x.sumber = clean(x.sumber); }));

const deck = { groups: groups.map((gr) => ({ name: gr.name, slides: gr.slides })) };
const json = JSON.stringify(deck).replace(/</g, '\\u003c');
const out = tpl.replace('/*__DECK__*/', json);
const dest = path.join(root, 'docs', 'presentasi-pdri.html');
fs.writeFileSync(dest, out);
console.log('OK', dest, groups.reduce((a, b) => a + b.slides.length, 0), 'slide dari outline');
