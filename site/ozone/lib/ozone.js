'use strict';
/* Protecting the Ozone Layer: the book's shared pieces (style.json "components").
   Loaded after engine.js. Everything is drawn around its own origin and placed with G()/put().
   Colours mean the same thing in every chapter (style.json look.meaning). */

const OZ = {
  uvC: '#8a5cf6', uvB: '#a77bff', uvA: '#c9b3ff',
  ozone: '#5cc8ff', oxygen: '#9fe3ff', ods: '#ff8a3d', law: '#ffd166', good: '#5fd39a', climate: '#ff6b7d',
  ink: '#eef3fb', dim: '#93a4c3', faint: '#4a5d82', ground: '#1d3b2f', land: '#2f5a45', sea: '#123a6b', ice: '#dfe9f5',
  carbon: '#7d8799', fluorine: '#c8e07a', bromine: '#c0603a', smog: '#b08a5a',
};

/* ---------- ambient life ----------
   Things on screen keep a gentle motion of their own (molecules drift, the Sun's glow breathes, the ozone band
   shimmers), so a picture never freezes while the narrator talks. Constructors register what may move with ozBob();
   each beat calls ozLive() once, last, which drives everything registered since the previous call from the beat clock.
   Bob only a key nothing else tweens: molecules bob an inner group, so their own x/y tweens stay free. */
let OZ_BOB = [];
function ozBob(e, { amp = 4, per = 3.2, key = 'y', base = 0 } = {}) {
  OZ_BOB.push({ e, amp, per, key, base, ph: (OZ_BOB.length * 1.618) % (Math.PI * 2) });
  return e;
}
function ozLive() {
  const list = OZ_BOB; OZ_BOB = [];
  if (!list.length) return;
  clockRun(t => { for (const b of list) put(b.e, { [b.key]: b.base + b.amp * Math.sin(t / b.per * Math.PI * 2 + b.ph) }); }, 0, { tail: true });
}

/* ---------- small text helpers ---------- */
// a label that starts hidden; reveal it with show()
function ozLabel(p, str, x, y, { size = 28, fill = OZ.ink, anchor = 'start', weight = 600 } = {}) {
  return T(p, str, { x, y, size, fill, anchor, weight, o: 0 });
}
// a rounded tag: coloured outline with text, centred on (x, y)
function ozTag(p, str, x, y, colr, { size = 26, pad = 18, fill = 'rgba(8,16,36,.82)' } = {}) {
  const g = G(p, { x, y, o: 0 });
  const w = textW(str, size) * 1.02 + pad * 2, h = size * 1.7;
  mk('rect', { x: -w / 2, y: -h / 2, width: w, height: h, rx: h / 2, fill, stroke: colr, 'stroke-width': 2.5 }, g);
  T(g, str, { x: 0, y: size * .36, size, fill: colr, anchor: 'middle', weight: 650 });
  g.w = w;
  return g;
}

