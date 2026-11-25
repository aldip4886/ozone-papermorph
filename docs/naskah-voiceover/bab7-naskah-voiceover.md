# Naskah Voice Over Bab 7 PDRI

Nov 22, 2026 · @John. Ditulis ulang 23 Nov 2026: Bab 7 berubah total dari "Barang Kiriman" menjadi "Upaya Hukum dan Hak Wajib Pajak", mengikuti [outline v3](07-outline-materi-v3.md), [session plan v3](08-session-plan-v3.md), dan [bahan ajar v3](bahan-ajar-pdri-v3.md). Dipadatkan jadi 14 adegan (setara bab lain): Kasus 3 (SPTNP) dan jalur kepabeanan lengkap; sisi perpajakan diringkas satu adegan sengketa-vs-permohonan dan satu adegan bandingan, tanpa Kasus 4 tersendiri.

## Cara kerja

Bab 7 memakai 14 file suara pendek, satu per adegan. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan, dan pembuka "Mari kita lanjutkan, ya, sobat".

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan bab sebelumnya.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-14 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan bab sebelumnya. Prompt ini sama dengan Bab 6, ditambah lafal istilah upaya hukum dan hak wajib pajak.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Kalimat kutipan staf importir dibacakan sedikit lebih cemas, tetapi tetap dengan suara yang sama. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit. Saat membacakan angka rupiah atau tenggat, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum setiap langkah jalur dan hasil perhitungan.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: PPN (pe-pe-en), PPh (pe-pe-ha), PDRI (pe-de-er-i), PMK (pe-em-ka), DJBC (de-je-be-ce), DJP (de-je-pe), KPP (ka-pe-pe), KUP (ka-u-pe), SPTNP (es-pe-te-en-pe), SPKTNP (es-pe-ka-te-en-pe), SPP (es-pe-pe), SPSA (es-pe-es-a), SKPKB (es-ka-pe-ka-be), STP (es-te-pe), PK (pe-ka), UUD (u-u-de), UU (u-u), PT (pe-te).
Istilah Inggris dibaca dengan lafal Inggris yang wajar: certainty, equality.
Penekanan: beri tekanan ringan pada nama setiap jalur (keberatan, banding, gugatan, peninjauan kembali, pembetulan, permohonan) dan pada tenggat waktunya.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 14 adegan, sekitar 5 menit 40 detik (perkiraan 140 kata per menit; belum ada rekaman). Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 12 detik | Judul bab; ikon timbangan di tengah, SPTNP, DJBC, DJP, sanksi, permohonan, dan Pengadilan Pajak mengelilinginya | Mari kita lanjutkan, ya, sobat. Inilah materi ketujuh: upaya hukum, dan hak wajib pajak ketika tidak setuju dengan penetapan DJBC atau ketetapan DJP. |
| 2 | `ask` | 18 detik | Dua kartu map (SPTNP dari DJBC, SKPKB dan STP dari KPP); kutipan staf | Staf PT Kain Prima Nusantara datang membawa dua map: map biru berisi SPTNP dari DJBC, map kuning berisi SKPKB dan STP dari KPP. Dua-duanya kami tidak setuju, dan kas kami sedang seret, apa saja yang bisa kami lakukan? |
| 3 | `penetapan` | 49 detik | Empat kartu surat DJBC; rantai kenaikan nilai pabean; catatan denda | Penetapan pejabat bea dan cukai bisa datang dalam empat bentuk surat. SPTNP, Pasal enam belas, soal tarif dan nilai pabean. SPKTNP, Pasal tujuh belas, penetapan kembali oleh Direktur Jenderal. SPP, Pasal sembilan puluh tiga A, untuk penetapan selain tarif dan nilai pabean. SPSA, Pasal sembilan puluh empat, sanksi administrasi berupa denda. Begini rantainya: nilai pabean naik, Bea Masuk kurang dibayar, nilai impor ikut naik, dan PPN serta PPh Pasal dua puluh dua Impor ikut kurang. Denda kesalahan nilai pabean dihitung dari kekurangan Bea Masuk saja: seratus persen untuk kekurangan sampai lima puluh persen dari Bea Masuk yang dibayar, berlapis sampai seribu persen. |
| 4 | `kasus3` | 45 detik | Tabel hitung SPTNP Kasus 3, total Rp37.962.105 | Mari kita hitung Kasus tiga. Selisih nilai pabeannya: enam ribu dolar dikali delapan belas ribu seratus lima puluh lima rupiah, seratus delapan koma sembilan tiga juta. Kekurangan Bea Masuk sepuluh persen, sepuluh koma delapan sembilan tiga juta. Selisih nilai impornya seratus sembilan belas koma delapan dua tiga juta. Kekurangan PPN Impor tiga belas koma satu delapan juta, dan kekurangan PPh Pasal dua puluh dua dua koma sembilan sembilan lima juta. Dendanya seratus persen dari kekurangan Bea Masuk, sepuluh koma delapan sembilan tiga juta. Jadi, total tagihan SPTNP-nya tiga puluh tujuh koma sembilan enam dua juta rupiah. |
| 5 | `jalur1` | 26 detik | Tiga langkah jalur kepabeanan: keberatan, banding, peninjauan kembali | Terhadap penetapan ini, PT Kain Prima Nusantara bisa melakukan upaya hukum. Pertama, keberatan ke Direktur Jenderal Bea dan Cukai lewat Portal DJBC, enam puluh hari sejak tanggal penetapan, dengan jaminan sebesar tagihan. Kedua, banding ke Pengadilan Pajak, enam puluh hari setelah tagihan dilunasi. Dan ketiga, peninjauan kembali ke Mahkamah Agung, dengan alasan terbatas, hanya satu kali. |
| 6 | `q1` | 12 detik | Kuis: ke mana dan berapa lama keberatan atas SPTNP | Sekarang, mari kita cek pemahaman kamu. Importir menerima SPTNP yang menaikkan nilai pabean. Ke mana dan berapa lama ia bisa mengajukan keberatan, ya? |
| 7 | `hak` | 35 detik | Dua kartu: Sengketa (keberatan, banding, gugatan, PK) dan Permohonan (pembetulan, sanksi, angsuran) | Di bidang perpajakan, wajib pajak punya dua kelompok hak. Pertama, sengketa. Hak ini digunakan untuk menguji kebenaran ketetapan, lewat keberatan, banding, gugatan, atau peninjauan kembali. Kalau kalah, risikonya sanksi tiga puluh persen untuk keberatan, dan enam puluh persen untuk banding atau peninjauan kembali. Kedua, permohonan. Permohonan bertujuan memperbaiki atau meringankan tanpa sengketa, lewat pembetulan SPT, pembetulan ketetapan, pengurangan atau penghapusan sanksi, atau angsuran dan penundaan pembayaran. Permohonan ini tidak menggantikan keberatan untuk SKP yang sama. |
| 8 | `q2` | 15 detik | Kuis (hinge question): STP denda karena khilaf, jalur apa | Sekarang, kita cek pemahaman lagi, ya. PT Kain Prima Nusantara menerima STP denda lima ratus ribu rupiah karena SPT Masa PPN-nya terlambat, dan ia merasa khilaf. Jalur apa yang tepat? |
| 9 | `bandingkan` | 32 detik | Tabel banding DJBC vs DJP: tenggat, syarat bayar, risiko | Upaya hukum untuk Dua jalur penetapan ini berbeda di tiga hal. Tenggat keberatannya: enam puluh hari untuk DJBC, tiga bulan untuk DJP. Syarat bayarnya: jaminan sebesar tagihan untuk DJBC, melunasi jumlah yang disetujui untuk DJP. Tenggat bandingnya: enam puluh hari setelah lunas untuk DJBC, tiga bulan dengan sisa pajak tertangguh untuk DJP. Dan risikonya: DJBC tidak mengenakan sanksi khusus, sedangkan DJP mengenakan sanksi tiga puluh atau enam puluh persen jika kalah.|
| 10 | `lensa` | 34 detik | Tiga kartu lensa: kontrol wewenang, kepastian dan keadilan, peran Anda | Mengapa hak untuk melakukan upaya hukum ini diberikan oleh undang-undang? Pertama, kontrol atas wewenang: Pasal dua puluh tiga A Undang-Undang Dasar seribu sembilan ratus empat puluh lima mensyaratkan pungutan diatur berdasarkan undang-undang, dan penetapan pejabat harus dapat diuji. Kedua, kepastian dan keadilan: asas certainty dan equality tidak cukup di atas kertas, wajib pajak perlu jalan resmi untuk menguji penetapan yang menurutnya keliru. Dan peran Anda: tetapkan dengan benar, lalu jelaskan hak pengguna jasa dengan jujur. Jangan menilai peluang menang.|
| 11 | `jawab` | 27 detik | Tiga kartu jawaban: map SPTNP, map SKPKB, kas seret | Jadi, bagaimana menjawab dua map tadi? Untuk map SPTNP, sampaikan haknya: keberatan ke Direktur Jenderal Bea dan Cukai lewat Portal DJBC, enam puluh hari. Untuk map SKPKB, keberatan ke Direktur Jenderal Pajak, tiga bulan, setelah melunasi jumlah yang disetujui. Dan untuk kas yang sedang seret, sampaikan permohonan angsuran atau penundaan, lewat KPP tempat ia terdaftar. |
| 12 | `wrap` | 19 detik | Tiga kartu rangkuman | Ini rangkumannya. Penetapan DJBC diuji ke DJBC: keberatan enam puluh hari dengan jaminan. Untuk ketetapan dari DJP, wajib pajak bisa menempuh jalur sengketa, yang berisiko sanksi, atau permohonan, yang tidak ada sanksi. Dan sebutkan hak serta tenggatnya dengan jujur. Jangan menilai peluang menang. |
| 13 | `final1` | 7 detik | Latihan bab: tiga situasi, pilih jalurnya | Nah, ini latihan bab, ya. Coba kamu pilih jalurnya untuk tiga situasi berikut ini. |
| 14 | `finish` | 10 detik | Kartu selesai | Materi ketujuh selesai. Berikutnya, kita kembali ke Kasus satu, dan menyusun jawaban lengkap untuk tagihan PT Kain Prima Nusantara. |

Anda boleh memperbaiki kalimat saat merekam, seperti di bab sebelumnya. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
