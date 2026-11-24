# Handoff — voiceover Chapter 3

**Tanggal:** 24 November 2026  
**Status:** Semua 16 klip voiceover sudah dibuat dan dipasang ke aset Chapter 3.

## Yang sudah dikerjakan

- Menggunakan Google AI Studio dengan model **Gemini 3.8 Flash TTS**, suara **Bodi**, serta prompt gaya Chapter 3. Deskripsi gaya meminta tempo sekitar **150 kata per menit**. API key sudah tertaut oleh pengguna; jangan membuat atau meminta key baru.
- Membuat dan mengunduh satu WAV untuk setiap beat: `intro`, `ask`, `sistem`, `alur`, `q1`, `jenis`, `syarat`, `rina`, `hukum`, `hierarki`, `peran`, `identitas`, `q2`, `wrap`, `final1`, dan `finish`.
- Mengonversi semua WAV menjadi MP3 mono 44,1 kHz, 96 kbps, lalu menaruhnya di `site/pdri-mck/ch03/audio/id/`. `syarat.mp3` dan `rina.mp3` adalah aset baru; 14 aset beat lainnya menggantikan audio lama.
- Menyalin WAV dan MP3 hasil baru ke `dist/ch03-voiceover-staging/`. Audio MP3 sebelum penggantian disimpan di `dist/ch03-voiceover-staging/original/`.
- Memperbarui metadata suara/rate di `content/pdri-mck/ch03/narration.id.json`.
- Memperbarui `site/pdri-mck/ch03/audio/id/timings.js`: durasi mengikuti durasi WAV baru, `silent` dimatikan untuk semua beat, dan cue/mark lama diskalakan secara proporsional berdasarkan perubahan durasi.
- Menyamakan beat `intro` di narration JSON dan cue dengan naskah rekaman yang menyebut “ya sobat”. Memperbarui instruksi suara dan tempo di `docs/naskah-voiceover/bab3-naskah-voiceover.md`.

## Durasi

Total audio sekitar **6 menit 1 detik**. Hitungan tiap klip disimpan di `timings.js`.

## Pekerjaan lanjutan yang disarankan

1. Dengarkan seluruh klip untuk memastikan pelafalan, angka, singkatan, dan kualitas suara sesuai naskah.
2. Tinjau cue subtitle dan mark animasi di `timings.js`. Posisi sekarang merupakan skala proporsional dari timing draf, bukan alignment ujaran per kata.
3. Bila ada perbaikan pada naskah atau pelafalan, buat ulang hanya beat yang terdampak, lalu perbarui aset dan timing terkait.

Belum dilakukan review dengar menyeluruh atau preview chapter setelah pemasangan audio.

## Catatan workspace

Working tree bersama sudah berisi perubahan lain sebelum pekerjaan voiceover ini. Jangan menjalankan `git reset`, `git clean`, atau membuang perubahan global; batasi perubahan lanjutan ke file yang sedang ditangani.
