/* PDRI, McKinsey version: a McKinsey-style exhibit deck in the INSW e-learning design (design.md from the user).
   Paper slides carry the exhibits (action title = the slide's conclusion, a gold tag above it, a source line under
   the exhibit); navy aurora slides open, divide and close. Poppins throughout, gold accent, 3D-flat icon tiles,
   the Kemenkeu, DJBC and PBC logo pill top right. The narration script shows on screen as the subtitle pill
   (voice: John’s Google AI Studio recording; captions follow the CC toggle). Stage 1600x900 = design.md's 1920x1080 at 5/6. Loaded after engine.js. */
'use strict';

const MK = {
  navy: '#0A2A5C', navyDeep: '#071E45', navy2: '#0E3A78', glow: '#12468C', blue: '#0055A5', sky: '#3A9BE1',
  gold: '#F5B324', goldDark: '#C8901A', goldLight: '#FFE29A', paper: '#FBFAF6', line: '#D6DEEA',
  red: '#D83C3C', green: '#22A55A', white: '#FFFFFF', dim: '#4A5F80', faint: '#9AA9C2',
};
Object.assign(COL, { chalk: MK.navy, dim: MK.dim, faint: MK.faint, board: MK.paper, task: MK.gold, good: MK.green, bad: MK.red });
const idNum = n => String(Math.round(Math.abs(n))).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
const rp = n => (n < 0 ? '−' : '') + 'Rp' + idNum(n);
const IMG = '../lib/img/';
const K = 5 / 6;   // design.md pixels to stage pixels

/* ---------- stage-wide pieces: gradients for the tiles, the logo pill ---------- */
(() => {
  const st = document.getElementById('stage');
  const defs = document.createElementNS(NS, 'defs');
  const V = { gold: ['#FFD05A', '#F5B324', '#E9A41B'], blue: ['#2B7FD0', '#0055A5', '#004A91'], sky: ['#7CC0F2', '#3A9BE1', '#2F8AD0'] };
  let s = '';
  for (const [k, [a, b, c]] of Object.entries(V))
    s += `<linearGradient id="mkFace-${k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${a}"/><stop offset=".55" stop-color="${b}"/><stop offset="1" stop-color="${c}"/></linearGradient>`;
  s += '<linearGradient id="mkGloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>';
  s += '<radialGradient id="mkAurora" cx=".7" cy=".3" r=".9"><stop offset="0" stop-color="#12468C"/><stop offset=".55" stop-color="#0A2A5C"/><stop offset="1" stop-color="#071E45"/></radialGradient>';
  s += '<radialGradient id="mkVignette" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#0A2A5C" stop-opacity="0"/><stop offset="1" stop-color="#0A2A5C" stop-opacity=".08"/></radialGradient>';
  s += '<pattern id="mkGrid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#0055A5" stroke-opacity=".07" stroke-width="2"/></pattern>';
  s += '<pattern id="mkDots" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="1.6" fill="#fff" fill-opacity=".1"/></pattern>';
  s += '<clipPath id="mkPhoto"><circle cx="0" cy="0" r="230"/></clipPath>';
  defs.innerHTML = s;
  st.insertBefore(defs, st.firstChild);
  const g = document.createElementNS(NS, 'g');
  g.setAttribute('id', 'chrome'); g.setAttribute('aria-hidden', 'true');
  st.appendChild(g);
  // design.md: top 40, right 48, height 96 (x 5/6)
  mk('rect', { x: 1560 - 290, y: 37, width: 290, height: 80, rx: 40, fill: 'rgba(10,42,92,.18)' }, g);
  mk('rect', { x: 1560 - 290, y: 33, width: 290, height: 80, rx: 40, fill: '#fff' }, g);
  mk('image', { href: IMG + 'logos.png', x: 1560 - 268, y: 43, width: 246, height: 60, preserveAspectRatio: 'xMidYMid meet' }, g);
})();

