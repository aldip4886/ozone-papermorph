// Membangun versi 3: shell presentasi (docs/presentasi-pdri-v3.html) yang memuat adegan modul HTML
// (dist/pdri/html/babN/*.html) sebagai iframe. Adegan disalin ke docs/presentasi-pdri-v3-scenes/ dengan patch kecil
// agar tombol Lanjut/Beranda dan penanda selesai tersambung ke shell. File asli di dist tidak diubah.
// Prasyarat: python tools/pdri-deck/patch-motion.py ; python tools/pdri-deck/patch-v3.py
// Pakai: node tools/pdri-deck/build3.js
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..', '..');
const md = fs.readFileSync(path.join(root, 'docs', 'outline-slide-pdri-v2.md'), 'utf8');
const tpl = fs.readFileSync(path.join(__dirname, 'template-v3.html'), 'utf8');
const clean = (t) => t.replace(/\*\*/g, '').replace(/`/g, '');
// Variabel lingkungan (opsional, dipakai build4 untuk Bab 1-5 tanpa mengubah v3): PDRI_MAXBAB, PDRI_TAG, PDRI_OUTDOCS
const MAXBAB = +process.env.PDRI_MAXBAB || 3, TAG = process.env.PDRI_TAG || 'v3';
const OUTDOCS = process.env.PDRI_OUTDOCS ? path.resolve(process.env.PDRI_OUTDOCS) : path.join(root, 'docs');
const SCENES_DIR = `presentasi-pdri-${TAG}-scenes`;
const outScenes = path.join(OUTDOCS, SCENES_DIR);
fs.rmSync(outScenes, { recursive: true, force: true });

// ---- slide dari outline v2 (sampul, penutup, judul pembatas bab)
const body = md.split('## Bagian B. Rincian Slide')[1].split('### Slide Cadangan')[0];
const byN = {};
let s = null, m;
for (const raw of body.split(/\r?\n/)) {
  const line = raw.trimEnd();
  if ((m = line.match(/^\*\*(\d+) · ([A-Z]{3}) · (.+)\*\*$/))) {
    s = { n: +m[1], type: m[2], title: clean(m[3].trim()), isi: '', sumber: '', catatan: '', layout: '', visual: '' };
    byN[s.n] = s; continue;
  }
  if (s && (m = line.match(/^- (Isi|Layout|Visual|Sumber|Catatan): (.*)$/))) {
    s[{ Isi: 'isi', Layout: 'layout', Visual: 'visual', Sumber: 'sumber', Catatan: 'catatan' }[m[1]]] = clean(m[2].trim());
  }
}

// ---- patch adegan
const SHIM = `<script>(function(){if(parent===window)return;
// Mode presentasi: semua elemen tampil tanpa mengikuti tempo narasi.
// 'build' = timeline dipercepat sampai selesai kira-kira 3 detik; 'instant' = langsung tampil penuh.
window.__mode='build';
window.__present=function(mode){
  try{
    if(mode)window.__mode=mode;
    hideCover();
    var last=BEATS.length-1;
    seek(last,false);
    if(window.__mode==='instant'){
      P.t=P.end;evalTo(Infinity);
      if(BEATS[last].ask){P.waiting=true}else{P.done=true}
      setPlaying(false);
    }else{
      P.rate=Math.max(2,Math.min(16,P.end/3.2));
      setPlaying(true);
    }
  }catch(err){console.error('present',err)}
};
addEventListener('message',function(e){var m=e.data||{};
if(m.pm==='pause'){try{setPlaying(false)}catch(_){}}
if(m.pm==='start'||m.pm==='restart'){window.__present(m.mode)}});
addEventListener('keydown',function(e){
var k=e.key,ask=false;try{ask=!!BEATS[P.i].ask}catch(_){}
var t=e.target;if(t&&/^(INPUT|TEXTAREA)$/.test(t.tagName))return;
var nav=['PageDown','PageUp','F5'].indexOf(k)>=0;
var free=!ask&&['ArrowRight','ArrowLeft','ArrowDown','ArrowUp',' ','b','B','.','Home','End'].indexOf(k)>=0;
if(nav||free){e.preventDefault();e.stopImmediatePropagation();parent.postMessage({pm:'key',key:k,shift:e.shiftKey},'*')}
},true);
parent.postMessage({pm:'ready'},'*');})();</script>`;
// Dalam shell: tanpa pemutar, tanpa kartu sampul, tanpa logo ganda; bingkai adegan transparan dan pas 16:9.
const HEAD = `<script>try{if(parent!==window){document.documentElement.classList.add('emb');window.__EMB=true;
Object.defineProperty(HTMLMediaElement.prototype,'volume',{get:function(){return 0},set:function(){}})}}catch(e){}</script>
<style id="emb-css">
html.emb,html.emb body{background:transparent!important}
html.emb #bar,html.emb #cover,html.emb .sound-note,html.emb #chrome,html.emb .paused-mark,html.emb .caption{display:none!important}
html.emb #frame{top:50%!important;height:var(--sh,900px)!important;overflow:hidden!important;border-radius:0!important;box-shadow:none!important;background:transparent!important}
</style>`;
const stats = { files: 0, next: 0, finish: 0, film: 0, home: 0, homeLink: 0, clip: 0, fit: 0, full: 0, restart: 0, beatDone: 0, bytesSaved: 0, dropped: [] };
function patchScene(h) {
  const before = h.length;
  // tanpa voice over: buang klip suara, tandai semua beat "silent" (mesin memakai durasi dari TIMINGS)
  const clipRe = /window\.CLIP = \{[^}]*\};/;
  if (clipRe.test(h)) { h = h.replace(clipRe, () => "window.CLIP = {};\nfor (const k in (window.TIMINGS || {})) window.TIMINGS[k].silent = true;"); stats.clip++; }
  else if (/<script>\r?\n'use strict';/.test(h)) { h = h.replace(/<script>\r?\n'use strict';/, () => "<script>window.CLIP = {};\nfor (const k in (window.TIMINGS || {})) window.TIMINGS[k].silent = true;</script>\n<script>\n'use strict';"); stats.clip++; }
  const fitOld = ': Math.min(innerWidth / (SW + 40), (innerHeight - (innerWidth <= 700 ? 120 : 0)) / (SH + 100)));';
  if (h.includes(fitOld)) { h = h.replace(fitOld, () => ': (parent !== window ? Math.min(innerWidth / SW, innerHeight / SH) : Math.min(innerWidth / (SW + 40), (innerHeight - (innerWidth <= 700 ? 120 : 0)) / (SH + 100))));'); stats.fit++; }
  const fullOld = 'if (phone && !document.fullscreenElement';
  if (h.includes(fullOld)) { h = h.replace(fullOld, () => 'if (parent === window && phone && !document.fullscreenElement'); stats.full++; }
  const restartOld = 'const restart = () => { for (const k in SCORE) delete SCORE[k]; hideCover(); seek(0, true); };';
  if (h.includes(restartOld)) { h = h.replace(restartOld, () => 'const restart = () => { if (window.__EMB) { window.__present && window.__present(); return; } for (const k in SCORE) delete SCORE[k]; hideCover(); seek(0, true); };'); stats.restart++; }
  const bdOld = 'function beatDone() {';
  if (h.includes(bdOld)) { h = h.replace(bdOld, () => "function beatDone() {\n  if (window.__EMB) { evalTo(Infinity, TW.filter(w => !w.tail)); if (BEATS[P.i].ask) P.waiting = true; else if (P.i < BEATS.length - 1) start(P.i + 1, true); else { P.done = true; setPlaying(false); try { parent.postMessage({ pm: 'done' }, '*'); } catch (e) {} } return; }"); stats.beatDone++; }
  h = h.replace("function filmDone() {\n  try { parent !== window && parent.postMessage({ pm: 'done' }, '*'); } catch (e) {}", () => "function filmDone() {\n  try { parent !== window && parent.postMessage({ pm: 'done' }, '*'); } catch (e) {}\n  if (window.__EMB) return;");
  { const i = h.indexOf('</head>'); if (i >= 0) h = h.slice(0, i) + HEAD + h.slice(i); }
  const emb = "(parent!==window?parent.postMessage({pm:'next'},'*'):(location.href=CHAPTER.next))";
  const parts = h.split('location.href = CHAPTER.next'); stats.next += parts.length - 1; h = parts.join(emb);
  const rep1 = (a, b, k) => { if (h.includes(a)) { h = h.replace(a, () => b); stats[k]++; } };
  rep1('function finishCard() {', "function finishCard() {\n  try { parent !== window && parent.postMessage({ pm: 'done' }, '*'); } catch (e) {}", 'finish');
  rep1('function filmDone() {', "function filmDone() {\n  try { parent !== window && parent.postMessage({ pm: 'done' }, '*'); } catch (e) {}", 'film');
  rep1("home.href = $('bHome').href;", "home.href = '#'; home.onclick = e => { if (parent !== window) { e.preventDefault(); parent.postMessage({ pm: 'menu' }, '*'); } };", 'homeLink');
  rep1('<a class="icon" id="bHome" href="../"', `<a class="icon" id="bHome" href="../" onclick="if(parent!==window){event.preventDefault();parent.postMessage({pm:'menu'},'*')}"`, 'home');
  const i = h.lastIndexOf('</body>');
  h = i >= 0 ? h.slice(0, i) + SHIM + h.slice(i) : h + SHIM;
  stats.files++;
  stats.bytesSaved += before - h.length;
  return h;
}

// ---- modul: judul adegan + narasi
const BABS = [
  { n: 1, group: 'Bab 1', outline: 8, divTitle: 'Hari Pertama di Pelabuhan' },
  { n: 2, group: 'Bab 2', outline: 15, divTitle: 'Dasar Negara Memungut Pajak' },
  { n: 3, group: 'Bab 3', outline: 26, divTitle: 'Pihak dan Sistem Pemungutan' },
  { n: 4, group: 'Bab 4', outline: 36, divTitle: 'PPN Impor' },
  { n: 5, group: 'Bab 5', outline: 48, divTitle: 'PPh Pasal 22 Impor' },
  { n: 6, group: 'Bab 6', outline: 57, divTitle: 'Barang Mewah dan Fasilitas' },
  { n: 7, group: 'Bab 7', outline: 64, divTitle: 'Barang Kiriman' },
  { n: 8, group: 'Bab 8', outline: 70, divTitle: 'Menjawab Staf Importir' },
].filter((b) => b.n <= MAXBAB);
// Slide interaksi dibuang: Cek pemahaman, Latihan bab, dan kartu Selesai (berisi skor kuis). Sisanya materi.
const INTERACTIVE = /^(Cek pemahaman|Latihan bab|Selesai)$/i;
function sceneSlides(b) {
  const dir = path.join(root, 'dist', 'pdri', 'html', 'bab' + b.n);
  const files = fs.readdirSync(dir).filter((f) => /^\d\d-.*\.html$/.test(f) && !f.startsWith('00-')).sort();
  const nar = fs.readFileSync(path.join(root, 'docs', 'naskah-voiceover', `bab${b.n}-naskah-voiceover.md`), 'utf8')
    .split(/\r?\n/).filter((l) => /^\|\s*\d+\s*\|/.test(l))
    .map((l) => { const c = l.split('|').slice(1, -1).map((x) => x.trim()).filter(Boolean); return c[c.length - 1]; });
  if (nar.length !== files.length) console.warn(`Peringatan: bab ${b.n}: ${files.length} adegan, ${nar.length} baris narasi`);
  fs.mkdirSync(path.join(outScenes, 'bab' + b.n), { recursive: true });
  const kept = [];
  files.forEach((f, i) => {
    const raw = fs.readFileSync(path.join(dir, f), 'utf8');
    const t = raw.match(/<title>Bab \d+ .{1,3} Adegan (\d+): (.*?)<\/title>/);
    const title = t ? t[2].trim() : `Adegan ${i + 1}`;
    if (INTERACTIVE.test(title)) { stats.dropped.push(`bab${b.n}/${f}`); return; }
    fs.writeFileSync(path.join(outScenes, 'bab' + b.n, f), patchScene(raw));
    kept.push({ f, i, title });
  });
  const slides = kept.map((k, j) => ({
    n: `${b.n}.${String(j + 1).padStart(2, '0')}`, type: 'SCN',
    title: k.title, tag: `Bab ${b.n} · Slide ${j + 1} dari ${kept.length}`,
    isi: '', sumber: '', catatan: nar[k.i] ? 'Narasi: ' + nar[k.i] : '',
    src: `${SCENES_DIR}/bab${b.n}/${k.f}`,
  }));
  return { slides, intro: nar[0] || '' };
}

const groups = [];
groups.push({ name: 'Pembukaan', slides: [byN[1]] });
for (const b of BABS) {
  const { slides, intro } = sceneSlides(b);
  const div = {
    n: byN[b.outline].n, type: 'PER', title: b.divTitle, sumber: '', catatan: byN[b.outline].catatan || '',
    isi: `Nomor KB 0${b.n}. ${intro}`, layout: 'S2', visual: byN[b.outline].visual,
  };
  groups.push({ name: b.group, slides: [div, ...slides] });
}
const pen = Object.assign({}, byN[75], { isi: 'Terima kasih; Ulangi slide yang masih terasa sulit; Gunakan rangkuman tiap bab sebagai pengingat; ' + (MAXBAB >= 8 ? 'Lanjutkan ke post-test 10 soal' : MAXBAB >= 5 ? 'Lanjutkan ke Bab 6: Barang Mewah dan Fasilitas' : MAXBAB >= 4 ? 'Lanjutkan ke Bab 5: PPh Pasal 22 Impor' : 'Lanjutkan ke Bab 4: PPN Impor') });
groups.push({ name: 'Penutup', slides: [pen] });

// logo Kemenkeu, DJBC, PBC yang sudah ada di adegan, dipakai juga di bilah atas shell
const logoSrc = fs.readFileSync(path.join(root, 'dist', 'pdri', 'html', 'bab1', '01-intro.html'), 'utf8');
const logoM = logoSrc.match(/mk\('image', \{ href: '(data:image\/png;base64,[^']+)', x: 1560 - 268/);
if (!logoM) console.warn('Peringatan: logo tidak ditemukan di adegan');
const json = JSON.stringify({ groups }).replace(/</g, '\\u003c');
fs.mkdirSync(OUTDOCS, { recursive: true });
const dest = path.join(OUTDOCS, `presentasi-pdri-${TAG}.html`);
fs.writeFileSync(dest, tpl.replace('/*__DECK__*/', () => json).replace('/*__LOGO__*/', () => (logoM ? logoM[1] : '')));
const total = groups.reduce((a, x) => a + x.slides.length, 0);
console.log('OK', dest, total, 'slide (+ agenda dan ringkasan otomatis)');
console.log('Patch adegan:', JSON.stringify(stats));
