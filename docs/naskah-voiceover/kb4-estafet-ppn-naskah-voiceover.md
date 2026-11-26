# Naskah Voice Over KB 4 · Estafet PPN

26 Nov 2026. Dari [storyboard KB 4 Estafet PPN v1](../storyboard-kb4-estafet-ppn-v1.md). Materi terpisah dari Bab 4: folder `site/pdri-mck/ch41`, label "KB 4".

## Cara kerja

Materi ini memakai 13 file suara pendek, satu per adegan, seperti Bab 2 sampai 8. Gaya bahasanya sama: "Anda" atau kalimat netral saat menjelaskan, "kamu" dan "ya" saat mengajak latihan.

1. Buka Google AI Studio, menu **Generate speech**, model **Gemini 3.8 Flash TTS**, suara **Bodi** (sama seperti Bab 3 dan 4).
2. Tempel **prompt gaya** di bawah ke kolom Style.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. File dipasang sebagai `site/pdri-mck/ch41/audio/id/<kode file>.mp3` (24 kHz, 48 kbps), lalu subtitle dan animasinya diselaraskan dengan forced-alignment.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka (`content/pdri-mck/ch41/narration.id.json`).

## Prompt untuk Google AI Studio

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang natural, ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: ramah, tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sekitar 150 kata per menit. Saat membacakan rumus dan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum pertanyaan untuk peserta.
Angka: ucapkan angka persis seperti tertulis dalam kata. "Sebelas per dua belas" dibaca sebagai pecahan, tanpa jeda di tengah.
Singkatan dibaca per huruf: PPN (pe-pe-en), PKP (pe-ka-pe), PIB (pe-i-be), PT (pe-te).
Penekanan: beri tekanan ringan pada istilah pajak keluaran, pajak masukan, kurang bayar, lebih bayar, dikreditkan, dan pada hasil akhir setiap perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

## Naskah per adegan

