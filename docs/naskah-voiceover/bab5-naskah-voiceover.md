# Naskah Voice Over Bab 5 PDRI

Nov 22, 2026 · @John. Diperbarui 24 Nov 2026 untuk [outline v4](../09-outline-materi-v4.md).

## Cara kerja

Bab 5 memakai 16 file suara pendek, satu per adegan, sama seperti Bab 2 sampai 4. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan, dan pembuka "Mari kita lanjutkan, ya, sobat".

1. Buka Google AI Studio, menu **Generate speech**, model **Gemini 3.8 Flash TTS**, suara **Bodi** (sama seperti Bab 3 dan 4).
2. Tempel **prompt gaya** di bawah ke kolom Style instructions.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-16 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan bab sebelumnya. Prompt ini sama dengan Bab 4, ditambah lafal istilah baru di bab ini.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang natural, ramah dan netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Kalimat staf importir yang bertanya dibacakan sedikit lebih ingin tahu, tetapi tetap dengan suara yang sama. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih cepat dari percakapan biasa, sekitar 160 kata per menit. Saat membacakan tarif, rumus, dan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum hasil perhitungan dan sebelum setiap pertanyaan dalam urutan pemeriksaan.
Angka: ucapkan angka persis seperti tertulis dalam kata, misalnya "dua koma lima persen" dan "nol koma dua lima persen".
Singkatan dibaca per huruf: PPh (pe-pe-ha), PPN (pe-pe-en), PDRI (pe-de-er-i), PIB (pe-i-be), DJBC (de-je-be-ce), PMK (pe-em-ka), SPT (es-pe-te), UU (u-u), UU PPh (u-u pe-pe-ha), PT (pe-te), CV (se-ve). API dibaca a-pe-i, API-U dibaca a-pe-i u, API-P dibaca a-pe-i pe, ber-API dibaca ber-a-pe-i.
Istilah Inggris dibaca dengan lafal Inggris yang wajar: withholding.
Penekanan: beri tekanan ringan pada "tidak final", "kredit pajak", "arus kas", nomor pasal, dan hasil akhir setiap perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 16 adegan, sekitar 5 menit 40 detik dengan suara draf. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 14 detik | Judul bab dan label Bagian II; dompet PPh 22 di tengah, enam ikon alur mengelilinginya | Mari kita lanjutkan, ya, sobat. Pada materi kelima ini, kita masuk ke bagian kedua: menghitung, memeriksa, dan menjelaskan. Kita mulai dari PPh Pasal dua puluh dua Impor. |
| 2 | `ask` | 18 detik | Pertanyaan kasus 4; jawaban singkat "Cicilan di muka" | Staf PT Kain Prima Nusantara punya pertanyaan terakhir. Kain kami belum terjual. Mengapa PPh sudah dipungut di pelabuhan? Jawaban singkatnya: PPh Pasal dua puluh dua Impor bukan pajak tambahan, melainkan cicilan di muka atas PPh perusahaan tahun ini. |
| 3 | `lunas` | 37 detik | Empat kartu PPh Pasal 21, 22, 23, 25; kurung withholding | Menurut Undang-Undang PPh, wajib pajak dapat melunasi sebagian PPh-nya sebelum tahun pajak berakhir. Lewat PPh Pasal dua puluh satu, yang dipotong pemberi kerja atas gaji pegawai. Lewat PPh Pasal dua puluh dua, yang dipungut pihak tertentu, termasuk atas impor. Lewat PPh Pasal dua puluh tiga, yang dipotong atas dividen, bunga, royalti, sewa, dan jasa tertentu. Dan lewat PPh Pasal dua puluh lima, angsuran bulanan oleh wajib pajak sendiri. Pemotongan dan pemungutan, keduanya termasuk withholding. |
| 4 | `ketentuan` | 25 detik | Empat kartu ketentuan PMK 51/2025 | Ketentuan terbarunya ada di PMK lima puluh satu Tahun dua ribu dua puluh lima, yang berlaku sejak satu Agustus dua ribu dua puluh lima. Pemungutnya DJBC dan bank devisa. Dasar pemungutannya nilai impor. PPh ini terutang bersamaan dengan pembayaran Bea Masuk. Dan sifatnya tidak final. Importir memperhitungkannya sebagai kredit pajak dalam SPT Tahunan PPh. |
| 5 | `rina` | 27 detik | Panggil ulang kewajiban subjektif (KB 3.3); kartu PT Kain Prima Nusantara (SPT Badan) dan Bu Rina (SPT OP) | Ingat materi ketiga? PPh Pasal dua puluh dua Impor dipungut atas transaksi, tapi menjadi angsuran kewajiban subjektif PPh importir sendiri. Bagaimana maksudnya? Jawabannya: melalui pengkreditan di SPT Tahunan, PPh yang sudah dibayar ini akan menjadi pengurang PPh di akhir tahun. PT Kain Prima Nusantara mengkreditkannya di SPT Tahunan PPh Badan, dan Bu Rina di SPT Tahunan PPh orang pribadi. Keadaan subjek importir juga memengaruhi tarifnya: yang memiliki API dikenai tarif lebih rendah. |
| 6 | `tarif` | 34 detik | Grafik batang enam tarif | Tarifnya bergantung pada barang dan importirnya. Importir yang memiliki API dikenai dua koma lima persen dari nilai impor. Tanpa API, tujuh koma lima persen. Kedelai, gandum, dan tepung terigu yang diimpor importir ber-API dikenai nol koma lima persen. Emas batangan nol koma dua lima persen. Barang tertentu yang tercantum dalam lampiran PMK lima puluh satu dikenai sepuluh persen atau tujuh koma lima persen, sesuai lampirannya. Dan barang yang tidak dikuasai dikenai tujuh koma lima persen dari harga jual lelang. |
| 7 | `urutan` | 29 detik | Tiga pertanyaan berurutan dengan jawaban tarif | Supaya tidak salah pilih, periksa dengan urutan ini. Pertama, apakah barangnya tercantum di lampiran PMK lima puluh satu? Kalau ya, pakai tarif lampiran. Kalau tidak, apakah barangnya kedelai, gandum, terigu, atau emas batangan? Kalau ya, pakai tarif khusus. Kalau tidak juga, baru lihat status API importir: dua koma lima persen kalau punya API, tujuh koma lima persen kalau tidak. |
| 8 | `q1` | 8 detik | Kuis: tarif untuk tiga importir | Sekarang, mari kita cek pemahaman kamu. Coba pilih tarif yang tepat untuk setiap importir ini, ya. |
| 9 | `hitung` | 30 detik | Cek syarat, nilai impor, hasil Rp38.205.750 | Sekarang kita hitung PPh Pasal dua puluh dua Impor untuk Kasus satu. Cek dulu: kain kapas pos lima puluh dua tidak tercantum dalam daftar tarif sepuluh persen di lampiran PMK lima puluh satu, dan importirnya memiliki API-U. Jadi tarifnya dua koma lima persen. Nilai impornya tetap satu koma lima dua delapan miliar rupiah. PPh Pasal dua puluh dua Impor sama dengan dua koma lima persen dikali nilai impor, hasilnya tiga puluh delapan juta dua ratus lima ribu tujuh ratus lima puluh rupiah. |
| 10 | `alur` | 18 detik | Lima langkah alur uang dari PIB sampai SPT Tahunan | Lalu, ke mana uang ini mengalir? Importir mengajukan PIB, lalu membayar PDRI bersama Bea Masuk. Dananya masuk ke kas negara. DJBC melaporkan hasil pemungutannya, dan importir mengkreditkan PPh Pasal dua puluh dua itu dalam SPT Tahunan. |
| 11 | `kas` | 26 detik | Dua batang: dengan API dan tanpa API; selisih Rp76.411.500 | Lalu, apa bedanya punya API atau tidak? Dengan API, PPh Pasal dua puluh dua Impor Kasus satu sebesar tiga puluh delapan koma dua juta rupiah. Tanpa API, tarifnya tujuh koma lima persen, jadi seratus empat belas koma enam juta rupiah. Keduanya tetap bisa dikreditkan dalam SPT Tahunan. Jadi, dampak tarif yang lebih tinggi terutama pada arus kas: lebih banyak uang tertahan di muka. |
| 12 | `q2` | 7 detik | Kuis: sifat PPh Pasal 22 Impor | Sekarang, kita cek pemahaman lagi, ya. Apa sifat PPh Pasal dua puluh dua Impor? |
| 13 | `jawab` | 24 detik | Pertanyaan kasus 4 dijawab dalam tiga poin | Jadi, apa jawaban untuk pertanyaan staf importir tadi? PPh Pasal dua puluh dua Impor adalah pembayaran di muka atas PPh perusahaan tahun ini, bukan pajak tambahan. PPh tiga puluh delapan koma dua juta rupiah itu dikreditkan dalam SPT Tahunan PPh. Jadi, meskipun kainnya belum terjual, yang terasa hanyalah arus kasnya, bukan beban pajak baru.|
| 14 | `wrap` | 24 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. PPh Pasal dua puluh dua Impor adalah pembayaran di muka atas PPh importir, dan tidak bersifat final. Untuk memilih tarif, periksa lampiran PMK lima puluh satu lebih dulu, lalu jenis barang khusus, lalu status API. Tarif tanpa API lebih tinggi, tetapi tetap dapat dikreditkan, jadi dampaknya terutama pada arus kas. |
| 15 | `final1` | 7 detik | Latihan bab: Pilih Tarifmu (delapan skenario), hitung varian 50.000 meter, dan skenario tanpa API | Nah, sekarang kita latihan, ya. Coba kamu pilih tarif untuk setiap skenario berikut ini. |
| 16 | `finish` | 10 detik | Kartu selesai | Bagus, materi kelima selesai. Berikutnya, kita bahas barang mewah dan fasilitas, lewat sepeda motor besar yang diimpor CV Roda Jaya. |

Anda boleh memperbaiki kalimat saat merekam, seperti di bab sebelumnya. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
