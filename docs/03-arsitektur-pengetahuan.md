# Analisis Arsitektur Pengetahuan: Materi PDRI untuk Pegawai Baru Bea Cukai

21 Nov 2026 · @John

Dokumen ini menjadi dasar outline v2 ([04-outline-materi-v2.md](04-outline-materi-v2.md)) dan session plan v2 ([05-session-plan-v2.md](05-session-plan-v2.md)). Outline dan session plan v1 tetap disimpan apa adanya.

**Jenis input:** course (pelatihan 8 JP x 45 menit)
**Peserta:** pegawai baru DJBC, usia sekitar 20 sampai 25 tahun, maksimal 30 orang per kelas
**Tujuan belajar (ringkas):** memahami teori dasar dan sistem pemungutan pajak di Indonesia, memahami mekanisme PPN (PK-PM) dan *withholding* PPh 22, lalu menghitung PPN Impor, PPnBM Impor, dan PPh Pasal 22 Impor untuk impor umum, barang mewah, dan barang kiriman, serta menjelaskan tagihan itu kepada pengguna jasa.
**Batas:** nilai pabean, kurs, Bea Masuk, dan BMTP sudah diajarkan di materi lain dan masuk sebagai data kasus. Cukai dibahas di modul tersendiri.

## 1. Diagnosis epistemik

**Tipe arsitektur:** campuran, dengan porsi hierarkis paling besar.
**Proporsi (perkiraan):** 50% hierarkis, 30% horizontal, 20% disposisional.

**Hierarkis (50%).** Seluruh tujuan "menghitung" punya rantai prasyarat yang tegas. Nilai impor harus benar dulu sebelum PPN, PPnBM, dan PPh 22 bisa dihitung, karena ketiganya memakai nilai impor sebagai dasar. Kesalahan di bawah merambat ke atas: kalau BMTP lupa dimasukkan ke nilai impor, PPN dan PPh 22 ikut salah. Bagian konsep juga sebagian hierarkis. Peserta perlu paham *self assessment* dan kredit pajak sebelum bisa memahami kenapa PPh 22 Impor tidak final, dan perlu paham PK-PM sebelum bisa menjelaskan kenapa PPN Impor bukan "uang hilang" bagi importir PKP.

**Horizontal (30%).** Teori pembenaran pajak (asuransi, kepentingan, daya pikul, bakti, daya beli), asas pemungutan (Adam Smith; domisili, sumber, kebangsaan), fungsi pajak, dan pembedaan pajak dengan pungutan lain adalah lensa-lensa untuk membaca satu fenomena yang sama: kenapa tagihan impor itu sah dan adil. Urutannya bisa dibolak-balik. Teori asuransi tidak perlu dikuasai dulu sebelum teori daya pikul. Yang berkembang adalah kemampuan analisisnya: dari sekadar menyebut teori, lalu menerapkannya ke kasus, sampai melihat ketegangan antar lensa (misalnya fungsi *regulerend* BMTP lawan asas netralitas PPN).

**Disposisional (20%).** Dua kemampuan tidak bisa diuji dengan satu soal. Pertama, menjelaskan tagihan kepada pengguna jasa dengan tenang dan jelas (target role play JP 8). Kedua, kecermatan: kebiasaan memeriksa status importir, jenis barang, tarif, dan aturan yang berlaku sebelum menghitung. Keduanya baru terlihat lewat pengamatan berulang, jadi harus dilatih di setiap JP, bukan hanya di akhir.

## 2. Peta arsitektur pengetahuan

### Elemen hierarkis

**Rantai A: perhitungan PDRI** (inti tujuan pelatihan)

