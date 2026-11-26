# Naskah Voice Over KB 5 · PPh Pasal 22 Impor

26 Nov 2026. Dari [storyboard KB 5 PPh Pasal 22 Impor v1](../storyboard-kb5-pph22-impor-v1.md). Materi terpisah dari Bab 5: folder `site/pdri-mck/ch51`, label "KB 5".

## Cara kerja

Materi ini memakai 13 file suara pendek, satu per adegan, sama seperti KB 4. Gaya bahasanya juga sama: kalimat netral saat menjelaskan, "kamu" dan "ya" saat mengajak latihan.

1. Buka Google AI Studio, menu **Generate speech**, model **Gemini 3.8 Flash TTS**, suara **Bodi**.
2. Tempel **prompt gaya** di bawah ke kolom Style.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh. Urutan unduhan mengikuti nomor baris supaya mudah dicocokkan, meskipun file juga dicocokkan otomatis dari isi ucapannya.
4. File dipasang sebagai `site/pdri-mck/ch51/audio/id/<kode file>.mp3` (24 kHz, 48 kbps), lalu subtitle dan animasinya diselaraskan dengan forced-alignment.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka (`content/pdri-mck/ch51/narration.id.json`).

## Prompt untuk Google AI Studio

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang natural, ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: ramah, tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Kalimat staf importir yang bertanya dibacakan sedikit lebih ingin tahu. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sekitar 150 kata per menit. Saat membacakan tarif, nomor pos tarif, dan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum pertanyaan untuk peserta.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: PPh (pe-pe-ha), PIB (pe-i-be), DJBC (de-je-be-ce), PMK (pe-em-ka), SPT (es-pe-te), API (a-pe-i), API-U (a-pe-i u), PT (pe-te).
Penekanan: beri tekanan ringan pada istilah dipotong, dipungut, pembayaran di muka, tidak final, dikreditkan, dan pada tarif serta hasil akhir perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

## Naskah per adegan