/* ---------- backgrounds ---------- */
// paper: warm white, a faint blue 40 px grid, a soft vignette
function bgPaper(p) {
  const g = G(p);
  mk('rect', { width: SW, height: SH, fill: MK.paper }, g);
  mk('rect', { width: SW, height: SH, fill: 'url(#mkGrid)' }, g);
  mk('rect', { width: SW, height: SH, fill: 'url(#mkVignette)' }, g);
  return g;
}
// navy aurora: the radial gradient, translucent triangles drifting, a dot grid, a few rising particles
function bgNavy(p, seed = 1, D = 30) {
  const g = G(p);
  mk('rect', { width: SW, height: SH, fill: 'url(#mkAurora)' }, g);
  let s = seed * 9301 + 49297;
  const rnd = () => ((s = (s * 9301 + 49297) % 233280) / 233280);
  const tris = [];
  for (let i = 0; i < 16; i++) {
    const r = 75 + rnd() * 270, x = rnd() * SW, y = rnd() * SH;
    const e = path(g, `M0 ${-r}L${r * .87} ${r / 2}L${-r * .87} ${r / 2}Z`, { fill: rnd() < .75 ? MK.sky : MK.blue, 'fill-opacity': .05 + rnd() * .09 });
    tris.push({ e, x, y, a: rnd() * 360, v: (rnd() - .5) * 4, dx: (rnd() - .5) * 18 });
  }
  mk('rect', { width: SW, height: SH, fill: 'url(#mkDots)' }, g);
  const dots = [];
  for (let i = 0; i < 24; i++) {
    const e = mk('circle', { r: 1.5 + rnd() * 2.5, fill: rnd() < .4 ? MK.gold : '#fff', 'fill-opacity': .35 + rnd() * .4 }, g);
    dots.push({ e, x: rnd() * SW, y: rnd() * SH, v: 8 + rnd() * 16 });
  }
  clockRun(t => {
    for (const r of tris) r.e.setAttribute('transform', `translate(${r.x + r.dx * Math.sin(t * .2)} ${r.y}) rotate(${r.a + r.v * t})`);
    for (const d of dots) { const y = ((d.y - d.v * t) % SH + SH) % SH; d.e.setAttribute('cx', d.x); d.e.setAttribute('cy', y); }
  }, D, { tail: true });
  return g;
}
/* the stage change: two skewed panels (gold, then navy) that cover the screen at the cut and slide off to the right */
function wipeIn(p) {
  const g = G(p);
  const band = (col, d) => {
    const e = path(g, `M-400 -100H2100L1800 1000H-700Z`, { fill: col });
    put(e, { x: 0 });
    tw(e, { x: 2300 }, d, .9, io);
    return e;
  };
  band(MK.gold, .12); band(MK.navy, 0);
  return g;
}

/* ---------- type ---------- */
/* actionTitle: the slide's conclusion, top left (design: left 110, top 72, Poppins Bold 64 -> 92, 60, 53), up to two
   lines split with '|', clear of the logo pill; a gold tag above names the stage. Lines rise in on the slide's clock. */
function actionTitle(p, str, { tag, t0 = .25, dark = false, size = 40 } = {}) {
  const g = G(p);
  if (tag) {
    const tg = wrap(pill(g, tag, 92, 52, { size: 19, bg: MK.gold, ink: MK.navy, anchor: 'start' }));
    put(tg, { o: 0, x: -14 }); tw(tg, { o: 1, x: 0 }, t0, .4, out);
  }
  const lines = str.split('|');
  lines.forEach((ln, i) => {
    const e = wrap(T(g, ln, { x: 92, y: 118 + i * size * 1.22, size, weight: 700, fill: dark ? '#fff' : MK.navy }));
    put(e, { y: 18, o: 0 }); tw(e, { o: 1, y: 0 }, t0 + .15 + i * .12, .55, out);
  });
  g.bottom = 118 + (lines.length - 1) * size * 1.22;
  return g;
}
// the exhibit's source line, bottom left above the subtitle band
function source(p, str, t0 = .6, dark = false) {
  const e = T(p, 'Sumber: ' + str, { x: 92, y: 752, size: 18, weight: 500, fill: dark ? '#9FB6D8' : MK.dim, o: 0 });
  show(e, t0, .5);
  return e;
}
// a pill (tag) with text; anchor start puts its left edge at x
function pill(p, str, x, y, { size = 22, bg = MK.gold, ink = MK.navy, anchor = 'middle', weight = 700, stroke } = {}) {
  const w = textW(str, size) * 1.05 + size * 1.3, h = size * 1.75;
  const g = G(p, { x: anchor === 'start' ? x + w / 2 : x, y });
  mk('rect', { x: -w / 2, y: -h / 2, width: w, height: h, rx: h / 2, fill: bg, ...(stroke ? { stroke, 'stroke-width': 2.5 } : {}) }, g);
  T(g, str, { y: size * .36, size, weight, anchor: 'middle', fill: ink });
  g._w = w;
  return g;
}
// gold marker under a word or phrase, grown from the left (design: highlight on paper)
function marker(p, x, y, w, t0, size = 30) {
  const r = mk('rect', { x, y: y - size * .32, width: 0, height: size * .42, rx: 3, fill: MK.gold, 'fill-opacity': .6 }, p);
  p.insertBefore(r, p.firstChild);
  prog(q => r.setAttribute('width', w * q), t0, .5, out);
  return r;
}
// lines of text centred or left, one T per line ('|' splits)
function lines(p, str, x, y, { size = 24, lh = 1.3, weight = 500, fill = MK.navy, anchor = 'start' } = {}) {
  str.split('|').forEach((ln, i) => T(p, ln, { x, y: y + i * size * lh, size, weight, fill, anchor }));
}

