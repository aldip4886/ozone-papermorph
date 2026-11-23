# Templat ikon 3D-flat INSW (SVG sebagai teks)

Salin blok di bawah ke berkas `icon-tile-template.svg` untuk dipakai. Panduan lengkap: `design.md` bagian 6.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <!-- Ikon 3D-flat INSW: ganti isi <g id="glyph"> dengan path SVG ikon 2D (satu warna, viewBox 24x24).
       Varian warna: gold (default), blue, sky. Ubah 3 stop gradien + warna "ledge" sesuai tabel di design.md. -->
  <defs>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFD05A"/><stop offset=".55" stop-color="#F5B324"/><stop offset="1" stop-color="#E9A41B"/>
    </linearGradient>
    <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="9"/></filter>
    <filter id="glyphShadow" filterUnits="userSpaceOnUse" x="-4" y="-4" width="32" height="34"><feDropShadow dx="0" dy="0.6" stdDeviation="0.5" flood-color="#8A5E0B" flood-opacity=".35"/></filter>
  </defs>
  <ellipse cx="256" cy="474" rx="150" ry="16" fill="#0A2A5C" opacity=".28" filter="url(#blur)"/>
  <rect x="48" y="84" width="416" height="372" rx="104" fill="#C8901A"/>               <!-- ledge (sisi bawah) -->
  <rect x="48" y="48" width="416" height="372" rx="104" fill="url(#face)"/>            <!-- muka ikon -->
  <path d="M64 150 Q64 62 160 62 L352 62 Q448 62 448 150 Q256 215 64 150Z" fill="url(#gloss)"/> <!-- kilau atas -->
  <g id="glyph" transform="translate(136 124) scale(10)" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" filter="url(#glyphShadow)">
    <path d="M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z"/>   <!-- contoh: perisai (24x24) -->
  </g>
</svg>
```
