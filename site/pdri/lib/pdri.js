/* PDRI book library: flat 2D infographic pieces drawn in code (style.json components). Loaded after engine.js.
   Light board, bright flat colours, rounded shapes, no outlines, no people. Every piece is drawn around its own
   origin and placed with G({x, y}); bars stand on their origin (bottom centre). */
'use strict';

/* PDRI book library, Template Media Lite look (style.json): DJBC blue board with the template's texture (book.css),
   navy bands and cards, yellow accent, light-grey info cards, white titles beside a yellow tab, the three-logo pill
   top right, Poppins everywhere. Pieces drawn in code, flat, no outlines, no people. Every piece is drawn around its
   own origin and placed with G({x, y}); bars stand on their origin (bottom centre). Loaded after engine.js. */
'use strict';

const PD = {
  bg: '#1565b5', navy: '#0b3358', navy2: '#0f4777', light: '#eef1f5', yellow: '#ffcc29', sky: '#3fa0e0',
  card: '#0b3358', shadow: '#0a2c4d', line: '#d9dfe8', ink: '#ffffff', dim: '#c4daf2', faint: '#5f8fc4',
  text: '#0b3358', textDim: '#5a6b85',   // ink and dim text on the light cards
  pabean: '#3fa0e0', bm: '#f7941d', bmtp: '#e8612c', ppn: '#2ecc71', ppnbm: '#a66cf0', pph: '#ffcc29',
  assume: '#ff5a7a', good: '#2ecc71', bad: '#ff5a7a',
  sea: '#0e4c8a', seaLine: '#3fa0e0', quay: '#0b3358', steel: ['#3fa0e0', '#e8612c', '#ffcc29', '#2ecc71'], cloth: ['#fbe7c6', '#f7d6d0', '#d9ecf7', '#e6f2d9'],
};
const tint = (c, q = .82) => mix(c, '#ffffff', q);
const shade = (c, q = .22) => mix(c, '#000000', q);
// a levy colour made dark enough to read on a light card
const onLight = c => ({ [PD.pabean]: '#1673c0', [PD.ppn]: '#1b9a52', [PD.pph]: '#a87b00', [PD.bm]: '#c96a00', [PD.ppnbm]: '#7b3fc9' })[c] || c;
// the engine's drawing palette follows this book's blue board (book.css does the CSS side)
Object.assign(COL, { chalk: PD.ink, dim: PD.dim, faint: PD.faint, board: PD.bg, task: PD.yellow, good: PD.good, bad: PD.bad });

// Rupiah as written in Indonesia: Rp1.528.230.000
const idNum = n => String(Math.round(Math.abs(n))).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
const rp = n => (n < 0 ? '−' : '') + 'Rp' + idNum(n);
const IMG = '../lib/img/';
const pic = (p, href, x, y, w, h, extra = {}) => mk('image', { href: IMG + href, x, y, width: w, height: h, preserveAspectRatio: 'xMidYMid slice', ...extra }, p);

/* The template's fixed chrome: the white pill with the Kemenkeu, Bea Cukai and PBC logos, top right, over every beat.
   It sits on the stage above the scene, so it stays put while the panels change. */
(() => {
  const st = document.getElementById('stage');
  const g = document.createElementNS(NS, 'g');
  g.setAttribute('id', 'chrome'); g.setAttribute('aria-hidden', 'true');
  st.appendChild(g);
  mk('rect', { x: 1158, y: 36, width: 356, height: 110, rx: 55, fill: '#ffffff' }, g);
  mk('image', { href: IMG + 'logos.png', x: 1190, y: 52, width: 274, height: 78, preserveAspectRatio: 'xMidYMid meet' }, g);
})();

/* slideHead: the template's slide title. A yellow tab bleeding off the top left, the title in white beside it, and an
   optional subtitle (the regulation) under it. */