/* ---------- molecules ---------- */
const ATOM = {
  O:  { fill: OZ.oxygen, r: 30, ink: '#0b1730' },
  Oz: { fill: OZ.ozone,  r: 30, ink: '#0b1730', sym: 'O' },   // an oxygen atom that is part of ozone
  Cl: { fill: OZ.ods,    r: 38, ink: '#2a1204' },
  Br: { fill: OZ.bromine, r: 40, ink: '#fff2e8' },
  C:  { fill: OZ.carbon, r: 32, ink: '#0b1730' },
  F:  { fill: OZ.fluorine, r: 26, ink: '#1c2608' },
};
// one atom drawn around (0,0); { eyes: true } gives it two simple eyes (the chlorine "villain", the ozone trio)
function atom(p, kind, x = 0, y = 0, { r, eyes = false, o = 1, s = 1, bob = true } = {}) {
  const a = ATOM[kind], R = r || a.r, g0 = G(p, { x, y, o, s }), g = G(g0, {});
  if (bob) ozBob(g, { amp: 3.5, per: 2.6 + (x % 7) * .1 });
  mk('circle', { r: R, fill: a.fill, stroke: 'rgba(0,0,0,.35)', 'stroke-width': 2 }, g);
  mk('ellipse', { cx: -R * .32, cy: -R * .38, rx: R * .38, ry: R * .24, fill: '#fff', opacity: .35 }, g);
  if (eyes) {
    for (const ex of [-R * .3, R * .3]) {
      mk('ellipse', { cx: ex, cy: -R * .05, rx: R * .13, ry: R * .17, fill: '#fff' }, g);
      mk('circle', { cx: ex + R * .03, cy: -R * .02, r: R * .07, fill: '#10162a' }, g);
    }
    T(g, a.sym || kind, { y: R * .62, size: R * .42, fill: a.ink, anchor: 'middle', weight: 800 });
  } else {
    T(g, a.sym || kind, { y: R * .3, size: R * .8, fill: a.ink, anchor: 'middle', weight: 750 });
  }
  g0.R = R;
  return g0;
}
// a bond line between two atoms (drawn under them); returns the path so it can be faded or "snapped"
function bond(p, x1, y1, x2, y2, o = 1) {
  return path(p, `M${x1} ${y1}L${x2} ${y2}`, { stroke: 'rgba(238,243,251,.55)', 'stroke-width': 7, 'stroke-linecap': 'round' }, { o });
}
// O₂: two oxygen atoms side by side around (0,0); .a and .b are the atoms, .bond the bond
function O2(p, x, y, { o = 1, kind = 'O' } = {}) {
  const g = G(p, { x, y, o }), in_ = ozBob(G(g, {}), { amp: 4, per: 3.1 });
  g.bond = bond(in_, -26, 0, 26, 0);
  g.a = atom(in_, kind, -26, 0, { bob: false }); g.b = atom(in_, kind, 26, 0, { bob: false });
  return g;
}
// O₃: three oxygen atoms in a bent chain (the ozone trio); .atoms[0..2], .bonds[0..1]
function O3(p, x, y, { o = 1, eyes = false } = {}) {
  const g = G(p, { x, y, o }), in_ = ozBob(G(g, {}), { amp: 4.5, per: 3.4 });
  const pts = [[-46, 18], [0, -14], [46, 18]];
  g.bonds = [bond(in_, ...pts[0], ...pts[1]), bond(in_, ...pts[1], ...pts[2])];
  g.atoms = pts.map(([ax, ay], i) => atom(in_, 'Oz', ax, ay, { eyes: eyes && i === 1, bob: false }));
  g.pts = pts;
  return g;
}
// a CFC (CFC-11, CCl₃F): carbon in the middle, three chlorines and one fluorine; .cl[0..2], .f, .c, .bonds
function CFC(p, x, y, { o = 1, s = 1 } = {}) {
  const g = G(p, { x, y, o, s }), in_ = ozBob(G(g, {}), { amp: 4, per: 3.6 });
  const arms = [[0, -72, 'Cl'], [-66, 40, 'Cl'], [66, 40, 'Cl'], [0, 0, 'F']];
  g.bonds = arms.slice(0, 3).map(([ax, ay]) => bond(in_, 0, 0, ax, ay));
  g.f = atom(in_, 'F', 30, -28, { r: 24, bob: false });   // fluorine sits behind, up and right
  g.c = atom(in_, 'C', 0, 0, { bob: false });
  g.cl = arms.slice(0, 3).map(([ax, ay]) => atom(in_, 'Cl', ax, ay, { r: 32, bob: false }));
  return g;
}

