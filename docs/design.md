# design.md — Panduan Desain Media Pembelajaran e-Learning Lembaga National Single Window (INSW)

Dokumen ini merangkum sistem desain yang dipakai pada video motion graphic **"Efisiensi Proses Bisnis"** (13 scene, 1920×1080, 30 fps, 449,7 dtk) dan acuan penutup dari e-Learning *Impor dan Ekspor Barang Kiriman*. Pakai sebagai rujukan awal untuk proyek berikutnya agar tampilan, gerak, dan audio tetap konsisten.

Semua nilai di bawah diambil dari kode proyek (`src/scenes/*.js`, `scene01.js` sebagai pustaka helper) kecuali yang ditandai **[rekomendasi]**.

---

## 1. Karakter visual

| Aspek | Ketentuan |
|---|---|
| Kesan | Resmi, bersih, ramah; "biru Kemenkeu + emas" |
| Gaya | Flat modern dengan kedalaman ringan (bayangan lembut, ikon 3D-flat), bukan realistis |
| Ritme | Latar **navy** dan **kertas** bergantian per tahap; pergantian ditandai wipe diagonal emas + navy |
| Fokus | Satu gagasan per layar; elemen muncul sesuai kata yang diucapkan di voiceover |
| Bahasa | Bahasa Indonesia baku, kalimat pendek, istilah kunci dicetak tebal |

## 2. Kanvas dan tata letak

- Kanvas **1920×1080**, 30 fps. Semua koordinat dalam piksel kanvas.
- **Pill logo** (Kemenkeu › DJBC › PBC) selalu di kanan atas: `top 40px; right 48px; height 96px`, `z-index 50`, bayangan `0 6px 14px rgba(0,0,0,.25)`. Jangan taruh konten di area ini.
- **Judul layar**: kiri atas `left 110px; top 72px`, tinggi baris 96px, Poppins Bold 64px.
- Area konten: x 110–1810, y 190–980. Sisakan **bawah ±100px** untuk subtitle bila dipakai.
- Pusatkan diagram pada sumbu tengah layar; alur dibaca **kiri → kanan**, rincian turun ke bawah.
- Tepi aman: minimal 48px dari semua sisi untuk teks.

## 3. Warna

### 3.1 Token

| Token | Hex | Pemakaian |
|---|---|---|
| `navy` | `#0A2A5C` | Latar utama, teks pada kartu putih/kertas, garis tinta |
| `navy-deep` | `#071E45` | Tepi gradien latar, panel wipe, pita subtitle |
| `navy2` | `#0E3A78` | Kartu/bidang sekunder di atas navy |
| `navy-glow` | `#12468C` | Titik terang gradien latar |
| `blue` | `#0055A5` | Biru Kemenkeu; ikon, aksen, tombol |
| `sky` | `#3A9BE1` | Aksen lembut, segitiga latar, ikon varian muda |
| `gold` | `#F5B324` | Aksen utama: sorotan, garis alur, nomor, wipe |
| `gold-dark` | `#C8901A` | Sisi bawah ikon (ledge), bayangan emas |
| `gold-light` | `#FFE29A` | Kilau pada emas |
| `paper` | `#FBFAF6` | Latar tahap "kertas" |
| `line` | `#D6DEEA` | Garis tepi kartu kertas, kisi |
| `red` | `#D83C3C` | Tidak / ditolak / masalah |
| `green` | `#22A55A` | Ya / berhasil / sesudah |
| `white` | `#FFFFFF` | Teks di atas navy, kartu |

### 3.2 Kontras (dihitung WCAG)

| Pasangan | Rasio | Catatan |
|---|---|---|
| Putih di atas navy `#0A2A5C` | 14,0 | Teks utama pada latar navy |
| Navy di atas kertas `#FBFAF6` | 13,4 | Teks utama pada latar kertas |
| Navy di atas emas | 7,6 | Teks pada pita/tag emas |
| Emas di atas navy | 7,6 | Teks aksen di latar navy |
| Putih di atas biru `#0055A5` | 7,4 | Tombol/ikon biru |
| Sky di atas navy | 4,6 | Cukup untuk teks besar ≥ 24px |
| Merah di atas putih | 4,5 | Hanya teks tebal/besar |
| **Emas di atas putih** | **1,85** | **Jangan dipakai sebagai warna teks.** Emas pada latar terang hanya sebagai sorotan di bawah teks |
| Hijau di atas putih | 3,2 | Hanya untuk ikon/penanda, bukan teks kecil |

