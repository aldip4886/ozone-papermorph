# Naskah Voice Over Bab 1 PDRI

Nov 21, 2026 · @John

## Cara kerja

Ya, suara voice over bisa Anda buat sendiri, dengan rekaman suara Anda atau dengan Google AI Studio. Bab 1 memutar satu file suara per beat, jadi Anda membuat 15 file pendek, bukan satu rekaman panjang.

1. Buka Google AI Studio, pilih menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** dari bagian berikut ke kolom instruksi gaya (Style instructions), lalu pilih suara.
3. Untuk setiap beat di tabel naskah, tempel teksnya, klik Run, dengarkan, lalu unduh hasilnya.
4. Beri nama file persis sama dengan **kode beat**, misalnya `intro.wav`, `port.wav`, `groups.wav`. Format WAV atau MP3 sama-sama bisa.
5. Kirim ke-15 file itu di thread ini. Saya yang memasang dan menyinkronkan animasinya.

Tips: buat satu beat dulu (misalnya `port`), dengarkan di bab, baru lanjutkan yang lain. Pakai suara dan prompt gaya yang sama untuk semua beat agar warna suaranya konsisten.

## Prompt untuk Google AI Studio

Pengaturan yang saya sarankan: model TTS Gemini yang tersedia di akun Anda (versi Pro bila ada, karena intonasinya lebih stabil), suara pria yang tenang seperti **Charon** (informatif) atau **Iapetus** (jernih), temperature sekitar 1. Nama model dan suara di AI Studio bisa berubah, jadi pilih yang paling dekat bila nama itu tidak ada.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit.
Jeda: jeda pendek setelah koma, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum angka penting.
Angka: ucapkan angka persis seperti tertulis dalam kata. Singkatan PPN, PPnBM, PPh, BMTP, CIF, API, PKP, BTKI, PMK dibaca per huruf (pe-pe-en, pe-pe-en-be-em, pe-pe-ha, be-em-te-pe, ce-i-ef, a-pe-i, pe-ka-pe, be-te-ka-i, pe-em-ka). PDRI dibaca pe-de-er-i.
Penekanan: beri tekanan ringan pada istilah kunci seperti nilai impor, nilai pabean, Bea Masuk, dan PDRI.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suaranya terlalu cepat atau datar, ubah satu baris saja di prompt (misalnya tempo menjadi lebih lambat) lalu ulangi beat yang sama.

## Naskah per beat

Total 15 beat, sekitar 4 menit 35 detik dengan suara Ardi sekarang. Tempel kolom Teks apa adanya; durasi hanya patokan, rekaman Anda boleh sedikit lebih panjang atau lebih pendek karena animasi akan saya sinkronkan ulang.

