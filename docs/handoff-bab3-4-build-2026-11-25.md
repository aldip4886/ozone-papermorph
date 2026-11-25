# Handoff: build Bab 3 dan Bab 4 PDRI

**Tanggal:** 25 November 2026
**Branch:** `claude/pdri-bab3-4-build`
**Status:** Bab 3 dan Bab 4 sudah dibangun ulang dengan voiceover final. Ketiga output (SCORM, HTML per adegan, PDF layar penuh) sudah diverifikasi.

## 1. Status voiceover

### Bab 3: sudah memakai VO terbaru

Saya membandingkan 17 WAV di `Downloads/vo_materi_3/new` dengan aset proyek memakai hash MD5:

- **16 WAV identik** dengan `dist/ch03-voiceover-staging/*.wav`. Setiap MP3 di `site/pdri-mck/ch03/audio/id/` sama byte demi byte dengan MP3 staging. Artinya ke-16 beat (`intro` … `finish`, termasuk `syarat` dan `rina` yang baru) sudah memakai rekaman terbaru: Google AI Studio, Gemini 3.8 Flash TTS, suara Bodi.
- **1 WAV tidak dipakai untuk Bab 3.** File `Generated Audio November 24, 2026 - 5_06PM.wav` (29,76 detik) ternyata beat **`rina` Bab 4**: durasinya persis sama dengan `site/pdri-mck/ch04/audio/id/rina.mp3`, dan isinya sesuai transkripsi. File ini tersasar ke folder Bab 3 dan tidak perlu dipasang ke Bab 3.

**Timing Bab 3 sudah diperbaiki.** Handoff sebelumnya (`handoff-ch03-voiceover-2026-11-24.md`) mencatat bahwa cue dan mark animasi Bab 3 hanya diskalakan secara proporsional dari draf. Sekarang semua 16 beat sudah di-*forced-align* ke audio sebenarnya. Prosesnya memakai faster-whisper `small` dan fungsi `align()` dari skill `pdri-voiceover`. Hasilnya ditulis ke `site/pdri-mck/ch03/audio/id/timings.js` dan `content/pdri-mck/ch03/narration.id.timings.json`, yang sebelumnya masih berisi kata-kata dari audio lama. Total durasi 6 menit 5 detik, sehingga `CHAPTER.minutes` Bab 3 dinaikkan dari 5 menjadi 6.

### Bab 4: sudah memakai rekaman final, bukan VO sampel

- Ke-16 MP3 Bab 4 berasal dari rekaman Google AI Studio (Bodi): 15 WAV di `Downloads` (24 Nov, 17:35–17:45) ditambah `5_06PM.wav` untuk `rina`. Durasi setiap MP3 sama persis dengan WAV-nya. Draf suara Ardi (edge-tts) sudah tidak dipakai.
- `timings.js` dan `narration.id.timings.json` Bab 4 sudah hasil alignment dari audio asli: durasi = MP3 + 0,25 detik, dengan kata ASR per beat.
- Metadata `content/pdri-mck/ch04/narration.id.json` masih menyebut `id-ID-ArdiNeural`, jadi sudah saya perbarui menjadi Gemini 3.8 Flash TTS, Bodi.

### Kecocokan isi dengan naskah dan storyboard

Semua 32 beat (Bab 3 dan Bab 4) ditranskripsi, lalu dibandingkan kata per kata dengan `narration.id.json`, `docs/naskah-voiceover/bab{3,4}-naskah-voiceover.md`, dan `docs/storyboard-pdri/bab4-storyboard.md`. **Tidak ada kalimat yang hilang, tertukar, atau berbeda.** Selisih yang muncul hanya akibat ejaan ASR, misalnya "DJBC" ditulis "dgbc", "11/12" ditulis "11x12", dan "Bu Rina" ditulis "burina", serta angka di naskah yang dieja dengan huruf. Total durasi Bab 4 adalah 5 menit 30 detik.

