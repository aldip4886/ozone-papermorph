# Outline Slide Presentasi v3: Memahami dan Menghitung PDRI

23 November 2026 · versi 3 (revisi), materi KB 7 diganti menjadi upaya hukum dengan titik berat bidang perpajakan

Versi ini mengikuti [outline slide v2](outline-slide-pdri-v2.md) dengan sistem desain yang sama ([DESIGN.md](../DESIGN.md)). Perubahannya ada di KB 7: slide barang kiriman (64 sampai 69 di v2) diganti dua belas slide upaya hukum (64 sampai 75), sehingga slide KB 8 dan penutup bergeser enam nomor dari v2. Isi mengikuti [bahan ajar v3](bahan-ajar-pdri-v3.md), [outline materi v3](07-outline-materi-v3.md), dan [session plan v3](08-session-plan-v3.md).

**Revisi 23 November 2026.** KB 7 kini menitikberatkan langkah yang dapat ditempuh wajib pajak di bidang perpajakan. Slide kepabeanan diringkas menjadi pintu masuk (64 sampai 67). Delapan slide berikutnya (68 sampai 75) membahas jalur sengketa (keberatan, banding, gugatan, PK) dan jalur permohonan (pembetulan, pengurangan atau penghapusan sanksi, pembatalan ketetapan yang tidak benar, angsuran atau penundaan) dengan Kasus 4. Isinya mengikuti KB 7.5 sampai 7.12 bahan ajar v3 yang sudah direvisi.

Jumlah slide: 81, ditambah 5 slide cadangan. Rincian: 1 halaman judul, 13 studi kasus, 26 materi, 22 interaksi, 10 peralihan, 8 rangkuman, 1 penutup.

**Status deck.** Deck PPTX v2 (`media/slide-pdri-v2.pptx`) belum dibangun ulang. Outline v3 ini ditulis tangan; untuk membangun deck v3, isi `media/sumber-deck-v2/slides.js` perlu diperbarui mengikuti outline ini.

**Kode jenis slide:** JUD (judul), PER (peralihan), MAT (materi), INT (interaksi), KAS (studi kasus), RAN (rangkuman), PEN (penutup), CAD (cadangan).

**Cara membaca setiap slide:**
- **Judul** di baris nomor adalah *action title*: kalimat kesimpulan yang dibaca peserta sebagai pesan slide. Judul slide peralihan dan interaksi berupa nama kegiatan atau pertanyaan.
- **Isi:** teks dan angka yang tampil.
- **Layout:** kode templat dari Bagian A3.
- **Visual:** ikon tile, grafik, atau diagram.
- **Sumber:** teks kaki slide kiri.
- **Catatan:** catatan fasilitator (juga tersimpan sebagai catatan pembicara di PPTX).

---

## Bagian A. Panduan Desain

### A1. Prinsip gaya McKinsey yang dipakai

1. **Action title.** Judul slide materi, kasus, dan rangkuman berupa satu kalimat kesimpulan, maksimal dua baris. Peserta yang hanya membaca judul tetap mendapat alur cerita.
2. **Satu pesan per slide.** Slide yang dulu memuat dua pesan dipecah (teori pembenaran dan asas Adam Smith kini dua slide).
3. **Grafik bersih.** Tanpa garis kisi dan sumbu nilai; angka ditulis langsung di atas batang dengan format Indonesia. Warna batang mengikuti kode pungutan (A2).
4. **Sumber di kaki slide.** Kaki kiri memuat sumber; kaki kanan memuat penanda kegiatan belajar dan nomor slide.
5. **Angka kunci disorot.** Angka yang menjadi pesan slide diberi penanda sorotan emas di separuh bawah teks, bukan teks berwarna emas di latar terang.

### A2. Ukuran, warna, dan huruf

**Ukuran:** 16:9, 13,333 x 7,5 inci (1920 x 1080 px). Tepi konten kiri 110 px, kanan 1810 px. Pill logo Kemenkeu, PBC, DJBC di kanan atas, area ini tidak diisi konten.

| Token | Kode | Pemakaian |
| --- | --- | --- |
| navy | #0A2A5C | Latar navy, teks utama di latar kertas, kotak hasil |
| navy-deep | #071E45 | Tepi gradien latar, pil pewaktu |
| navy2 | #0E3A78 | Blok PPnBM, bidang sekunder |
| blue | #0055A5 | Blok PPN, ikon institusi |
| sky | #3A9BE1 | Blok Bea Masuk dan BMTP, ikon pendukung |
| gold | #F5B324 | Aksen, nomor, sorotan, blok PPh Pasal 22 |
| gold-light | #FFE29A | Pil "cek" untuk angka asumsi |
| paper | #FBFAF6 | Latar kertas dengan kisi biru 7% |
| line | #D6DEEA | Garis tabel, blok nilai pabean |
| red / green | #D83C3C / #22A55A | Cabang Tidak / Ya, status Berlaku, selalu bersama kata |

Emas tidak dipakai sebagai warna teks di latar kertas (kontras 1,85). Teks emas hanya di atas navy (kontras 7,6).

**Huruf:** Poppins. Judul slide Bold 26 pt (52 px), judul peralihan Bold 40 pt, teks isi 14 sampai 18 pt, angka hasil Bold 24 sampai 48 pt, kaki slide 12 pt. Tidak ada teks di bawah 12 pt (24 px).

**Ikon:** tile 3D-flat dari templat ikon INSW: kotak membulat emas, biru, atau sky dengan glyph putih Lucide atau Tabler. Emas untuk ikon utama, biru untuk institusi, sky untuk data pendukung. Maksimal tiga warna tile per slide.

**Latar:** navy aurora untuk sampul, peralihan, dan interaksi; kertas untuk materi, kasus, dan rangkuman. Pergantian latar menandai pergantian tahap: membaca di kertas, bekerja di navy.

**Foto:** hanya foto kapal peti kemas di sampul, dipotong lingkaran. Tidak ada foto pegawai bea cukai.

### A3. Templat layout

| Kode | Nama dan susunan |
| --- | --- |
| S1 | Sampul: latar navy aurora, judul kiri, foto lingkaran kanan, pill logo kanan atas |
| S2 | Peralihan: latar navy aurora, nomor emas besar, judul, pertanyaan kasus, ikon tile besar di kanan |
| S3 | Kolom ikon atau diagram khusus di latar kertas, action title dua baris, sumber di kaki |
| S4 | Dua kolom banding dengan garis pemisah tipis, opsional catatan di bawah |
| S5 | Tabel hitung (Langkah, Perhitungan, Hasil) di kiri, kotak hasil navy di kanan |
| S6 | Grafik batang bersih di kiri, angka kunci dan rincian di kanan |
| S7 | Tabel bergaris horizontal tipis, kepala tabel bergaris navy |
| S8 | Kutipan pasal dengan tanda kutip emas, baris unsur di bawah |
| S9 | Interaksi: latar navy, tag emas di atas judul, langkah bernomor, pewaktu |
| S10 | Rangkuman: butir dengan ikon centang di kiri, kartu jawaban navy di kanan |
| S11 | Penutup: panel navy dengan medali emas, pita diagonal emas dan sky, panel kertas |

---

## Bagian B. Rincian Slide

### Pembukaan

**1 · JUD · Memahami dan Menghitung Pajak dalam Rangka Impor (PDRI)**
- Isi: Judul, subjudul, nama fasilitator, tanggal, lokasi (isian kosong).
- Layout: S1.
- Visual: Foto kapal peti kemas dipotong lingkaran dengan border putih, cincin sky, dan dua busur emas. Latar navy aurora. Pill logo kanan atas.

**2 · KAS · Sejak 10 Januari 2026, setiap meter kain kapas impor pos 5208.21.00 dikenai BMTP Rp3.300**
- Isi: Video berita BMTP kain (1 sampai 2 menit) di kiri. Tiga fakta di kanan: pos tarif 5208.21.00, BMTP tahun pertama Rp3.300 per meter, berlaku 10 Januari 2026 sampai 9 Januari 2029.
- Layout: S3 dengan diagram khusus.
- Visual: Bingkai video bergaris putus-putus; tiga ikon tile (kapal, stempel, kalender).
- Sumber: PMK 98 Tahun 2025.
- Catatan: Putar video berita BMTP secara otomatis. Jika video tidak tersedia, bacakan judul berita dan tunjukkan tiga fakta di kanan.