```
[Data kasus dari materi lain] Nilai pabean (CIF x kurs), Bea Masuk, BMTP
    ↓ [prasyarat keras]
A1. Nilai impor = nilai pabean + BM + bea masuk tambahan (BMTP, BMAD, dst.)
    ↓ [prasyarat keras untuk A2, A3, A4]
    ├── A2. PPN Impor
    │     objek PPN impor → tarif 12% → barang mewah atau bukan?
    │     ├── non mewah: 12% x 11/12 x nilai impor (efektif 11%, PMK 131/2024)
    │     └── mewah: 12% x nilai impor
    ├── A3. PPnBM Impor  [prasyarat keras: A1; prasyarat lunak: A2]
    │     barang mewah? → tarif sesuai PMK (motor > 500 cc: 95%) → tarif x nilai impor
    └── A4. PPh 22 Impor  [prasyarat keras: A1]
          status API? → barang ada di lampiran PMK 51/2025? → tarif → tarif x nilai impor
    ↓ [prasyarat keras]
A5. Fasilitas dan pengecualian (SKB PPh 22, PPN tidak dipungut atau dibebaskan)
    ↓ [prasyarat lunak]
A6. Barang kiriman: rezim tersendiri (batas FOB USD 3 dan USD 1.500, komoditas tertentu)
    ↓ [prasyarat keras: A1 sampai A6]
A7. Perhitungan terpadu dan diagnosis kesalahan
```

**Rantai B: konsep yang memberi makna pada angka**

```
B1. Pengertian dan unsur pajak (Pasal 1 angka 1 UU KUP, Pasal 23A UUD 1945)
    ↓ [prasyarat lunak]
B2. Sistem pemungutan: official assessment, self assessment, withholding
    ↓ [prasyarat keras untuk B3b]
    ├── B3a. PPN sebagai pajak konsumsi bertingkat → PK-PM → PPN Impor = pajak masukan
    │         [prasyarat keras untuk menjelaskan "uang PPN ke mana"]
    └── B3b. PPh: pelunasan dalam tahun berjalan → withholding → PPh 22 Impor = kredit pajak, tidak final
```

**Titik temu.** Rantai A dan B bertemu di dua tempat: A2 dengan B3a (menghitung PPN lalu menjelaskan nasibnya di SPT Masa importir) dan A4 dengan B3b (menghitung PPh 22 lalu menjelaskan bahwa uang itu nanti jadi kredit pajak). Di v1, kedua pasangan ini dipisah 2 sampai 3 JP. Di v2, konsep dan hitungannya diajarkan di JP yang sama.

### Elemen horizontal

**Hub 1: "Kenapa tagihan kain ini sah dan adil?"**

```
                        ┌── Lensa hukum: Pasal 23A UUD 1945, UU KUP, UU PPN, UU PPh
                        ├── Lensa fungsi: budgetair (penerimaan) dan regulerend (BMTP, tarif non-API)
Tagihan Rp645 juta ─────├── Lensa teori pembenaran: asuransi, kepentingan, daya pikul, bakti, daya beli
                        ├── Lensa asas: equality, certainty, convenience, economy; domisili, sumber, kebangsaan
                        └── Lensa pembeda: pajak, retribusi, PNBP, bea masuk (cukai hanya disebut)
```

**Hub 2: "Siapa memegang peran apa?"**

```
                        ┌── Importir: menghitung sendiri di PIB (self assessment)
                        ├── DJBC: meneliti dan memungut di pelabuhan (official assessment, withholding)
Satu dokumen PIB ───────├── Bank devisa: menerima pembayaran
                        ├── DJP: mengurus pengkreditan dan SPT importir
                        └── Konsumen akhir: penanggung PPN sebenarnya
```

**Perkembangan kemampuan analisis:**

| Tahap | Yang dilakukan peserta |
| --- | --- |
| Menyebut | "Pajak itu iuran wajib berdasarkan undang-undang." |
| Menerapkan | "BMTP kain ini contoh fungsi *regulerend*, karena tujuannya melindungi industri tekstil dalam negeri." |
| Membandingkan | "Tarif PPh 22 non-API 7,5% bersifat mengatur, tapi dari sisi asas *equality*, importir kecil bisa merasa diperlakukan lebih berat." |
| Menilai | "Karena PPh 22 tetap bisa dikreditkan, tarif non-API lebih menekan arus kas daripada menambah beban pajak akhir. Dari sisi itu, kebijakannya masih bisa dibela." |

