/* PDRI book library: isometric pieces drawn in code (style.json components). Loaded after engine.js.
   Isometric axes: x runs right-down, y runs left-down, z up. Every piece is drawn around its own origin
   (the centre of its footprint on the floor) and placed with put()/G({x, y}). No people: objects carry the story. */
'use strict';

const PD = {
  board: '#0e1d33', floor: '#16294a', floorEdge: '#22395f', ink: '#eef3fb', dim: '#93a4c3', faint: '#4a5d82',
  pabean: '#4da3ff', bm: '#ff8a3d', bmtp: '#ff6f2c', ppn: '#3fcf8e', ppnbm: '#b07cff', pph: '#f5c84b',
  assume: '#ff6b8a', steel: ['#5d7896', '#4f6d7a', '#6f7f99', '#3f5a78'], desk: '#5a6b88', paper: '#f4f1e8', water: '#123a5c',
};
const ISO_C = Math.cos(Math.PI / 6), ISO_S = 0.5;
const iso = (x, y, z = 0) => [(x - y) * ISO_C, (x + y) * ISO_S - z];
const isoPts = pts => pts.map(([x, y, z]) => iso(x, y, z).map(v => v.toFixed(1)).join(' ')).join(' ');
const isoPoly = pts => 'M' + pts.map(([x, y, z]) => iso(x, y, z).map(v => v.toFixed(1)).join(' ')).join('L') + 'Z';
const pdMix = (a, b, q) => mix(a, b, q);
const pdLight = c => pdMix(c, '#ffffff', .28), pdDark = c => pdMix(c, '#000000', .32);

// Rupiah as written in Indonesia: Rp1.528.230.000
function rp(n) {
  const s = String(Math.round(Math.abs(n))).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  return (n < 0 ? '−' : '') + 'Rp' + s;
}
const idNum = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.');

/* isoBlock: a box w (along x) × d (along y) × h (up), three shaded faces. b.set(h) redraws its height;
   b.top(h) is the screen y of the top face's centre. grow() tweens the height on the beat clock. */
function isoBlock(p, { x = 0, y = 0, w = 100, d = 100, h = 40, col = PD.pabean, o = 1, line = true } = {}) {
  const g = G(p, { x, y, o });
  const stroke = line ? { stroke: pdDark(pdDark(col)), 'stroke-width': 1.2, 'stroke-linejoin': 'round' } : {};
  const L = mk('path', { fill: col, ...stroke }, g), R = mk('path', { fill: pdDark(col), ...stroke }, g),
    Tp = mk('path', { fill: pdLight(col), ...stroke }, g);
  const a = w / 2, b = d / 2;
  const b0 = { g, L, R, Tp, w, d, h, col };
  b0.set = hh => {
    hh = Math.max(0, hh); b0.h = hh;
    L.setAttribute('d', isoPoly([[-a, b, 0], [a, b, 0], [a, b, hh], [-a, b, hh]]));
    R.setAttribute('d', isoPoly([[a, -b, 0], [a, b, 0], [a, b, hh], [a, -b, hh]]));
    Tp.setAttribute('d', isoPoly([[-a, -b, hh], [a, -b, hh], [a, b, hh], [-a, b, hh]]));
  };
  b0.top = (hh = b0.h) => -hh;
  b0.set(h);
  return b0;
}
function grow(b, h0, h1, t0, dur = .8, ease = out) { b.set(h0); prog(q => b.set(h0 + (h1 - h0) * q), t0, dur, ease); }

// a flat floor slab (a quay, a platform) with a soft shadow edge
function isoFloor(p, { x = 0, y = 0, w = 600, d = 400, h = 14, col = PD.floor, o = 1 } = {}) {
  const f = isoBlock(p, { x, y, w, d, h, col, o, line: false });
  f.Tp.setAttribute('stroke', PD.floorEdge); f.Tp.setAttribute('stroke-width', 1.5);
  return f;
}