**3 · KAS · Kain senilai Rp1,09 miliar dikenai pungutan Rp645 juta, dan importir bertanya dari mana angkanya**
- Isi: Kutipan staf PT Kain Prima Nusantara: "Pak, Bu, hitungan ini dari mana? Pungutannya lebih dari separuh harga kain kami." Kartu tagihan: nilai pabean Rp1.089.300.000, rincian disembunyikan, total pungutan Rp645.241.050.
- Layout: S3 dengan diagram khusus.
- Visual: Kartu kutipan dengan ikon tile pesan; kartu tagihan bergaya kuitansi dengan tanda tanya di baris rincian.
- Sumber: Bahan ajar, Skenario pembuka; PMK 98 Tahun 2025.
- Catatan: Jangan buka rinciannya. Pertanyaan ini menjadi benang merah delapan JP.

**4 · MAT · Delapan JP, ponsel untuk kuis, dan Paspor Misi menjadi aturan main kelas ini**
- Isi: Tiga kolom: waktu (8 JP x 45 menit dalam dua bagian), ponsel (dipakai untuk kuis, voting, dan pre-test), stempel (Paspor Misi diberi stempel setelah pertanyaan kasus terjawab).
- Layout: S3.
- Visual: Ikon tile jam (biru), ponsel (sky), stempel (emas).

**5 · INT · Pre-test: kerjakan 10 soal dalam 9 menit untuk melihat titik awal Anda**
- Isi: 10 soal pilihan ganda dan isian, 9 menit, mandiri. Skor tidak dinilai. Kode QR dan kode akses kuis di kanan.
- Layout: S9.
- Visual: Ikon tile daftar periksa; kartu QR putih.
- Catatan: Sampaikan bahwa skor tidak dinilai, hanya untuk melihat titik awal. Kisi-kisi sama dengan post-test.

**6 · INT · Tebak cepat: komponen apa saja yang membentuk tagihan Rp645 juta?**
- Isi: Satu menit menebak komponen tagihan per kelompok lewat aplikasi kuis, lalu awan kata dibahas.
- Layout: S9.
- Visual: Ikon tile bola lampu; kartu QR.
- Catatan: Tampilkan awan kata dari aplikasi kuis di layar terpisah, lalu bahas singkat.

### Bagian I

**7 · PER · Memahami Sambil Mulai Menghitung**
- Isi: Label Bagian I, judul, empat pertanyaan kasus bernomor.
- Layout: S2.
- Visual: Angka romawi emas besar, ikon tile gedung pemerintahan (biru).

### KB 1

**8 · PER · Hari Pertama di Pelabuhan**
- Isi: Nomor KB 01, judul, tujuan satu kalimat.
- Layout: S2.
- Visual: Ikon tile kapal (emas).

**9 · MAT · Importir membayar dua kelompok pungutan: pungutan kepabeanan dan pajak dalam rangka impor**
- Isi: Kiri: pungutan kepabeanan (Bea Masuk; bea masuk tambahan seperti BMTP, antidumping, imbalan; sudah dipelajari di materi kepabeanan). Kanan: PDRI (PPN Impor, PPnBM Impor, PPh Pasal 22 Impor beserta dasar hukumnya). Catatan: cukai dibahas di modul tersendiri.
- Layout: S4.
- Visual: Ikon tile peti kemas (sky) dan dokumen pajak (biru).
- Sumber: UU PPN; UU PPh; PMK 131 Tahun 2024; PMK 51 Tahun 2025.

**10 · MAT · Empat pertanyaan kasus memandu Anda selama delapan JP**
- Isi: Empat kolom pertanyaan kasus dengan KB tempat menjawabnya: dasar memungut (KB 2), pihak dan cara (KB 3), nasib PPN Rp168 juta (KB 4), PPh dipungut di muka (KB 5).
- Layout: S3.
- Visual: Ikon tile timbangan, orang-orang, koin, kalender.

**11 · MAT · Semua PDRI dihitung dari nilai impor, sehingga kesalahan pada nilai impor terbawa ke tiga pajak**
- Isi: Rumus: nilai impor = nilai pabean + Bea Masuk + bea masuk tambahan (misalnya BMTP). Diagram: tiga input (nilai pabean, Bea Masuk, BMTP) mengalir ke nilai impor, lalu ke PPN Impor, PPnBM Impor, PPh Pasal 22 Impor. Nilai impor tidak termasuk PPN dan PPnBM.
- Layout: S3 dengan diagram khusus.
- Visual: Diagram rantai kiri ke kanan; kotak nilai impor navy di tengah; garis alur navy berpanah; kode warna pungutan.
- Sumber: UU PPN (definisi nilai impor); PMK 51 Tahun 2025.
- Catatan: Tunjukkan bagian input, nilai impor, lalu tiga pajak secara bertahap.

**12 · KAS · Nilai impor Kasus 1 sebesar Rp1,53 miliar, 40% lebih tinggi dari nilai pabeannya**
- Isi: Empat langkah: nilai pabean USD 60.000 x Rp18.155 = Rp1.089.300.000; Bea Masuk 10% (cek) = Rp108.930.000; BMTP 100.000 m x Rp3.300 = Rp330.000.000; nilai impor Rp1.528.230.000.
- Layout: S5.
- Visual: Tabel hitung bergaris tipis; penanda cek pada baris Bea Masuk; kotak hasil navy dengan angka emas.
- Sumber: KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026); PMK 98 Tahun 2025.
- Catatan: Tampilkan baris satu per satu. Tarif Bea Masuk MFN 10% masih asumsi (cek di BTKI atau INSW).

**13 · INT · Giliran Anda: hitung nilai impor jika impornya hanya 50.000 meter**
- Isi: Varian Kasus 1: 50.000 m, CIF USD 30.000, data lain sama. Berpasangan 6 menit. Daftar "Cek dulu sebelum hitung" di kanan.
- Layout: S9.
- Visual: Ikon tile dua orang; kartu daftar periksa putih.
- Catatan: Kunci: nilai impor Rp764.115.000 (ditampilkan di slide rangkuman).

**14 · RAN · Periksa nilai impor lebih dahulu, karena semua PDRI dihitung darinya**
- Isi: Tiga butir: PDRI terdiri atas PPN, PPnBM, PPh Pasal 22 Impor; Bea Masuk dan bea masuk tambahan masuk ke nilai impor; semua PDRI dihitung dari nilai impor. Jawaban varian: Rp764.115.000.
- Layout: S10.
- Visual: Ikon tile centang biru; kartu jawaban navy dengan angka emas.

### KB 2

**15 · PER · Dasar Negara Memungut Pajak**
- Isi: Nomor KB 02, judul, Pertanyaan 1.
- Layout: S2.
- Visual: Ikon tile timbangan (biru).

**16 · INT · Jika importir menolak membayar Rp645 juta, apa dasar negara memaksanya?**
- Isi: Pertanyaan pancingan, dijawab spontan.
- Layout: S9.
- Visual: Ikon tile palu hakim.
- Catatan: Tampung jawaban spontan tanpa dikoreksi. Jawaban dibangun di slide berikutnya dari empat sudut pandang.

**17 · MAT · Negara boleh memaksa karena kewajiban pajak ditetapkan dengan undang-undang**
- Isi: Kutipan Pasal 23A UUD 1945. Lima unsur pajak menurut Pasal 1 angka 1 UU KUP.
- Layout: S8.
- Visual: Tanda kutip emas besar; lima ikon tile biru untuk lima unsur.
- Sumber: UUD 1945 Pasal 23A; UU KUP Pasal 1 angka 1.

**18 · MAT · Pungutan atas kain impor menjalankan dua fungsi sekaligus: mengisi kas negara dan mengatur impor**
- Isi: Budgetair: pajak membiayai belanja negara; PPN dan PPh 22 kain masuk kas negara. Regulerend: BMTP melindungi industri tekstil; PPh 22 tanpa API 7,5%, dengan API 2,5%.
- Layout: S4.
- Visual: Ikon tile celengan (biru) dan tuas pengatur (emas).
- Sumber: Bahan ajar KB 2.2; PMK 98 Tahun 2025; PMK 51 Tahun 2025.

**19 · INT · Stasiun lensa: setiap kelompok membaca Kasus 1 dari satu sudut pandang**
- Isi: Empat kartu lensa (teori pembenaran; asas Adam Smith; asas domisili, sumber, kebangsaan; pembeda pungutan). 6 menit membaca, 1 menit presentasi per kelompok.
- Layout: S9.
- Visual: Empat kartu lensa putih dengan ikon tile.
- Catatan: Cukai hanya disebut pada kartu pembeda pungutan. Catat lensa yang dipakai setiap kelompok untuk debat.

