// Membangun docs/presentasi-pdri-v2.html: halaman modul PDF layar penuh (Bab 1-3) sebagai materi utama,
// dilengkapi slide dari outline v2 untuk pembukaan, KB 4-8, dan penutup.
// Prasyarat: python tools/pdri-deck/render_pages.py ; python tools/pdri-deck/patch-v2.py
// Pakai: node tools/pdri-deck/build2.js
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..', '..');
const md = fs.readFileSync(path.join(root, 'docs', 'outline-slide-pdri-v2.md'), 'utf8');
const tpl = fs.readFileSync(path.join(__dirname, 'template-v2.html'), 'utf8');
const clean = (t) => t.replace(/\*\*/g, '').replace(/`/g, '');

// ---- outline v2
const body = md.split('## Bagian B. Rincian Slide')[1].split('### Slide Cadangan')[0];
const groups = [];
let g = null, s = null;
for (const raw of body.split(/\r?\n/)) {
  const line = raw.trimEnd();
  let m;
  if ((m = line.match(/^### (.+)$/))) { g = { name: m[1].trim(), slides: [] }; groups.push(g); continue; }
  if ((m = line.match(/^\*\*(\d+) · ([A-Z]{3}) · (.+)\*\*$/))) {
    s = { n: +m[1], type: m[2], title: clean(m[3].trim()), isi: '', sumber: '', catatan: '', layout: '', visual: '' };
    g.slides.push(s); continue;
  }
  if (s && (m = line.match(/^- (Isi|Layout|Visual|Sumber|Catatan): (.*)$/))) {
    s[{ Isi: 'isi', Layout: 'layout', Visual: 'visual', Sumber: 'sumber', Catatan: 'catatan' }[m[1]]] = clean(m[2].trim());
  }
}

// ---- modul PDF: judul adegan (dari dist/pdri/html) + narasi (dari docs/naskah-voiceover)
const BAB = {
  KB1: { n: 1, pdf: 'bab1-hari-pertama-di-pelabuhan-fullscreen.pdf' },
  KB2: { n: 2, pdf: 'bab2-dasar-negara-memungut-pajak-fullscreen.pdf' },
  KB3: { n: 3, pdf: 'bab3-pihak-dan-sistem-pemungutan-fullscreen.pdf' },
};
const pagesDir = path.join(__dirname, 'pages');
const PAGES = {};
function pdfSlides(b) {
  const dir = path.join(root, 'dist', 'pdri', 'html', 'bab' + b.n);
  const files = fs.readdirSync(dir).filter((f) => /^\d\d-/.test(f) && !f.startsWith('00-')).sort();
  const nar = fs.readFileSync(path.join(root, 'docs', 'naskah-voiceover', `bab${b.n}-naskah-voiceover.md`), 'utf8')
    .split(/\r?\n/).filter((l) => /^\|\s*\d+\s*\|/.test(l))
    .map((l) => { const c = l.split('|').slice(1, -1).map((x) => x.trim()).filter(Boolean); return c[c.length - 1]; });
  if (nar.length !== files.length) console.warn(`Peringatan: bab ${b.n} punya ${files.length} halaman tetapi ${nar.length} baris narasi`);
  return files.map((f, i) => {
    const html = fs.readFileSync(path.join(dir, f), 'utf8');
    const t = html.match(/<title>Bab \d+ .{1,3} Adegan (\d+): (.*?)<\/title>/);
    const k = `${b.n}p${String(i + 1).padStart(2, '0')}`;
    for (const pre of ['b', 't']) {
      const buf = fs.readFileSync(path.join(pagesDir, `${pre}${k}.webp`));
      PAGES[pre + k] = 'data:image/webp;base64,' + buf.toString('base64');
    }
    return {
      n: `${b.n}.${String(i + 1).padStart(2, '0')}`, type: 'PDF',
      title: t ? t[2].trim() : `Halaman ${i + 1}`, tag: `Bab ${b.n} · Adegan ${i + 1}`,
      isi: '', sumber: '', catatan: nar[i] ? 'Narasi: ' + nar[i] : '',
      img: 'b' + k, th: 't' + k, bab: b.n, pdf: '../dist/pdri/pdf/' + b.pdf,
    };
  });
}

const out = [];
for (const gr of groups) {
  const ng = { name: gr.name, slides: gr.slides };
  if (BAB[gr.name.replace(/\s+/g, '')]) {
    const b = BAB[gr.name.replace(/\s+/g, '')];
    ng.slides = gr.slides.filter((x) => x.type === 'PER').concat(pdfSlides(b)); // pembatas bab + halaman modul
  }
  out.push(ng);
}
const json = JSON.stringify({ groups: out }).replace(/</g, '\\u003c');
const pages = JSON.stringify(PAGES);
const html = tpl.replace('/*__DECK__*/', () => json).replace('/*__PAGES__*/', () => pages);
const dest = path.join(root, 'docs', 'presentasi-pdri-v2.html');
fs.writeFileSync(dest, html);
const cnt = out.reduce((a, x) => a + x.slides.length, 0);
console.log('OK', dest, cnt, 'slide dari outline/modul,', Object.keys(PAGES).length / 2, 'halaman PDF,', (html.length / 1e6).toFixed(1), 'MB');