Aturan: warna status (merah/hijau) selalu disertai ikon atau kata ("Ya"/"Tidak", centang/silang) agar tidak bergantung pada warna saja.

### 3.3 Latar

**Navy (aurora)**
- Gradien: `radial-gradient(ellipse at 70% 30%, #12468C 0%, #0A2A5C 55%, #071E45 100%)`.
- 22 segitiga translusen (warna `sky` 75% / `blue` 25%, opasitas 0,05–0,14, ukuran 90–410px) bergeser dan berputar pelan.
- Kisi titik putih opasitas 0,10 (jarak 48px), 34 partikel kecil emas/putih naik pelan.
- Setiap scene memakai *seed* berbeda, tetapi memakai fungsi yang sama (`makeBackground(seed)`).

**Kertas**
- Dasar `#FBFAF6`, kisi biru `rgba(0,85,165,.07)` 2px setiap 48px, vinyet tepi `rgba(10,42,92,.08)`, derau halus (`feTurbulence`, opasitas 6%).
- Dipakai untuk tahap yang berisi diagram alur/proses agar elemen berwarna lebih jelas (`makePaper()`).

## 4. Tipografi

- Keluarga: **Poppins** (Regular 400, Medium 500, SemiBold 600, Bold 700). File ada di `public/fonts`.
- Dominan **Bold 700** (±65% pemakaian), SemiBold untuk subtitle dan label, Medium/Regular untuk keterangan.

| Peran | Ukuran | Bobot |
|---|---|---|
| Judul scene | 64px (60–58px bila panjang) | 700 |
| Judul panel / kartu besar | 44–46px | 700 |
| Subtitle | 38px | 600 |
| Teks kartu utama | 34–40px | 700 |
| Teks kartu / label diagram | 26–32px | 600–700 |
| Keterangan kecil | 24px (minimum) | 500 |

- Tinggi baris 1,2–1,3. Teks rata kiri untuk judul, rata tengah di dalam kartu.
- Jangan pakai ukuran di bawah **24px** pada kanvas 1920×1080.
- **Penanda sorotan**: garis emas tebal di belakang separuh bawah kata kunci (`linear-gradient(transparent 52%, rgba(245,179,36,.6) 52% 92%, transparent 92%)`), dianimasikan melebar dari kiri. Dipakai di latar kertas.

## 5. Komponen

**Kartu putih (di atas navy)**: latar `#fff`, radius **28px**, bayangan `0 18px 40px rgba(0,0,0,.35)`, teks navy, isi rata tengah.

**Kartu kertas**: latar `#fff`, border `2px #D6DEEA`, radius **18px**, bayangan `0 10px 26px rgba(10,42,92,.12)`.

**Chip ikon + label**: kartu 220×190px, radius 20px, ikon 100×100 di atas, label Bold 25px di bawah.

**Tag kecil (kategori)**: pil emas dengan teks navy 700, di atas judul (contoh "Pengajuan", "Rilis DO"). Berfungsi sebagai penanda tahap.

**Keputusan (diamond)**: belah ketupat emas dengan pertanyaan; cabang **Ya** hijau, **Tidak** merah (label kecil berpil di garis).

**Garis alur**: tebal 4px, ujung bulat, panah di ujung. Di latar navy memakai emas; di kertas memakai navy ("tinta") atau emas untuk jalur utama. Garis selalu **digambar bertahap** (stroke-dash) searah alur.

**Paket data**: bulatan/ikon kecil yang berjalan sepanjang garis untuk menunjukkan perpindahan data atau dokumen.

**Subtitle**: pil navy `rgba(7,30,69,.86)`, border `2px rgba(245,179,36,.6)`, radius 22px, teks putih Poppins 600 38px, padding `12px 36px`, lebar maks 1560px, tengah, `bottom 34px`. Satu frasa per tampil, fade 0,17 dtk.

**Panel penutup**: kiri navy dengan medali emas dan sinar berputar, ikon topik mengorbit; dua pita diagonal (emas dan biru muda); kanan kertas dengan "Selamat, Sobat Pemelajar!", subteks, dan pil tautan `insw.go.id` yang diketik.

**Marquee istilah kunci**: baris teks berjalan di dasar layar ringkasan (nama-nama materi dipisah ◆), opasitas rendah.

