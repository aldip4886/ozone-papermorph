# Handoff: bangun ulang SCORM Bab 3 PDRI

**Tanggal:** 26 November 2026
**Status:** Bab 3 dibangun ulang dari `main`. SCORM 1.2 dan 2004 langsung membuka pelajaran (tanpa cover dan layar pilih bab), HTML per adegan dan PDF layar penuh ikut diperbarui. Semua cek lulus.

## 1. Kenapa sebelumnya gagal

Setelah build Bab 3 yang benar (commit `d56bd3a`, 25 Nov), commit `8028992` ("s") dan merge `a4a9bb2` menimpa sebagian Bab 3 dengan keadaan lama dari 23 Nov:

- 14 MP3 di `site/pdri-mck/ch03/audio/id/` kembali ke take Bodi 23 Nov (sama byte demi byte dengan `audio/bodi/`);
- `audio/id/timings.js` kembali ke versi 14 adegan, **tanpa `syarat` dan `rina`**;
- `content/pdri-mck/ch03/narration.id.json` juga kembali ke versi 14 adegan.

Sementara `index.html` Bab 3 tetap 16 adegan. Akibatnya pelajaran berhenti di awal dengan error
`audio/id/timings.js has no timings for beat syarat, rina`, sehingga setiap build ulang Bab 3 gagal (e2e: "lesson plays").

Selain itu, folder Bab 3 berisi file kerja yang ikut masuk ke paket SCORM lama: `AUDIO_REVIEW_REPORT.md`, `EXECUTIVE_SUMMARY.md`, `OUTPUT_PLAN.md`, `PEKERJAAN_SELESAI.txt`, `PROJECT_SUMMARY.md`, dan `outputs/` (termasuk `scene_01_intro.html` yang tidak lengkap). Folder `audio/bodi/` dan `audio/bodi-wav/` (±13 MB WAV) juga akan ikut terbawa ke build berikutnya.

## 2. Perbaikan

- `audio/id/*.mp3`, `audio/id/timings.js`, dan `narration.id.json` dipulihkan ke versi `d56bd3a`: rekaman final 24 Nov (16 adegan), sama byte demi byte dengan `dist/ch03-voiceover-staging/`, dengan timing hasil forced-alignment. Durasi di `timings.js` = MP3 + ±0,2 dtk untuk ke-16 adegan.
- File kerja di `site/pdri-mck/ch03/` (5 laporan + `outputs/`) dihapus dari repo.
- `tools/pdri/scorm/stage_chapter.py` sekarang membuang `*.md`, `*.txt`, `*.wav`, `chNN/outputs/`, dan subfolder audio selain folder bahasa (`audio/id`) dari paket. Folder `audio/bodi*` tetap ada di repo, tapi tidak ikut ke SCORM.

## 3. Output

| Output | Path | Ukuran |
|---|---|---|
| SCORM 1.2 | `dist/pdri/ch03-scorm12.zip` | 4,9 MB, 42 file |
| SCORM 2004 4th ed. | `dist/pdri/ch03-scorm2004.zip` | 4,9 MB |
| HTML per adegan (16 + daftar) | `dist/pdri/html/bab3/` | ±1 MB per adegan |
| PDF layar penuh (16 hlm) | `dist/pdri/pdf/bab3-pihak-dan-sistem-pemungutan-fullscreen.pdf` | 5,8 MB |

Salinan di folder proyek: `pdri/paket-zip/media-interaktif/pdri-bab3-scorm{12,2004}.zip` dan `pdri/bab3-html-pdf/{html,pdf}/`.

## 4. Verifikasi

| Cek | Hasil |
|---|---|
| `tools/pdri/e2e_mck_ch03.py` (16 adegan: playback, replay, layout kuis, jawaban, finish) | lulus |
| `DIRECT=1 check_scorm.py` 1.2 dan 2004 (sesi, link bab, finish card, objective, resume, tanpa error) | 5/5 lulus, keduanya |
| `DIRECT=1 check_interactions.py` 1.2 dan 2004 | lulus, 14 record `cmi.interactions`, tidak ada SetValue ditolak |
| `skip_cover.py`: paket membuka `book/ch03/index.html` langsung | ok |
| Screenshot 16 adegan, dicek visual | ok, tidak ada teks terpotong |

## 5. Cara membangun ulang

```sh
export PYTHONUTF8=1
python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 3
python .claude/skills/pdri-scorm-skip-cover/scripts/skip_cover.py dist/pdri/ch03-scorm12.zip dist/pdri/ch03-scorm2004.zip
```

## 6. Yang tersisa

- Uji di LMS sungguhan (atau SCORM Cloud).
- Di salinan lokal John (`main`), jangan commit ulang isi `site/pdri-mck/ch03/audio/id` dari folder lama; tarik `main` setelah PR ini di-merge.