Total 13 adegan, sekitar 4 menit 20 detik suara. Durasi draf diperkirakan dari 150 kata per menit.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `pembuka` | 15 detik | PER. Judul KB 5; pertanyaan pengarah; ikon kalender, kapal, dokumen pajak, koin; Paspor Misi | Mari kita lanjutkan, ya, sobat. Staf PT Kain Prima Nusantara bertanya lagi: kain kami belum laku, kok PPh sudah dipungut? Ini pertanyaan keempat di Paspor Misi kamu. Mari kita jawab bersama. |
| 2 | `jalur` | 26 detik | MAT. Garis waktu Januari–Desember; PPh 21, 22 (emas), 23, 25; berakhir di SPT Tahunan | Mulai dari gambaran besarnya. Selama tahun berjalan, PPh dilunasi melalui beberapa jalur. PPh dua puluh satu dipotong oleh pemberi kerja. PPh dua puluh dua dipungut oleh pihak tertentu, termasuk atas impor. PPh dua puluh tiga dipotong atas penghasilan tertentu. Dan PPh dua puluh lima diangsur sendiri setiap bulan. Semuanya adalah pelunasan PPh tahun berjalan, yang diperhitungkan di SPT Tahunan. |
| 3 | `beda` | 22 detik | INT. Kartu pemotongan dan pemungutan; drag PPh 21, 22 Impor, 23, 25 ke kelompoknya | Apakah bedanya dipotong dan dipungut? Pada pemotongan, pihak yang membayar penghasilan memotong pajak dari pembayarannya. Pada pemungutan, pihak yang ditunjuk memungut pajak atas transaksi tertentu. Sekarang, coba seret PPh dua puluh satu, PPh dua puluh dua Impor, PPh dua puluh tiga, dan PPh dua puluh lima ke kelompok yang tepat. |
| 4 | `pungut` | 18 detik | MAT. Empat kartu: pemungut, dasar, saat terutang, sifat | PPh Pasal dua puluh dua Impor dipungut saat impor. Pemungutnya DJBC dan bank devisa. Dasar pemungutannya nilai impor. Terutangnya bersamaan dengan pembayaran Bea Masuk. Dan sifatnya tidak final. Ketentuannya ada dalam PMK lima puluh satu Tahun dua ribu dua puluh lima. |
| 5 | `dimuka` | 20 detik | MAT. Diagram dua lapis: transaksi impor → kewajiban PPh importir → SPT Tahunan | Jadi, apa sebenarnya PPh dua puluh dua Impor ini? Ia dipungut atas transaksi impor, tetapi sebenarnya merupakan pembayaran di muka atas PPh importir. Karena itu, PPh dua puluh dua Impor dikreditkan dalam SPT Tahunan PPh importir. Ingat, PPh dua puluh dua Impor mengangsur kewajiban subjektif importir. |
| 6 | `spt` | 17 detik | MAT. PT Kain Prima Nusantara → SPT Tahunan PPh Badan; Bu Rina → SPT Tahunan PPh Orang Pribadi | Ke SPT mana kreditnya masuk? Itu mengikuti jenis wajib pajaknya. PT Kain Prima Nusantara adalah badan, jadi kreditnya masuk SPT Tahunan PPh Badan. Bu Rina adalah orang pribadi, jadi kreditnya masuk SPT Tahunan PPh Orang Pribadi. |
| 7 | `hitung` | 26 detik | KAS. Tabel cek tarif; nilai impor; peserta menghitung PPh 22 | Sekarang kita hitung untuk Kasus satu. Cek dulu: pos lima dua nol delapan titik dua satu titik nol nol tidak tercantum dalam Lampiran A sampai D PMK lima puluh satu Tahun dua ribu dua puluh lima, dan importirnya memiliki API-U. Jadi tarifnya dua koma lima persen dari nilai impor. Nilai impornya satu miliar lima ratus dua puluh delapan juta dua ratus tiga puluh ribu rupiah. Coba hitung PPh dua puluh dua Impornya, ya. |
| 8 | `langkah` | 35 detik | MAT. Diagram keputusan tiga belah ketupat dengan cabang Ya/Tidak | Bagaimana memilih tarif PPh dua puluh dua Impor? Ikuti tiga langkah. Langkah pertama, cek apakah barangnya tercantum di Lampiran A atau B. Jika ya, tarifnya sepuluh persen atau tujuh koma lima persen. Langkah kedua, cek apakah barangnya emas batangan. Jika ya, tarifnya nol koma dua lima persen. Langkah ketiga, cek status API. Dengan API, tarifnya dua koma lima persen, atau nol koma lima persen untuk kedelai, gandum, dan tepung terigu. Tanpa API, tarifnya tujuh koma lima persen. |
| 9 | `tarif` | 16 detik | INT. Pilih Tarifmu: kisi 4 × 2 kartu skenario, tarif diseret ke setiap skenario | Sekarang giliran kamu: pilih tarifmu. Seret tarif yang tepat ke setiap skenario, dengan mengikuti tiga langkah tadi. Ingat, tarif nol koma lima persen untuk kedelai, gandum, dan tepung terigu hanya berlaku dengan API. |
| 10 | `alur` | 19 detik | INT. Lima lingkaran bernomor bergaris emas; susun tahap, lalu pasangkan pihak atau dokumen | Sekarang, ikuti uangnya. PPh dua puluh dua Impor berjalan melalui lima tahap, dari PIB sampai SPT Tahunan. Coba susun kelima tahap itu, lalu pasangkan pihak atau dokumen pada setiap tahap. Kalau ada yang keliru, kartunya kembali, dan kamu bisa mencoba lagi. |
| 11 | `kredit` | 20 detik | MAT. Tiga pesan, dokumen SPT, Paspor Misi dengan stempel misi KB 5 | Jadi, inilah jawaban untuk staf importir tadi. PPh dua puluh dua Impor dipungut atas transaksi impor. Ia menjadi pembayaran di muka atas PPh importir. Dan ia dikreditkan dalam SPT Tahunan, bukan pajak final. Misi KB lima selesai. |
| 12 | `api` | 16 detik | INT. Timbangan: 2,5% dengan API dan 7,5% tanpa API; pilih pernyataan yang paling tepat | Satu pertanyaan terakhir. Untuk barang lain, tarifnya dua koma lima persen dengan API, dan tujuh koma lima persen tanpa API, tiga kali lipat. Apa dampaknya bagi importir tanpa API? Pilih pernyataan yang paling tepat. |
| 13 | `finish` | 12 detik | Kartu selesai | Sekarang kamu tahu kan  mengapa PPh sudah dipungut walaupun kain belum laku. Lihat hasilmu, lalu ulangi bagian yang masih ragu, ya. |
