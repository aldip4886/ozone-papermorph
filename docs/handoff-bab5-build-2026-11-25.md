# Handoff: build Bab 5 PDRI

**Tanggal:** 25 November 2026
**Branch:** `claude/pdri-bab5-build`, bercabang dari `claude/pdri-bab3-4-build`. Branch Ch3–4 berisi hook tracking `engine.js` dan perbaikan tooling yang dibutuhkan di sini, jadi gabungkan PR Bab 3–4 lebih dulu.
**Cara kerja:** skill proyek `pdri-build-chapter` (`.claude/skills/pdri-build-chapter/`), yang kini ikut tersimpan di repo.

## 1. Voiceover

**Sebelumnya:** 15 beat masih memakai draf suara Ardi (edge-tts, commit `845788e`), dan beat `rina` senyap tanpa audio.

**Sekarang:** ke-16 beat memakai rekaman Google AI Studio (Gemini 3.8 Flash TTS, Bodi) dari `Downloads/vo_materi_5`. Ke-16 WAV direkam 25 Nov pukul 05:16–05:25.

- **Pemetaan WAV ke beat.** Pemetaan dilakukan berdasarkan isi ucapan dengan `map_wavs.py` (transkripsi faster-whisper), bukan nama file. Hasilnya satu take untuk setiap beat, tanpa take sisa, dan urutan waktunya cocok dengan urutan beat.
- **Format.** WAV dikonversi ke MP3 mono 24 kHz / 48 kbps, sama dengan Bab 4. Draf Ardi tidak disimpan di repo karena masih ada di riwayat git (`845788e`).
- **Timing.** Semua beat di-forced-align ulang ke `timings.js` dan `narration.id.timings.json`. Total durasi ±5 menit 12 detik, sehingga `CHAPTER.minutes` tetap 5.

### Perbedaan rekaman dengan teks, dan penanganannya

| Beat | Temuan | Tindakan |
|---|---|---|
| `rina` | Rekaman mengikuti naskah terbaru ("…menjadi angsuran… Bagaimana maksudnya? Jawabannya: melalui pengkreditan… pengurang PPh di akhir tahun."), sedangkan `narration.id.json` masih versi lama | Teks narasi disamakan dengan naskah. Mark `jwb`, `pt`, dan `rina` tetap |
| `jawab` | Rekaman dan naskah berbunyi "jawaban untuk **pertanyaan** staf importir", sedangkan narasi belum memuat kata itu | Teks narasi disamakan dengan rekaman |
| `intro` | Rekaman mulai dari "Sobat, pada materi kelima…". Kalimat "Mari kita lanjutkan, ya," dari naskah **tidak diucapkan** | Subtitle disamakan dengan ucapan di rekaman. **Kandidat rekam ulang** bila pembuka standar ingin dipertahankan |
| `alur` | Rekaman diawali kalimat yang tidak ada di naskah: "Lima langkah: alur uang dari PIB sampai SPT Tahunan", kemungkinan judul layar yang ikut terbaca | Bagian itu dipotong pada jeda di detik 4,40, dengan fade-in 50 ms. Durasi 20,96 menjadi 16,56 detik. WAV asli di Downloads tidak diubah |

Selisih lain hanya ejaan ASR, misalnya "DJBC" ditulis "dgbc", "2,5 persen" ditulis "2 5", dan "Bu Rina" ditulis "burina".

## 2. Output

| Output | Lokasi |
|---|---|
| SCORM 1.2 | `dist/pdri/ch05-scorm12.zip` (2,5 MB) |
| SCORM 2004 4th ed. | `dist/pdri/ch05-scorm2004.zip` (2,5 MB) |
| HTML per adegan (16 + daftar) | `dist/pdri/html/bab5/` |
| PDF layar penuh (16 hlm) | `dist/pdri/pdf/bab5-pajak-penghasilan-pasal-22-impor-fullscreen.pdf` |

Pengaturan SCORM sama dengan bab lain: mastery 70%, judul "PDRI: Pajak dalam Rangka Impor (Bab 5)", dan setiap jawaban dicatat sebagai `cmi.interactions`.

## 3. Verifikasi

| Cek | Hasil |
|---|---|
| e2e bab (`tools/pdri/e2e_mck_ch05.py`, skrip baru): playback, replay, layout kuis, jawaban, finish | lulus |
| `check_scorm.py`, SCORM 1.2 dan 2004 | 5/5 lulus |
| `check_interactions.py`, SCORM 1.2 dan 2004 | lulus, 8 record |
| Semua 6 soal tercatat (`check_all_interactions.py`): `c-tarif`, `c-sifat`, `p-pilih-tarif`, `p-pilih-tarif-2`, `p-pph-50rb`, `p-tanpa-api` | ok |
| Screenshot 16 adegan tanpa error konsol, dicek visual | ok |

## 4. Membangun ulang

```sh
python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 5
```

Langkah lengkapnya (cek VO, pemetaan take, alignment, e2e) ada di `.claude/skills/pdri-build-chapter/SKILL.md`.

## 5. Lanjutan

1. Putuskan apakah `intro` direkam ulang dengan pembuka "Mari kita lanjutkan, ya, sobat."
2. Lakukan review dengar, terutama pelafalan persentase (0,25%, 0,5%, 7,5%) dan "PMK 51".
3. Uji paket di SCORM Cloud atau LMS target.
4. Gambar storyboard Bab 5 dan kolom "Durasi draf" di naskah belum diperbarui.
5. Skill membutuhkan clone lokal `Papermorph/`, yang berisi `scorm-bridge.js` dengan tracking interaksi. Lihat catatan di handoff Bab 3–4.