function slideHead(p, title, { sub, t0 = .1, size = 46 } = {}) {
  const g = G(p, { o: 0 });
  mk('rect', { x: 30, y: -40, width: 50, height: 150, rx: 25, fill: PD.yellow }, g);
  T(g, title, { x: 118, y: sub ? 80 : 92, size, weight: 700, fill: '#fff' });
  if (sub) T(g, sub, { x: 118, y: 122, size: 24, weight: 600, fill: '#fff' });
  show(g, t0, .4);
  return g;
}
// a navy band right across the slide (template: the content band under the title)
const navyBand = (p, y, h, o = .94) => mk('rect', { x: 0, y, width: SW, height: h, fill: PD.navy, 'fill-opacity': o }, p);
// the template's step number: a white circle with a bold blue number
function numDisc(p, n, x, y, { r = 44, o = 0 } = {}) {
  const g = G(p, { x, y, o });
  mk('circle', { r, fill: '#fff' }, g);
  T(g, n, { y: r * .36, size: r * .95, weight: 800, anchor: 'middle', fill: '#1565b5' });
  return g;
}
// Poppins must be in before the first measure (textW, uiW) and the first frame: boot once the faces are loaded
function pdBoot() {
  const faces = ['400', '600', '700', '800'].map(w => document.fonts.load(`${w} 30px Poppins`));
  Promise.all(faces).catch(() => {}).finally(boot);
}

// a flat card (template: navy, or light grey with fill PD.light), optional coloured header band
function pcard(p, x, y, w, h, { r = 22, fill = PD.card, o = 1, head, headCol, headH = 70, headInk = '#fff' } = {}) {
  const g = G(p, { o });
  mk('rect', { x, y, width: w, height: h, rx: r, fill }, g);
  if (head) {
    path(g, `M${x} ${y + headH}V${y + r}a${r} ${r} 0 0 1 ${r} ${-r}H${x + w - r}a${r} ${r} 0 0 1 ${r} ${r}V${y + headH}Z`, { fill: headCol });
    T(g, head, { x: x + 32, y: y + headH / 2 + 11, size: 30, weight: 700, fill: headInk });
  }
  return g;
}

/* bar: a rounded flat bar standing on (x, y), width w. b.set(h) redraws its height; grow() tweens it. */
function bar(p, { x = 0, y = 0, w = 200, h = 40, col = PD.pabean, o = 1, r = 6, label } = {}) {
  const g = G(p, { x, y, o });
  const R = mk('rect', { x: -w / 2, width: w, rx: r, fill: col }, g);
  const hi = mk('rect', { x: -w / 2, width: w * .18, fill: '#ffffff', 'fill-opacity': .14 }, g);
  const b = { g, R, w, h, col };
  b.set = hh => { hh = Math.max(0, hh); b.h = hh; R.setAttribute('y', -hh); R.setAttribute('height', hh); hi.setAttribute('y', -hh); hi.setAttribute('height', hh); };
  b.set(h);
  return b;
}
function grow(b, h0, h1, t0, dur = .8, ease = out) { b.set(h0); prog(q => b.set(h0 + (h1 - h0) * q), t0, dur, ease); }

/* stack: bars on one footprint, bottom-up; vals in rupiah, k px per rupiah. Each layer keeps its base and full
   height; a 3 px seam of board colour separates them. */
function stackBars(p, x, y, w, vals, cols, k) {
  let base = 0;
  const layers = vals.map((v, i) => {
    const hFull = v * k;
    const b = bar(p, { x, y: y - base, w, h: 0, col: cols[i], o: 0, r: i ? 4 : 6 });
    b.base = base; b.hFull = hFull; base += hFull;
    return b;
  });
  return { layers, x, y, w, total: base };
}

