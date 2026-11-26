# Handoff: KB 4 · Estafet PPN (materi baru)

**Tanggal:** 26 November 2026
**Sumber:** [storyboard KB 4 Estafet PPN v1](storyboard-kb4-estafet-ppn-v1.md), [naskah VO](naskah-voiceover/kb4-estafet-ppn-naskah-voiceover.md)
**Status:** pelajaran, voiceover final (Bodi, 13 adegan), SCORM 1.2 dan 2004, HTML per adegan, dan PDF layar penuh sudah dibangun. Semua cek lulus.

## 1. Penempatan

Materi ini terpisah dari Bab 4. Foldernya `site/pdri-mck/ch41` dan `content/pdri-mck/ch41`, karena tool build memberi nomor pada setiap pelajaran. Peserta melihatnya sebagai **"KB 4"**, bukan "Bab 41": `CHAPTER.label = 'KB 4'`, dan teks "Bab {n}" di-override di halaman ini. Daftar isi buku utama (`site/pdri-mck/index.html`) tidak diubah.

## 2. Isi (13 adegan)

| No | Adegan | Jenis | Isi |
|---|---|---|---|
| 1 | `susun` | INT | Drag-and-drop menyusun empat tahap alur PPN. Kartu yang salah kembali ke tempat awal (`c-susun`). |
| 2 | `tahap` | MAT | Empat ciri PPN pada rantai transaksi. |
| 3 | `rumus` | MAT | PK − PM = setoran, kurang bayar atau lebih bayar; PIB dipersamakan dengan faktur pajak. |
| 4 | `status` | MAT | PT Kain Prima Nusantara (PKP) dan Bu Rina (bukan PKP). |
| 5 | `estafet` | INT | Rantai importir kain → konveksi → toko → pembeli kemeja; kartu estafet berpindah. |
| 6–9 | `pos1`–`pos4` | KAS | Kartu estafet per pos; peserta mengisi PM atau setoran (`c-pos1`–`c-pos4`). Jawaban benar muncul di kartu. |
| 10 | `total` | RAN | Grafik air terjun: 168.105.300 + 29.894.700 + 77.000.000 + 77.000.000 = Rp352.000.000. |
| 11 | `cocok` | INT | Drag-and-drop 9 kartu angka ke PK, PM, dan setoran tiga transaksi; coba lagi untuk pasangan yang keliru (`p-cocok`). |
| 12 | `inti` | RAN | Kutipan inti dan stempel selesai. |
| 13 | `finish` | – | Kartu selesai. |

Drag-and-drop (`dragBoard` di `ch41/index.html`) bisa dikerjakan dengan menyeret pakai mouse atau jari, dengan klik kartu lalu klik tempatnya, atau dengan tombol angka 1–9 (Backspace mengambil kembali). Setiap tempat dilaporkan sebagai satu baris `cmi.interactions`.

## 3. Voiceover

- Rekaman ada di `Downloads/vo_materi_4_1`: 13 WAV Google AI Studio. Dipetakan ke adegan berdasarkan isi ucapan (`map_wavs.py`, skor 0,84–1,00, tidak ada file tersisa), lalu dikonversi ke MP3 24 kHz/48 kbps.
- Transkrip dibandingkan dengan naskah: hanya noise ASR (konfeksi/konveksi, import/impor, angka ditulis berbeda). Tidak ada frasa yang hilang atau bertambah.
- Perubahan naskah dari Anda di pos 1 ("dikali nilai impornya") sudah disamakan di `narration.id.json`.
- Timing hasil forced-alignment (`align_chapter.py`) ditulis ke `audio/id/timings.js` dan `narration.id.timings.json`. Total sekitar 4 menit 20 detik, sehingga `CHAPTER.minutes = 4`.

## 4. Output

| Output | Path | Ukuran |
|---|---|---|
| SCORM 1.2 | `dist/pdri/kb4-scorm12.zip` | 2,2 MB, 39 file |
| SCORM 2004 | `dist/pdri/kb4-scorm2004.zip` | 2,2 MB |
| HTML per adegan (13 + daftar) | `dist/pdri/html/kb4/` | 7,1 MB |
| PDF layar penuh (13 hlm) | `dist/pdri/pdf/kb4-estafet-ppn-dalam-rantai-produksi-dan-distribusi-fullscreen.pdf` | 4,7 MB |

Judul SCORM: "PDRI: Pajak dalam Rangka Impor (KB 4: Estafet PPN dalam Rantai Produksi dan Distribusi)", mastery 70. Paket langsung membuka pelajaran, tanpa cover. Entri zip berformat DOS dengan izin 0644, jadi aman untuk LMS di server Linux (lihat kasus upload Bab 3).

## 5. Verifikasi

| Cek | Hasil |
|---|---|
| `tools/pdri/e2e_mck_ch41.py` (pemutaran, replay, tata letak kuis, semua jawaban termasuk drag-and-drop, finish) | lulus |
| Drag dengan mouse sungguhan: susun (salah → kartu kembali → perbaiki dengan klik) dan cocok (9 kartu) | lulus, `c-susun` dan `p-cocok` terlapor |
| `check_scorm.py` (DIRECT) 1.2 dan 2004 | 5/5 lulus, keduanya |
| `check_interactions.py` 1.2 dan 2004 | lulus; 4 record `c-pos1`–`c-pos4` (cek generik tidak bisa mengisi soal drag-and-drop) |
| Screenshot 13 adegan, dicek visual | ok |

## 6. Cara membangun ulang

```sh
export PYTHONUTF8=1 PW_CHANNEL=chrome
python .claude/skills/pdri-build-chapter/scripts/build_outputs.py 41 --skip-cover
```

## 7. Perubahan tool

- `tools/pdri/chapter_name.py` (baru): nama output dari `CHAPTER.label` (`kb4`) atau "Bab N" (`babN`, `chNN`).
- `build_outputs.py`: memakai nama itu untuk zip, folder HTML, PDF, dan judul SCORM. Ada opsi baru `--skip-cover`. Penamaan Bab 1–8 tidak berubah.
- `build_scenes.py`, `pack_scenes.py`: judul adegan dan daftar adegan memakai nama itu.
- `tools/pdri/vo/silent_timings.py` (baru): timing sementara dari narasi sebelum ada rekaman.

## 8. Yang tersisa

- Uji di LMS sungguhan (atau SCORM Cloud).
- Dengarkan sekali seluruh rekaman; pastikan "sebelas persen" di `estafet` dan `pos1` terbaca jelas.
- Presentasi HTML (skill `pdri-presentasi`) belum dibuat untuk KB 4; bisa dibuat bila diperlukan.
