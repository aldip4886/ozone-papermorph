# Naskah Voice Over Bab 7 PDRI

Nov 22, 2026 · @John

## Cara kerja

Bab 7 memakai 15 file suara pendek, satu per adegan, sama seperti bab sebelumnya. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan, dan pembuka "Mari kita lanjutkan, ya, sobat".

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan bab sebelumnya.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-15 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan bab sebelumnya. Prompt ini sama dengan Bab 6, ditambah lafal istilah barang kiriman.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Kalimat pertanyaan Dita dibacakan sedikit lebih heran, tetapi tetap dengan suara yang sama. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit. Saat membacakan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum hasil perhitungan.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: PPN (pe-pe-en), PPh (pe-pe-ha), PMK (pe-em-ka), PIB (pe-i-be), PIBK (pe-i-be-ka), PPJK (pe-pe-je-ka), DJBC (de-je-be-ce), BTKI (be-te-ka-i), FOB (ef-o-be), CIF (si-ai-ef), PT (pe-te).
Istilah Inggris dibaca dengan lafal Inggris yang wajar: earbuds, sneakers, Consignment Note.
Penekanan: beri tekanan ringan pada batas nilai FOB, pada "tarif khusus", "dikecualikan", dan hasil akhir setiap perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 15 adegan, sekitar 5 menit 3 detik dengan suara draf Ardi. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 11 detik | Judul bab; ikon paket di tengah, Dita, earbuds, sneakers, dan lainnya mengelilinginya | Mari kita lanjutkan, ya, sobat. Pada materi ketujuh ini, kita membahas barang kiriman: paket belanja daring yang datang lewat jasa titipan atau pos. |
| 2 | `ask` | 22 detik | Kartu Kasus 3: dua paket Dita; pertanyaan Dita | Kali ini kita pakai Kasus tiga. Dita, mahasiswi di Bekasi, menerima dua paket lewat Perusahaan Jasa Titipan: earbuds dengan nilai FOB tiga puluh dolar, dan sepatu sneakers dengan nilai FOB delapan puluh dolar. Lalu Dita bertanya, saya beli sepatu sekitar satu koma tujuh juta rupiah, mengapa tagihannya hampir tujuh ratus delapan puluh ribu? |
| 3 | `hukum` | 20 detik | PMK 96/2023 → PMK 4/2025; dua kelonggaran | Barang kiriman punya aturan sendiri. Dasarnya PMK sembilan puluh enam Tahun dua ribu dua puluh tiga, yang sudah beberapa kali diubah, terakhir dengan PMK empat Tahun dua ribu dua puluh lima. Perubahan terakhir itu antara lain melonggarkan ketentuan untuk barang kiriman jemaah haji, serta hadiah perlombaan atau penghargaan internasional. |
| 4 | `ambang` | 28 detik | Tiga kartu batas nilai FOB | Pungutannya ditentukan oleh nilai FOB per kiriman. Sampai tiga dolar, Bea Masuk dibebaskan dan PPh dikecualikan. Yang dibayar hanya PPN, dengan beban efektif sebelas persen. Di atas tiga dolar sampai seribu lima ratus dolar, Bea Masuknya tujuh koma lima persen, PPh tetap dikecualikan, dan PPN-nya sama. Di atas seribu lima ratus dolar, berlaku tarif umum, seperti impor biasa. |
| 5 | `komoditas` | 26 detik | Delapan ikon komoditas; kartu alas kaki BM 25% dan PPh 5% | Tapi ada pengecualian. Delapan kelompok komoditas dikenai tarif yang berbeda dari tujuh koma lima persen, antara lain tas, produk tekstil, alas kaki, sepeda, jam tangan, kosmetik, besi dan baja, serta buku. Untuk latihan ini, alas kaki kita hitung dengan Bea Masuk dua puluh lima persen dan PPh lima persen. Angka ini perlu dicocokkan dengan tabel resmi DJBC. |
| 6 | `q1` | 8 detik | Kuis: batas FOB untuk tiga paket | Sekarang, mari kita cek pemahaman kamu. Ketentuan mana yang berlaku untuk setiap paket ini, ya? |
| 7 | `beda` | 26 detik | Tabel barang kiriman vs impor umum | Apa bedanya dengan impor umum? Dokumennya bukan PIB, melainkan Consignment Note, atau PIBK. Yang mengurus adalah Perusahaan Jasa Titipan atau penyelenggara pos, bukan importir atau PPJK. Bea Masuknya tarif tunggal tujuh koma lima persen, bukan tarif BTKI. Dan PPh Pasal dua puluh dua dikecualikan sampai seribu lima ratus dolar, kecuali untuk komoditas tertentu. |
| 8 | `paketA` | 35 detik | Tabel hitung paket earbuds, total Rp140.338 | Sekarang kita hitung paket A, earbuds. Nilai pabeannya CIF empat puluh dolar dikali kurs delapan belas ribu seratus lima puluh lima rupiah, yaitu tujuh ratus dua puluh enam ribu dua ratus rupiah. Bea Masuk tujuh koma lima persen, lima puluh empat ribu empat ratus enam puluh lima rupiah. Nilai impornya tujuh ratus delapan puluh ribu enam ratus enam puluh lima rupiah, dan PPN dengan beban efektif sebelas persen sebesar delapan puluh lima ribu delapan ratus tujuh puluh tiga rupiah. PPh dikecualikan. Total pungutannya seratus empat puluh ribu tiga ratus tiga puluh delapan rupiah. |
| 9 | `paketB` | 42 detik | Tabel hitung paket sepatu, total Rp776.126 | Lalu paket B, sepatu sneakers. Nilai pabeannya CIF sembilan puluh lima dolar, yaitu satu juta tujuh ratus dua puluh empat ribu tujuh ratus dua puluh lima rupiah. Karena alas kaki, Bea Masuknya dua puluh lima persen, empat ratus tiga puluh satu ribu seratus delapan puluh satu rupiah. Nilai impornya dua juta seratus lima puluh lima ribu sembilan ratus enam rupiah, dan PPN-nya dua ratus tiga puluh tujuh ribu seratus lima puluh rupiah. Ditambah PPh lima persen, seratus tujuh ribu tujuh ratus sembilan puluh lima rupiah. Total pungutannya tujuh ratus tujuh puluh enam ribu seratus dua puluh enam rupiah. Angka ini belum dibulatkan; pembulatannya mengikuti ketentuan pengisian dokumen. |
| 10 | `banding` | 19 detik | Batang nilai pabean vs pungutan kedua paket (19% dan 45%) | Bandingkan keduanya. Pungutan earbuds sekitar sembilan belas persen dari nilai pabeannya. Pungutan sepatu sekitar empat puluh lima persen. Bedanya ada pada tarif khusus alas kaki, yaitu Bea Masuk dua puluh lima persen ditambah PPh, untuk melindungi industri alas kaki dalam negeri. |
| 11 | `q2` | 8 detik | Kuis: pungutan paket sepatu | Sekarang, kita cek pemahaman lagi, ya. Pungutan apa saja yang dikenakan pada paket sepatu Dita? |
| 12 | `jawab` | 21 detik | Pertanyaan Dita dijawab dalam tiga poin | Jadi, apa jawaban untuk Dita? Sepatu termasuk komoditas dengan tarif khusus, untuk melindungi industri alas kaki dalam negeri. Bea Masuknya dua puluh lima persen dari nilai pabean, ditambah PPN dan PPh. Pungutan earbuds lebih kecil, karena earbuds memakai tarif umum barang kiriman tujuh koma lima persen, tanpa PPh. |
| 13 | `wrap` | 22 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. Barang kiriman memakai ketentuan khusus, berdasarkan nilai FOB dan jenis komoditas. Untuk FOB di atas tiga sampai seribu lima ratus dolar, Bea Masuknya tujuh koma lima persen dan PPh dikecualikan, kecuali komoditas tertentu. PPN tetap dipungut, dengan beban efektif sebelas persen. |
| 14 | `final1` | 7 detik | Latihan bab: tali sepatu USD 2, total paket earbuds, penjelasan untuk Dita | Nah, sekarang kita latihan, ya. Coba kamu jawab latihan berikut ini. |
| 15 | `finish` | 11 detik | Kartu selesai | Bagus, materi ketujuh selesai. Di materi terakhir, kita kembali ke staf PT Kain Prima Nusantara, dan menyusun jawaban lengkap untuk tagihannya. |

Anda boleh memperbaiki kalimat saat merekam, seperti di bab sebelumnya. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