/* ---------- the atmosphere cross-section ---------- */
// box: x, y (top), w, h (top = top km). Returns { g, yAt(km), parts… } with the bands hidden (o: 0) for reveals:
//   .ground, .tropo, .strato, .band (ozone layer 15–35 km), .axis; .topKm. Heights are to scale.
function atmosphere(p, { x = 220, y = 70, w = 900, h = 720, top = 60, tropoTop = 12, o = 1 } = {}) {
  const g = G(p, { o });
  const yAt = km => y + h - km / top * h;
  const A = { g, yAt, x, y, w, h, top };
  // troposphere: a soft, slightly lighter air band
  A.tropo = G(g, { o: 0 });
  mk('rect', { x, y: yAt(tropoTop), width: w, height: yAt(0) - yAt(tropoTop), fill: '#1a3a6a', opacity: .55 }, A.tropo);
  for (const [cx, cy, s] of [[x + w * .22, yAt(4), 1], [x + w * .62, yAt(6.5), .8], [x + w * .86, yAt(3), .7]]) cloud(A.tropo, cx, cy, s);
  // stratosphere
  A.strato = G(g, { o: 0 });
  mk('rect', { x, y: yAt(50), width: w, height: yAt(tropoTop) - yAt(50), fill: '#13284f', opacity: .7 }, A.strato);
  // above 50 km: darker
  A.space = G(g, { o: 0 });
  mk('rect', { x, y: yAt(top), width: w, height: yAt(50) - yAt(top), fill: '#060d22', opacity: .8 }, A.space);
  // the ozone layer, 15–35 km, glowing blue, with a scatter of tiny O₃ dots
  A.band = G(g, { o: 0 });
  const by0 = yAt(35), by1 = yAt(15);
  mk('rect', { x, y: by0, width: w, height: by1 - by0, fill: OZ.ozone, opacity: .16 }, A.band);
  mk('rect', { x, y: (by0 + by1) / 2 - (by1 - by0) * .22, width: w, height: (by1 - by0) * .44, fill: OZ.ozone, opacity: .14 }, A.band);
  let seed = 11; const rnd = () => (seed = seed * 16807 % 2147483647) / 2147483647;
  let dots = '';
  for (let i = 0; i < 70; i++) { const dx = x + 10 + rnd() * (w - 20), dy = by0 + 6 + rnd() * (by1 - by0 - 12); dots += `M${dx.toFixed(1)} ${dy.toFixed(1)}m-3 0a3 3 0 1 0 6 0a3 3 0 1 0-6 0`; }
  ozBob(path(A.band, dots, { fill: OZ.ozone, 'fill-opacity': .75, 'stroke-opacity': .75 }), { amp: 6, per: 7, key: 'x' });
  // ground
  A.ground = G(g, {});
  mk('rect', { x: x - 30, y: yAt(0), width: w + 60, height: 22, rx: 6, fill: OZ.ground }, A.ground);
  path(A.ground, `M${x - 30} ${yAt(0)}H${x + w + 30}`, { stroke: OZ.good, 'stroke-width': 3, 'fill-opacity': .6, 'stroke-opacity': .6 });
  // altitude axis on the left
  A.axis = G(g, {});
  path(A.axis, `M${x - 40} ${yAt(0)}V${yAt(top)}`, { stroke: OZ.dim, 'stroke-width': 2, 'fill-opacity': .7, 'stroke-opacity': .7 });
  for (let km = 0; km <= top; km += 10) {
    path(A.axis, `M${x - 48} ${yAt(km)}H${x - 32}`, { stroke: OZ.dim, 'stroke-width': 2, 'fill-opacity': .7, 'stroke-opacity': .7 });
    T(A.axis, `${km}`, { x: x - 58, y: yAt(km) + 8, size: 22, fill: OZ.dim, anchor: 'end', weight: 500 });
  }
  T(A.axis, 'km', { x: x - 58, y: yAt(top) - 22, size: 20, fill: OZ.dim, anchor: 'end', weight: 600 });
  return A;
}
function cloud(p, x, y, s = 1) {
  const g = G(p, { x, y, s });
  ozBob(g, { amp: 14, per: 9 + s * 3, key: 'x', base: x });
  path(g, 'M-60 10a26 26 0 0 1 22-30a34 34 0 0 1 62-6a24 24 0 0 1 36 24a16 16 0 0 1-4 22H-52a14 14 0 0 1-8-10z', { fill: '#cfe0f5', 'fill-opacity': .28, 'stroke-opacity': .28 });
  return g;
}