**20 · MAT · Lima teori pembenaran menjelaskan mengapa negara berhak memungut pajak atas kain impor**
- Isi: Tabel lima teori (asuransi, kepentingan, daya pikul, bakti, daya beli) dengan inti pemikiran dan bacaannya atas Kasus 1.
- Layout: S7.
- Visual: Ikon tile kecil per baris: perisai, jabat tangan, beban, hati, keranjang.
- Sumber: Bahan ajar KB 2.3.

**21 · MAT · Empat asas Adam Smith menguji apakah cara memungut PDRI adil, pasti, mudah, dan hemat**
- Isi: Empat kolom: equality, certainty, convenience, economy, dengan pengertian dan contoh PDRI. Catatan: asas domisili, sumber, kebangsaan.
- Layout: S3.
- Visual: Ikon tile timbangan, dokumen centang, kursi, koin.
- Sumber: Adam Smith, The Wealth of Nations (1776).

**22 · MAT · Pajak dan Bea Masuk tidak memberi imbalan langsung, berbeda dengan retribusi dan PNBP**
- Isi: Tabel pembeda: pajak, retribusi, PNBP, Bea Masuk menurut imbalan, dasar, dan contoh. Cukai disebut sebagai pembanding.
- Layout: S7.
- Visual: Ikon tile per baris: dokumen pajak, pin lokasi, paspor, peti kemas.
- Sumber: Bahan ajar KB 2.5; UU Kepabeanan; UU PNBP.

**23 · INT · Debat: dukung atau tolak BMTP dan PPN atas kain impor**
- Isi: Kubu A mendukung, Kubu B menolak. 3 menit argumen per kubu, 2 menit sanggahan per kubu. Wajib menyebut minimal satu lensa.
- Layout: S9.
- Visual: Dua kartu kubu (jempol ke atas biru, jempol ke bawah sky).
- Catatan: Catat lensa yang dipakai setiap kubu. Tutup dengan menunjukkan bahwa kedua kubu memakai sudut pandang yang sah.

**24 · KAS · Tanpa API, PPh Pasal 22 Kasus 1 naik tiga kali lipat menjadi Rp114,6 juta**
- Isi: Grafik dua batang: dengan API 2,5% Rp38.205.750; tanpa API 7,5% Rp114.617.250. Pertanyaan: fungsi pajak apa yang bekerja?
- Layout: S6.
- Visual: Batang emas (warna PPh 22), label nilai langsung di atas batang.
- Sumber: PMK 51 Tahun 2025; bahan ajar Latihan 2.
- Catatan: Jawaban: fungsi regulerend, pemerintah mendorong importir memiliki API.

**25 · RAN · Undang-undang memberi dasar memaksa; fungsi, teori, dan asas membantu Anda menjelaskannya**
- Isi: Tiga butir rangkuman KB 2.
- Layout: S10.
- Visual: Ikon tile centang; stempel Paspor nomor 1.

### KB 3

**26 · PER · Pihak dan Sistem Pemungutan**
- Isi: Nomor KB 03, judul, Pertanyaan 2.
- Layout: S2.
- Visual: Ikon tile orang-orang (sky).

**27 · INT · Siapa yang mengisi angka PDRI di dokumen impor ini?**
- Isi: Contoh tiruan baris PIB Kasus 1 dengan kolom PDRI disorot. Peserta menebak siapa yang mengisi.
- Layout: S9.
- Visual: Tabel PIB tiruan di kartu putih; kolom PPN dan PPh 22 disorot emas.
- Catatan: Tabel ini tiruan untuk latihan, bukan tangkapan layar PIB asli. Jawaban: importir mengisi sendiri (self assessment), petugas meneliti.

**28 · MAT · Dalam satu impor, tiga sistem berjalan bersama: importir menghitung, DJBC meneliti dan memungut**
- Isi: Tiga kolom: official assessment (fiskus menentukan; DJBC meneliti PIB dan dapat menetapkan kekurangan), self assessment (wajib pajak menghitung sendiri; importir mengisi PIB), withholding (pihak ketiga memungut; DJBC memungut PPh 22). Sistem utama Indonesia: self assessment.
- Layout: S3.
- Visual: Ikon tile kaca pembesar (biru), formulir (emas), tangan memegang koin (sky).
- Sumber: UU KUP; bahan ajar KB 3.1.

**29 · MAT · Tiga cara membagi jenis pajak menempatkan PPN dan PPh pada kelompok yang berbeda**
- Isi: Tabel: lembaga pemungut (pusat: PPN, PPnBM, PPh, Bea Meterai; daerah: PKB, pajak hotel), pihak yang menanggung (langsung: PPh; tidak langsung: PPN, PPnBM), sifat (subjektif: PPh; objektif: PPN).
- Layout: S7.
- Visual: Ikon tile gedung, panah dua arah, orang.
- Sumber: Bahan ajar KB 3.2.

**30 · MAT · Semua undang-undang yang menjadi dasar PDRI masih berlaku per November 2026**
- Isi: Kiri: piramida peraturan (UU, PP, PMK, Peraturan Dirjen). Kanan: tabel UU KUP, PPh, PPN (terakhir diubah UU 6/2023), UU HPP (tarif PPN 12%), UU Kepabeanan (diubah UU 17/2006) dengan status Berlaku.
- Layout: S3 dengan diagram khusus.
- Visual: Piramida empat tingkat bergradasi navy ke sky; label status hijau dengan tanda centang.
- Sumber: JDIH Kemenkeu, diperiksa 20 sampai 21 November 2026.

**31 · MAT · DJBC memungut PDRI di pelabuhan, sedangkan DJP mengadministrasikan pengkreditannya**
- Isi: Diagram pusat PIB dengan enam pihak: importir, PPJK, DJBC, bank persepsi/devisa, DJP, konsumen akhir, beserta perannya. Baris identitas importir: NPWP/NIK, API-U/API-P, PKP, Coretax.
- Layout: S3 dengan diagram khusus.
- Visual: Kotak PIB navy di tengah, enam kartu pihak dengan ikon tile, empat pil identitas di bawah.
- Sumber: Bahan ajar KB 3.4.

**32 · INT · Siapa Saya? Pasangkan enam peran dengan sistem pemungutan dan instansinya**
- Isi: Kartu peran (importir, PPJK, petugas DJBC, bank devisa, DJP, konsumen). Kelompok mencocokkan peran dengan sistem pemungutan dan instansi, presentasi 1 menit. 14 menit.
- Layout: S9.
- Visual: Enam kartu peran putih kecil dengan ikon tile.

**33 · INT · Importir mengisi sendiri, lalu petugas meneliti. Sistem apa yang bekerja?**
- Isi: Pertanyaan engsel dengan empat pilihan A sampai D lewat aplikasi kuis. Jawaban benar C.
- Layout: S9.
- Visual: Empat kartu pilihan berlabel huruf emas; kartu QR.
- Catatan: Jawaban: C. Importir menghitung sendiri (self assessment); petugas meneliti dan dapat menetapkan (official assessment). Jika lebih dari 30% kelas memilih jawaban lain, ulas slide tiga sistem.

**34 · INT · "Kenapa saya yang harus menghitung sendiri?" Jawab dalam 30 detik**
- Isi: Berpasangan: satu peserta menjadi pengguna jasa, satu menjadi petugas. Tukar peran. Templat yang sama dipakai di KB 4 (slide 44) dan KB 7 (slide 75).
- Layout: S9.
- Visual: Ikon tile pesan; pewaktu 30 detik.
- Catatan: Fasilitator berkeliling dan mencatat peserta yang masih di level Awal.

**35 · RAN · Importir menghitung, DJBC meneliti dan memungut, lalu DJP mengadministrasikan pengkreditannya**
- Isi: Dua butir rangkuman KB 3 dan stempel 2.
- Layout: S10.
- Visual: Ikon tile centang; kartu Paspor.

### KB 4

**36 · PER · PPN Impor**
- Isi: Nomor KB 04, judul, Pertanyaan 3.
- Layout: S2.
- Visual: Ikon tile kuitansi (biru).