## 6. Ikon: 3D-flat dan 2D-flat

### 6.1 Gaya ikon proyek ini

- Bentuk: **kotak membulat** (squircle, radius ±20% sisi) berwarna emas, biru, atau sky; satu **glyph putih** di tengah.
- Kedalaman: gradien vertikal pada muka, **kilau putih** di bagian atas, **sisi bawah (ledge)** lebih gelap setebal ±8% tinggi, dan **bayangan lantai** elips lembut di bawah. Ukuran aset 512×512 PNG transparan; di layar dipakai 56–110px.
- Glyph: sederhana, tebal, satu warna putih, bayangan tipis. Tidak ada outline hitam.
- Aturan warna: emas untuk ikon utama/aktif, biru untuk ikon institusi/sistem, sky untuk data/dokumen pendukung. Tidak lebih dari 3 warna dalam satu layar.
- Ukuran ikon dalam kartu: 90–110px; dalam alur kecil: 56–72px.

Varian warna tile (emas diukur dari aset proyek; nilai biru dan sky adalah **[rekomendasi]** yang disetel mendekati ikon yang ada, cek visual terhadap `public/assets/ic/` sebelum dipakai):

| Varian | Muka (atas → bawah) | Ledge |
|---|---|---|
| Emas | `#FFD05A` → `#F5B324` → `#E9A41B` | `#C8901A` |
| Biru | `#2B7FD0` → `#0055A5` → `#004A91` | `#003A73` |
| Sky | `#7CC0F2` → `#3A9BE1` → `#2F8AD0` | `#1F6FAE` |

Templat SVG siap pakai ada di `icon-tile-template.svg` (ikut dokumen ini). Cara membuat ikon baru:

1. Ambil glyph 2D dari sumber gratis di 6.2 (SVG, grid 24×24).
2. Tempel path-nya ke elemen `<g id="glyph">` di templat. Untuk ikon *outline* (Lucide, Tabler) biarkan `stroke="#fff"`; untuk ikon *solid* (Font Awesome Free Solid) ganti menjadi `fill="#fff" stroke="none"`.
3. Ganti gradien/ledge sesuai varian warna di atas.
4. Ekspor ke PNG 512×512 transparan (misalnya dengan Playwright atau Inkscape) dan taruh di `public/assets/ic/`.
5. Beri nama berdasarkan konsep (`shield.png`, `ppbj.png`), bukan nomor.

### 6.2 Sumber ikon gratis

Lisensi diperiksa dari halaman resmi masing-masing pada 22 Nov 2026. Lisensi bisa berubah, jadi baca ulang berkas LICENSE sebelum dipakai di proyek baru.

**Glyph 2D flat (bahan utama tile 3D-flat)**