| No | Kode file | Durasi sekarang | Teks |  |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 9 detik | Hari pertama di pelabuhan. Kita akan mengenal komponen pungutan impor, lalu menghitung nilai impor. |  |
| 2 | `port` | 26 detik | Hari ini Anda mulai bertugas di Tanjung Priok. Sebuah kapal membawa kontainer berisi kain kapas milik PT Kain Prima Nusantara. Harga kainnya sekitar satu koma nol sembilan miliar rupiah. Tetapi tagihan pungutannya sekitar enam ratus empat puluh lima juta rupiah. Staf perusahaan datang ke meja layanan dan bertanya, hitungan ini dari mana? Di bab ini, kita mulai menyusun jawabannya. |  |
| 3 | `groups` | 29 detik | Saat barang masuk ke daerah pabean, importir membayar dua kelompok pungutan. Kelompok pertama adalah pungutan kepabeanan: Bea Masuk, dan bea masuk tambahan, seperti bea masuk tindakan pengamanan atau BMTP, bea masuk antidumping, dan bea masuk imbalan. Angka-angka ini sudah Anda pelajari di materi kepabeanan. Kelompok kedua adalah pajak dalam rangka impor, atau PDRI, yaitu pajak yang dipungut Bea dan Cukai pada saat impor. |  |
| 4 | `pdri` | 30 detik | PDRI terdiri atas tiga jenis. Pertama, PPN Impor. Pajak ini dikenakan atas impor barang kena pajak, oleh siapa pun yang mengimpor. Kedua, PPnBM Impor, yang hanya dikenakan atas barang yang tergolong mewah. Ketiga, PPh Pasal dua puluh dua Impor, yaitu pembayaran di muka atas pajak penghasilan importir. Barang kena cukai juga dapat menimbulkan cukai, tetapi itu dibahas di modul tersendiri. |  |
| 5 | `q1` | 5 detik | Sekarang, mari kita cek pemahaman kamu. Kelompokkan setiap pungutan ini ya!. |  |
| 6 | `nilai` | 31 detik | Lalu, dari angka apa semua pajak ini dihitung? Jawabannya: nilai impor. Nilai impor sama dengan nilai pabean dalam rupiah, ditambah Bea Masuk, ditambah bea masuk tambahan, misalnya BMTP. PPN dan PPnBM tidak termasuk di dalamnya. Dari satu angka ini, PPN, PPnBM, dan PPh Pasal dua puluh dua dihitung. Undang-undang PPN dan PMK lima puluh satu tahun dua ribu dua puluh lima memakai dasar yang sama. |  |
| 7 | `case` | 27 detik | Sekarang kita hitung untuk kasus kain tadi. Importir memasukkan seratus ribu meter kain tenunan kapas, dengan nilai CIF enam puluh ribu dolar Amerika. Kurs pajak minggu ini delapan belas ribu seratus lima puluh lima rupiah per dolar. Tarif Bea Masuknya kita anggap sepuluh persen. Angka ini masih asumsi latihan, jadi cocokkan dulu dengan BTKI. Kain ini juga dikenai BMTP tiga ribu tiga ratus rupiah per meter. |  |
| 8 | `step1` | 13 detik | Langkah pertama, nilai pabean dalam rupiah. Enam puluh ribu dolar dikali kurs. Hasilnya satu koma nol delapan sembilan miliar rupiah. Inilah balok dasar nilai impor. |  |
| 9 | `step2` | 23 detik | Langkah kedua, Bea Masuk. Sepuluh persen dari nilai pabean, yaitu sekitar seratus sembilan juta rupiah. Langkah ketiga, BMTP. Seratus ribu meter dikali tiga ribu tiga ratus rupiah, hasilnya tiga ratus tiga puluh juta rupiah. Perhatikan, BMTP dihitung per meter, bukan dari persentase harga. |  |
| 10 | `step3` | 18 detik | Langkah keempat, jumlahkan ketiganya. Nilai pabean, ditambah Bea Masuk, ditambah BMTP. Nilai impornya satu koma lima dua delapan miliar rupiah. Angka inilah yang akan menjadi dasar PPN Impor dan PPh Pasal dua puluh dua di bab-bab berikutnya. |  |
| 11 | `q2` | 5 detik | Sekarang kita Cek pemahaman lagi ya. Seorang petugas lupa memasukkan BMTP. |  |
| 12 | `check` | 25 detik | Karena itu, biasakan cek dulu sebelum hitung. Pertama, status importir: punya API atau tidak, PKP atau tidak. Kedua, jenis barang: tergolong mewah atau tidak. Ketiga, aturan dan kurs: masih berlaku, dan sesuai minggu berjalan. Satu kesalahan pada nilai impor akan terbawa ke semua pajak di bawahnya. |  |
| 13 | `wrap` | 20 detik | Jadi, ini rangkumannya. PDRI terdiri atas PPN Impor, PPnBM Impor, dan PPh Pasal dua puluh dua Impor. Bea Masuk dan bea masuk tambahan adalah pungutan kepabeanan, dan menjadi bagian dari nilai impor. Semua PDRI dihitung dari nilai impor, jadi periksa angka ini lebih dahulu. |  |
| 14 | `final1` | 5 detik | Nah, sekarang kita latihan ya. Coba kamu Hitung nilai impor untuk pesanan yang lebih kecil berikut ini. |  |
| 15 | `finish` | 8 detik | Bagus. materi pertama  selesai. Berikutnya, kita diskusikan mengapa negara boleh memungut pajak. |  |

## Setelah rekaman masuk

Animasi Bab 1 menunggu kata tertentu dalam narasi, misalnya kartu BMTP muncul tepat saat kata "BMTP" diucapkan. Karena itu, setelah Anda mengirim 15 file, saya akan:

1. Menyamakan kerasnya suara semua file dan memangkas hening di awal dan akhir.
2. Mencari waktu setiap kata penanda dalam rekaman Anda secara otomatis (pengenalan ucapan), lalu menulis ulang daftar waktunya.
3. Mengecek setiap beat di bab dan mengirim video pratinjau dengan suara Anda.

Yang perlu dijaga: jangan mengubah kata di naskah, karena penanda waktunya dicari dari kata-kata itu. Bila ingin mengubah kalimat, ubah dulu di tabel di atas, nanti saya sesuaikan animasinya.