**37 · INT · Jika importir PKP membayar PPN di pelabuhan, apakah uangnya hilang?**
- Isi: Voting Ya atau Tidak lewat aplikasi kuis.
- Layout: S9.
- Visual: Dua tombol besar Ya dan Tidak dengan ikon jempol; kartu QR.
- Catatan: Simpan hasil voting untuk dibandingkan di slide contoh hitung PPN.

**38 · MAT · PPN dikenakan di setiap tahap penjualan, tetapi hanya atas pertambahan nilainya**
- Isi: Tiga ciri PPN: pajak konsumsi, tidak langsung, bertingkat tanpa pajak berganda. Catatan Pasal 4 ayat (1) UU PPN: impor BKP objek PPN, dipungut dari siapa pun yang mengimpor; definisi PKP.
- Layout: S3.
- Visual: Ikon tile keranjang (biru), panah dua arah (sky), tumpukan lapis (emas).
- Sumber: UU PPN Pasal 4 ayat (1); bahan ajar KB 4.1 dan 4.2.

**39 · MAT · Barang tidak mewah menanggung PPN efektif 11%, barang mewah 12% penuh**
- Isi: Kiri: tidak tergolong mewah, DPP nilai lain 11/12, rumus 12% x 11/12 x nilai impor, beban efektif 11%. Kanan: tergolong mewah, DPP nilai impor, 12% x nilai impor. Catatan: per 10 September 2026 belum ada penurunan tarif.
- Layout: S4.
- Visual: Ikon tile kaos (sky) dan permata (emas); angka besar 11% dan 12% dengan sorotan emas.
- Sumber: UU HPP; PMK 131 Tahun 2024.

**40 · MAT · PKP mengkreditkan PPN Impor sebagai pajak masukan, jadi uang itu tidak hilang**
- Isi: Diagram PK dikurangi PM dengan dua hasil: PK lebih besar dari PM, setor selisih (kurang bayar); PM lebih besar dari PK, lebih bayar (restitusi atau kompensasi). PIB beserta bukti bayar setara faktur pajak.
- Layout: S3 dengan diagram khusus.
- Visual: Dua kotak PK dan PM dengan tanda minus; dua kartu hasil; ikon tile timbangan.
- Sumber: UU PPN; bahan ajar KB 4.4.

**41 · INT · Estafet PPN: ikuti kain Kasus 1 sampai menjadi kemeja di tangan pembeli**
- Isi: Empat pos: importir kain, konveksi, toko, pembeli kemeja. Setiap pos menghitung PK, PM, dan setoran, lalu meneruskan kartu. 14 menit.
- Layout: S9.
- Visual: Alur empat ikon tile (kapal, pabrik, toko, kemeja) dengan garis emas berpanah.
- Catatan: Angka disederhanakan dengan beban efektif 11%. Tutup dengan: PIB dipersamakan dengan faktur pajak.

**42 · KAS · Setoran di empat pos berjumlah Rp352 juta, sama dengan PPN yang dibayar pembeli akhir**
- Isi: Grafik air terjun: PPN Impor Rp168.105.300, setoran importir Rp29.894.700, konveksi Rp77.000.000, toko Rp77.000.000, total Rp352.000.000. Tabel ringkas di kanan.
- Layout: S6.
- Visual: Batang air terjun biru (PPN) dengan total navy; angka langsung di atas batang.
- Sumber: Bahan ajar KB 4.5 (angka disederhanakan untuk latihan).
- Catatan: Tampilkan batang satu per satu. Pesan: pengusaha hanya menyetorkan PPN, pembeli akhir yang menanggung.

**43 · KAS · PPN Impor Kasus 1 sebesar Rp168,1 juta, setara 11% dari nilai impor**
- Isi: Cek dulu: kain tidak tergolong mewah, importir PKP, DPP 11/12. Nilai impor Rp1.528.230.000. PPN 12% x 11/12 x Rp1.528.230.000 = Rp168.105.300. Latihan: varian 50.000 meter.
- Layout: S5.
- Visual: Tabel hitung; kotak hasil navy; pita hasil voting.
- Sumber: PMK 131 Tahun 2024; KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026).
- Catatan: Bandingkan dengan hasil voting tadi. Latihan varian 50.000 m dikerjakan mandiri; kunci Rp84.052.650 di slide rangkuman Bagian I.

**44 · INT · "PPN Rp168 juta ini hilang begitu saja?" Jawab dalam 30 detik**
- Isi: Templat Jelaskan 30 detik dengan pertanyaan KB 4.
- Layout: S9.
- Visual: Sama dengan slide Jelaskan 30 detik KB 3.

**45 · RAN · Bagian I selesai: Anda sudah bisa menghitung nilai impor dan PPN Impor barang tidak mewah**
- Isi: Empat butir: nilai impor, dasar pemungutan, sistem pemungutan, PPN Impor. Jawaban varian PPN Rp84.052.650. Stempel 3 dari 4.
- Layout: S10.
- Visual: Ikon tile centang; kartu jawaban navy.

### Bagian II

**46 · PER · Menghitung, Memeriksa, Menjelaskan**
- Isi: Label Bagian II, judul, tiga lencana misi.
- Layout: S2.
- Visual: Ikon tile kalkulator besar; tiga ikon tile misi.

**47 · INT · Kuis kilat: lima soal ulasan Bagian I, skor masuk papan kelompok**
- Isi: 5 soal ulasan Bagian I, termasuk satu soal nilai impor dan satu soal PPN. Dijawab per kelompok.
- Layout: S9.
- Visual: Ikon tile petir; kartu QR.

### KB 5

**48 · PER · PPh Pasal 22 Impor**
- Isi: Nomor KB 05, judul, Pertanyaan 4.
- Layout: S2.
- Visual: Ikon tile kalender (emas).

**49 · MAT · PPh dilunasi lewat empat jalur selama tahun berjalan, lalu diperhitungkan di SPT Tahunan**
- Isi: Garis waktu: PPh 21 (pemotongan oleh pemberi kerja), PPh 22 (pemungutan, termasuk atas impor), PPh 23 (pemotongan atas dividen, bunga, royalti, sewa, jasa), PPh 25 (angsuran bulanan) menuju SPT Tahunan.
- Layout: S3 dengan diagram khusus.
- Visual: Garis waktu Januari sampai Desember; empat penanda ikon tile; PPh 22 disorot emas; ujung kanan SPT Tahunan.
- Sumber: UU PPh; bahan ajar KB 5.1.

**50 · MAT · PPh Pasal 22 Impor dipungut bersama Bea Masuk dan menjadi kredit pajak importir**
- Isi: Empat kolom ketentuan PMK 51/2025: pemungut (DJBC dan bank devisa), dasar (nilai impor), saat terutang (bersamaan pembayaran Bea Masuk), sifat (tidak final, dikreditkan di SPT Tahunan).
- Layout: S3.
- Visual: Ikon tile perisai, kalkulator, jam, dokumen centang.
- Sumber: PMK 51 Tahun 2025 (berlaku 1 Agustus 2025); laman DJP.

**51 · MAT · Pilih tarif PPh Pasal 22 dengan memeriksa lampiran, barang khusus, lalu status API**
- Isi: Kiri: tabel enam kondisi tarif (API 2,5%; tanpa API 7,5%; kedelai, gandum, terigu dengan API 0,5%; lampiran 10% atau 7,5%; emas batangan 0,25%; barang tidak dikuasai 7,5% harga lelang). Kanan: diagram keputusan tiga langkah.
- Layout: S3 dengan diagram khusus.
- Visual: Tabel tarif; diagram keputusan dengan belah ketupat emas, cabang Ya hijau dan Tidak merah.
- Sumber: PMK 51 Tahun 2025.

**52 · KAS · PPh Pasal 22 Kasus 1 sebesar Rp38,2 juta karena kain tidak masuk lampiran dan importir memiliki API-U**
- Isi: Cek dulu: pos 52 tidak tercantum dalam daftar 10% lampiran PMK 51/2025; importir API-U; tarif 2,5%. Nilai impor Rp1.528.230.000. PPh 22 = 2,5% x Rp1.528.230.000 = Rp38.205.750. Daftar 7,5% untuk pos 52 masih perlu dicek.
- Layout: S5.
- Visual: Tabel hitung; penanda cek; kotak hasil navy.
- Sumber: PMK 51 Tahun 2025.
- Catatan: Daftar tarif 7,5% dalam lampiran PMK 51 Tahun 2025 untuk pos 52 masih perlu dicocokkan.