// a pill label: text on a coloured or outlined capsule, centred on (x, y)
function pdTag(p, str, x, y, col, { size = 24, solid = true, o = 0, weight = 700, ink } = {}) {
  const g = G(p, { x, y, o });
  const w = textW(str, size) * 1.08 + size * 1.3, hh = size * 1.6;
  mk('rect', { x: -w / 2, y: -hh / 2, width: w, height: hh, rx: hh / 2, fill: solid ? col : PD.board, stroke: col, 'stroke-width': 2.5 }, g);
  T(g, str, { x: 0, y: size * .36, size, weight, anchor: 'middle', fill: ink || (solid ? '#0b1526' : col) });
  g._w = w;
  return g;
}

// a label with a leader line from a point on a piece to the text (text starts at tx, ty)
function pdCallout(p, str, fromX, fromY, tx, ty, col, { size = 26, sub, o = 0, weight = 700, anchor = 'start' } = {}) {
  const g = G(p, { o });
  const ex = anchor === 'start' ? tx - 12 : tx + 12;
  path(g, `M${fromX} ${fromY}L${ex} ${ty - size * .35}`, { stroke: col, 'stroke-width': 2, fill: 'none', 'stroke-dasharray': '4 5' });
  mk('circle', { cx: fromX, cy: fromY, r: 5, fill: col }, g);
  T(g, str, { x: tx, y: ty, size, weight, fill: col, anchor });
  if (sub) T(g, sub, { x: tx, y: ty + size * 1.15, size: size * .72, weight: 500, fill: PD.dim, anchor });
  return g;
}

/* container: long along x, doors on the +x end (the right face). c.doors fades to open it. */
function container(p, { x = 0, y = 0, w = 200, d = 80, h = 80, col = PD.steel[0], o = 1, ribs = 9 } = {}) {
  const c = isoBlock(p, { x, y, w, d, h, col, o });
  const a = w / 2, b = d / 2;
  let dl = '';
  for (let i = 1; i <= ribs; i++) { const xx = -a + i * w / (ribs + 1); dl += isoPoly([[xx, b, 4], [xx, b, h - 4], [xx, b, h - 4], [xx, b, 4]]); }
  path(c.g, dl, { stroke: pdDark(col), 'stroke-width': 2, fill: 'none' });
  const doors = G(c.g);
  mk('path', { d: isoPoly([[a, -b + 4, 4], [a, 0, 4], [a, 0, h - 4], [a, -b + 4, h - 4]]), fill: pdDark(pdDark(col)), stroke: pdDark(col) }, doors);
  mk('path', { d: isoPoly([[a, 0, 4], [a, b - 4, 4], [a, b - 4, h - 4], [a, 0, h - 4]]), fill: pdDark(pdDark(col)), stroke: pdDark(col) }, doors);
  const [hx, hy] = iso(a, -b / 2, h / 2), [hx2, hy2] = iso(a, b / 2, h / 2);
  path(doors, `M${hx} ${hy - 18}V${hy + 18}M${hx2} ${hy2 - 18}V${hy2 + 18}`, { stroke: PD.dim, 'stroke-width': 3 });
  const inside = mk('path', { d: isoPoly([[a, -b + 4, 4], [a, b - 4, 4], [a, b - 4, h - 4], [a, -b + 4, h - 4]]), fill: '#0a1322' }, c.g);
  c.g.insertBefore(inside, doors);
  c.doors = doors;
  put(doors, { o: 1 });
  return c;
}