Total 13 adegan, sekitar 4 menit suara. Durasi draf diperkirakan dari 150 kata per menit.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `susun` | 15 detik | INT. Empat kartu bergambar (kapal, kain, pabrik, toko) diseret ke jalur alur | Mari kita lanjutkan, ya, sobat. Kain impor PT Kain Prima Nusantara akan berpindah tangan beberapa kali sampai menjadi kemeja di tangan pembeli. Coba susun empat tahap ini dari kiri ke kanan, mulai dari PPN Impor sampai penjualan kepada pembeli akhir. |
| 2 | `tahap` | 22 detik | MAT. Rantai transaksi dengan keranjang; empat ciri PPN | Mengapa urutan ini penting? PPN adalah pajak atas konsumsi. PPN juga pajak tidak langsung: penjual memungut dan menyetor, pembeli yang menanggung. PPN dikenakan bertingkat, pada setiap tahap penjualan, tetapi tidak dipungut berganda secara penuh, karena setiap tahap menghitung PPN keluaran dan PPN masukan. |
| 3 | `rumus` | 25 detik | MAT. PK − PM = setoran, bercabang kurang bayar atau lebih bayar; PIB setara faktur pajak | Lalu, berapa yang disetor di setiap tahap? PPN yang harus disetor sama dengan pajak keluaran dikurangi pajak masukan yang dapat dikreditkan. Bila pajak keluaran lebih besar, hasilnya kurang bayar, dan selisihnya disetor. Bila pajak masukan lebih besar, hasilnya lebih bayar. Bagi importir, PIB dan bukti pembayarannya dapat dipersamakan dengan faktur pajak, sehingga PPN Impor menjadi pajak masukan. |
| 4 | `status` | 17 detik | MAT. Dua kartu: PT Kain Prima Nusantara (PKP) dan Bu Rina (bukan PKP) | Tetapi tidak semua importir dapat mengkreditkannya. PT Kain Prima Nusantara berstatus PKP, jadi PPN Impor yang dibayarnya dapat dikreditkan. Bu Rina, yang kita temui di materi sebelumnya, bukan PKP. Ia tetap membayar PPN Impor, tetapi tidak dapat mengkreditkannya. |
| 5 | `estafet` | 21 detik | INT. Rantai importir kain → konveksi → toko → pembeli kemeja; kartu estafet berpindah | Sekarang, mari kita main estafet PPN. Ikuti kain dari importir, ke konveksi, ke toko, sampai menjadi kemeja di tangan pembeli. Di setiap pos, kamu memegang kartu estafet. Catat pajak keluaran, pajak masukan, dan setorannya, lalu teruskan ke pos berikutnya. Supaya sederhana, kita pakai beban efektif sebelas persen. |
| 6 | `pos1` | 15 detik | KAS. Pos 1, importir kain: kapal, PIB, label PPN Impor; peserta mencatat PM | Pos satu, importir kain. Saat kain masuk, importir membayar PPN Impor sebesar dua belas persen dikali sebelas per dua belas dikali nilai impornya. Bagi importir PKP, PPN Impor ini menjadi pajak masukan. Berapa angkanya? Catat di kartu estafetmu, ya. |
| 7 | `pos2` | 16 detik | KAS. Pos 2, importir menjual kain ke konveksi; peserta menghitung PK − PM | Pos dua, importir menjual kain ke konveksi seharga satu koma delapan miliar rupiah, sebelum PPN. Pajak keluarannya sebelas persen, yaitu seratus sembilan puluh delapan juta rupiah. Pajak masukannya adalah PPN Impor dari pos satu. Berapa PPN yang disetor importir? Hitung selisihnya, ya. |
| 8 | `pos3` | 16 detik | KAS. Pos 3, konveksi menjual ke toko; peserta menghitung setoran | Pos tiga, konveksi menjual kemeja ke toko seharga dua koma lima miliar rupiah. Pajak keluarannya dua ratus tujuh puluh lima juta rupiah. Pajak masukannya seratus sembilan puluh delapan juta rupiah, yaitu pajak keluaran importir yang diteruskan kepada konveksi. Hitung setoran konveksi, lalu teruskan kartumu. |
| 9 | `pos4` | 16 detik | KAS. Pos 4, toko menjual kemeja kepada pembeli; perhitungan terakhir | Pos terakhir, toko menjual kemeja kepada pembeli seharga tiga koma dua miliar rupiah. Pajak keluarannya tiga ratus lima puluh dua juta rupiah, dan pajak masukannya dua ratus tujuh puluh lima juta rupiah. Pembeli akhir tidak mengkreditkan PPN, karena dialah yang menanggungnya. Berapa setoran toko? |
| 10 | `total` | 20 detik | RAN. Grafik air terjun: batang setoran satu per satu, total Rp352 juta | Sekarang, jumlahkan setoran di setiap pos. PPN Impor, sekitar seratus enam puluh delapan koma satu juta rupiah. Setoran importir, sekitar dua puluh sembilan koma sembilan juta rupiah. Setoran konveksi, tujuh puluh tujuh juta rupiah. Dan setoran toko, tujuh puluh tujuh juta rupiah. Totalnya tiga ratus lima puluh dua juta rupiah, sama dengan PPN yang dibayar pembeli akhir. |
| 11 | `cocok` | 12 detik | INT. Pencocokan kartu angka PK, PM, dan setoran ke tiga transaksi | Sekarang giliran kamu. Pasangkan setiap kartu angka dengan transaksinya: pajak keluaran, pajak masukan, dan PPN yang disetor. Kalau ada pasangan yang keliru, kartunya kembali, dan kamu bisa mencoba lagi. |
| 12 | `inti` | 17 detik | RAN. Rantai empat tahap dengan stempel selesai; kutipan inti | Inilah inti estafet PPN. Pengusaha menyetorkan selisih PPN keluaran dan PPN masukan. Pembeli akhir menanggung PPN. Jadi, PPN Impor tidak hilang bagi importir PKP: ia dikreditkan, dan total setoran di sepanjang rantai sama dengan PPN yang dibayar pembeli akhir. |
| 13 | `finish` | 10 detik | Kartu selesai | Bagus, estafet PPN selesai. Kamu sudah mengikuti PPN dari pelabuhan sampai ke pembeli akhir. Lihat hasilmu, lalu ulangi bagian yang masih ragu, ya. |