**53 · INT · Pilih Tarifmu: tentukan tarif PPh Pasal 22 untuk delapan importir**
- Isi: 8 kartu skenario (bahan ajar Latihan 5), 6 menit, skor masuk papan. Kunci di slide cadangan C2.
- Layout: S9.
- Visual: Kisi 4 x 2 kartu skenario putih bernomor emas.
- Catatan: Kunci di slide cadangan C2. Minta peserta mencentang "cek dulu" pada setiap kartu.

**54 · INT · Ikuti uangnya: lengkapi alur PPh Pasal 22 Kasus 1 dari PIB sampai SPT Tahunan**
- Isi: Lembar alur kosong lima lingkaran: PIB diajukan, pembayaran bersama Bea Masuk, kas negara, laporan DJBC, SPT Tahunan importir. Kelompok melengkapi dan menempel di dinding.
- Layout: S9.
- Visual: Lima lingkaran bernomor dengan garis emas; label kosong.
- Catatan: Kunci: PIB diajukan, importir membayar PDRI bersama Bea Masuk, dana masuk kas negara, DJBC melaporkan hasil pemungutan, importir mengkreditkan PPh 22 di SPT Tahunan.

**55 · INT · Tarif tanpa API tiga kali lipat. Adilkah menurut asas equality?**
- Isi: Diskusi kelas memakai asas equality dan fungsi regulerend.
- Layout: S9.
- Visual: Ikon tile timbangan (emas).
- Catatan: Arahkan: importir tetap dapat mengkreditkan PPh 22, jadi dampaknya terutama pada arus kas. Kaitkan dengan fungsi regulerend.

**56 · RAN · PPh Pasal 22 Impor adalah pembayaran di muka yang dikreditkan, dan tarifnya dipilih dalam tiga langkah**
- Isi: Tiga butir rangkuman KB 5; stempel 4 dari 4.
- Layout: S10.
- Visual: Ikon tile centang; kartu Paspor.

### KB 6

**57 · PER · Barang Mewah dan Fasilitas**
- Isi: Nomor KB 06, judul, nama misi dan pancingan.
- Layout: S2.
- Visual: Ikon tile motor (emas).

**58 · MAT · Barang mewah dikenai PPN 12% penuh ditambah PPnBM yang tidak dapat dikreditkan**
- Isi: Kiri: PPN barang mewah 12% x nilai impor tanpa 11/12. Kanan: PPnBM dikenakan satu kali, tidak dapat dikreditkan; motor 250 sampai 500 cc 60%, lebih dari 500 cc 95%.
- Layout: S4.
- Visual: Ikon tile permata (biru) dan gembok (emas); angka besar 12% dan 95%.
- Sumber: PMK 131 Tahun 2024; PMK 141/PMK.010/2021 jo. PMK 42/PMK.010/2022.

**59 · KAS · Kasus 2: CV Roda Jaya mengimpor satu motor 1.000 cc yang tergolong barang mewah**
- Isi: Data Kasus 2: CV Roda Jaya (API-U, PKP), 1 unit sepeda motor CBU 1.000 cc pos 8711.50, CIF USD 20.000, kurs Rp18.155, BM 40% (cek), PPh 22 10% (cek). Tugas berpasangan 16 menit.
- Layout: S7.
- Visual: Tabel data dengan ikon tile motor; penanda cek; kartu tugas navy.
- Sumber: KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026).
- Catatan: Lembar kerja memuat langkah Kasus 1 sebagai contoh. Pasangan mengerjakan Kasus 2 lalu mencocokkan dengan kunci di slide berikutnya.

**60 · KAS · Total pungutan motor Rp740 juta, lebih dari dua kali nilai pabeannya**
- Isi: Grafik dua batang: nilai pabean Rp363.100.000 dibanding total pungutan Rp739.997.800 (BM Rp145.240.000, PPN Rp61.000.800, PPnBM Rp482.923.000, PPh 22 Rp50.834.000). Rincian di kanan.
- Layout: S6.
- Visual: Batang bertumpuk dengan kode warna pungutan; penanda cek pada BM dan PPh 22.
- Sumber: KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026); PMK 141/PMK.010/2021.
- Catatan: Jelaskan angka sebesar ini dengan fungsi regulerend dan teori daya pikul. BM 40% dan PPh 22 10% masih asumsi.

**61 · MAT · Fasilitas mengubah jumlah yang dibayar, jadi periksa dokumen fasilitas sebelum menghitung**
- Isi: Tiga kolom: SKB PPh 22 (tidak dipungut), PPN tidak dipungut (PM tetap dapat dikreditkan), PPN dibebaskan (PM tidak dapat dikreditkan). Varian Kasus 1 dengan SKB: PDRI hanya PPN Rp168.105.300.
- Layout: S3.
- Visual: Ikon tile sertifikat, tangan berhenti, hadiah.
- Sumber: Bahan ajar KB 6.4.

**62 · INT · Seorang petugas menghitung PPN motor seperti ini. Di mana salahnya, dan berapa selisihnya?**
- Isi: Tabel hitung salah: PPN motor 12% x 11/12 x Rp508.340.000 = Rp55.917.400, baris dilingkari merah putus-putus. Jawaban setelah klik.
- Layout: S9.
- Visual: Kartu tabel putih; lingkaran merah putus-putus; ikon tile kaca pembesar.
- Catatan: Jawaban: motor tergolong barang mewah, DPP memakai nilai impor tanpa 11/12. PPN benar Rp61.000.800. Selisih kurang pungut Rp5.083.400. Tambahkan animasi klik di Canva atau PowerPoint jika ingin menampilkan jawaban di layar.

**63 · RAN · Barang mewah: PPN 12% penuh ditambah PPnBM, dan periksa fasilitas sebelum menghitung**
- Isi: Tiga butir rangkuman KB 6; lencana Misi Barang Mewah.
- Layout: S10.
- Visual: Ikon tile centang; kartu lencana.

### KB 7

*Pintu masuk: penetapan DJBC (slide 64 sampai 67, sekitar 13 menit)*

**64 · PER · Upaya Hukum dan Hak Wajib Pajak**
- Isi: Nomor KB 07, judul, kutipan staf importir: "Dua-duanya kami tidak setuju, dan kas kami sedang seret. Apa saja yang bisa kami lakukan?" Di bawah kutipan, dua label map: "SPTNP dari DJBC" dan "SKPKB dan STP dari KPP".
- Layout: S2.
- Visual: Ikon tile timbangan (emas) besar; dua ikon tile map kecil (sky untuk DJBC, biru untuk DJP).
- Catatan: Peserta menebak lewat aplikasi kuis: ada berapa pilihan, dan ke mana diajukan. Simpan jawabannya untuk dibandingkan di slide 68.

**65 · MAT · Penetapan pejabat dapat menimbulkan kekurangan Bea Masuk, PDRI, dan denda sekaligus**
- Isi: Kiri: empat jenis penetapan DJBC (SPTNP Pasal 16, SPKTNP Pasal 17, SPP Pasal 93A, SPSA Pasal 94 UU Kepabeanan). Kanan: rantai selisih nilai pabean, kekurangan BM, selisih nilai impor, kekurangan PPN dan PPh 22, denda. Catatan kecil: denda kesalahan nilai pabean dihitung dari kekurangan BM saja, 100% untuk kekurangan sampai 50% dari BM yang dibayar (sepuluh lapis sampai 1.000%).
- Layout: S4.
- Visual: Ikon tile stempel (biru) di kiri; rantai lima kotak dengan kode warna pungutan di kanan.
- Sumber: UU 10/1995 jo. UU 17/2006; PP 28/2008 jo. PP 39/2019.
- Catatan: Cukup 3 menit. Kaitkan dengan official assessment di KB 3. Status PP 39/2019 perlu dicek sebelum kelas.

**66 · KAS · Kasus 3: SPTNP menaikkan nilai kain menjadi USD 66.000, dan tagihannya Rp37.962.105**
- Isi: Cek dulu: penetapan nilai pabean oleh pejabat, BMTP spesifik tidak berubah, importir API-U dan PKP. Selisih nilai pabean USD 6.000 x Rp18.155 = Rp108.930.000. Kekurangan BM 10% = Rp10.893.000 (cek). Selisih nilai impor Rp119.823.000. Kekurangan PPN 12% x 11/12 = Rp13.180.530. Kekurangan PPh 22 2,5% = Rp2.995.575. Denda 100% x Rp10.893.000 = Rp10.893.000. Total tagihan Rp37.962.105. SPTNP tanggal 2 Maret 2026.
- Layout: S5.
- Visual: Tabel hitung; penanda cek pada BM dan denda; kotak hasil navy.
- Sumber: KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026); PMK 131 Tahun 2024; PMK 51 Tahun 2025; PP 39/2019.
- Catatan: Kelompok menghitung dulu selama 4 menit dengan mengganti CIF Kasus 1 menjadi USD 66.000 di kalkulator, baru slide ini dibuka. Tekankan bahwa PDRI (Rp16.176.105) lebih besar daripada kekurangan BM.