/* fabric roll lying along x: length len, radius r, colour col. Drawn around its centre on the floor. */
function fabricRoll(p, { x = 0, y = 0, len = 110, r = 18, col = '#e8e2d2', o = 1 } = {}) {
  const g = G(p, { x, y, o });
  const end = (xx) => {
    const pts = [];
    for (let i = 0; i < 28; i++) { const t = i / 28 * Math.PI * 2; pts.push(iso(xx, Math.cos(t) * r, r + Math.sin(t) * r)); }
    return pts;
  };
  const e0 = end(-len / 2), e1 = end(len / 2);
  // body: hull of both ends (bottom-left to top-right silhouette)
  const all = [...e0, ...e1];
  const cx = all.reduce((s, q) => s + q[0], 0) / all.length, cy = all.reduce((s, q) => s + q[1], 0) / all.length;
  all.sort((A, B) => Math.atan2(A[1] - cy, A[0] - cx) - Math.atan2(B[1] - cy, B[0] - cx));
  const hull = [];
  for (const q of all) {   // monotone chain on angle-sorted points is enough for this convex pair of ellipses
    while (hull.length >= 2) { const [a1, a2] = [hull[hull.length - 2], hull[hull.length - 1]]; if ((a2[0] - a1[0]) * (q[1] - a1[1]) - (a2[1] - a1[1]) * (q[0] - a1[0]) <= 0) hull.pop(); else break; }
    hull.push(q);
  }
  mk('path', { d: 'M' + hull.map(q => q.map(v => v.toFixed(1)).join(' ')).join('L') + 'Z', fill: pdDark(col) }, g);
  mk('path', { d: 'M' + e1.map(q => q.map(v => v.toFixed(1)).join(' ')).join('L') + 'Z', fill: col, stroke: pdDark(col), 'stroke-width': 1 }, g);
  const [c1x, c1y] = iso(len / 2, 0, r);
  mk('ellipse', { cx: c1x, cy: c1y, rx: r * .32, ry: r * .38, fill: 'none', stroke: pdDark(col), 'stroke-width': 1.5, transform: `rotate(-30 ${c1x} ${c1y})` }, g);
  return g;
}

/* ship: hull along x with stacked containers on deck */
function ship(p, { x = 0, y = 0, len = 520, beam = 130, o = 1 } = {}) {
  const g = G(p, { x, y, o });
  const a = len / 2, b = beam / 2, hh = 46;
  // hull: a box with a pointed bow at +x
  mk('path', { d: isoPoly([[-a, b, 0], [a - 40, b, 0], [a + 30, 0, hh], [a - 40, b, hh], [-a, b, hh]]), fill: '#24344f' }, g);
  mk('path', { d: isoPoly([[-a, b, 0], [a - 40, b, 0], [a - 40, b, hh], [-a, b, hh]]), fill: '#2c3e5c', stroke: '#1a2840' }, g);
  mk('path', { d: isoPoly([[a - 40, b, 0], [a + 30, 0, hh], [a - 40, b, hh]]), fill: '#22324c' }, g);
  mk('path', { d: isoPoly([[a - 40, -b, 0], [a + 30, 0, hh], [a - 40, b, 0]]), fill: '#1d2b44' }, g);
  mk('path', { d: isoPoly([[-a, -b, hh], [a - 40, -b, hh], [a + 30, 0, hh], [a - 40, b, hh], [-a, b, hh]]), fill: '#3a4d6d', stroke: '#2c3e5c' }, g);
  // red waterline stripe
  mk('path', { d: isoPoly([[-a, b, 8], [a - 40, b, 8], [a - 40, b, 16], [-a, b, 16]]), fill: '#8e3b46' }, g);
  // bridge at the stern
  isoBlock(g, { x: iso(-a + 45, 0, 0)[0], y: iso(-a + 45, 0, 0)[1] - hh, w: 60, d: beam - 20, h: 70, col: '#d7dde8' });
  // container stacks
  const deck = G(g);
  const cols = 5, rows = 2, cw = (len - 180) / cols;
  for (let i = 0; i < cols; i++) for (let j = 0; j < rows; j++) for (let k = 0; k < 2; k++) {
    const cx = -a + 120 + cw * (i + .5), cy = -b / 2 + j * b;
    const [sx, sy] = iso(cx, cy, hh + k * 34);
    isoBlock(deck, { x: sx, y: sy, w: cw - 6, d: b - 6, h: 34, col: PD.steel[(i + j + k) % 4] });
  }
  g.deck = deck;
  return g;
}