/* ---------- UV rays ---------- */
// A wavy ray from (x, y0) straight down to y1, drawn on with draw(). kind 'C' | 'B' | 'A'.
// Returns { g, ray, head, burst, label }: head is an arrowhead at the end (for a ray that arrives),
// burst a small starburst at the end (for a ray that is absorbed). All start hidden.
function uvRay(p, kind, x, y0, y1, { label = true, width } = {}) {
  const colr = OZ['uv' + kind], wl = { C: 26, B: 36, A: 48 }[kind], amp = { C: 9, B: 10, A: 11 }[kind];
  const g = G(p, {});
  let d = `M${x} ${y0}`;
  for (let yy = y0; yy < y1; yy += 4) d += `L${(x + amp * Math.sin((yy - y0) / wl * Math.PI * 2)).toFixed(1)} ${Math.min(yy + 4, y1)}`;
  const R = { g, colr };
  R.ray = path(g, d, { fill: 'none', stroke: colr, 'stroke-width': width || 5, 'stroke-linecap': 'round' }, { d: 0 });
  R.head = G(g, { x, y: y1, o: 0 });
  path(R.head, 'M-14 -16L0 4L14 -16', { fill: 'none', stroke: colr, 'stroke-width': 5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' });
  R.burst = G(g, { x, y: y1, o: 0, s: .3 });
  let b = '';
  for (let i = 0; i < 8; i++) { const a = i / 8 * Math.PI * 2; b += `M${(Math.cos(a) * 10).toFixed(1)} ${(Math.sin(a) * 10).toFixed(1)}L${(Math.cos(a) * 24).toFixed(1)} ${(Math.sin(a) * 24).toFixed(1)}`; }
  path(R.burst, b, { stroke: colr, 'stroke-width': 4, 'stroke-linecap': 'round' });
  mk('circle', { r: 8, fill: colr }, R.burst);
  if (label) R.label = ozLabel(g, 'UV-' + kind, x, y0 - 18, { size: 26, fill: colr, anchor: 'middle', weight: 750 });
  return R;
}
// play a ray: label, draw down, then absorbed (burst) or arrives (head)
function playRay(R, t0, dur = 1, absorbed = true) {
  if (R.label) show(R.label, t0, .3);
  draw(R.ray, t0, dur, lin);
  if (absorbed) { tw(R.burst, { o: 1, s: 1 }, t0 + dur, .3, back); tw(R.burst, { o: .55 }, t0 + dur + .4, .5); }
  else show(R.head, t0 + dur - .1, .2);
}

/* ---------- the Sun ---------- */
function sun(p, x, y, r = 70, o = 1) {
  const g = G(p, { x, y, o }), halo = ozBob(G(g, { s: 1 }), { amp: .08, per: 4, key: 's', base: 1 });
  mk('circle', { r: r * 2.1, fill: '#ffd166', opacity: .07 }, halo);
  mk('circle', { r: r * 1.5, fill: '#ffd166', opacity: .12 }, halo);
  mk('circle', { r, fill: '#ffd57a' }, g);
  mk('circle', { r: r * .78, fill: '#ffe39e' }, g);
  return g;
}

/* ---------- the globe, seen from above the South Pole ---------- */
// Drawn around (0,0) with radius r. .hole is the ozone-hole patch (scale it with s), .ice Antarctica,
// .vortex a ring of wind arrows (rotate it with r), .clouds polar stratospheric clouds. All decorations start hidden.
function globe(p, x, y, r = 280, { o = 1 } = {}) {
  const g = G(p, { x, y, o });
  const k = r / 280;
  mk('circle', { r: r + 14, fill: OZ.ozone, opacity: .12 }, g);   // the ozone layer around the planet, a thin glow
  mk('circle', { r, fill: OZ.sea }, g);
  const land = G(g, { s: k });
  // southern tips of the continents at the rim (stylised, not a map)
  path(land, 'M-118 -276C-96 -238 -104 -196 -78 -170C-62 -184 -58 -224 -52 -276Z', { fill: OZ.land });          // South America
  path(land, 'M206 -190C188 -170 172 -150 182 -132C214 -142 236 -168 246 -184Z', { fill: OZ.land });             // Africa's tip
  path(land, 'M196 150C176 168 166 196 186 214C220 212 246 192 252 168C236 150 214 146 196 150Z', { fill: OZ.land }); // Australia
  path(land, 'M70 246C78 232 96 230 98 244C92 258 78 262 70 246Z', { fill: OZ.land });                          // New Zealand
  g.ice = G(g, { s: k });
  path(g.ice, 'M-120 -40C-150 -90 -96 -128 -40 -118C0 -150 60 -132 92 -96C142 -80 150 -20 120 20C130 70 92 112 40 104C0 128 -60 120 -86 84C-130 70 -150 10 -120 -40Z', { fill: OZ.ice });
  path(g.ice, 'M-150 -60C-176 -50 -190 -30 -176 -18C-160 -24 -150 -40 -150 -60Z', { fill: OZ.ice });           // the peninsula
  // the hole: a soft orange patch, centred on the pole, drawn at "full" size; scale with s
  g.hole = G(g, { s: 0, o: .9 });
  mk('circle', { r: 180 * k, fill: OZ.ods, opacity: .12 }, g.hole);
  path(g.hole, `M${-150 * k} 0C${-150 * k} ${-110 * k} ${-60 * k} ${-170 * k} ${20 * k} ${-160 * k}C${110 * k} ${-150 * k} ${165 * k} ${-80 * k} ${158 * k} 0C${150 * k} ${90 * k} ${80 * k} ${150 * k} 0 ${150 * k}C${-90 * k} ${150 * k} ${-150 * k} ${90 * k} ${-150 * k} 0Z`,
    { fill: OZ.ods, 'fill-opacity': .3, stroke: OZ.ods, 'stroke-width': 3, 'stroke-dasharray': '10 8' });
  // polar vortex: four curved arrows in a ring
  g.vortex = G(g, { o: 0 });
  for (let i = 0; i < 4; i++) {
    const a0 = i * 90 + 10, a1 = a0 + 60, rr = r * .78;
    const p0 = [Math.cos(a0 * Math.PI / 180) * rr, Math.sin(a0 * Math.PI / 180) * rr], p1 = [Math.cos(a1 * Math.PI / 180) * rr, Math.sin(a1 * Math.PI / 180) * rr];
    path(g.vortex, `M${p0[0].toFixed(1)} ${p0[1].toFixed(1)}A${rr} ${rr} 0 0 1 ${p1[0].toFixed(1)} ${p1[1].toFixed(1)}`, { fill: 'none', stroke: OZ.ink, 'stroke-width': 6, 'stroke-linecap': 'round', 'fill-opacity': .8, 'stroke-opacity': .8 });
    const ah = (a1 + 4) * Math.PI / 180, tx = -Math.sin(a1 * Math.PI / 180), ty = Math.cos(a1 * Math.PI / 180);
    const hx = Math.cos(ah) * rr, hy = Math.sin(ah) * rr;
    path(g.vortex, `M${(hx - tx * 20 - ty * 14).toFixed(1)} ${(hy - ty * 20 + tx * 14).toFixed(1)}L${hx.toFixed(1)} ${hy.toFixed(1)}L${(hx - tx * 20 + ty * 14).toFixed(1)} ${(hy - ty * 20 - tx * 14).toFixed(1)}`, { fill: 'none', stroke: OZ.ink, 'stroke-width': 6, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'fill-opacity': .8, 'stroke-opacity': .8 });
  }
  // polar stratospheric clouds: pearly wisps over the ice
  g.clouds = G(g, { o: 0, s: k });
  for (const [cx, cy, w, c] of [[-70, -50, 120, '#f2b6e6'], [40, -10, 140, '#b6e9f2'], [-20, 60, 110, '#f6e0a6']]) {
    path(g.clouds, `M${cx - w / 2} ${cy}C${cx - w / 4} ${cy - 22} ${cx + w / 4} ${cy - 22} ${cx + w / 2} ${cy}C${cx + w / 4} ${cy + 10} ${cx - w / 4} ${cy + 10} ${cx - w / 2} ${cy}Z`, { fill: c, 'fill-opacity': .75, 'stroke-opacity': .75 });
  }
  return g;
}

/* ---------- the treaty timeline ---------- */
// A gold line from x0 to x1 at y for the years [y0, y1]; pins: [{ year, label, sub?, up? }].
// Returns { g, xAt(year), line, pins: [{ g, year }] }; line starts undrawn, pins hidden.
function timeline(p, { x0 = 160, x1 = 1440, y = 520, from = 1970, to = 2020, pins = [], ticks = 10 } = {}) {
  const g = G(p, {});
  const xAt = yr => x0 + (yr - from) / (to - from) * (x1 - x0);
  const L = { g, xAt };
  L.line = path(g, `M${x0} ${y}H${x1}`, { stroke: OZ.law, 'stroke-width': 4, 'stroke-linecap': 'round', 'fill-opacity': .8, 'stroke-opacity': .8 }, { d: 0 });
  L.ticks = G(g, { o: 0 });
  for (let yr = Math.ceil(from / ticks) * ticks; yr <= to; yr += ticks) {
    path(L.ticks, `M${xAt(yr)} ${y - 8}V${y + 8}`, { stroke: OZ.law, 'stroke-width': 3, 'fill-opacity': .7, 'stroke-opacity': .7 });
    T(L.ticks, String(yr), { x: xAt(yr), y: y + 42, size: 22, fill: OZ.dim, anchor: 'middle', weight: 500 });
  }
  L.pins = pins.map(({ year, label, sub, up = true }) => {
    const pg = G(g, { x: xAt(year), y, o: 0 });
    const dy = up ? -1 : 1;
    path(pg, `M0 0V${dy * 70}`, { stroke: OZ.law, 'stroke-width': 3 });
    mk('circle', { r: 10, fill: OZ.law }, pg);
    T(pg, String(year), { y: dy * 70 + (up ? -44 : 34), size: 30, fill: OZ.law, anchor: 'middle', weight: 750 });
    T(pg, label, { y: dy * 70 + (up ? -12 : 64), size: 24, fill: OZ.ink, anchor: 'middle', weight: 600 });
    if (sub) T(pg, sub, { y: dy * 70 + (up ? 14 : 90), size: 20, fill: OZ.dim, anchor: 'middle', weight: 500 });
    return { g: pg, year };
  });
  return L;
}

/* ---------- small icons (used in several lessons) ---------- */
// each drawn around (0,0) about 110 px across, in line style
function ozIcon(p, name, x, y, { s = 1, o = 0, colr = OZ.ink } = {}) {
  const g = G(p, { x, y, s, o });
  const st = { fill: 'none', stroke: colr, 'stroke-width': 5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' };
  const D = {
    fridge: 'M-34 -56H34V56H-34ZM-34 -10H34M-20 -40V-24M-20 6V30',
    ac: 'M-56 -30H56V14H-56ZM-44 -2H44M-36 28C-30 40 -30 48 -36 58M0 28C6 40 6 48 0 58M36 28C42 40 42 48 36 58',
    foam: 'M-56 -20H56V30H-56ZM-56 -20C-40 -34 40 -34 56 -20M-40 4H-30M-12 12H-2M14 0H24M34 14H44',
    shoe: 'M-56 10C-56 -20 -40 -40 -20 -40C-10 -20 10 -10 40 -6C54 -4 58 6 56 18H-56ZM-56 30H56',
    spray: 'M-18 -20H18V56H-18ZM-10 -20V-34H10V-20M10 -30H22M34 -44L44 -50M34 -30H48M34 -16L44 -10',
    inhaler: 'M-14 -50H20V30H-14ZM-14 30L-40 30L-40 52L20 52L20 30',
    extinguisher: 'M-20 -22H20V56H-20ZM-20 -22C-20 -40 20 -40 20 -22M0 -36V-48H30L42 -36',
    farm: 'M-56 40H56M-40 40V0L-10 -24L20 0V40M-22 40V16H2V40M28 40V-6H52V40M28 4H52',
    eye: 'M-56 0C-30 -36 30 -36 56 0C30 36 -30 36 -56 0ZM0 -16A16 16 0 1 1 0 16A16 16 0 1 1 0 -16Z',
    skin: 'M-10 -56C-30 -40 -40 -10 -36 20C-30 50 30 50 36 20C40 -10 30 -40 10 -56ZM-6 0A8 8 0 1 0 -6 1M12 20A6 6 0 1 0 12 21',
    shield: 'M0 -56L46 -38V2C46 30 24 50 0 58C-24 50 -46 30 -46 2V-38Z',
    fish: 'M-50 0C-30 -28 20 -28 40 0C20 28 -30 28 -50 0ZM40 0L58 -18V18ZM-30 -6A4 4 0 1 0 -30 -5',
    plankton: 'M-30 -10A14 14 0 1 0 -30 18A14 14 0 1 0 -30 -10M20 -36A12 12 0 1 0 20 -12A12 12 0 1 0 20 -36M24 14A16 16 0 1 0 24 46A16 16 0 1 0 24 14M-30 -10L-36 -26M-44 4L-58 0M20 -36L24 -50M8 30L-6 34',
    bottle: 'M-12 -56H12V-40C30 -30 30 -10 30 0V56H-30V0C-30 -10 -30 -30 -12 -40ZM-30 6H30M-6 18L4 30L-2 42',
    car: 'M-56 16V-4L-40 -10L-24 -32H24L40 -10L56 -4V16ZM-34 16A12 12 0 1 0 -34 17M34 16A12 12 0 1 0 34 17',
    factory: 'M-56 50V-10L-26 10V-10L4 10V-10L34 10V-50H50V50Z',
    lungs: 'M0 -50V-10M0 -10C-10 0 -14 10 -14 20M0 -10C10 0 14 10 14 20M-14 -26C-44 -30 -56 0 -50 30C-44 50 -20 52 -14 40ZM14 -26C44 -30 56 0 50 30C44 50 20 52 14 40Z',
    rocket: 'M0 -58C20 -40 24 -10 20 20H-20C-24 -10 -20 -40 0 -58ZM-20 20L-36 40H-14ZM20 20L36 40H14ZM-8 20L0 50L8 20M0 -26A8 8 0 1 0 0 -25',
    thermometer: 'M-10 -56H10V22A20 20 0 1 1 -10 22ZM0 22V-30',
    doc: 'M-36 -56H20L40 -36V56H-36ZM20 -56V-36H40M-22 -24H22M-22 -6H26M-22 12H26M-22 30H10',
    medal: 'M-24 -56L0 -14L24 -56M0 -14A30 30 0 1 1 -0.1 -14ZM0 2L6 14L20 16L10 26L12 40L0 34L-12 40L-10 26L-20 16L-6 14Z',
    person: 'M0 -50A18 18 0 1 1 -0.1 -50ZM-34 48C-34 6 34 6 34 48Z',
    gavel: 'M-50 50H10M-30 -20L-6 -44L22 -16L-2 8ZM8 -2L48 38',
    flask: 'M-12 -56H12M-8 -56V-14L-40 46H40L8 -14V-56M-28 24H28',
    chart: 'M-50 50V-50M-50 50H50M-36 30L-12 4L8 18L42 -30',
    info: 'M0 -50A50 50 0 1 1 -0.1 -50ZM0 -10V30M0 -26V-24',
    tech: 'M0 -36A36 36 0 1 1 -0.1 -36ZM0 -16A16 16 0 1 1 -0.1 -16ZM0 -50V-36M0 36V50M-50 0H-36M36 0H50M-35 -35L-25 -25M25 25L35 35M-35 35L-25 25M25 -25L35 -35',
    building: 'M-50 50H50M-40 50V-10M40 50V-10M-50 -10H50L0 -50ZM-20 50V10M0 50V10M20 50V10',
    globe: 'M0 -50A50 50 0 1 1 -0.1 -50ZM-50 0H50M0 -50C-26 -30 -26 30 0 50C26 30 26 -30 0 -50',
  };
  path(g, D[name], st);
  return g;
}

/* ---------- a simple city skyline (ground-level ozone) ---------- */
function skyline(p, x, y, w, { o = 1 } = {}) {
  const g = G(p, { x, y, o });
  let d = `M0 0`, cx = 0, seed = 5;
  const rnd = () => (seed = seed * 16807 % 2147483647) / 2147483647;
  while (cx < w) { const bw = 40 + rnd() * 60, bh = 60 + rnd() * 150; d += `V${-bh.toFixed(0)}H${(cx + bw).toFixed(0)}`; cx += bw; }
  d += `V0Z`;
  path(g, d, { fill: '#16294c', stroke: '#2b4677', 'stroke-width': 2 });
  return g;
}