**Fleksibilitas urutan.** Lensa bisa dibuka dalam urutan apa pun. Untuk peserta baru, lensa hukum dan fungsi paling mudah jadi pintu masuk karena langsung terlihat di kasus kain. Lensa teori pembenaran dan asas lebih abstrak, jadi diberikan sesudahnya dan dipakai dalam debat. Lensa yang sama dipanggil lagi di JP 5 (tarif non-API), JP 6 (PPnBM), dan JP 7 (BM alas kaki barang kiriman) supaya teori tidak berhenti di JP 2.

### Elemen disposisional

**Kompetensi 1: Menjelaskan tagihan kepada pengguna jasa**

| Level | Indikator yang bisa diamati |
| --- | --- |
| Awal | Membacakan angka tanpa menjelaskan asalnya. Memakai istilah teknis (DPP, PK-PM) tanpa penjelasan. Gugup atau defensif saat ditanya balik. |
| Berkembang | Menjelaskan urutan hitungan dengan benar, tapi masih panjang dan berbelit. Menyebut dasar hukum saat diminta. |
| Cakap | Menjelaskan tagihan dalam 2 menit dengan urutan nilai impor, PPN, PPh 22. Menerjemahkan istilah ke bahasa awam. Menyebut aturan yang tepat (PMK 131/2024, PMK 51/2025) tanpa diminta. |
| Mahir | Mengantisipasi keberatan ("PPN ini bisa Bapak kreditkan karena perusahaan PKP"). Tetap tenang saat pengguna jasa marah. Tahu kapan harus mengarahkan ke DJP atau ke seksi lain. |

**Kompetensi 2: Kecermatan dan kebiasaan verifikasi**

| Level | Indikator yang bisa diamati |
| --- | --- |
| Awal | Langsung menghitung dengan tarif yang diingat. Tidak memeriksa status API, PKP, atau jenis barang. |
| Berkembang | Memeriksa status importir saat diingatkan. Mulai memakai tabel tarif, tapi belum mengecek lampiran barang tertentu. |
| Cakap | Sebelum menghitung, selalu mengecek status importir, jenis barang (mewah atau bukan), lampiran PMK 51/2025, dan kurs minggu berjalan. Mengecek ulang komponen nilai impor. |
| Mahir | Menemukan kesalahan di hitungan orang lain dan menjelaskan dampaknya dalam Rupiah. Mempertanyakan data kasus yang janggal. Bertanya "aturan ini masih berlaku?" sebelum memakai angka. |

## 3. Catatan arsitektur campuran

**Hierarkis dengan horizontal.** Debat di JP 2 (horizontal) butuh pemahaman dasar tentang apa itu BMTP dan PPN. Karena itu, JP 1 sudah membedah tagihan dan menghitung nilai impor, supaya debat punya angka nyata untuk diperdebatkan. Sebaliknya, lensa *regulerend* baru terasa tajam setelah peserta menghitung sendiri selisih PPh 22 API dan non-API (JP 5) dan melihat PPnBM 95% motor (JP 6).

**Hierarkis dengan disposisional.** Role play penutup (disposisional) tidak bisa berhasil kalau rantai A belum tuntas. Peserta yang belum yakin hitungannya cenderung defensif. Karena itu lomba hitung dan diagnosis kesalahan ditaruh sebelum role play di JP 8, dan setiap JP punya latihan "jelaskan 30 detik" yang singkat sebagai pemanasan.

**Horizontal dengan disposisional.** Kemampuan menjawab keberatan pengguna jasa ("kenapa saya harus bayar PPh padahal kain belum laku?") memakai lensa teori dan sistem pemungutan. Jadi teori di JP 2 dan JP 3 bukan hafalan, tapi bahan jawaban di loket.

