# Naskah Voice Over Bab 8 PDRI

Nov 22, 2026 · @John. Diperbarui 23 Nov 2026 untuk [session plan v3](08-session-plan-v3.md).

**Pembaruan v3.** JP 7 berubah dari Barang Kiriman menjadi Upaya Hukum, dan role play JP 8 kini memuat satu keberatan tak terduga tentang jalur hukum: "Kalau saya tidak setuju, saya harus ke mana?" ([outline v3](07-outline-materi-v3.md), [bahan ajar v3](bahan-ajar-pdri-v3.md) 8.4). Ditambah satu adegan baru, `hak`, setelah `jelaskan` dan sebelum `layanan`, supaya kursus menutup penjelasan tagihan dengan hak keberatan pengguna jasa. Adegan lain tidak berubah.

## Cara kerja

Bab 8 adalah materi terakhir dan memakai 15 file suara pendek, satu per adegan. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan, dan pembuka "Mari kita lanjutkan, ya, sobat".

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan bab sebelumnya.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-14 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan bab sebelumnya. Prompt ini sama dengan Bab 7, ditambah lafal istilah di bab ini dan nada penutup kursus.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Kalimat staf importir yang bertanya dibacakan sedikit lebih ingin tahu. Adegan penutup dibacakan dengan nada bangga dan hangat. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit. Saat membacakan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum setiap langkah penjelasan dan hasil perhitungan.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: PPN (pe-pe-en), PPh (pe-pe-ha), PDRI (pe-de-er-i), BMTP (be-em-te-pe), DPP (de-pe-pe), SKB (es-ka-be), SPT (es-pe-te), PMK (pe-em-ka), DJBC (de-je-be-ce), DJP (de-je-pe), PKP (pe-ka-pe), UUD (u-u-de), PT (pe-te). API dibaca a-pe-i. Pasal 23A dibaca pasal dua puluh tiga a.
Penekanan: beri tekanan ringan pada nama setiap langkah penjelasan, pada kata "kurang", dan hasil akhir setiap perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 15 adegan, sekitar 5 menit 55 detik dengan rekaman final (Google AI Studio, 26 Nov 2026). Teks di kolom Teks sesuai ucapan di rekaman. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi rekaman | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 9 detik | Judul bab; ikon jawaban di tengah, enam bekal mengelilinginya | Inilah materi kedelapan, materi terakhir. Kita kembali ke staf PT Kain Prima Nusantara, dan menyusun jawaban lengkap untuk tagihannya. |
| 2 | `ask` | 17 detik | Pertanyaan hari pertama; empat kartu bekal | Ingat pertanyaan di hari pertama? Pak, Bu, hitungan ini dari mana? Pungutannya lebih dari separuh harga kain kami. Sekarang Anda punya semua bekalnya: nilai impor, PPN, PPh Pasal dua puluh dua, dan dasar hukumnya. |
| 3 | `lengkap` | 46 detik | Tabel jawaban lengkap Kasus 1 | Mari kita susun jawaban lengkapnya. Nilai pabean enam puluh ribu dolar dikali delapan belas ribu seratus lima puluh lima rupiah, yaitu satu koma nol delapan sembilan miliar rupiah. Bea Masuk sepuluh persen, seratus delapan koma sembilan juta, dan BMTP seratus ribu meter dikali tiga ribu tiga ratus rupiah, tiga ratus tiga puluh juta. Jadi nilai impornya satu koma lima dua delapan miliar rupiah. PPN Impor seratus enam puluh delapan koma satu juta dan PPh Pasal dua puluh dua tiga puluh delapan koma dua juta, sehingga total PDRI dua ratus enam koma tiga juta. Total pungutannya enam ratus empat puluh lima koma dua juta rupiah. |
| 4 | `porsi` | 34 detik | Batang komposisi pungutan terhadap nilai pabean (59%) | Dari mana tagihan yang lebih dari separuh harga kain itu? Porsi terbesar adalah BMTP, tiga ratus tiga puluh juta, bea pengaman untuk melindungi industri tekstil dalam negeri. Lalu PPN seratus enam puluh delapan koma satu juta, yang dapat dikreditkan sebagai pajak masukan. Dan PPh Pasal dua puluh dua tiga puluh delapan koma dua juta, yang dikreditkan di SPT Tahunan. Jadi, PDRI sebesar dua ratus enam koma tiga juta itu dapat diperhitungkan kembali oleh importir. |
| 5 | `variasi` | 35 detik | Tiga kartu variasi: tanpa API, lupa BMTP, SKB | Sekarang, tiga variasi. Kalau importir tidak memiliki API, PPh Pasal dua puluh dua menjadi seratus empat belas koma enam juta, dan total PDRI dua ratus delapan puluh dua koma tujuh juta. Kalau petugas lupa memasukkan BMTP, nilai impornya hanya satu koma satu sembilan delapan miliar. PPN menjadi seratus tiga puluh satu koma delapan juta dan PPh tiga puluh juta, keduanya kurang pungut. Dan kalau importir memiliki SKB PPh Pasal dua puluh dua, PDRI-nya hanya PPN, seratus enam puluh delapan koma satu juta. |
| 6 | `q1` | 8 detik | Kuis: total PDRI tanpa API | Sekarang, mari kita cek pemahaman kamu. Berapa total PDRI kalau importir tidak memiliki API, ya? |
| 7 | `salah` | 37 detik | Tabel tiga kesalahan yang sering terjadi | Ada tiga kesalahan yang sering terjadi. Pertama, Bea Masuk atau BMTP tidak dimasukkan ke nilai impor. Akibatnya PPN kurang tiga puluh enam koma tiga juta, dan PPh Pasal dua puluh dua kurang delapan koma dua lima juta. Kedua, DPP sebelas per dua belas dipakai untuk barang mewah. PPN motor Kasus dua jadi kurang lima koma nol delapan juta. Ketiga, tarif PPh Pasal dua puluh dua salah pilih. Importir tanpa API dikenai dua koma lima persen, sehingga PPh-nya kurang tujuh puluh enam koma empat juta. |
| 8 | `q2` | 5 detik | Kuis: temukan kesalahan di lembar hitung | Sekarang, kita cek pemahaman lagi, ya. Coba temukan kesalahan dalam hitungan ini. |
| 9 | `jelaskan` | 54 detik | Empat kartu langkah penjelasan | Lalu, bagaimana menjelaskannya kepada pengguna jasa? Susun dalam empat langkah, paling lama dua menit. Satu, nilai impor: pajak dihitung dari harga kain dalam rupiah ditambah Bea Masuk dan BMTP, sebesar satu koma lima tiga miliar. Dua, PPN Impor seratus enam puluh delapan koma satu juta, yang dapat dikreditkan sebagai pajak masukan di SPT Masa PPN. Tiga, PPh Pasal dua puluh dua tiga puluh delapan koma dua juta, pembayaran di muka yang dapat dikreditkan di SPT Tahunan. Empat, dasar hukumnya: PMK seratus tiga puluh satu Tahun dua ribu dua puluh empat untuk PPN, dan PMK lima puluh satu Tahun dua ribu dua puluh lima untuk PPh Pasal dua puluh dua. Importir pun jadi paham bahwa sistem di Indonesia itu adil dan transparan. |
| 10 | `hak` | 20 detik | Baru di v3. Kartu pertanyaan staf, lalu kartu jawaban hak keberatan dengan tenggat 60 hari | Kadang, pengguna jasa tetap tidak setuju. Kalau saya tidak setuju, saya harus ke mana? Tutup dengan haknya, dari materi ketujuh: Bapak, Ibu, dapat mengajukan keberatan kepada Direktur Jenderal Bea dan Cukai melalui Portal DJBC, paling lambat enam puluh hari sejak tanggal penetapan. |
| 11 | `layanan` | 19 detik | Empat kartu kriteria penjelasan | Penjelasan yang baik memenuhi empat hal. Angkanya tepat: semua komponen benar. Dasar hukumnya disebut tanpa diminta. Bahasanya awam, dan selesai dalam dua menit. Dan sikapnya tenang saat ditanya balik, serta tahu kapan mengarahkan pengguna jasa ke DJP. |
| 12 | `empat` | 33 detik | Empat pertanyaan kasus dan jawabannya | Selama delapan sesi ini, Anda sudah menjawab empat pertanyaan kasus. Atas dasar apa negara memungut? Undang-undang, sesuai Pasal dua puluh tiga A Undang-Undang Dasar seribu sembilan ratus empat puluh lima. Siapa yang memungut? DJBC di pelabuhan, dengan tiga sistem pemungutan yang bekerja bersama. Apakah PPN Impor hilang? Tidak, PPN dikreditkan sebagai pajak masukan. Mengapa PPh dipungut sebelum kain terjual? Karena PPh Pasal dua puluh dua Impor adalah cicilan di muka. |
| 13 | `wrap` | 20 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. Hitung dari nilai impor, yaitu nilai pabean ditambah Bea Masuk dan BMTP. Waspadai tiga kesalahan yang sering terjadi: nilai impor, DPP barang mewah, dan tarif PPh Pasal dua puluh dua. Jelaskan dalam empat langkah, dengan bahasa awam dan dasar hukum yang jelas. |
| 14 | `final1` | 5 detik | Lomba hitung: tiga variasi dan urutan penjelasan | Nah, ini latihan terakhir, ya. Coba kamu kerjakan hitungan berikut ini. |
| 15 | `finish` | 14 detik | Kartu selesai kursus | Selamat, sobat, seluruh materi PDRI sudah selesai. Terakhir, tuliskan refleksi Anda di Paspor Misi: satu hal yang paling berguna, dan satu kesalahan yang ingin Anda hindari. Sampai jumpa di meja layanan! |

Anda boleh memperbaiki kalimat saat merekam, seperti di bab sebelumnya. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
