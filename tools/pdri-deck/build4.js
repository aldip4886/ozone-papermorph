// Versi 4: layar bersih (tanpa header dan footer), animasi disinkronkan ulang tanpa voice over.
// Sumber: docs/presentasi-pdri-v3.html (daftar slide) dan docs/presentasi-pdri-v3-scenes (adegan Bab 1-3).
// Keluaran: docs/presentasi-pdri-v4.html dan docs/presentasi-pdri-v4-scenes/.
// Urutan untuk Bab 1-5 (v3 tidak berubah):
//   python tools/pdri-deck/patch-v3.py
//   PDRI_MAXBAB=5 PDRI_TAG=v4src PDRI_OUTDOCS=<folder sementara> node tools/pdri-deck/build3.js
//   PDRI_SRCDOCS=<folder sementara> PDRI_TAG=v4src python tools/pdri-deck/patch-v4.py
//   PDRI_SRCDOCS=<folder sementara> PDRI_TAG=v4src node tools/pdri-deck/build4.js
// Tanpa variabel itu, build4 memakai keluaran build3 biasa (Bab 1-3).
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..', '..');
const docs = path.join(root, 'docs');
// Sumber: keluaran build3 untuk Bab 1-5 (PDRI_TAG=v4src, PDRI_MAXBAB=5, PDRI_OUTDOCS=<folder sementara>); bawaan: v3 di docs.
const SRC = process.env.PDRI_SRCDOCS ? path.resolve(process.env.PDRI_SRCDOCS) : docs, TAG = process.env.PDRI_TAG || 'v3';
const V3 = `presentasi-pdri-${TAG}-scenes`, V4 = 'presentasi-pdri-v4-scenes';
const inDir = path.join(SRC, V3), outDir = path.join(docs, V4);
const tpl = fs.readFileSync(path.join(__dirname, 'template-v4.html'), 'utf8');

// ---- daftar slide dari v3
const v3 = fs.readFileSync(path.join(SRC, `presentasi-pdri-${TAG}.html`), 'utf8');
const dm = v3.match(/<script type="application\/json" id="deck-data">([\s\S]*?)<\/script>/);
if (!dm) throw new Error('deck-data v3 tidak ditemukan. Jalankan build3.js lebih dulu.');
const deck = JSON.parse(dm[1]);
for (const g of deck.groups) for (const s of g.slides) if (s.src) s.src = s.src.replace(V3, V4);

// ---- sinkron ulang animasi tanpa voice over
// Titik sinkron (marks) asli mengikuti tempo narasi (jeda 3-5 detik). Di sini jeda antar titik dipadatkan menjadi
// 0,7-1,6 detik, sedangkan lama tiap gerakan tetap alami. Beat memakai durasi barunya sendiri.
const SILENT_OLD = "window.CLIP = {};\nfor (const k in (window.TIMINGS || {})) window.TIMINGS[k].silent = true;";
const RESYNC = `window.CLIP = {};
(function () {
  var T = window.TIMINGS || {};
  for (var id in T) {
    var tm = T[id]; tm.silent = true;
    var marks = tm.marks || {}, vals = [];
    for (var k in marks) if (typeof marks[k] === 'number' && vals.indexOf(marks[k]) < 0) vals.push(marks[k]);
    vals.sort(function (a, b) { return a - b; });
    var map = {}, at = 0.7, prev = vals[0];
    vals.forEach(function (t, i) { if (i) { at += Math.min(1.6, Math.max(0.7, (t - prev) * 0.25)); prev = t; } map[t] = at; });
    for (var k2 in marks) if (typeof marks[k2] === 'number') marks[k2] = map[marks[k2]];
    tm.dur = Math.max(3, (vals.length ? map[vals[vals.length - 1]] : 1) + 2.4);
  }
})();`;
const RATE_OLD = 'P.rate=Math.max(2,Math.min(16,P.end/3.2));';
const WAKE = `<script>(function(){if(parent===window)return;var t=0;function w(){var n=Date.now();if(n-t>300){t=n;parent.postMessage({pm:'wake'},'*')}}
addEventListener('mousemove',w,true);addEventListener('pointerdown',w,true);addEventListener('touchstart',w,true);})();</script>`;
const stats = { files: 0, resync: 0, rate: 0 };
function patch(h) {
  if (h.includes(SILENT_OLD)) { h = h.replace(SILENT_OLD, () => RESYNC); stats.resync++; }
  if (h.includes(RATE_OLD)) { h = h.replace(RATE_OLD, () => 'P.rate=1;'); stats.rate++; }
  const i = h.lastIndexOf('</body>');
  h = i >= 0 ? h.slice(0, i) + WAKE + h.slice(i) : h + WAKE;
  stats.files++;
  return h;
}

fs.rmSync(outDir, { recursive: true, force: true });
for (const bab of fs.readdirSync(inDir)) {
  const d = path.join(inDir, bab);
  if (!fs.statSync(d).isDirectory()) continue;
  fs.mkdirSync(path.join(outDir, bab), { recursive: true });
  for (const f of fs.readdirSync(d)) {
    fs.writeFileSync(path.join(outDir, bab, f), patch(fs.readFileSync(path.join(d, f), 'utf8')));
  }
}

const json = JSON.stringify(deck).replace(/</g, '\\u003c');
const dest = path.join(docs, 'presentasi-pdri-v4.html');
fs.writeFileSync(dest, tpl.replace('/*__DECK__*/', () => json).replace('/*__LOGO__*/', () => ''));
const n = deck.groups.reduce((a, g) => a + g.slides.length, 0);
console.log('OK', dest, n, 'slide (+ agenda dan ringkasan otomatis)');
console.log('Patch adegan:', JSON.stringify(stats));