**Ketegangan utama di v1.** Empat JP pertama seluruhnya konsep, dan hitungan baru dimulai di JP 6. Ini profil semantik yang datar: lama di tingkat abstrak, jauh dari kasus. Pasangan konsep dan hitungan juga terpisah: PPN dibahas di JP 4 tapi dihitung di JP 6; PPh 22 dibahas di JP 5 tapi tarifnya di JP 7. Akibatnya, peserta harus mengingat konsep selama dua JP sebelum memakainya. V2 memperbaiki ini dengan pola gelombang di setiap JP: kasus konkret, konsep, hitungan, lalu kembali ke prinsip.

## 4. Implikasi untuk urutan dan tempo

**Urutan yang terkunci (hierarkis).** Nilai impor (JP 1) harus sebelum PPN (JP 4), PPN sebelum PPnBM (JP 6), PPh 22 (JP 5) sebelum fasilitas SKB (JP 6), dan semuanya sebelum barang kiriman (JP 7) dan perhitungan terpadu (JP 8). Sistem pemungutan (JP 3) harus sebelum *withholding* PPh 22 (JP 5).

**Urutan yang lentur (horizontal).** Lensa teori dan asas di JP 2 boleh disusun ulang fasilitator. Contoh pertanyaan lensa yang dipanggil lagi di JP 5 sampai 7 juga boleh diganti dengan isu terbaru.

**Benang merah (disposisional).** Setiap JP ditutup dengan satu latihan singkat: "jelaskan 30 detik ke importir" atau "cek dulu sebelum hitung". Paspor Misi memuat kolom refleksi singkat yang dibaca fasilitator untuk melihat perkembangan.

**Tempo.** Bagian I tetap condong ke konsep, tapi sudah ada dua hitungan (nilai impor di JP 1, PPN kain di JP 4). Bagian II condong ke praktik, dengan konsep PPh 22, PPnBM, dan barang kiriman diberikan tepat sebelum dipakai.

## 5. Implikasi untuk penilaian

**Bisa dinilai otomatis (aplikasi kuis atau spreadsheet):**
- Menghitung nilai impor, PPN Impor (non mewah dan mewah), PPnBM Impor, PPh 22 Impor, dan pungutan barang kiriman. Jawabannya angka tunggal.
- Memilih tarif PPh 22 dari kartu skenario. Satu jawaban benar per kartu.
- Mengklasifikasikan sistem pemungutan dan instansi pemungut. Pilihan ganda.

**Perlu penilaian fasilitator:**
- Role play menjelaskan tagihan (Kompetensi 1). Perlu rubrik dan pengamatan langsung.
- Kualitas argumen debat di JP 2 (horizontal, tahap membandingkan dan menilai).
- Kecermatan (Kompetensi 2). Diamati dari kebiasaan selama latihan, bukan dari satu soal.

**Sebagian otomatis:**
- Soal diagnosis kesalahan. Aplikasi bisa menilai "komponen mana yang salah", tapi alasan dan dampaknya perlu dibaca fasilitator.
- Isian singkat "jelaskan kenapa PPh 22 tidak final". Kata kunci bisa dicek otomatis, kedalaman penjelasan perlu dibaca.

## 6. Implikasi untuk alat bantu digital

- **Kalkulator PDRI (spreadsheet).** Dipakai sesuai rantai A: kolom nilai impor terkunci sampai diisi benar, baru kolom PPN dan PPh 22 terbuka. Dengan begitu, kesalahan di A1 tidak merambat diam-diam.
- **Aplikasi kuis.** Cocok untuk pre-test, kuis kilat, *hinge question*, dan post-test. Umpan balik langsung hanya untuk soal hitung dan klasifikasi.
- **Bagian horizontal dan disposisional.** Jangan dinilai otomatis. Aplikasi cukup dipakai untuk mengumpulkan jawaban refleksi atau argumen, lalu fasilitator yang membaca dan memberi umpan balik.

## Keterbatasan analisis

Proporsi 50/30/20 adalah perkiraan untuk membantu keputusan desain, bukan ukuran pasti. Kategori disposisional bukan bagian dari teori Bernstein; dipakai di sini sebagai alat desain. Analisis berangkat dari tujuan yang tertulis di outline v1; hasil di kelas tetap bergantung pada pelaksanaan.