/* quay crane: legs on the floor, a boom out over the water, a trolley cable */
function crane(p, { x = 0, y = 0, h = 260, o = 1, col = '#e0b84a' } = {}) {
  const g = G(p, { x, y, o });
  const leg = (xx, yy) => iso(xx, yy, 0), top = (xx, yy) => iso(xx, yy, h);
  const P = (q) => q.map(v => v.toFixed(1)).join(' ');
  const L = [[-30, -30], [30, -30], [30, 30], [-30, 30]];
  let d = '';
  for (const [xx, yy] of L) d += `M${P(leg(xx, yy))}L${P(top(xx, yy))}`;
  d += `M${P(top(-30, -30))}L${P(top(-30, 30))}M${P(top(30, -30))}L${P(top(30, 30))}`;
  // the boom runs along -y (out to the water on the left)
  d += `M${P(top(-30, 40))}L${P(top(-30, -260))}M${P(top(30, 40))}L${P(top(30, -260))}`;
  d += `M${P(iso(0, 30, h + 60))}L${P(top(0, -260))}M${P(iso(0, 30, h + 60))}L${P(top(0, 40))}`;
  path(g, d, { stroke: col, 'stroke-width': 6, fill: 'none', 'stroke-linecap': 'round' });
  g.hook = (yy) => iso(0, yy, h);   // where the trolley hangs, in the crane's own coordinates
  return g;
}

/* serviceDesk: a counter with a monitor, a document tray and a hanging sign. No people. */
function serviceDesk(p, { x = 0, y = 0, o = 1, sign = 'MEJA LAYANAN' } = {}) {
  const g = G(p, { x, y, o });
  isoFloor(g, { w: 360, d: 260, h: 8, col: '#1b3155' });
  const c = isoBlock(g, { x: iso(0, 30)[0], y: iso(0, 30)[1], w: 260, d: 70, h: 86, col: PD.desk });
  // monitor on the counter
  const [mx, my] = iso(-60, 20, 86);
  isoBlock(g, { x: mx, y: my, w: 16, d: 16, h: 30, col: '#33435e' });
  const scr = G(g, { x: mx, y: my - 30 });
  mk('path', { d: isoPoly([[0, -46, 0], [0, 46, 0], [0, 46, 64], [0, -46, 64]]), fill: '#1f2d45', stroke: '#33435e', 'stroke-width': 3 }, scr);
  mk('path', { d: isoPoly([[2, -40, 6], [2, 40, 6], [2, 40, 58], [2, -40, 58]]), fill: '#2f6db5', opacity: .85 }, scr);
  // document tray with a sheet
  const [tx, ty] = iso(70, 30, 86);
  isoBlock(g, { x: tx, y: ty, w: 70, d: 52, h: 8, col: '#2a3a55' });
  const sheet = G(g, { x: tx, y: ty - 9 });
  mk('path', { d: isoPoly([[-30, -22, 0], [30, -22, 0], [30, 22, 0], [-30, 22, 0]]), fill: PD.paper }, sheet);
  let lines = '';
  for (let i = 0; i < 4; i++) lines += isoPoly([[-22 + i * 13, -16, .5], [-22 + i * 13 + 2, -16, .5], [-22 + i * 13 + 2, 16, .5], [-22 + i * 13, 16, .5]]);
  path(sheet, lines, { fill: '#b9c2d3', stroke: 'none' });
  // hanging sign
  const [sx, sy] = iso(0, -40, 230);
  const sg = G(g, { x: sx, y: sy });
  path(sg, 'M-70 -60V-20M70 -60V-20', { stroke: PD.faint, 'stroke-width': 2 });
  mk('rect', { x: -110, y: -22, width: 220, height: 44, rx: 8, fill: '#183059', stroke: PD.pabean, 'stroke-width': 2 }, sg);
  T(sg, sign, { y: 9, size: 20, weight: 700, anchor: 'middle', fill: PD.ink });
  g.sheet = sheet; g.counterTop = iso(0, 30, 86);
  return g;
}