**67 · MAT · Surat dari DJBC diuji di DJBC: keberatan 60 hari dengan jaminan, lalu banding setelah tagihan dilunasi**
- Isi: Tangga empat anak tangga: penetapan (SPKTNP dari Dirjen langsung ke banding); keberatan ke Dirjen Bea dan Cukai lewat Portal DJBC (60 hari sejak tanggal penetapan, jaminan sebesar tagihan, satu kali, diputus 60 hari, lewat = dianggap dikabulkan); banding ke Pengadilan Pajak (60 hari sejak keputusan, setelah lunas); PK ke Mahkamah Agung. Pita bawah berisi pegangan: "Lihat siapa penerbit surat. Surat DJBC ke DJBC; surat DJP (SKP, STP) mengikuti UU KUP dan diurus di KPP."
- Layout: S3 dengan diagram khusus.
- Visual: Tangga naik dari kiri ke kanan dengan ikon tile dokumen, kotak surat, palu, gedung, semua sky (warna DJBC); pita pegangan navy dengan teks emas di bawah.
- Sumber: UU 17/2006 Pasal 93, 93A, 94, 95; PMK 51/PMK.04/2017 jo. PMK 136/PMK.04/2022.
- Catatan: Cukup 3 menit. Peserta menulis tenggat keberatan Kasus 3 (1 Mei 2026) di kalender. Pengecualian jaminan: barang belum keluar dari kawasan pabean, tagihan sudah lunas, atau penetapan tidak menimbulkan kekurangan.

*Inti: hak wajib pajak di bidang perpajakan (slide 68 sampai 75, sekitar 32 menit)*

**68 · MAT · Wajib pajak punya dua keluarga hak: menyengketakan ketetapan atau memohon perbaikan tanpa sengketa**
- Isi: Kiri, **Sengketa** (menguji kebenaran ketetapan, dapat berujung di pengadilan, berisiko sanksi bila kalah): keberatan, banding, gugatan, peninjauan kembali. Kanan, **Permohonan** (memperbaiki atau meringankan, diputus DJP, tanpa sanksi 30% atau 60%): pembetulan SPT, pembetulan ketetapan, pengurangan atau penghapusan sanksi, pengurangan atau pembatalan SKP dan STP yang tidak benar, pembatalan hasil pemeriksaan, angsuran atau penundaan. Baris bawah: "Permohonan bukan pengganti keberatan untuk SKP yang sama."
- Layout: S4.
- Visual: Ikon tile palu hakim (biru) di kiri, ikon tile formulir dengan pena (emas) di kanan; daftar butir dengan pasal di ujung kanan setiap butir.
- Sumber: UU KUP Pasal 8, 9, 16, 23, 25, 26, 27, 36; PMK 118 Tahun 2024 jo. PMK 71 Tahun 2026.
- Catatan: Bandingkan dengan tebakan peserta di slide 64. Peserta mengisi lembar Peta Hak Wajib Pajak di Paspor sambil mengikuti slide 69 dan 72.

**69 · MAT · Keberatan, banding, dan PK masing-masing bertenggat 3 bulan, sedangkan gugatan dipakai untuk penagihan**
- Isi: Tangga sengketa: SKP (SKPKB, SKPKBT, SKPLB, SKPN, atau pemotongan dan pemungutan pihak ketiga; STP bukan objek keberatan) → keberatan ke Dirjen Pajak (3 bulan sejak dikirim, satu keberatan satu SKP, lunasi jumlah yang disetujui dalam pembahasan akhir, diputus 12 bulan, lewat = dianggap dikabulkan) → banding ke Pengadilan Pajak (3 bulan sejak keputusan diterima; sisa pajak tertangguh) → PK ke Mahkamah Agung (alasan terbatas, 3 bulan, satu kali, tidak menunda putusan). Cabang samping: gugatan ke Pengadilan Pajak atas pelaksanaan penagihan (14 hari) atau keputusan lain (30 hari), tidak menunda penagihan. Pita bawah: pembinaan Pengadilan Pajak beralih ke Mahkamah Agung paling lambat 31 Desember 2026; hukum acara UU 14/2002 tetap.
- Layout: S3 dengan diagram khusus.
- Visual: Tangga naik empat anak tangga, ikon tile biru (warna DJP): dokumen, kotak surat, palu, gedung; cabang gugatan bergaris putus-putus dengan ikon tile rantai; pita info sky di bawah.
- Sumber: UU KUP Pasal 23, 25, 26, 27; UU 14/2002 Pasal 35, 40, 43, 77, 91, 92; Putusan MK 26/PUU-XXI/2023.
- Catatan: Alasan PK: bukti palsu atau tipu muslihat, bukti tertulis baru yang menentukan, putusan melebihi tuntutan, tuntutan belum diputus, atau putusan nyata-nyata tidak sesuai undang-undang. Sanksi 60% PK dikenakan jika putusan PK menambah pajak yang harus dibayar (Pasal 27 ayat (5f) UU KUP). Per 14 November 2026, Perpres pengalihan Pengadilan Pajak baru selesai harmonisasi; perbarui pita bila sudah diundangkan.

**70 · KAS · Kalah banding dua kali lebih mahal daripada kalah keberatan: sanksi Rp48 juta lawan Rp24 juta**
- Isi: Kasus 4a: SKPKB PPN pokok Rp100.000.000; Rp20.000.000 disetujui dan dilunasi; Rp80.000.000 diajukan keberatan. Grafik tiga batang "yang harus dibayar setelah putusan": keberatan dikabulkan Rp0; keberatan ditolak Rp104.000.000 (Rp80.000.000 + sanksi 30% Rp24.000.000); banding ditolak Rp128.000.000 (Rp80.000.000 + sanksi 60% Rp48.000.000, sanksi 30% tidak dikenakan). Catatan: ketiga sanksi (30% keberatan, 60% banding, 60% PK) tidak dapat dikurangi.
- Layout: S6.
- Visual: Batang bertumpuk: pokok biru (warna PPN), sanksi navy2 berlabel "sanksi"; angka langsung di atas batang; sorotan emas pada Rp48.000.000.
- Sumber: UU KUP Pasal 25 ayat (9), Pasal 27 ayat (5d); PMK 71 Tahun 2026. Angka disusun untuk latihan.
- Catatan: Kelas menghitung bersama sebelum batang dibuka. Tekankan bahwa SKPKB asli juga memuat sanksi bunga Pasal 13; latihan hanya memakai pokok. Petugas tidak menilai jalur mana yang sebaiknya dipilih.

**71 · INT · STP denda Rp500.000 karena SPT Masa PPN terlambat. Apakah jalurnya keberatan?**
- Isi: Pertanyaan engsel dengan empat pilihan: A) keberatan ke Dirjen Pajak dalam 3 bulan; B) banding ke Pengadilan Pajak; C) permohonan pengurangan atau penghapusan sanksi (Pasal 36 ayat (1) huruf a); D) keberatan ke Dirjen Bea dan Cukai. Lewat aplikasi kuis.
- Layout: S9.
- Visual: Empat kartu pilihan berlabel huruf emas; kartu QR.
- Catatan: Jawaban: C. STP bukan objek keberatan Pasal 25 ayat (1), dan STP diterbitkan DJP. Jika kurang dari 80% benar, ulas slide 68 selama 2 menit.