// a pill: text on a solid colour (or outlined), centred on (x, y)
function pdTag(p, str, x, y, col, { size = 26, solid = true, o = 0, weight = 800, ink } = {}) {
  const g = G(p, { x, y, o });
  const w = textW(str, size) * 1.06 + size * 1.4, hh = size * 1.7;
  mk('rect', { x: -w / 2, y: -hh / 2, width: w, height: hh, rx: hh / 2, fill: solid ? col : 'none', stroke: col, 'stroke-width': solid ? 0 : 3 }, g);
  T(g, str, { x: 0, y: size * .36, size, weight, anchor: 'middle', fill: ink || (solid ? ([PD.pph, PD.yellow, PD.ppn, PD.pabean, '#ffffff'].includes(col) ? PD.navy : '#fff') : col) });
  g._w = w;
  return g;
}
// a round badge with short letters (the levy icons)
function badge(p, str, x, y, col, { r = 56, size, o = 0 } = {}) {
  const g = G(p, { x, y, o });
  const halo = mk('circle', { r: r + 10, fill: col }, g);
  mk('circle', { r, fill: col }, g);
  T(g, str, { y: (size || r * .5) * .36, size: size || r * .5, weight: 800, anchor: 'middle', fill: [PD.pph, PD.ppn, PD.pabean].includes(col) ? PD.navy : '#fff' });
  // the halo breathes slowly while the badge is on screen (a pure function of the beat clock)
  const ph = (x * 7 + y * 3) % 6.28;
  put(halo, { s: 1, o: .3 });
  clockRun(t => put(halo, { s: 1 + .06 * Math.sin(t * 1.6 + ph), o: .3 }), 0, { tail: true });
  return g;
}
// a short label on a line to the right of a point
function sideLabel(p, str, x, y, col, { dx = 36, size = 26, sub, o = 0 } = {}) {
  const g = G(p, { o });
  mk('circle', { cx: x, cy: y, r: 5, fill: col }, g);
  path(g, `M${x} ${y}H${x + dx - 10}`, { stroke: col, 'stroke-width': 2.5 });
  T(g, str, { x: x + dx, y: y + size * .35, size, weight: 800, fill: col });
  if (sub) T(g, sub, { x: x + dx, y: y + size * 1.4, size: size * .75, weight: 600, fill: PD.dim });
  return g;
}
// a straight arrow drawn on at t0
function arrowTo(p, x1, y1, x2, y2, col, t0, w = 4) {
  const g = G(p);
  const a = Math.atan2(y2 - y1, x2 - x1), k = 16;
  draw(path(g, `M${x1} ${y1}L${x2} ${y2}`, { stroke: col, 'stroke-width': w, 'stroke-linecap': 'round' }, { d: 0 }), t0, .55);
  show(path(g, `M${x2 - k * Math.cos(a - .5)} ${y2 - k * Math.sin(a - .5)}L${x2} ${y2}L${x2 - k * Math.cos(a + .5)} ${y2 - k * Math.sin(a + .5)}`,
    { stroke: col, 'stroke-width': w, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', fill: 'none' }, { o: 0 }), t0 + .45, .15);
  return g;
}

/* container, side view, standing on its origin (bottom centre); the doors are on the right end (c.doors) */
function container(p, { x = 0, y = 0, w = 240, h = 100, col = PD.steel[0], o = 1 } = {}) {
  const g = G(p, { x, y, o });
  mk('rect', { x: -w / 2, y: -h, width: w, height: h, rx: 6, fill: col }, g);
  let d = '';
  for (let i = 1; i < 10; i++) d += `M${-w / 2 + i * w / 10} ${-h + 10}V-10`;
  path(g, d, { stroke: shade(col, .18), 'stroke-width': 4 });
  mk('rect', { x: -w / 2, y: -h, width: w, height: 10, rx: 4, fill: shade(col, .12) }, g);
  const inside = mk('rect', { x: w / 2 - 6, y: -h + 6, width: 10, height: h - 12, fill: '#2a3550' }, g);
  const doors = G(g, { x: w / 2 });
  mk('rect', { x: -4, y: -h + 4, width: 12, height: h - 8, rx: 3, fill: shade(col, .3) }, doors);
  put(doors, { o: 1 });
  g.doors = doors; g.inside = inside;
  return g;
}
// a fabric roll seen end-on beside its length: a capsule with a spiral end, standing on its origin
function fabricRoll(p, { x = 0, y = 0, len = 110, r = 20, col = PD.cloth[0], o = 1 } = {}) {
  const g = G(p, { x, y, o });
  mk('rect', { x: -len / 2, y: -2 * r, width: len, height: 2 * r, rx: 6, fill: col }, g);
  path(g, `M${-len / 2 + 14} ${-2 * r + 6}V-6M${-len / 2 + 30} ${-2 * r + 6}V-6`, { stroke: shade(col, .08), 'stroke-width': 3 });
  mk('circle', { cx: len / 2, cy: -r, r, fill: shade(col, .06) }, g);
  path(g, `M${len / 2} ${-r}m-4 0a4 4 0 1 1 8 0a8 8 0 1 1 -16 0a12 12 0 1 1 24 0`, { stroke: shade(col, .25), 'stroke-width': 2.5, fill: 'none' });
  return g;
}
/* ship, side view: hull, bridge at the stern, container rows on deck; standing on the waterline at its origin */
function ship(p, { x = 0, y = 0, len = 560, o = 1 } = {}) {
  const g = G(p, { x, y, o });
  const a = len / 2;
  path(g, `M${-a} -70H${a + 30}L${a - 20} 20H${-a + 30}Z`, { fill: '#082640' });
  path(g, `M${-a + 8} -6H${a + 6}L${a - 2} 20H${-a + 30}Z`, { fill: '#d64a4a' });
  mk('rect', { x: -a + 20, y: -170, width: 80, height: 100, rx: 6, fill: '#eef2f8' }, g);
  for (let i = 0; i < 3; i++) mk('rect', { x: -a + 32, y: -156 + i * 28, width: 56, height: 12, rx: 3, fill: '#9cc4f2' }, g);
  mk('rect', { x: -a + 48, y: -200, width: 18, height: 34, rx: 3, fill: '#e2632b' }, g);
  const n = Math.floor((len - 160) / 62);
  for (let i = 0; i < n; i++) for (let j = 0; j < 2; j++) {
    mk('rect', { x: -a + 120 + i * 62, y: -70 - (j + 1) * 38, width: 58, height: 35, rx: 3, fill: PD.steel[(i + j) % 4] }, g);
  }
  return g;
}
// quay crane, side view: two legs on the quay, a boom out to the left over the water; c.hookX is the trolley's x
function crane(p, { x = 0, y = 0, h = 360, boom = 380, o = 1, col = '#ffcc29' } = {}) {
  const g = G(p, { x, y, o });
  path(g, `M-50 0L-30 ${-h}M50 0L30 ${-h}M-40 -120H40M-34 -260H34`, { stroke: col, 'stroke-width': 12, 'stroke-linecap': 'round' });
  path(g, `M${-boom} ${-h}H120M0 ${-h - 70}L${-boom + 30} ${-h}M0 ${-h - 70}L110 ${-h}M0 ${-h - 70}V${-h}`, { stroke: col, 'stroke-width': 9, 'stroke-linecap': 'round' });
  mk('rect', { x: -60, y: -h - 30, width: 70, height: 40, rx: 6, fill: shade(col, .15) }, g);
  return g;
}
/* service desk, front view: counter, monitor, a tray with a PIB sheet, a hanging sign. No people. */
function serviceDesk(p, { x = 0, y = 0, o = 1, sign = 'MEJA LAYANAN' } = {}) {
  const g = G(p, { x, y, o });
  mk('rect', { x: -170, y: -110, width: 340, height: 110, rx: 10, fill: PD.sky }, g);
  mk('rect', { x: -186, y: -126, width: 372, height: 22, rx: 8, fill: '#eef1f5' }, g);
  mk('rect', { x: -120, y: -80, width: 240, height: 8, rx: 4, fill: '#ffffff', 'fill-opacity': .25 }, g);
  mk('rect', { x: -120, y: -216, width: 120, height: 80, rx: 8, fill: PD.navy }, g);
  mk('rect', { x: -110, y: -206, width: 100, height: 60, rx: 4, fill: '#9cc4f2' }, g);
  mk('rect', { x: -70, y: -136, width: 20, height: 12, fill: PD.navy }, g);
  const sheet = G(g, { x: 80, y: -128 });
  mk('rect', { x: -40, y: -66, width: 80, height: 66, rx: 4, fill: '#fff', stroke: PD.line, 'stroke-width': 2 }, sheet);
  path(sheet, 'M-28 -50H28M-28 -36H28M-28 -22H12', { stroke: PD.faint, 'stroke-width': 4, 'stroke-linecap': 'round' });
  T(sheet, 'PIB', { y: -6, size: 14, weight: 800, anchor: 'middle', fill: '#1673c0' });
  const sg = G(g, { y: -330 });
  path(sg, 'M-80 -60V-24M80 -60V-24', { stroke: PD.dim, 'stroke-width': 3 });
  mk('rect', { x: -130, y: -26, width: 260, height: 52, rx: 26, fill: PD.yellow }, sg);
  T(sg, sign, { y: 8, size: 20, weight: 700, anchor: 'middle', fill: PD.navy });
  return g;
}
// a question bubble with its tail pointing down at (x + tailX, y + h/2 + 26)
function askCard(p, str, x, y, { size = 30, o = 0, tailX = 0 } = {}) {
  const w = textW(str, size) * 1.06 + 60, hh = size * 2.3;
  const g = G(p, { x, y, o });
    mk('path', { d: `M${-w / 2} ${-hh / 2}h${w}v${hh}H${tailX + 22}l-22 26l-6 -26H${-w / 2}Z`, fill: '#fff', 'stroke-linejoin': 'round' }, g);
  T(g, str, { y: size * .36, size, weight: 700, anchor: 'middle', fill: PD.text });
  return g;
}
// the 'asumsi latihan' stamp for figures marked (cek) in the source
function assumeStamp(p, x, y, { r = -6, s = 1, o = 0, str = 'ASUMSI LATIHAN' } = {}) {
  const g = G(p, { x, y, r, s, o });
  const w = textW(str, 18) * 1.15 + 28;
  mk('rect', { x: -w / 2, y: -18, width: w, height: 36, rx: 18, fill: tint(PD.assume, .85), stroke: PD.assume, 'stroke-width': 2.5 }, g);
  T(g, str, { y: 7, size: 18, weight: 800, anchor: 'middle', fill: PD.assume });
  return g;
}
/* calcCard: the step calculator on a light-grey card (template info card). rows: { label, formula, result, col }. c.row(i, tLabel, tResult)
   shows a row's label and formula, then counts its result up. */
function calcCard(p, x, y, w, rows, { title = 'Langkah hitung', rowH = 104, o = 0 } = {}) {
  const H = 76 + rows.length * rowH;
  const g = G(p, { o });
  pcard(g, x, y, w, H, { fill: PD.light });
  T(g, title.toUpperCase(), { x: x + 32, y: y + 48, size: 20, weight: 700, fill: PD.textDim });
  const els = rows.map((r, i) => {
    const ry = y + 70 + i * rowH;
    const rg = G(g, { o: 0 });
    mk('rect', { x: x + 24, y: ry + 10, width: w - 48, height: rowH - 16, rx: 14, fill: tint(r.col, .86) }, rg);
    mk('rect', { x: x + 24, y: ry + 10, width: 10, height: rowH - 16, rx: 5, fill: r.col }, rg);
    T(rg, r.label, { x: x + 52, y: ry + 44, size: 21, weight: 600, fill: PD.textDim });
    T(rg, r.formula, { x: x + 52, y: ry + 78, size: 24, weight: 600, fill: PD.text });
    const res = T(g, '', { x: x + w - 44, y: ry + 72, size: 30, weight: 800, fill: onLight(r.col), anchor: 'end', o: 0 });
    return { rg, res, value: r.result };
  });
  g.row = (i, tLabel, tResult, count = .9) => {
    const e = els[i];
    show(e.rg, tLabel, .45);
    if (tResult === undefined) return;
    show(e.res, tResult, .2);
    prog(q => { e.res.textContent = rp(e.value * q); }, tResult, count, out);
  };
  g.H = H;
  return g;
}
// waves on the sea that drift, a pure function of the beat clock
function waves(p, { x0 = 0, y0 = 0, w = 600, rows = 3, D = 30 } = {}) {
  const g = G(p);
  const els = [];
  for (let j = 0; j < rows; j++) for (let i = 0; i < 6; i++) {
    const e = path(g, 'M0 0q15 -10 30 0t30 0', { stroke: PD.seaLine, 'stroke-width': 4, 'stroke-linecap': 'round', fill: 'none' });
    els.push({ e, bx: x0 + i * (w / 6) + (j % 2) * 40, by: y0 + j * 60, ph: i + j * 2 });
  }
  clockRun(t => { for (const r of els) put(r.e, { x: r.bx + 18 * Math.sin(t * .8 + r.ph), y: r.by, o: .55 + .35 * Math.sin(t * .9 + r.ph) }); }, D, { tail: true });
  return g;
}
