# Handoff: build Bab 6 dan Bab 7 PDRI

**Tanggal:** 25 November 2026
**Branch:** `claude/pdri-bab6-7-vo`, dari `main` yang sudah memuat `Papermorph/` (PR #15).
**Cara kerja:** skill proyek `pdri-build-chapter` (`.claude/skills/pdri-build-chapter/`).

## 1. Voiceover

**Sebelumnya:** Bab 6 memakai draf suara; Bab 7 belum punya audio sama sekali (naskah sudah berubah dari "Barang Kiriman" menjadi "Upaya Hukum dan Hak Wajib Pajak").

**Sekarang:** rekaman Google AI Studio (Bodi) tanggal 25 Nov. Bab 6: 15 WAV (`Downloads/vo-chapter-6`, 08:57–09:14). Bab 7: 14 WAV (`Downloads/vo-chapter-7`, 09:17–09:32).

- **Pemetaan WAV ke beat.** Dengan `map_wavs.py` (transkripsi faster-whisper). Hasilnya satu take per beat, tanpa take sisa, urutan waktu cocok dengan urutan beat.
- **Format.** MP3 mono 24 kHz / 48 kbps. Draf lama Bab 6 dicadangkan ke folder sementara, tetap ada di riwayat git.
- **Timing.** Semua beat di-forced-align ke `timings.js` dan `narration.id.timings.json`. Total Bab 6 ±4 menit 40 detik (`minutes` tetap 5), Bab 7 ±5 menit 29 detik (`minutes` diubah dari 6 menjadi 5).
- **Scene terakhir Bab 6 (`finish`)** sudah diganti: materi berikutnya adalah upaya hukum (bukan barang kiriman).

### Perbedaan rekaman dengan teks, dan penanganannya

Pembacaan mengikuti naskah `docs/naskah-voiceover/` yang lebih baru, sedangkan `narration.id.json` masih versi lama. Teks narasi disamakan dengan ucapan (semua `[[mark]]` dipertahankan).

| Bab | Beat | Temuan | Tindakan |
|---|---|---|---|
| 6 | `intro` | Rekaman "Sobat, pada materi keenam ini, kita akan pelajari bagaimana penghitungan…"; kalimat "Mari kita lanjutkan, ya," tidak diucapkan | Narasi disamakan dengan rekaman. **Kandidat rekam ulang** bila pembuka standar ingin dipertahankan |
| 6 | `ppnbm` | "UU PPN" dibaca "Undang-Undang PPN" | Narasi disamakan |
| 6 | `wrap`, `finish` | Tanpa "Jadi," dan tanpa "Bagus," | Narasi disamakan |
| 7 | `jalur1` | Kalimat pembuka rekaman "Terhadap penetapan ini, PT Kain Prima Nusantara bisa melakukan upaya hukum." | Narasi disamakan |
| 7 | `hak` | "dua kelompok hak", ditambah "Hak ini digunakan untuk…" dan "Permohonan bertujuan…" | Narasi disamakan. Teks di layar (adegan `hak`) sudah diubah menjadi "dua kelompok hak" |
| 7 | `bandingkan`, `lensa` | Kalimat pembuka dan "Undang-Undang Dasar", "berdasarkan undang-undang" berbeda dari narasi lama | Narasi disamakan |
| 7 | `wrap` | Pembaca mengucapkan "Untuk ketetapan dari DJP, wajib pajak bisa menempuh jalur sengketa… atau permohonan, yang tidak ada sanksi", tanpa "Jadi," | Narasi dan naskah md disamakan |
| 7 | `finish` | Tanpa "Bagus," | Narasi dan naskah md disamakan |

Selisih lain hanya ejaan ASR (angka, "DJBC"→"dgbc", "Bu Rina", dan sebagainya). Cek pelafalan (`check_pronunciation.py`): angka dan persen terbaca terbilang; lafal singkatan (PDRI, SKB, DJP) tampak huruf per huruf. Perlu dikonfirmasi dengan review dengar.

## 2. Output

| Output | Bab 6 | Bab 7 |
|---|---|---|
| SCORM 1.2 | `dist/pdri/ch06-scorm12.zip` (2,3 MB) | `dist/pdri/ch07-scorm12.zip` (2,6 MB) |
| SCORM 2004 4th ed. | `dist/pdri/ch06-scorm2004.zip` (2,3 MB) | `dist/pdri/ch07-scorm2004.zip` (2,6 MB) |
| HTML per adegan | `dist/pdri/html/bab6/` (15 + daftar) | `dist/pdri/html/bab7/` (14 + daftar) |
| PDF layar penuh | `dist/pdri/pdf/bab6-barang-mewah-dan-fasilitas-fullscreen.pdf` (15 hlm) | `dist/pdri/pdf/bab7-upaya-hukum-dan-hak-wajib-pajak-fullscreen.pdf` (14 hlm) |

Pengaturan SCORM sama dengan bab lain: mastery 70%, judul "PDRI: Pajak dalam Rangka Impor (Bab N)", setiap jawaban dicatat sebagai `cmi.interactions`.

Folder HTML Bab 7 lama (barang kiriman, 15 file) diganti seluruhnya. `dist/pdri/pdf/bab7-barang-kiriman-fullscreen.pdf` (23 Nov) adalah sisa lama, tidak dilacak git, dan boleh dihapus.

## 3. Verifikasi

| Cek | Bab 6 | Bab 7 |
|---|---|---|
| e2e bab (`tools/pdri/e2e_mck_ch06.py`, `e2e_mck_ch07.py`, skrip baru) | lulus (15 beat) | lulus (14 beat) |
| `check_scorm.py`, SCORM 1.2 dan 2004 | lulus | lulus (5/5 tiap versi) |
| `check_interactions.py`, SCORM 1.2 dan 2004 | lulus | lulus, 5 record |
| Semua soal tercatat (`check_all_interactions.py`) | 5 soal: `c-tarif-ppnbm`, `c-kredit`, `p-temukan-salah`, `p-selisih`, `p-efek-skb` | 5 soal: `c-jalur-djbc`, `c-stp-khilaf`, `p-sptnp`, `p-stp-khilaf2`, `p-surat-paksa` |
| Screenshot semua adegan, dicek visual | ok | ok |

## 4. Membangun ulang

```sh
export PYTHONUTF8=1 PW_CHANNEL=chrome
python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 6
python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 7
```

## 5. Perubahan tooling

- Skrip cek (`check_scorm.py`, `check_interactions.py`, `check_all_interactions.py`, `shoot_scenes.py`) kini membaca env `PW_CHANNEL`. Di mesin ini Chromium headless-shell bawaan Playwright crash saat membuka paket (bahkan paket Bab 5 yang sudah lulus), sehingga dipakai Chrome terpasang (`PW_CHANNEL=chrome`). Tanpa env itu perilaku lama tidak berubah.
- Untuk `e2e_mck_chNN.py`, set `CHROME="C:/Program Files/Google/Chrome/Application/chrome.exe"`.

## 6. Pembaruan susulan (25 Nov)

- Teks layar Bab 7 adegan `hak` (judul adegan dan judul aksi) diubah dari "dua keluarga hak" menjadi "dua kelompok hak", sesuai naskah dan rekaman. Paket SCORM, HTML per adegan, dan PDF Bab 7 dibangun ulang; semua cek lulus lagi.
- Kolom "Durasi draf" di naskah Bab 6–7 kini "Durasi rekaman" (detik dari MP3 final), beserta total durasi di atas tabel.
- Storyboard Bab 6–7 dibangun ulang dengan `make_storyboard.py`: lembar kontak `books/pdri/review/ch0{6,7}-mck/storyboard-adegan.jpg` dan `docs/storyboard-pdri/bab{6,7}-storyboard.md`. Storyboard Bab 7 sebelumnya masih versi "Barang Kiriman". Kolom durasi memakai durasi VO, bukan durasi pratinjau MP4.

## 7. Lanjutan

1. Review dengar kedua bab.
2. Uji paket di SCORM Cloud atau LMS target.
3. `dist/pdri/pdf/bab7-barang-kiriman-fullscreen.pdf` adalah sisa lama (tidak dilacak git) dan boleh dihapus.