| Sumber | Lisensi | Atribusi | Catatan |
|---|---|---|---|
| [Lucide](https://lucide.dev/license) | ISC (turunan Feather: MIT) | Sertakan pemberitahuan hak cipta dan lisensi dalam salinan | Outline konsisten, ringan, cocok sebagai glyph tile |
| [Tabler Icons](https://github.com/tabler/tabler-icons) | MIT | Sertakan pemberitahuan lisensi | ±6.500 ikon (outline dan filled), SVG/PNG; cakupan topik luas (kapal, dokumen, gudang, stempel) |
| [Font Awesome Free](https://github.com/FortAwesome/Font-Awesome) | Ikon CC BY 4.0, font SIL OFL 1.1, kode MIT | **Wajib** menyebut atribusi; berkas unduhan sudah memuat komentar atribusi, jangan dihapus | Gaya solid tegas, cocok untuk glyph putih tebal. Hanya set *Free* |
| Phosphor Icons, Material Symbols | MIT; Apache 2.0 | Sertakan pemberitahuan lisensi | Alternatif bila konsep tidak ada di atas. Baca lisensi di repo masing-masing |

**Ikon 3D / emoji siap pakai**

| Sumber | Lisensi | Catatan |
|---|---|---|
| [Microsoft Fluent Emoji](https://github.com/microsoft/fluentui-emoji) | Halaman repo menyebut MIT | Tersedia gaya 3D, Color, Flat, dan High Contrast. Hanya konsep emoji (kapal, dokumen, gembok, globe). **Cek berkas LICENSE di repo** sebelum rilis, karena halaman utama tidak menjelaskan cakupan lisensi untuk aset |
| [Twemoji (jdecked)](https://github.com/jdecked/twemoji) | Grafis CC BY 4.0, kode MIT | Atribusi diterima di README, halaman "Tentang", atau komentar sumber. Gaya flat 2D |

**Ilustrasi (bukan ikon)**

| Sumber | Lisensi | Catatan |
|---|---|---|
| [unDraw](https://undraw.co/license) | Bebas dipakai komersial dan boleh diubah, **atribusi tidak wajib** | Dilarang didistribusikan ulang sebagai paket, di-scrape, atau dipakai melatih model AI |

Tidak direkomendasikan tanpa membaca syarat: situs yang mewajibkan akun/atribusi per berkas (misalnya Flaticon gratis, Storyset), dan ikon dari hasil pencarian gambar tanpa lisensi jelas.

### 6.3 Aturan atribusi

- Buat satu berkas `docs/CREDITS.md` di tiap proyek berisi: nama ikon/ilustrasi, sumber, lisensi, tautan.
- Untuk lisensi yang mewajibkan atribusi (Font Awesome Free, Twemoji): cantumkan di kredit penutup video atau di README/halaman "Tentang" materi. Isi `KREDIT` di scene penutup bila ingin ditampilkan.
- Logo institusi (Kemenkeu, DJBC, PBC, INSW) dan foto resmi **bukan** ikon gratis; pakai berkas dari unit yang berwenang dan jangan diubah proporsinya.

### 6.4 Do dan Don't ikon

- Do: satu gaya, satu ketebalan garis, satu sudut kilau di seluruh set.
- Do: ikon mewakili konsep (stempel = izin, perisai = karantina, kapal = angkutan laut).
- Don't: campur ikon 3D dengan ikon outline pada satu layar.
- Don't: ubah warna ikon di luar tiga varian tile.
- Don't: ikon sebagai satu-satunya pembawa makna; selalu beri label teks.

## 7. Foto dan ilustrasi

- Foto utama (kapal peti kemas) dipotong **lingkaran** dengan border putih 10px dan bayangan `0 20px 50px rgba(0,0,0,.45)`, dikelilingi cincin sky dan dua busur emas tebal.
- Peta, gambar dokumen, dan objek 3D (gedung/terminal) dipakai sebagai pendamping, selalu dengan bayangan lembut yang sama.
- Medali emas dan pita dipakai hanya di penutup.

## 8. Gerak (motion)

Semua animasi dihitung dari waktu `t` (detik) lewat fungsi `render(t)` agar hasil render deterministik. Helper: `P(t, mulai, selesai, easing)`.

| Easing | Pemakaian |
|---|---|
| `outCubic` | Default: fade/geser masuk |
| `outBack` | Munculnya kartu dan ikon (pop) |
| `outElastic` | Kemunculan khusus yang ingin menonjol (contoh ikon kapal) |
| `outExpo` | Zoom/transisi cepat |
| `inOut` (kubik) | Wipe dan perpindahan panel |
| `inCubic` | Keluar |

Pola gerak baku:

| Pola | Parameter |
|---|---|
| Pop | skala 0,6 → 1, 0,6 dtk, `outBack`, opasitas naik di separuh pertama |
| Slide-up | geser 30px ke atas + fade, 0,6 dtk |
| Teks judul | *mask reveal*: baris naik dari bawah garis potong |
| Garis alur | stroke-dash, durasi mengikuti panjang |
| Sorotan teks | lebar penanda 0 → 100%, ±0,5 dtk |
| Masuk/keluar tahap | fade 0,4–0,5 dtk + geser ±30px |
| Transisi antar tahap | **wipe diagonal** dua panel (emas lalu navy) miring −18°, 1,0–1,1 dtk |
| Sapuan cahaya | `sweep` singkat di titik pergantian tahap |
| Pembukaan scene | wipe terbuka (reveal) pada detik 0–1,0; scene tertutup oleh cover pada 1,1 dtk terakhir |
| Penutup | zoom X-ZOM ke panel penutup |

Aturan sinkronisasi:
- Setiap elemen penting muncul **tepat saat kata terkait diucapkan** (0–0,1 dtk setelahnya). Simpan waktunya dalam objek `CUE` di bagian atas file scene.
- Jangan ada dua animasi besar bersamaan; beri jeda ≥0,3 dtk.
- Biarkan layar **diam sebentar (≥1 dtk)** setelah elemen terakhir lengkap sebelum pindah tahap.
- Latar boleh terus bergerak pelan; konten tidak.

## 9. Audio

- **Voiceover**: suara Google AI Studio model **Leda**, tenang, ramah, resmi, tempo sedang, jeda jelas antar kalimat. Normalisasi `loudnorm` −16 LUFS.
- **Musik latar**: satu trek **kontinu** untuk seluruh video (loop dengan crossfade 4 dtk), level ±−14 dB di bawah VO. Tidak dipotong per scene.
- **Ducking**: musik otomatis mengecil saat VO berbicara (`sidechaincompress`, ambang 0,02, rasio 6, attack 30 ms, release 500 ms).
- **Dinamika**: fade-in 3 dtk di awal; build-up + riser 7 dtk sebelum momen puncak; **impact** pada kata "Selamat"; musik naik ±3 dB di penutup; fade-out 3,5 dtk.
- **SFX**: seperlunya (pop ikon, kapal), selalu di bawah level VO.
- Mix dibuat sekali untuk seluruh video (`tools/build_master_audio.py`); jangan mencampur per scene.

## 10. Struktur materi

| Bagian | Isi | Durasi acuan |
|---|---|---|
| Pembuka | Judul, foto utama, tujuan singkat | 20 dtk |
| Agenda | Outline materi (kartu muncul satu per satu, lalu menyatu ke "satu pintu") | 20 dtk |
| Materi inti | Satu scene per topik; pola: definisi → alur/diagram → manfaat | 30–60 dtk per scene |
| Ringkasan | Kartu topik menyala sesuai kata + prinsip utama | ±20 dtk |
| Penutup | Panel medali, pesan, tautan | ±20 dtk |

Pola penjelas yang dipakai berulang: **Sebelum vs Sesudah** (merah vs hijau), **Dulu vs Kini**, **alur N langkah** bernomor, **satu pintu** (banyak masukan → satu pusat), **timeline tahap**, **keputusan Ya/Tidak**.

Total video ideal ≤ 8 menit; satu scene tidak melebihi 60 dtk.

## 11. Aksesibilitas dan QA

Sebelum rilis, cek:

- [ ] Teks ≥ 24px; kontras sesuai tabel 3.2.
- [ ] Makna tidak hanya lewat warna.
- [ ] Setiap elemen yang disebut di VO muncul di layar dan sebaliknya.
- [ ] Subtitle tersedia, satu frasa per tampil, tidak menutupi konten.
- [ ] Animasi sinkron dengan VO (selisih < 0,15 dtk).
- [ ] Ikon satu gaya dan atribusi tercatat di `CREDITS.md`.
- [ ] Istilah dan regulasi dikonfirmasi SME dan masih berlaku.
- [ ] Mix audio: tidak ada klik/dip di sambungan scene; puncak di bawah −1 dBFS.
- [ ] Durasi file hasil render sama dengan jumlah durasi scene.

## 12. Berkas rujukan

| Kebutuhan | Lokasi |
|---|---|
| Helper (PAL, easing, latar, wipe, kartu, sorotan) | `src/scenes/scene01.js` (blok di atas `Scene 1`) |
| Contoh scene diagram alur dengan VO dan subtitle | `src/scenes/scene10b.js` |
| Contoh scene ringkasan/penutup | `src/scenes/scene12.js` |
| Daftar scene dan audio | `src/sceneList.js`, `src/Root.jsx` |
| Ikon 3D-flat proyek ini | `public/assets/ic/*.png` (72 berkas) |
| Pill logo, foto, medali | `public/assets/` |
| Font | `public/fonts/` |
| Skrip audio | `tools/build_master_audio.py`, `tools/mix.sh` |
| Templat ikon | `icon-tile-template.svg` |

Acuan penutup berasal dari storyboard S17 "Rangkuman dan penutup" pada e-Learning Impor dan Ekspor Barang Kiriman: kartu menyala saat disebut, istilah kunci berjalan, aurora, zoom ke panel navy + medali dengan pita diagonal emas dan biru muda.

---
*Dokumen disusun 22 Nov 2026 dari proyek "e-Learning Lembaga Nasional Single Window". Perbarui bagian Warna dan Ikon bila identitas visual berubah.*