// a question card that rises from a point (the desk): a rounded card with a small tail, no speaker drawn
function askCard(p, str, x, y, { w = 420, size = 30, col = PD.ink, o = 0, tailX = 0 } = {}) {
  const g = G(p, { x, y, o });
  const hh = size * 2.4;
  mk('path', { d: `M${-w / 2} ${-hh / 2}h${w}v${hh}H${tailX + 22}l-22 26l-6 -26H${-w / 2}Z`, fill: '#f4f6fb', stroke: '#c9d3e6', 'stroke-width': 2, 'stroke-linejoin': 'round' }, g);
  T(g, str, { y: size * .36, size, weight: 700, anchor: 'middle', fill: '#0e1d33' });
  return g;
}

// the 'asumsi latihan' stamp for figures marked (cek) in the source
function assumeStamp(p, x, y, { r = -8, s = 1, o = 0, str = 'ASUMSI LATIHAN' } = {}) {
  const g = G(p, { x, y, r, s, o });
  const w = textW(str, 18) * 1.2 + 26;
  mk('rect', { x: -w / 2, y: -17, width: w, height: 34, rx: 5, fill: 'none', stroke: PD.assume, 'stroke-width': 3 }, g);
  T(g, str, { y: 7, size: 18, weight: 800, anchor: 'middle', fill: PD.assume });
  return g;
}

/* calcCard: the step calculator. rows: { label, formula, result, col }. Each row's parts appear on their own
   times via c.row(i, tLabel, tResult): label and formula at tLabel, the result counts up at tResult. */
function calcCard(p, x, y, w, rows, { title = 'Langkah hitung', rowH = 96, o = 0 } = {}) {
  const g = G(p, { x, y, o });
  const H = 70 + rows.length * rowH;
  mk('rect', { x: 0, y: 0, width: w, height: H, rx: 16, fill: '#13284a', stroke: '#2a4470', 'stroke-width': 2 }, g);
  T(g, title.toUpperCase(), { x: 28, y: 44, size: 20, weight: 700, fill: PD.dim });
  const els = rows.map((r, i) => {
    const ry = 70 + i * rowH;
    const rg = G(g, { o: 0 });
    if (i) mk('rect', { x: 24, y: ry, width: w - 48, height: 1.5, fill: '#2a4470' }, rg);
    mk('rect', { x: 24, y: ry + 22, width: 8, height: rowH - 40, rx: 4, fill: r.col }, rg);
    T(rg, r.label, { x: 48, y: ry + 38, size: 22, weight: 600, fill: PD.dim });
    T(rg, r.formula, { x: 48, y: ry + 74, size: 26, weight: 500, fill: PD.ink });
    const res = T(g, '', { x: w - 28, y: ry + 74, size: 30, weight: 800, fill: r.col, anchor: 'end', o: 0 });
    return { rg, res, value: r.result };
  });
  g.row = (i, tLabel, tResult, count = .9) => {
    const e = els[i];
    show(e.rg, tLabel, .45);
    if (tResult === undefined) return;
    show(e.res, tResult, .2);
    prog(q => { e.res.textContent = rp(e.value * q); }, tResult, count, out);
  };
  g.els = els; g.H = H;
  return g;
}

// gentle continuous drift for water ripples and such, a pure function of the beat clock
function ripples(p, { x0 = 0, y0 = 0, w = 600, n = 10, col = '#2e6a98', D = 30, o = .6 } = {}) {
  const g = G(p, { o });
  const els = [];
  for (let i = 0; i < n; i++) {
    const e = path(g, 'M0 0h34', { stroke: col, 'stroke-width': 3, 'stroke-linecap': 'round' });
    els.push({ e, bx: x0 + ((i * 197) % w), by: y0 + ((i * 61) % 120), ph: i * .7 });
  }
  clockRun(t => {
    for (const r of els) {
      const k = ((t * 14 + r.ph * 20) % 60) - 30;
      put(r.e, { x: r.bx + k * ISO_C, y: r.by + k * ISO_S, o: .35 + .35 * Math.sin(t * .9 + r.ph) });
    }
  }, D, { tail: true });
  return g;
}
