# Naskah Voice Over Bab 3 PDRI

Nov 22, 2026 · @John

## Cara kerja

Bab 3 memakai 14 file suara pendek, satu per adegan, sama seperti Bab 2. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan.

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan Bab 1 dan 2.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-14 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan Bab 1 dan 2. Prompt ini sama dengan Bab 2, ditambah cara membaca istilah dan singkatan baru di bab ini.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu" atau "ya"), nadanya lebih santai dan bersahabat. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum nama sistem atau nama pihak.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: PIB (pe-i-be), PPJK (pe-pe-je-ka), DJBC (de-je-be-ce), DJP (de-je-pe), PPN (pe-pe-en), PPh (pe-pe-ha), PDRI (pe-de-er-i), SPT (es-pe-te), NPWP (en-pe-we-pe), NIK (en-i-ka), PKP (pe-ka-pe), PMK (pe-em-ka), UU (u-u), UU KUP (u-u ka-u-pe). API-U dibaca a-pe-i u, API-P dibaca a-pe-i pe. PPnBM dibaca pe-pe-en-be-em.
Istilah Inggris dibaca dengan lafal Inggris yang wajar: official assessment, self assessment, withholding. Coretax dibaca "kor-teks".
Penekanan: beri tekanan ringan pada nama tiga sistem dan pada nama pihak (importir, PPJK, DJBC, bank, DJP, konsumen akhir).
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 14 adegan, sekitar 4 menit 27 detik dengan suara draf Ardi. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 9 detik | Judul bab; PIB di tengah, enam ikon pihak mengelilinginya | Mari kita lanjutkan, ya sobat. Pada materi ketiga ini, kita akan melihat siapa yang memungut pajak, dan dengan cara apa. |
| 2 | `ask` | 18 detik | Pertanyaan staf; kartu PIB; angka 6 pihak dan 3 sistem | Staf PT Kain Prima Nusantara kini bertanya, siapa sebenarnya yang memungut, dan dengan cara apa? Jawabannya bertemu dalam satu dokumen, yaitu Pemberitahuan Impor Barang, atau PIB. Di balik satu PIB itu, ada enam pihak dan tiga sistem pemungutan yang bekerja bersama. |
| 3 | `sistem` | 37 detik | Tiga kartu sistem: siapa yang menentukan, contoh Kasus 1 | Kita mulai dari tiga sistem pemungutan pajak. Pertama, official assessment: petugas pajak, atau fiskus, yang menentukan besarnya pajak. Dalam Kasus satu, pejabat DJBC meneliti PIB dan dapat menetapkan kekurangan pembayaran. Kedua, self assessment: wajib pajak menentukan sendiri. Importir menghitung sendiri Bea Masuk dan PDRI dalam PIB. Ketiga, withholding: pihak ketiga yang ditunjuk undang-undang memungut pajaknya. DJBC memungut PPh Pasal dua puluh dua Impor atas penghasilan importir. |
| 4 | `alur` | 15 detik | Garis alur satu PIB: hitung → teliti → pungut, dengan label sistem | Sistem utama di Indonesia adalah self assessment. Tetapi dalam impor, ketiganya berjalan bersama. Importir menghitung, DJBC meneliti, dan DJBC juga memungut PPh Pasal dua puluh dua. |
| 5 | `q1` | 7 detik | Kuis: sistem apa di setiap langkah | Sekarang, mari kita cek pemahaman kamu. Sistem apa yang bekerja di setiap langkah ini, ya? |
| 6 | `jenis` | 34 detik | Tiga dasar pembagian pajak, masing-masing dua sisi | Pajak juga dapat dibagi menurut tiga dasar. Menurut lembaga pemungutnya, ada pajak pusat, seperti PPN, PPnBM, PPh, dan Bea Meterai, dan ada pajak daerah, seperti pajak kendaraan bermotor dan pajak hotel. Menurut pihak yang menanggung, PPh adalah pajak langsung, sedangkan PPN dan PPnBM adalah pajak tidak langsung. Menurut sifatnya, PPh adalah pajak subjektif, karena memperhatikan keadaan wajib pajak, sedangkan PPN adalah pajak objektif, karena memperhatikan objeknya. |
| 7 | `hukum` | 30 detik | Garis waktu empat undang-undang dan perubahannya | Lalu, aturan mana yang menjadi pegangan? UU KUP, UU PPh, dan UU PPN berasal dari tahun seribu sembilan ratus delapan puluh tiga, dan terakhir diubah dengan UU enam Tahun dua ribu dua puluh tiga tentang Cipta Kerja. UU Harmonisasi Peraturan Perpajakan menetapkan tarif PPN dua belas persen, paling lambat satu Januari dua ribu dua puluh lima. Untuk kepabeanan, pegangannya UU sepuluh Tahun seribu sembilan ratus sembilan puluh lima, yang diubah dengan UU tujuh belas Tahun dua ribu enam. |
| 8 | `hierarki` | 17 detik | Piramida UU → PP → PMK → Perdirjen | Dalam pekerjaan, Anda akan menemui peraturan dengan urutan ini. Undang-undang, Peraturan Pemerintah, Peraturan Menteri Keuangan atau PMK, lalu Peraturan Direktur Jenderal. Ingat, peraturan yang lebih rendah tidak boleh bertentangan dengan peraturan yang lebih tinggi. |
| 9 | `peran` | 33 detik | Enam kartu pihak; DJBC dan DJP disorot | Sekarang, siapa melakukan apa? Importir menghitung dan membayar Bea Masuk dan PDRI, serta mengisi PIB. PPJK mengurus kewajiban kepabeanan atas kuasa importir. DJBC meneliti PIB, memungut PDRI, dan menetapkan kekurangan pembayaran. Bank persepsi atau bank devisa menerima pembayarannya. DJP mengadministrasikan pengkreditan PPN dan PPh Pasal dua puluh dua dalam SPT importir. Dan konsumen akhir menanggung PPN di ujung rantai penjualan. |
| 10 | `identitas` | 19 detik | Kartu identitas PT Kain Prima: NPWP, API, PKP → Coretax | Saat melayani, Anda akan sering memeriksa identitas importir. NPWP atau NIK, Angka Pengenal Importir, API-U atau API-P, dan status Pengusaha Kena Pajak, atau PKP. Data ini terhubung dengan Coretax, sistem administrasi perpajakan DJP. |
| 11 | `q2` | 7 detik | Kuis: Importir, DJBC, atau DJP | Sekarang, kita cek pemahaman lagi, ya. Siapa yang menjalankan setiap peran ini? |
| 12 | `wrap` | 23 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. Dalam impor, self assessment, official assessment, dan withholding berjalan bersama. DJBC memungut PDRI di pelabuhan, sedangkan DJP mengadministrasikan pengkreditannya. Dan sebelum melayani, periksa dulu identitas importir: NPWP, API, dan status PKP. |
| 13 | `final1` | 7 detik | Latihan bab: tiga soal | Nah, sekarang kita latihan, ya. Coba kamu jawab latihan berikut ini. |
| 14 | `finish` | 10 detik | Kartu selesai | Bagus, materi ketiga selesai. Berikutnya, kita bahas PPN Impor, dan mengapa PPN yang sudah dibayar importir tidak hilang begitu saja. |

Anda boleh memperbaiki kalimat saat merekam, seperti di Bab 1 dan 2. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
