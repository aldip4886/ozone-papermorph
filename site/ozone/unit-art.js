// Chalk sketches for the unit headers on the contents page, one per unit, drawn in the unit's colour.
// Each entry is the inside of an SVG with viewBox 0 0 600 180; keep the left ~200 px light (the unit title sits there
// on narrow screens). Classes, styled in lib/units.css:
//   d  a stroke that draws itself in when the unit scrolls into view (--k orders the strokes)
//   t  text or a filled shape that fades in
//   a  faint chalk white instead of the unit colour;  faint  even fainter
// A sketch may add one looping motion after it is drawn: give an element a class that lib/units.css animates (swap-a,
// hop, orbit, ride, spin, tilt, breathe, ...), or add your own .seen .unit-art .NAME rule and keyframes in a <style> in index.html.
'use strict';
(() => {
  let k = 0;
  const P = (d, cls = '', extra = '') => `<path class="d ${cls}" pathLength="1" style="--k:${k++}" d="${d}" ${extra}/>`;
  const Tx = (x, y, s, size = 24, cls = '', anchor = 'start') => `<text class="t ${cls}" style="--k:${k++}" x="${x}" y="${y}" font-size="${size}" text-anchor="${anchor}">${s}</text>`;
  const C = (cx, cy, r, cls = '') => `<circle class="d ${cls}" pathLength="1" style="--k:${k++}" cx="${cx}" cy="${cy}" r="${r}"/>`;
  const reset = s => { k = 0; return s; };

  window.UNIT_ART = [
    // 1 The ozone layer: a band of sky with ultraviolet waves stopped in it, the Sun breathing above.
    reset(P('M220 150H580', 'a') + P('M220 70H580') + P('M220 110H580') +
      P('M300 20l6 8l-6 8l6 8l-6 8l6 8l-6 8') + P('M380 20l6 8l-6 8l6 8l-6 8l6 8l-6 8') + P('M460 20l6 8l-6 8l6 8l-6 8l6 8l-6 8l6 8l-6 8l6 8l-6 8l6 8l-6 8l6 8l-6 8') +
      `<circle class="t breathe" r="18" cx="555" cy="34" fill="currentColor" stroke="none" style="--k:${k++}"/>` +
      Tx(240, 100, 'O₃', 26) + Tx(500, 172, 'the ozone layer', 20, 'a')),
  ];
})();