**72 · MAT · Tanpa bersengketa, wajib pajak dapat membetulkan, meminta keringanan, membatalkan, atau mengangsur**
- Isi: Tabel enam baris (kolom: langkah, dipakai saat, diajukan ke, batas dan syarat):
  - Pembetulan SPT (Pasal 8): SPT sendiri keliru; DJP; selama belum ada pemeriksaan, lebih bayar paling lama 2 tahun sebelum daluwarsa penetapan.
  - Pembetulan ketetapan (Pasal 16): SKP, STP, atau keputusan salah tulis, salah hitung, atau keliru menerapkan ketentuan tertentu yang tidak bersifat sengketa; DJP; diputus 6 bulan, lewat = dianggap dikabulkan.
  - Pengurangan atau penghapusan sanksi (Pasal 36 ayat (1) huruf a): sanksi timbul karena kekhilafan atau bukan kesalahan wajib pajak; DJP; atas sanksi yang belum dibayar, paling banyak dua kali (ayat (1a)), diputus 6 bulan.
  - Pengurangan atau pembatalan SKP dan STP yang tidak benar (huruf b dan c): ketetapan keliru tetapi tidak diajukan keberatan; DJP; paling banyak dua kali, diputus 6 bulan; tidak bisa bila keberatan atas SKP itu sudah dicabut dan pencabutannya disetujui (PMK 71/2026).
  - Pembatalan hasil pemeriksaan atau SKP (huruf d): pemeriksaan tanpa SPHP atau tanpa pembahasan akhir; DJP; hanya satu kali (ayat (1b)), diputus 6 bulan.
  - Angsuran atau penundaan (Pasal 9 ayat (4); Pasal 113 sampai 121 PMK 81/2024): wajib pajak menerima tagihan tetapi mengalami kesulitan likuiditas; DJP lewat KPP (Coretax); sebelum permohonan lelang barang sitaan, jaminan aset berwujud minimal senilai utang, diputus 7 hari kerja, angsuran sama besar paling lama 24 bulan, bunga Pasal 19 ayat (2) (0,61% per bulan untuk November 2026).
- Layout: S7.
- Visual: Ikon tile per baris: pensil, kalkulator, perisai, dokumen silang, kaca pembesar, kalender. Semua biru (warna DJP).
- Sumber: UU KUP Pasal 8, 9, 16, 19, 36 (Pasal 9 dan 19 sebagaimana diubah UU 6/2023); PMK 118 Tahun 2024 jo. PMK 71 Tahun 2026; PMK 81 Tahun 2024; KMK 52/MK/EF.2/2026.
- Catatan: Padanan di bahan ajar: KB 7.7. Tarif bunga berubah setiap bulan; ganti 0,61% dengan tarif KMK bulan kelas. Pasal 36 ayat (1) huruf b sedang diuji di MK (Perkara 91/PUU-XXIV/2026); perbarui baris kedua bila sudah diputus.

**73 · KAS · PPh 22 Impor yang lupa dikreditkan tidak hangus: pembetulan SPT menghasilkan lebih bayar Rp19,1 juta**
- Isi: Kasus 4c, dua kolom SPT semula dan SPT pembetulan: PPh Badan terutang Rp250.000.000 (sama); kredit pajak lain Rp200.000.000 (sama); PPh 22 Impor Rp0 menjadi Rp19.102.875; PPh Pasal 29 Rp50.000.000 (sudah dilunasi) menjadi Rp30.897.125. Hasil: lebih bayar Rp19.102.875. Syarat: DJP belum memulai pemeriksaan.
- Layout: S5.
- Visual: Tabel dua kolom; baris PPh 22 Impor disorot emas (warna PPh 22); kotak hasil navy dengan angka emas.
- Sumber: UU KUP Pasal 8 ayat (1) dan (1a); PMK 51 Tahun 2025. Angka disusun untuk latihan.
- Catatan: Sambungkan ke KB 5: PPh 22 Impor adalah kredit pajak. Angka Rp19.102.875 sama dengan PPh 22 varian 50.000 meter. DJP dapat memeriksa sebelum mengembalikan kelebihan bayar.

**74 · INT · Pilih Jalurmu: tentukan jalur, tujuan, dan tenggat untuk sepuluh situasi**
- Isi: 10 kartu situasi (1 kepabeanan, 9 perpajakan, sebagian dari Kasus 4), 6 menit, bahas 3 menit, skor masuk papan. Kunci di slide cadangan C5.
- Layout: S9.
- Visual: Kisi 5 x 2 kartu situasi putih bernomor emas; kartu 1 bertepi sky (DJBC), kartu 2 sampai 10 bertepi biru (DJP).
- Catatan: Kunci di slide cadangan C5. Tekankan kartu 3 dan 4: keputusan keberatan yang sama, dua pilihan berbeda (banding atau angsuran). Tutup dengan pertanyaan lensa: "Asas apa yang dijaga oleh hak pejabat menetapkan dan hak wajib pajak menguji serta memohon? Kenapa kalah banding dikenai sanksi?"

**75 · RAN · Lihat penerbit surat, pilih sengketa atau permohonan, lalu sebutkan hak wajib pajak beserta tenggatnya**
- Isi: Empat butir rangkuman: (1) penetapan DJBC menimbulkan kekurangan BM, PDRI, dan denda, dan diuji ke DJBC; (2) ketetapan DJP diuji lewat keberatan, banding, dan PK dengan risiko sanksi 30% atau 60%, sedangkan gugatan untuk penagihan; (3) tanpa sengketa, wajib pajak dapat membetulkan, meminta pengurangan sanksi, membatalkan ketetapan yang tidak benar, atau mengangsur; (4) petugas menyebut hak dan tenggat dengan jujur tanpa menilai peluang menang. Latihan "jelaskan 30 detik": "Kami tidak setuju SKPKB ini dan kas kami sedang seret." Lencana Misi Upaya Hukum.
- Layout: S10.
- Visual: Ikon tile centang; kartu lencana; pewaktu 30 detik.
- Catatan: Jawaban yang diharapkan: keberatan ke Dirjen Pajak dalam 3 bulan bila tidak setuju, atau angsuran bila menerima tagihan; urus di KPP tempat terdaftar.

### KB 8

**76 · PER · Menjawab Staf Importir**
- Isi: Nomor KB 08, judul, nama misi.
- Layout: S2.
- Visual: Ikon tile piala (emas).

**77 · KAS · Lebih dari separuh tagihan Rp645 juta berasal dari BMTP, bukan dari pajak**
- Isi: Grafik air terjun jawaban lengkap Kasus 1: BM Rp108.930.000, BMTP Rp330.000.000, PPN Rp168.105.300, PPh 22 Rp38.205.750, total Rp645.241.050. BMTP 51% dari total; PDRI Rp206.311.050.
- Layout: S6.
- Visual: Batang air terjun dengan kode warna pungutan; total navy; angka di atas batang dalam juta Rupiah.
- Sumber: KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026); PMK 98 Tahun 2025; PMK 131 Tahun 2024; PMK 51 Tahun 2025.
- Catatan: Slide baru di v2: menutup pertanyaan pembuka sebelum role play. BM 10% masih asumsi (cek).

**78 · INT · Lomba hitung: tiga variasi Kasus 1 dan tiga hitungan yang salah**
- Isi: Baris atas: tiga variasi (tanpa API, BMTP lupa, ada SKB). Baris bawah: tiga hitungan salah dari daftar kesalahan umum. Papan skor. Kunci di cadangan C1.
- Layout: S9.
- Visual: Enam kartu putih dalam dua baris dengan ikon tile; pewaktu.
- Catatan: Kunci variasi di slide cadangan C1. Kunci kesalahan: lihat bahan ajar 8.3.

**79 · INT · Role play: jelaskan tagihan Rp645 juta kepada staf importir dalam dua menit**
- Isi: Empat langkah penjelasan (nilai impor, PPN, PPh 22, dasar hukum). Rubrik empat aspek. Tiga kelompok tampil; fasilitator memberi satu keberatan tak terduga.
- Layout: S9.
- Visual: Empat langkah bernomor; kartu rubrik putih; pewaktu 2 menit.
- Catatan: Fasilitator memerankan staf importir dan memberi satu keberatan tak terduga. Untuk satu kelompok, pakai: "Kalau saya tidak setuju, saya harus ke mana?" Untuk kelompok lain: "Kami juga dapat SKPKB dari KPP dan kas sedang seret. Apa pilihan kami?" (keduanya materi KB 7). Kelompok lain menilai dengan rubrik (Awal, Berkembang, Cakap, Mahir).

