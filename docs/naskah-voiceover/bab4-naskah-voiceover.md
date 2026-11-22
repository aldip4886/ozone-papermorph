# Naskah Voice Over Bab 4 PDRI

Nov 22, 2026 · @John

## Cara kerja

Bab 4 memakai 15 file suara pendek, satu per adegan, sama seperti Bab 2 dan 3. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan. Pembukanya "Mari kita lanjutkan, ya, sobat", mengikuti perubahan Anda di naskah Bab 3.

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan Bab 1 sampai 3.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-15 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan Bab 1 sampai 3. Prompt ini sama dengan Bab 3, ditambah cara membaca istilah dan pecahan baru di bab ini.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Kalimat staf importir yang bertanya dibacakan sedikit lebih ingin tahu, tetapi tetap dengan suara yang sama. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit. Saat membacakan rumus dan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum hasil perhitungan.
Angka: ucapkan angka persis seperti tertulis dalam kata. "Sebelas per dua belas" dibaca sebagai pecahan, tanpa jeda di tengah.
Singkatan dibaca per huruf: PPN (pe-pe-en), PPh (pe-pe-ha), PPnBM (pe-pe-en-be-em), PKP (pe-ka-pe), PIB (pe-i-be), DPP (de-pe-pe), BKP (be-ka-pe), PMK (pe-em-ka), SPT (es-pe-te), UU (u-u), UU PPN (u-u pe-pe-en), UU HPP (u-u ha-pe-pe), PT (pe-te).
Penekanan: beri tekanan ringan pada istilah pajak keluaran, pajak masukan, kurang bayar, lebih bayar, dan pada hasil akhir setiap perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 15 adegan, sekitar 5 menit 3 detik dengan suara draf Ardi. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 12 detik | Judul bab; ikon PPN di tengah, rantai impor sampai kas negara mengelilinginya | Mari kita lanjutkan, ya, sobat. Pada materi keempat ini, kita membahas PPN Impor: cara menghitungnya, dan ke mana PPN itu mengalir setelah dibayar. |
| 2 | `ask` | 20 detik | Pertanyaan staf; kartu PPN Rp168.105.300; jawaban "Tidak." | Staf PT Kain Prima Nusantara datang lagi dengan pertanyaan baru. Perusahaan kami sudah membayar PPN sekitar seratus enam puluh delapan juta rupiah. Apakah uang itu hilang begitu saja? Jawabannya, tidak. Tapi untuk menjelaskannya, kita perlu mengenal dulu cara kerja PPN. |
| 3 | `ciri` | 26 detik | Tiga kartu ciri PPN | PPN punya tiga ciri. Pertama, PPN adalah pajak atas konsumsi barang dan jasa di dalam daerah pabean. Kedua, PPN termasuk pajak tidak langsung. Penjual atau importir yang menyetor, tetapi konsumen akhir yang menanggung. Ketiga, PPN dikenakan di setiap tahap penyerahan, tetapi hanya atas pertambahan nilainya, jadi tidak menimbulkan pajak berganda. |
| 4 | `objek` | 23 detik | Kartu Pasal 4 ayat (1); importir PKP dan bukan PKP sama-sama dicentang; definisi PKP | Lalu, apa yang dikenai PPN Impor? Pasal empat ayat satu UU PPN menetapkan impor Barang Kena Pajak sebagai objek PPN. Dan PPN Impor dipungut dari siapa pun yang mengimpor, baik PKP maupun bukan PKP. PKP, atau Pengusaha Kena Pajak, adalah pengusaha yang menyerahkan barang atau jasa yang dikenai pajak berdasarkan UU PPN. |
| 5 | `tarif` | 30 detik | Dua kartu: tidak mewah (beban 11%) dan mewah (beban 12%) | Berapa tarifnya? UU HPP menetapkan tarif PPN dua belas persen, dan PMK seratus tiga puluh satu Tahun dua ribu dua puluh empat mengatur cara menerapkannya. Untuk barang yang tidak tergolong mewah, dasar pengenaannya sebelas per dua belas dari nilai impor, sehingga beban efektifnya sebelas persen. Untuk barang mewah yang dikenai PPnBM, dasarnya nilai impor penuh, jadi bebannya dua belas persen. Saat bahan ajar ini disusun, aturan ini masih berlaku. |
| 6 | `q1` | 8 detik | Kuis: beban efektif PPN atas kain | Sekarang, mari kita cek pemahaman kamu. Kira-kira, berapa beban efektif PPN untuk kain kita, ya? |
| 7 | `hitung` | 29 detik | Cek syarat, nilai impor, langkah hitung DPP lalu PPN | Sekarang kita hitung PPN Impor untuk Kasus satu. Cek dulu: kain tidak tergolong mewah, dan importirnya PKP. Jadi dasar pengenaannya sebelas per dua belas dari nilai impor. Nilai impornya sudah kita hitung di materi pertama, yaitu satu koma lima dua delapan miliar rupiah. PPN Impor sama dengan dua belas persen dikali sebelas per dua belas dikali nilai impor. Hasilnya seratus enam puluh delapan juta seratus lima ribu tiga ratus rupiah. |
| 8 | `pkpm` | 32 detik | Pajak keluaran dan pajak masukan → kurang bayar atau lebih bayar | Supaya tahu ke mana uang ini pergi, kenali dua istilah. Pajak keluaran adalah PPN yang dipungut PKP saat menjual barang. Pajak masukan adalah PPN yang dibayar PKP saat membeli atau mengimpor barang. Setiap masa pajak, PKP menghitung pajak keluaran dikurangi pajak masukan. Kalau pajak keluaran lebih besar, PKP menyetor selisihnya. Kalau pajak masukan yang lebih besar, terjadi lebih bayar, dan PKP bisa meminta pengembalian atau mengompensasikannya. |
| 9 | `faktur` | 15 detik | PIB + bukti bayar = faktur pajak → pajak masukan | Lalu, bagaimana PPN Impor masuk ke hitungan itu? PIB beserta bukti pembayarannya berkedudukan sama dengan faktur pajak. Jadi, importir yang PKP dapat mengkreditkan PPN Impor sebagai pajak masukan. |
| 10 | `estafet` | 40 detik | Tabel estafet PPN empat tahap; batang setoran berjumlah Rp352 juta | Mari kita ikuti perjalanan kain ini sampai menjadi kemeja. Angkanya disederhanakan, ya. Saat impor, importir membayar PPN sekitar seratus enam puluh delapan juta rupiah sebagai pajak masukan. Importir menjual kain ke konveksi, memungut PPN seratus sembilan puluh delapan juta, lalu menyetor selisihnya, sekitar dua puluh sembilan koma sembilan juta. Konveksi menjual ke toko dan menyetor tujuh puluh tujuh juta. Toko menjual ke pembeli, dan menyetor tujuh puluh tujuh juta lagi. Kalau dijumlahkan, kas negara menerima tiga ratus lima puluh dua juta rupiah, sama persis dengan PPN yang dibayar pembeli akhir. |
| 11 | `q2` | 7 detik | Kuis: PPN yang disetor konveksi | Sekarang, kita cek pemahaman lagi, ya. Berapa PPN yang disetor konveksi? |
| 12 | `jawab` | 19 detik | Pertanyaan staf dijawab dalam tiga poin | Jadi, apa jawaban untuk staf importir tadi? PPN Impor seratus enam puluh delapan juta itu tidak hilang. Sebagai PKP, perusahaan dapat mengkreditkannya sebagai pajak masukan saat menjual kain. Beban PPN-nya berpindah ke pembeli berikutnya, sampai ke konsumen akhir. |
| 13 | `wrap` | 25 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. PPN Impor dikenakan atas impor Barang Kena Pajak, oleh siapa pun. Untuk barang tidak mewah, rumusnya dua belas persen dikali sebelas per dua belas dikali nilai impor. Untuk barang mewah, dua belas persen dikali nilai impor. Importir PKP mengkreditkan PPN Impor sebagai pajak masukan, dan konsumen akhir yang menanggung PPN. |
| 14 | `final1` | 7 detik | Latihan bab: tiga soal | Nah, sekarang kita latihan, ya. Coba kamu jawab latihan berikut ini. |
| 15 | `finish` | 12 detik | Kartu selesai | Bagus, materi keempat selesai. Berikutnya, kita bahas PPh Pasal dua puluh dua Impor, dan mengapa PPh sudah dipungut di pelabuhan, padahal kainnya belum terjual. |

Anda boleh memperbaiki kalimat saat merekam, seperti di Bab 1 sampai 3. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