> Belum ada review dengar manual. Transkripsi memastikan kata-katanya benar, tetapi pelafalan singkatan (DJBC/DJP, API-U/API-P) sebaiknya didengar sekali oleh manusia.

## 2. Output

| Output | Bab 3 | Bab 4 |
|---|---|---|
| SCORM 1.2 | `dist/pdri/ch03-scorm12.zip` (5,0 MB) | `dist/pdri/ch04-scorm12.zip` (2,6 MB) |
| SCORM 2004 4th ed. | `dist/pdri/ch03-scorm2004.zip` | `dist/pdri/ch04-scorm2004.zip` |
| HTML per adegan (16 + daftar) | `dist/pdri/html/bab3/` | `dist/pdri/html/bab4/` |
| PDF layar penuh (16 hlm) | `dist/pdri/pdf/bab3-pihak-dan-sistem-pemungutan-fullscreen.pdf` | `dist/pdri/pdf/bab4-pajak-pertambahan-nilai-impor-fullscreen.pdf` |

**SCORM.** Paket dibangun dengan skill Papermorph versi terbaru (`Papermorph/.claude/skills/papermorph/scripts/scorm.py` beserta `scorm-bridge.js`/`scorm-host.js` yang sudah dimodifikasi). Pengaturan paket:

- Mastery 70%, judul "PDRI: Pajak dalam Rangka Impor (Bab N)", sama dengan paket Bab 1–3 sebelumnya.
- Data yang dilacak:
  - completion
  - score (jawaban percobaan pertama)
  - objective per bab
  - resume (`suspend_data`)
  - **setiap jawaban soal sebagai `cmi.interactions`** dengan id `chNN.<id-soal>[.<baris>]`. Hook-nya adalah `window.onInteraction` di `site/pdri-mck/lib/engine.js`.

**HTML per adegan.** Setiap file berdiri sendiri (suara, font, dan gambar sudah tertanam) dan punya tombol Lanjut ke adegan berikutnya. Bab 3 kini 16 adegan (sebelumnya 14, tanpa `syarat` dan `rina`), dan Bab 4 kini 16 adegan (sebelumnya 15, tanpa `rina`). File lama dengan penomoran yang bergeser sudah dihapus.

**PDF.** Isinya keadaan akhir setiap adegan, satu adegan per halaman, dengan `PageMode /FullScreen`.

## 3. Verifikasi yang sudah dijalankan

| Cek | Bab 3 | Bab 4 |
|---|---|---|
| e2e bab (`tools/pdri/e2e_mck_ch0N.py`): playback, replay tiap beat, layout kartu kuis, jawaban, finish | lulus | lulus (skrip baru) |
| `check_scorm.py` (mock LMS): sesi, folder link, finish card, objective, resume; 1.2 dan 2004 | 5/5 lulus | 5/5 lulus |
| `check_interactions.py`: hook terpasang, `cmi.interactions` tertulis, format id, tidak ada SetValue yang ditolak, tidak ada status `failed` palsu; 1.2 dan 2004 | lulus, 14 record | lulus, 3 record* |
| Screenshot 32 adegan (Chromium 1920×1080 @1.5x) tanpa error konsol, diperiksa visual | ok | ok |

\* Checker generik menjawab "0" pada soal isian Latihan 4.1. Jawaban yang salah itu menahan kartu latihan, sehingga 2 soal latihan berikutnya tidak tersentuh oleh checker. Saya mengecek terpisah dengan menjawab semua soal Bab 4: kelima soal (`c-efektif`, `c-setor`, `p-ppn-50rb`, `p-hilang`, `p-lebih`) memanggil `onInteraction`.

## 4. Cara membangun ulang

Jalankan dari root repo dengan `PYTHONUTF8=1`, karena skrip membaca file tanpa encoding eksplisit dan default Windows adalah cp1252.