**80 · RAN · Satu rantai hitung dan tiga kesalahan yang paling sering terjadi**
- Isi: Rantai hitung PDRI ringkas. Tiga kartu kesalahan dengan dampaknya: BM/BMTP tidak masuk nilai impor (PPN kurang Rp36.300.000, PPh 22 kurang Rp8.250.000); DPP 11/12 untuk barang mewah (PPN kurang Rp5.083.400); tarif PPh 22 salah pilih (kurang Rp76.411.500). QR post-test.
- Layout: S10.
- Visual: Rantai lima kotak; tiga kartu dengan ikon tile segitiga peringatan; kartu QR.
- Sumber: Bahan ajar 8.3.
- Catatan: Setelah slide ini buka post-test 10 soal dengan kisi-kisi yang sama dengan pre-test.

### Penutup

**81 · PEN · Terima kasih**
- Isi: Ucapan terima kasih, ajakan refleksi Paspor Misi, daftar sumber resmi, kontak fasilitator (isian kosong). Pengumuman kelompok pemenang dilakukan lisan.
- Layout: S11.
- Visual: Panel kiri navy dengan medali emas dan cincin; pita diagonal emas dan sky; panel kanan kertas.
- Catatan: Umumkan kelompok pemenang lomba hitung dan bagikan stempel terakhir.

### Slide Cadangan (tidak dihitung)

| Kode | Judul | Isi |
| --- | --- | --- |
| C1 | Kunci lomba hitung: setiap variasi mengubah PDRI Kasus 1 | Tiga kotak hasil: tanpa API PPh 22 Rp114.617.250 (PDRI Rp282.722.550); BMTP lupa: nilai impor Rp1.198.230.000, PPN kurang Rp36.300.000, PPh 22 kurang Rp8.250.000; SKB: PDRI hanya PPN Rp168.105.300. |
| C2 | Kunci Pilih Tarifmu: status API menentukan tarif, kecuali barang khusus dan lampiran | Kisi 4 x 2: 1) 2,5%; 2) 7,5%; 3) 0,5%; 4) 0,25%; 5) 7,5% dari harga lelang; 6) 10%; 7) 0,5%; 8) 7,5% (tarif 0,5% hanya untuk importir dengan API). |
| C3 | Semua peraturan yang dipakai dalam deck ini berlaku per November 2026 | Tabel referensi dan status keberlakuan (salinan ringkas dari bahan ajar v3), termasuk UU Kepabeanan, PMK 51/PMK.04/2017 jo. 136/PMK.04/2022, UU 14/2002, UU KUP (Pasal 8, 9, 16, 23, 25, 26, 27, 36), PMK 118/2024 jo. 71/2026, dan PMK 81/2024. |
| C4 | Glosarium: singkatan yang dipakai sepanjang pelatihan | Tabel dua kolom: API, BMTP, DPP, KPP, nilai impor, PDRI, PIB, PK, PKP, SKB, SKP, SKPKB, SPHP, SPSA, SPT, SPTNP, STP. |
| C5 | Kunci Pilih Jalurmu: lihat penerbit surat, lalu pilih sengketa atau permohonan | Kisi 5 x 2: 1) keberatan Dirjen BC lewat Portal DJBC, 60 hari, jaminan; 2) keberatan Dirjen Pajak, 3 bulan, lunasi Rp20 juta yang disetujui, risiko sanksi 30%; 3) banding Pengadilan Pajak, 3 bulan, risiko sanksi 60%; 4) angsuran atau penundaan Pasal 9 ayat (4), jaminan aset senilai utang, bunga 0,61% per bulan (November 2026); 5) pengurangan atau penghapusan sanksi Pasal 36 ayat (1) huruf a, bukan keberatan, paling banyak dua kali; 6) pembetulan Pasal 16, diputus 6 bulan; 7) pembatalan Pasal 36 ayat (1) huruf d, hanya satu kali; 8) pembetulan SPT Pasal 8, selama belum diperiksa; 9) gugatan Pengadilan Pajak, 14 hari, tidak menunda penagihan; 10) PK Mahkamah Agung, 3 bulan sejak bukti ditemukan, satu kali, sanksi 60% bila putusan PK menambah pajak. Kasus 3: keberatan paling lambat 1 Mei 2026, jaminan Rp37.962.105. |

---

## Bagian C. Rekap

### Rekap jenis slide

| Jenis | Nomor slide | Jumlah |
| --- | --- | --- |
| Halaman judul | 1 | 1 |
| Studi kasus | 2, 3, 12, 24, 42, 43, 52, 59, 60, 66, 70, 73, 77 | 13 |
| Materi | 4, 9, 10, 11, 17, 18, 20, 21, 22, 28, 29, 30, 31, 38, 39, 40, 49, 50, 51, 58, 61, 65, 67, 68, 69, 72 | 26 |
| Interaksi | 5, 6, 13, 16, 19, 23, 27, 32, 33, 34, 37, 41, 44, 47, 53, 54, 55, 62, 71, 74, 78, 79 | 22 |
| Peralihan | 7, 8, 15, 26, 36, 46, 48, 57, 64, 76 | 10 |
| Rangkuman | 14, 25, 35, 45, 56, 63, 75, 80 | 8 |
| Penutup | 81 | 1 |
| **Total** | | **81** |

### Perubahan dari v2

| Aspek | v2 | v3 (revisi) |
| --- | --- | --- |
| KB 7 | Barang kiriman, 6 slide (64 sampai 69) | Upaya hukum dengan titik berat bidang perpajakan, 12 slide (64 sampai 75): 4 slide kepabeanan sebagai pintu masuk, 8 slide hak wajib pajak |
| Kasus 3 | Dua paket belanja daring (earbuds, sepatu) | SPTNP atas Kasus 1, tagihan Rp37.962.105 |
| Kasus 4 | Tidak ada | Surat dari KPP: SKPKB PPN dan risiko sanksi (slide 70), PPh 22 Impor lupa dikreditkan (slide 73), STP dan angsuran (kartu Pilih Jalurmu) |
| Interaksi KB 7 | Studi kasus kelompok | *Hinge question* STP (slide 71) dan Pilih Jalurmu (10 kartu), kunci di cadangan C5 |
| Role play KB 8 (slide 79) | Keberatan tak terduga bebas | Dua keberatan: jalur hukum, dan SKPKB saat kas seret |
| Slide KB 8 dan penutup | 70 sampai 75 | 76 sampai 81 |
| Cadangan | C1 sampai C4 | Tambah C5; glosarium C4 tanpa CN dan PJT, tambah KPP, PK, SKP, SKPKB, SPHP, SPSA, SPT, SPTNP, STP |

### Daftar periksa sebelum presentasi

- [ ] Isi nama fasilitator, tanggal, lokasi (slide 1), kode QR dan kode akses kuis (slide 5, 6, 33, 37, 47, 64, 71, 80), video berita BMTP (slide 2), kontak fasilitator (slide 81).
- [ ] Perbarui kurs bila kelas tidak berlangsung 18 sampai 24 November 2026, lalu bangun ulang deck.
- [ ] Konfirmasi angka bertanda "cek": tarif BM 5208.21.00 dan 8711.50, PPh 22 motor 10%, status PP 39/2019 (denda Kasus 3).
- [ ] Nomor ayat, batas permohonan Pasal 36, ketentuan angsuran, dan tarif bunga di slide 69, 70, 72, dan 73 sudah dicocokkan dengan sumber sekunder per 23 November 2026. Sebelum kelas: ganti tarif bunga 0,61% dengan KMK bulan kelas, dan cek putusan MK Perkara 91/PUU-XXIV/2026 (Pasal 36 ayat (1) huruf b).
- [ ] Perbarui slide 69 jika Perpres pengalihan Pengadilan Pajak ke Mahkamah Agung sudah terbit atau kelas berlangsung setelah 1 Januari 2027.
- [ ] Tambahkan animasi klik (jawaban slide 62, batang grafik satu per satu) di PowerPoint atau Canva bila dibutuhkan.
- [ ] Pasang font Poppins di komputer presentasi, atau impor ke Canva yang sudah memiliki Poppins.

### Cara membangun deck v3

Generator v2 (`media/sumber-deck-v2/`) membangun outline dari `slides.js`. Untuk deck v3, salin generator menjadi `media/sumber-deck-v3/`, ganti isi slide 64 sampai 69 di `slides.js` dengan slide 64 sampai 75 di outline ini, geser nomor slide KB 8 dan penutup menjadi 76 sampai 81, tambahkan cadangan C5, lalu jalankan:

```
cd media/sumber-deck-v3
npm install
python3 prep_assets.py
node build.js ../slide-pdri-v3.pptx
node check-numbers.js         # sesuaikan agar membaca bahan-ajar-pdri-v3.md
```
