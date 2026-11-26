# Handoff: build Bab 8 PDRI

**Tanggal:** 26 November 2026
**Branch:** `claude/pdri-bab8-vo`, dari `main` (setelah PR #18).
**Permintaan:** "Bangun SCORM individu untuk ch7 berdasarkan voiceover ini" dengan 15 WAV (Google AI Studio, 26 Nov 07.59–08.13), plus SCORM tanpa halaman cover dan pemilihan bab.

## 1. Voiceover

- **Rekaman ini Bab 8, bukan Bab 7.** Ke-15 WAV dibuka dengan "Inilah materi kedelapan, materi terakhir" dan isinya sama urut dengan 15 adegan Bab 8 (`map_wavs.py`). Terhadap teks Bab 7 semua skor di bawah 0,45. Bab 7 tidak disentuh; ia tetap memakai rekaman 25 Nov.
- **Pemetaan (urutan jam = urutan adegan):** 07.59 `intro`, 08.00 `ask`, 08.01 `lengkap`, 08.02 `porsi`, 08.03 `variasi`, 08.04 `q1`, 08.05 `salah`, 08.06 `q2`, 08.07 `jelaskan`, 08.08 `hak`, 08.09 `layanan`, 08.10 `empat`, 08.11 `wrap`, 08.12 `final1`, 08.13 `finish`. Tidak ada take sisa.
- **Format.** WAV 24 kHz mono → MP3 24 kHz / 48 kbps di `site/pdri-mck/ch08/audio/id/`. Sebelumnya Bab 8 belum punya audio (waktu perkiraan saja).
- **Durasi total** ±5 menit 55 detik; `CHAPTER.minutes` diubah dari 5 menjadi 6.

### Perbedaan rekaman dengan naskah

Teks narasi (`narration.id.json`, sumber subtitle) dan kolom Teks naskah disamakan dengan ucapan di rekaman:

| Adegan | Naskah lama | Di rekaman |
|---|---|---|
| `intro` | diawali "Mari kita lanjutkan, ya, sobat." | kalimat pembuka itu tidak diucapkan (kandidat take ulang bila ingin konsisten dengan bab lain) |
| `porsi` | "Dari mana lebih dari separuh itu?" | "Dari mana tagihan yang lebih dari separuh harga kain itu?" |
| `jelaskan` | berakhir di "...PPh Pasal dua puluh dua." | ditambah "Importir pun jadi paham bahwa sistem di Indonesia itu adil dan transparan." |
| `empat` | "Selama delapan materi" | "Selama delapan sesi ini" |
| `empat` | "UUD seribu sembilan ratus empat puluh lima" | "Undang-Undang Dasar ..." (dibaca panjang) |
| `final1` | "lomba hitung berikut ini" | "hitungan berikut ini" (judul soal di layar tetap "Lomba hitung") |

Sisanya hanya beda ejaan ASR (angka sebagai digit, "DJBC"→"dgbc").

### Timing

Semua beat di-forced-align (`align_chapter.py`) ke `timings.js` dan `content/pdri-mck/ch08/narration.id.timings.json` (baru). Tidak ada beat `silent`.

## 2. Output

| Output | Path | Ukuran |
|---|---|---|
| SCORM 1.2 (tanpa cover dan pilih bab) | `dist/pdri/ch08-scorm12.zip` | 2,7 MB |
| SCORM 2004 4th ed. (tanpa cover dan pilih bab) | `dist/pdri/ch08-scorm2004.zip` | 2,7 MB |
| HTML per adegan | `dist/pdri/html/bab8/` (15 + `00-daftar-adegan.html`) | 0,4–0,8 MB per file |
| PDF layar penuh | `dist/pdri/pdf/bab8-menjawab-staf-importir-fullscreen.pdf` (15 hlm) | 5,3 MB |

Folder HTML Bab 8 lama (14 adegan, tanpa suara) diganti; nomor file bergeser karena adegan `hak` (10).

Salinan di project files: `papermorph/pdri/paket-zip/media-interaktif/pdri-bab8-scorm{12,2004}.zip`, `papermorph/pdri/bab8-html-pdf/{html,pdf}/`, `papermorph/pdri/voiceover/bab8/`.

## 3. Verifikasi

| Cek | Hasil |
|---|---|
| `tools/pdri/e2e_mck_ch08.py` (skrip baru) | lulus (15 beat) |
| `check_scorm.py` `DIRECT=1`, SCORM 1.2 dan 2004 | lulus, 5/5 tiap versi |
| `check_interactions.py` `DIRECT=1`, SCORM 1.2 dan 2004 | lulus |
| Semua soal tercatat (`check_all_interactions.py`) | 5 soal: `c-pdri-non`, `c-salah-lembar`, `p-lomba-non`, `p-lomba-lupa`, `p-urutan` |
| Tangkapan layar 15 adegan | dicek visual, tidak ada teks terpotong atau adegan kosong |

## 4. Bangun ulang

```
PYTHONUTF8=1 python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 8
PYTHONUTF8=1 python .claude/skills/pdri-scorm-skip-cover/scripts/skip_cover.py dist/pdri/ch08-scorm12.zip dist/pdri/ch08-scorm2004.zip
```

Di container cloud: model Whisper small dari tarball npm `@skillninja/shortmovie-telop-model-p0..p3` (HuggingFace diblokir); Python `playwright==1.63.0` agar cocok dengan Chromium yang terpasang.

## 5. Lanjutan

- Dengar ulang, terutama `intro` (tanpa pembuka) dan kalimat tambahan di `jelaskan`.
- Uji di LMS sungguhan atau SCORM Cloud.
- Storyboard Bab 8 (`docs/storyboard-pdri/bab8-storyboard.md`, kolom durasi) belum dibangun ulang dengan durasi rekaman.