```sh
# SCORM (N = 3 atau 4)
python tools/pdri/scorm/stage_chapter.py site/pdri-mck N dist/pdri/stage/ch0N
python Papermorph/.claude/skills/papermorph/scripts/scorm.py dist/pdri/stage/ch0N --version 1.2  --mastery 70 --title "PDRI: Pajak dalam Rangka Impor (Bab N)" --out dist/pdri
python Papermorph/.claude/skills/papermorph/scripts/scorm.py dist/pdri/stage/ch0N --version 2004 --mastery 70 --title "PDRI: Pajak dalam Rangka Impor (Bab N)" --out dist/pdri
python Papermorph/.claude/skills/papermorph/assets/scorm/test/check_scorm.py dist/pdri/ch0N-scorm12.zip
python Papermorph/.claude/skills/papermorph/assets/scorm/test/check_interactions.py dist/pdri/ch0N-scorm12.zip

# HTML per adegan + PDF
python tools/pdri/scenes/build_scenes.py WORK/html N
node tools/pdri/scenes/shoot_scenes.js WORK        # atau port Python-nya; butuh playwright
uv run --with pymupdf --with pillow python tools/pdri/scenes/pack_scenes.py WORK N "Judul bab" babN-<slug>-fullscreen.pdf
# lalu salin WORK/html/*.html ke dist/pdri/html/babN/ dan PDF ke dist/pdri/pdf/

# e2e (tanpa server lokal pun bisa, lewat file://)
URL="file:///<repo>/site/pdri-mck/ch0N/index.html" python tools/pdri/e2e_mck_ch0N.py
```

## 5. Perubahan tooling

- `tools/pdri/scorm/stage_chapter.py`: `shutil.rmtree(onexc=…)` hanya tersedia di Python 3.12+, sedangkan mesin ini memakai 3.11. Sekarang skrip memakai `onerror` di Python < 3.12.
- `tools/pdri/scenes/pack_scenes.py`: di Windows, link di `00-daftar-adegan.html` sebelumnya menjadi `html\01-intro.html` (rusak). Sekarang skrip memakai `os.path.basename`.
- `tools/pdri/e2e_mck_ch04.py`: skrip baru, kunci jawaban `q1`, `q2`, dan `final1` Bab 4.
- `content/pdri-mck/ch0{3,4}/narration.id*.json`: BOM UTF-8 dibuang karena `align_beat.py` gagal membaca file ber-BOM.

## 6. Catatan dan pekerjaan lanjutan

1. **Ketergantungan pada skill Papermorph lokal.** `scorm-bridge.js`/`scorm-host.js` versi tracking-interaksi dan `check_interactions.py` hanya ada di clone lokal `Papermorph/`. Clone ini tidak dilacak repo ini dan berisi perubahan yang belum di-commit di repo Papermorph sendiri. Untuk membangun ulang di mesin lain, perubahan itu perlu di-commit atau disalin terlebih dahulu.
2. **Uji di LMS sungguhan.** Sebelum dipakai peserta, unggah salah satu paket ke SCORM Cloud atau LMS target, lalu periksa laporan interaksinya.
3. **Gambar storyboard belum diperbarui.** `books/pdri/review/ch03-mck/storyboard.jpg` dan `ch04-mck/storyboard-adegan.jpg` belum dibangun ulang dari timing baru (`make_storyboard.py` butuh keluaran `render_preview.py`).
4. **Kolom "Durasi draf" di naskah Bab 3 dan 4 belum diperbarui** ke durasi rekaman final.
5. **File sisa di working tree tidak di-commit.** Yang dimaksud: `site/pdri-mck/ch03/{*_SUMMARY.md, AUDIO_REVIEW_REPORT.md, OUTPUT_PLAN.md, PEKERJAAN_SELESAI.txt, outputs/, scorm_package/}`, `dist/pdri/stage/`, `dist/pdri/unz/`, dan `dist/ch03-voiceover-staging/`. Sebagian besar tampaknya sisa percobaan sebelumnya. Perubahan Bab 5, 7, dan 8 serta dokumen v3/v4 juga tidak termasuk PR ini.
