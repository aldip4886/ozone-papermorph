# Handoff: KB 5 · Alur Pengkreditan PPh Pasal 22 Impor (materi baru)

**Tanggal:** 26 November 2026
**Sumber:** [storyboard KB 5 PPh 22 Impor v1](storyboard-kb5-pph22-impor-v1.md), [naskah VO](naskah-voiceover/kb5-pph22-impor-naskah-voiceover.md)
**Status:** pelajaran, voiceover final (Bodi, 13 adegan), SCORM 1.2 dan 2004, HTML per adegan, dan PDF layar penuh sudah dibangun. Semua cek lulus.

## 1. Penempatan

Sama seperti KB 4: folder `site/pdri-mck/ch51` dan `content/pdri-mck/ch51`, label tampilan **"KB 5"**. Bab 5 tidak disentuh.

## 2. Isi (13 adegan)

| No | Adegan | Jenis | Isi |
|---|---|---|---|
| 1 | `pembuka` | PER | "Kain belum laku, kok PPh sudah dipungut?"; Paspor Misi pertanyaan 4 |
| 2 | `jalur` | MAT | Garis waktu Jan–Des: PPh 21, 22 (emas), 23, 25 → SPT Tahunan |
| 3 | `beda` | INT | Pemotongan vs pemungutan; drag PPh 21/22 Impor/23/25 ke pemotongan, pemungutan, angsuran sendiri (`p-kategori`) |
| 4 | `pungut` | MAT | Pemungut DJBC dan bank devisa, dasar nilai impor, terutang bersama Bea Masuk, tidak final; PMK 51/2025 |
| 5 | `dimuka` | MAT | Dua lapis: transaksi impor → pembayaran di muka atas PPh importir → SPT Tahunan |
| 6 | `spt` | MAT | PT Kain Prima Nusantara → SPT PPh Badan; Bu Rina → SPT PPh Orang Pribadi |
| 7 | `hitung` | KAS | Cek tarif (pos 5208.21.00, API-U) → 2,5% × Rp1.528.230.000 = **Rp38.205.750** (isian, `c-pph22`) |
| 8 | `langkah` | MAT | Diagram keputusan tiga langkah (Lampiran A/B → emas batangan → API) |
| 9 | `tarif` | INT | Pilih Tarifmu: 8 skenario (kisi 4 × 2), tarif diseret ke setiap skenario (`p-tarif`) |
| 10 | `alur` | INT | Ikuti uangnya: susun 5 tahap (`p-alur-tahap`), lalu pasangkan pihak atau dokumen (`p-alur-pihak`) |
| 11 | `kredit` | MAT | Tiga pesan; Paspor Misi dengan stempel "MISI KB 5 SELESAI" |
| 12 | `api` | INT | Tanpa API 7,5% vs dengan API 2,5%; pilihan ganda reflektif (`c-api`) |
| 13 | `finish` | – | Kartu selesai |

Catatan isi:
- Storyboard adegan 9 menyebut kisi 4 × 2 tetapi hanya merinci 6 skenario. Dua skenario saya tambahkan dari tabel tarif: "Barang dalam Lampiran B" (7,5%) dan "Tepung terigu, importir ber-API" (0,5%).
- Pada adegan 10, tahap "Dana masuk ke kas negara" tidak punya pasangan di kunci storyboard, jadi tampil terisi sebagai "Kas negara".
- PPh 25 ikut diseret ke kelompok ketiga, "angsuran sendiri", sesuai catatan storyboard.

## 3. Voiceover

- Rekaman ada di `Downloads/vo_materi_5_1`: 14 WAV untuk 13 adegan. Semua dipetakan berdasarkan isi ucapan (skor 0,84–1,00).
- `10_27PM.wav` (20,7 dtk) tidak dipakai: itu versi lama `kredit` yang masih memuat "Stempel Paspor Misi kamu, ya". Yang dipakai `10_27PM (1).wav` (17,3 dtk), sesuai naskah terbaru.
- Perubahan naskah ikut disamakan di `narration.id.json`: `kredit` tanpa kalimat stempel, dan `finish` dimulai dengan "Sekarang kamu tahu kan…".
- Di `beda`, pembaca mengucapkan "Apakah bedanya…" (naskah: "Apa bedanya…"). Subtitle dan naskah disamakan dengan rekaman.
- Selisih lain hanya noise ASR. Timing hasil forced-alignment; total sekitar 4 menit 25 detik, sehingga `CHAPTER.minutes = 4`.

## 4. Output

| Output | Path | Ukuran |
|---|---|---|
| SCORM 1.2 | `dist/pdri/kb5-scorm12.zip` | 2,2 MB, 39 file |
| SCORM 2004 | `dist/pdri/kb5-scorm2004.zip` | 2,2 MB |
| HTML per adegan (13 + daftar) | `dist/pdri/html/kb5/` | |
| PDF layar penuh (13 hlm) | `dist/pdri/pdf/kb5-alur-pengkreditan-pph-pasal-22-impor-fullscreen.pdf` | 4,6 MB |

Paket langsung membuka pelajaran tanpa cover. Entri zip berformat DOS dengan izin 0644, aman untuk LMS di server Linux.

## 5. Verifikasi

| Cek | Hasil |
|---|---|
| `tools/pdri/e2e_mck_ch51.py` (pemutaran, replay, tata letak kuis, semua jawaban termasuk 4 drag-and-drop, finish) | lulus |
| Tinggi kartu kuis setelah dijawab (tombol Lanjutkan di atas bilah pemutar) | semua ≤ y 790 dari 900 |
| `check_scorm.py` (DIRECT) 1.2 dan 2004 | 5/5 lulus, keduanya |
| `check_interactions.py` 1.2 dan 2004 | lulus; cek generik hanya mengisi `c-pph22` dan `c-api` (soal drag-and-drop diuji di e2e) |
| Screenshot 13 adegan, dicek visual | ok |

## 6. Perubahan bersama

- `dragBoard`, `glyphSvg`, dan gaya drag-and-drop dipindah dari KB 4 ke `site/pdri-mck/lib/mck.js`, bersama glyph `store`, `calendar`, `bank`, dan `clock`. KB 4, Bab 1, dan Bab 4 tetap lulus e2e setelah pemindahan.
- `check_interactions.py` sempat gagal karena kartu `api` memanjang setelah dijawab sehingga tombolnya tertutup bilah pemutar. Teks pilihan dipendekkan dan kartu dinaikkan.

## 7. Gotcha

`build_scenes.py` (dan `build_deck.py`) mengenali adegan dari baris yang diawali dua spasi lalu `['id', '`. Baris data di halaman bab yang berbentuk sama ikut dihitung sebagai adegan. Indentasikan data seperti itu dengan tiga spasi (lihat `SCEN` di `ch51`).

## 8. Cara membangun ulang

```sh
export PYTHONUTF8=1 PW_CHANNEL=chrome
python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 51 --skip-cover
```

## 9. Yang tersisa

- Uji di LMS sungguhan (atau SCORM Cloud).
- Dengarkan rekaman sekali.
- Fakta yang diminta storyboard untuk dikonfirmasi (pemungut DJBC dan bank devisa, tarif PMK 51/2025, pos 5208.21.00 tidak tercantum di Lampiran A–D) dipakai apa adanya dari storyboard; konfirmasi akhirnya ada pada tim materi.