/* ---------- cards ---------- */
// white card: on navy a deep shadow (radius 28 -> 23), on paper a hairline edge and a light shadow (radius 18 -> 15)
function mcard(p, x, y, w, h, { dark = false, fill = '#fff', r } = {}) {
  const g = G(p);
  if (dark) {
    mk('rect', { x: x + 2, y: y + 14, width: w - 4, height: h, rx: r ?? 23, fill: '#000', 'fill-opacity': .28 }, g);
    mk('rect', { x, y, width: w, height: h, rx: r ?? 23, fill }, g);
  } else {
    mk('rect', { x: x + 1, y: y + 8, width: w - 2, height: h, rx: r ?? 15, fill: MK.navy, 'fill-opacity': .07 }, g);
    mk('rect', { x, y, width: w, height: h, rx: r ?? 15, fill, stroke: MK.line, 'stroke-width': 2 }, g);
  }
  return g;
}

/* ---------- 3D-flat icon tiles (icon-tile-template.svg) ---------- */
// glyphs drawn for this book on a 24 px grid, white stroke 2 (Lucide-like, own drawings)
const GLYPH = {
  ship: 'M2 16l2.5 4h15L22 16H2z M5 16v-5h14v5 M8 11V7h5v4 M10.5 7V4',
  container: 'M3 6h18v13H3z M7 9v7 M11 9v7 M15 9v7 M19 9v7',
  fabric: 'M7 4h11a3 3 0 0 1 0 6H7 M7 4a3 3 0 0 0 0 6 M7 10v10h11V10 M10 14h5',
  office: 'M3 21h18 M5 21V10 M19 21V10 M12 3L3 9h18z M9 21v-6h6v6',
  doc: 'M6 2h9l4 4v16H6z M14 2v5h5 M9 12h7 M9 16h7',
  calc: 'M6 2h12v20H6z M9 5.5h6v3H9z M9 13h.01 M12 13h.01 M15 13h.01 M9 17h.01 M12 17h.01 M15 17h.01',
  percent: 'M19 5L5 19 M4.5 7a2.5 2.5 0 1 0 5 0a2.5 2.5 0 1 0 -5 0 M14.5 17a2.5 2.5 0 1 0 5 0a2.5 2.5 0 1 0 -5 0',
  gem: 'M6 3h12l4 6-10 12L2 9z M2 9h20 M12 21L8 9l4-6 4 6z',
  wallet: 'M3 7h15a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3H3z M3 7l12-4v4 M16.5 14h.01',
  law: 'M12 3v18 M6 21h12 M4 7h16 M7 7l-3 7a3 3 0 0 0 6 0z M17 7l-3 7a3 3 0 0 0 6 0z',
  shield: 'M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z',
  check: 'M5 12.5l4.5 4.5L19 7.5',
  cross: 'M6 6l12 12M18 6L6 18',
  idcard: 'M3 5h18v14H3z M6.5 10a2 2 0 1 0 4 0a2 2 0 1 0-4 0 M5 16.5c1-2 5.5-2 6.5 0 M14 9h4 M14 13h4',
  rate: 'M4 8h14l-3-3 M20 16H6l3 3',
  question: 'M12 21a9 9 0 1 0 0-18a9 9 0 1 0 0 18z M9.3 9.2a2.8 2.8 0 1 1 3.8 2.6c-.7.3-1.1.9-1.1 1.7 M12 16.8h.01',
  layers: 'M12 3l9 5-9 5-9-5z M3 13l9 5 9-5',
  tag: 'M3 12V3h9l9 9-9 9z M7.5 7.5h.01',
  medal: 'M8 2l2 6M16 2l-2 6 M12 22a6 6 0 1 0 0-12a6 6 0 1 0 0 12z M12 13.5l1 2 2.2.3-1.6 1.5.4 2.2-2-1-2 1 .4-2.2-1.6-1.5 2.2-.3z',
  umbrella: 'M3 12a9 9 0 0 1 18 0z M12 12v6.5a2 2 0 0 0 4 0',
  factory: 'M3 21V10l5 3V10l5 3V10l5 3V4h3v17z M7 17h2 M12 17h2 M17 17h1',
  coins: 'M5 6.5a7 3 0 1 0 14 0a7 3 0 1 0-14 0 M5 6.5v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5 M5 11.5v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5',
  heart: 'M12 20s-8-4.7-8-10.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 8 2.5C20 15.3 12 20 12 20z',
  globe: 'M12 21a9 9 0 1 0 0-18a9 9 0 1 0 0 18z M3 12h18 M12 3c2.5 2.7 3.5 5.7 3.5 9s-1 6.3-3.5 9c-2.5-2.7-3.5-5.7-3.5-9s1-6.3 3.5-9z',
  home: 'M3 11l9-7 9 7 M5 10v10h14V10 M10 20v-6h4v6',
  users: 'M9 11a3.5 3.5 0 1 0 0-7a3.5 3.5 0 1 0 0 7z M2.5 20c.8-3.5 3.4-5.5 6.5-5.5s5.7 2 6.5 5.5 M16 4.5a3.5 3.5 0 0 1 0 6.5 M18 14.8c1.8.7 3 2.6 3.5 5.2',
  passport: 'M6 2h12v20H6z M12 13a3 3 0 1 0 0-6a3 3 0 1 0 0 6z M9 17h6',
  parking: 'M4 4h16v16H4z M10 17V7h3.5a3 3 0 0 1 0 6H10',
  flag: 'M5 21V4 M5 4h12l-2 4 2 4H5',
  book: 'M4 4h6a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4z M20 4h-6a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h6z',
  chat: 'M4 5h16v11H9l-5 4z M8 9h8 M8 12h5',
  pin: 'M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z M12 12a2.5 2.5 0 1 0 0-5a2.5 2.5 0 1 0 0 5z',
  shirt: 'M8 3L3 6l2 4 3-1v12h8V9l3 1 2-4-5-3c-.5 1.5-2 2.5-4 2.5S8.5 4.5 8 3z',
  road: 'M8 3L5 21 M16 3l3 18 M12 5v2 M12 11v2 M12 17v2',
  search: 'M10.5 17a6.5 6.5 0 1 0 0-13a6.5 6.5 0 1 0 0 13z M15.5 15.5L21 21',
  user: 'M12 11a4 4 0 1 0 0-8a4 4 0 1 0 0 8z M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5',
  briefcase: 'M3 8h18v12H3z M8 8V5h8v3 M3 13h18',
  cart: 'M3 4h2.5l2.2 10.5h10.6L21 7H6.5 M9 20a1.2 1.2 0 1 0 0-2.4a1.2 1.2 0 1 0 0 2.4z M17 20a1.2 1.2 0 1 0 0-2.4a1.2 1.2 0 1 0 0 2.4z',
  server: 'M4 4h16v6H4z M4 14h16v6H4z M8 7h.01 M8 17h.01 M12 7h5 M12 17h5',
  hand: 'M7 11V5a1.5 1.5 0 0 1 3 0v5 M10 10V3.5a1.5 1.5 0 0 1 3 0V10 M13 10V5a1.5 1.5 0 0 1 3 0v6 M16 9a1.5 1.5 0 0 1 3 0v4c0 4.5-3 8-7.5 8S5 18 4 15l-1.5-3.5a1.5 1.5 0 0 1 2.7-1.3L7 13',
  map: 'M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z M9 3v15 M15 6v15',
  motor: 'M5.5 19a3 3 0 1 0 0-6a3 3 0 1 0 0 6z M18.5 19a3 3 0 1 0 0-6a3 3 0 1 0 0 6z M5.5 16h5.5l3-5.5h3l1.5 5.5 M14 10.5l-1.5-3.5h-2.5 M16.5 7h2.5',
  box: 'M3 7.5l9-4.5 9 4.5v9l-9 4.5-9-4.5z M3 7.5l9 4.5 9-4.5 M12 12v9 M7.5 5.25l9 4.5',
  shoe: 'M3 17v-6l4-1 3 3h4l5.5 1.8a2.5 2.5 0 0 1 1.5 2.3V17z M3 20h18 M9 13l1.5-1.5 M12 13l1.5-1.5',
  headphones: 'M4 15v-3a8 8 0 0 1 16 0v3 M4 15h3v5H4z M17 15h3v5h-3z',
  watch: 'M12 17a5 5 0 1 0 0-10a5 5 0 1 0 0 10z M12 10v2l1.5 1.5 M9 7.5L9.5 3h5l.5 4.5 M9 16.5l.5 4.5h5l.5-4.5',
};
const LEDGE = { gold: '#C8901A', blue: '#003A73', sky: '#1F6FAE' };
/* tile: centred on (x, y), `size` px wide (design: 90-110 in cards, 56-72 in small flows -> 75-92 / 47-60) */
function tile(p, glyph, x, y, { size = 84, v = 'gold', o = 1, floor = true } = {}) {
  const g = G(p, { x, y, o });
  const k = size / 512;
  const t = G(g); t.setAttribute('transform', `scale(${k}) translate(-256 -256)`);
  if (floor) mk('ellipse', { cx: 256, cy: 474, rx: 150, ry: 18, fill: MK.navy, 'fill-opacity': .22 }, t);
  mk('rect', { x: 48, y: 84, width: 416, height: 372, rx: 104, fill: LEDGE[v] }, t);
  mk('rect', { x: 48, y: 48, width: 416, height: 372, rx: 104, fill: `url(#mkFace-${v})` }, t);
  path(t, 'M64 150 Q64 62 160 62 L352 62 Q448 62 448 150 Q256 215 64 150Z', { fill: 'url(#mkGloss)' });
  const gl = G(t); gl.setAttribute('transform', 'translate(136 124) scale(10)');
  path(gl, GLYPH[glyph], { fill: 'none', stroke: '#fff', 'stroke-width': 2, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' });
  return g;
}
/* Motion on a wrapper, never on the element itself: a piece drawn at its own x, y (T, G({x, y})) keeps them, and
   the wrapper's state does the moving. wrap(e, cx, cy) also gives the wrapper a pivot for scaling. */
function wrap(e, cx = 0, cy = 0) {
  const outer = G(e.parentNode, { x: cx, y: cy });
  e.parentNode.insertBefore(outer, e);
  const inner = G(outer);
  if (cx || cy) inner.setAttribute('transform', `translate(${-cx} ${-cy})`);
  inner.appendChild(e);
  return outer;
}
// pop: scale .6 -> 1 with outBack (design.md motion), about the piece's own centre (its box)
const popIn = (e, t0) => {
  const w = wrap(e), inner = w.firstChild;
  let b = { x: 0, y: 0, width: 0, height: 0 };
  try { b = inner.getBBox(); } catch {}
  const cx = b.x + b.width / 2, cy = b.y + b.height / 2;
  inner.setAttribute('transform', `translate(${-cx} ${-cy})`);
  put(w, { x: cx, y: cy, s: .6, o: 0 }); tw(w, { s: 1, o: 1 }, t0, .6, back);
  return w;
};
const slideUp = (e, t0, dur = .6) => { const w = wrap(e); put(w, { o: 0, y: 30 }); tw(w, { o: 1, y: 0 }, t0, dur, out); return w; };
// an arrow drawn on along its direction (gold on navy, navy ink on paper)
function flow(p, d, col, t0, dur = .7, w = 4) {
  const g = G(p);
  draw(path(g, d, { stroke: col, 'stroke-width': w, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', fill: 'none' }, { d: 0 }), t0, dur);
  return g;
}
function mkHead(p, x, y, ang, col, t0, k = 14) {
  const e = path(p, `M${x - k * Math.cos(ang - .5)} ${y - k * Math.sin(ang - .5)}L${x} ${y}L${x - k * Math.cos(ang + .5)} ${y - k * Math.sin(ang + .5)}`,
    { stroke: col, 'stroke-width': 4, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', fill: 'none' }, { o: 0 });
  show(e, t0, .15);
  return e;
}
function mkArrow(p, x1, y1, x2, y2, col, t0, dur = .6) {
  flow(p, `M${x1} ${y1}L${x2} ${y2}`, col, t0, dur);
  mkHead(p, x2, y2, Math.atan2(y2 - y1, x2 - x1), col, t0 + dur - .1);
}

// Poppins must be loaded before the first measure (textW) and frame
function mkBoot() {
  Promise.all(['400', '500', '600', '700'].map(w => document.fonts.load(`${w} 30px Poppins`))).catch(() => {}).finally(boot);
}
