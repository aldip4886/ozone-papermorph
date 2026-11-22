# Naskah Voice Over Bab 2 PDRI

Nov 22, 2026 · @John

## Cara kerja

Bab 2 memakai 14 file suara pendek, satu per adegan, sama seperti Bab 1. Gaya bahasanya mengikuti rekaman Bab 1 Anda: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan.

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan Bab 1.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti Bab 1 (jam di nama file sudah cukup), atau pakai kode adegan, misalnya `intro.wav`, `ask.wav`.
5. Kirim ke-14 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata (misalnya "dua puluh tiga A") supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan Bab 1 agar warna suaranya konsisten antarbab. Prompt ini sama dengan Bab 1, ditambah cara membaca istilah Belanda dan Inggris di bab ini.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu" atau "ya"), nadanya lebih santai dan bersahabat. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum nama teori atau asas.
Kutipan: kalimat dari Pasal 23A UUD 1945 dibaca sedikit lebih pelan dan tegas, seperti membacakan pasal.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: UUD (u-u-de), UU KUP (u-u ka-u-pe), DPR (de-pe-er), PPN (pe-pe-en), PPh (pe-pe-ha), BMTP (be-em-te-pe), API (a-pe-i), PMK (pe-em-ka), PDRI (pe-de-er-i), PNBP (pe-en-be-pe), DJBC (de-je-be-ce).
Istilah Belanda: budgetair dibaca "bud-zhe-ter", regulerend dibaca "re-khu-le-rent".
Istilah Inggris dibaca dengan lafal Inggris yang wajar: equality, certainty, convenience, economy, The Wealth of Nations, Adam Smith.
Penekanan: beri tekanan ringan pada nama sudut pandang (hukum, fungsi, teori pembenaran, asas pemungutan, pembeda pungutan) dan pada frasa "tanpa imbalan secara langsung".
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 14 adegan, sekitar 5 menit 16 detik dengan suara draf Ardi. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 7 detik | Judul bab, lima ikon sudut pandang mengelilingi tanda tanya | Mari kita lanjutkan ya. Pada materi kedua ini, kita akan membahas mengapa negara boleh memungut pajak, dari lima sudut pandang. |
| 2 | `ask` | 24 detik | Kartu pertanyaan staf importir; lima ikon sudut pandang muncul satu per satu | Di materi pertama, staf PT Kain Prima Nusantara bertanya dari mana angka tagihannya. Kali ini, pertanyaannya lebih mendasar. Kenapa kami harus bayar? Kami kan tidak mendapat imbalan langsung. Untuk menjawabnya, kita pakai lima sudut pandang: hukum, fungsi, teori pembenaran, asas pemungutan, dan pembeda pungutan. |
| 3 | `hukum` | 21 detik | Kutipan Pasal 23A; rantai DPR dan Presiden → undang-undang → wewenang memaksa | Kita mulai dari sudut pandang hukum. Pasal dua puluh tiga A UUD seribu sembilan ratus empat puluh lima menyatakan, pajak dan pungutan lain yang bersifat memaksa untuk keperluan negara diatur dengan undang-undang. DPR dan Presiden menetapkan kewajiban pajak dalam undang-undang. Karena itu, negara berwenang memaksa importir membayar. |
| 4 | `unsur` | 31 detik | Lima kartu unsur pajak; unsur keempat disorot emas | Lalu, apa sebenarnya pajak itu? Pasal satu angka satu UU KUP memberi definisinya, dan dari situ kita dapat lima unsur pajak. Pertama, kontribusi wajib kepada negara. Kedua, terutang oleh orang pribadi atau badan. Ketiga, bersifat memaksa berdasarkan undang-undang. Keempat, tanpa imbalan secara langsung. Kelima, digunakan untuk keperluan negara, bagi sebesar-besarnya kemakmuran rakyat. |
| 5 | `q1` | 7 detik | Kuis pilihan: mana yang bukan unsur pajak | Sekarang, mari kita cek pemahaman kamu. Mana yang bukan unsur pajak, ya? |
| 6 | `fungsi` | 38 detik | Budgetair (alur ke kas negara) dan regulerend (BMTP, batang PPh 22 dengan/tanpa API) | Sudut pandang kedua, fungsi pajak. Pertama, fungsi budgetair, atau penerimaan. PPN dan PPh Pasal dua puluh dua atas kain tadi masuk ke kas negara untuk membiayai belanja negara. Kedua, fungsi regulerend, atau mengatur. Pemerintah memakai pungutan untuk mengatur kegiatan ekonomi. BMTP melindungi industri tekstil dalam negeri. Tarif PPh Pasal dua puluh dua tanpa API, tujuh koma lima persen, juga lebih tinggi daripada dengan API, dua koma lima persen. Jadi, importir terdorong untuk memiliki API. |
| 7 | `teori` | 43 detik | Tabel lima teori: inti dan bacaan atas Kasus 1 | Sudut pandang ketiga, teori pembenaran. Ada lima teori yang menjelaskan mengapa negara berhak memungut pajak. Teori asuransi: negara melindungi rakyat, dan pajak menjadi semacam premi, misalnya untuk menjaga jalur perdagangan dan pelabuhan. Teori kepentingan: importir memakai pelabuhan, jalan, dan layanan kepabeanan, jadi ikut menanggung bebannya. Teori daya pikul: importir yang sanggup membeli kain satu miliar rupiah dianggap mampu memikul pajaknya. Teori bakti: membayar pajak adalah wujud bakti warga kepada negara. Dan teori daya beli: PPN atas kain akhirnya ditanggung pembeli kemeja, lalu kembali dalam bentuk layanan publik. |
| 8 | `asas` | 42 detik | Empat kartu asas Adam Smith dengan contoh Kasus 1 | Sudut pandang keempat, asas pemungutan. Adam Smith, dalam The Wealth of Nations, mengajukan empat asas. Equality: pajak adil sesuai kemampuan, misalnya tarif yang sama untuk importir dengan kondisi yang sama. Certainty: pajak harus pasti. Tarif PPh Pasal dua puluh dua tercantum dalam PMK lima puluh satu Tahun dua ribu dua puluh lima. Convenience: pajak dipungut pada saat yang paling memudahkan. PDRI dibayar bersamaan dengan Bea Masuk. Economy: biaya pemungutan harus lebih kecil daripada penerimaan. DJBC memungut PDRI dalam satu dokumen dan satu pembayaran. |
| 9 | `wilayah` | 23 detik | Tiga kartu: domisili, sumber, kebangsaan | Ada juga asas yang mengaitkan pajak dengan wilayah dan kewarganegaraan. Asas domisili: negara memajaki penduduknya atas seluruh penghasilan, dari dalam maupun luar negeri. Asas sumber: negara memajaki penghasilan yang bersumber di wilayahnya, siapa pun penerimanya. Dan asas kebangsaan, yang mengaitkan pengenaan pajak dengan kewarganegaraan. |
| 10 | `pembeda` | 36 detik | Tabel pajak, retribusi, PNBP, Bea Masuk: imbalan dan dasar | Sudut pandang kelima, pembeda pungutan. Tidak semua pungutan negara adalah pajak. Pajak, seperti PPN dan PPh, tidak memberi imbalan langsung dan berdasar undang-undang. Retribusi memberi imbalan langsung atas jasa, berdasar peraturan daerah, misalnya retribusi parkir. PNBP juga memberi imbalan langsung atas layanan, misalnya biaya paspor. Bea Masuk sama seperti pajak: tanpa imbalan langsung, berdasar UU Kepabeanan. Cukai juga pungutan berdasar undang-undang, dan dibahas di modul tersendiri. |
| 11 | `q2` | 7 detik | Kuis kelompokkan: imbalan langsung atau tidak | Sekarang, kita cek pemahaman lagi, ya. Kelompokkan setiap pungutan ini. |
| 12 | `wrap` | 20 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. Pasal dua puluh tiga A UUD seribu sembilan ratus empat puluh lima dan UU KUP menjadi dasar hukum pemungutan pajak. Pajak memiliki fungsi budgetair dan regulerend. Teori pembenaran dan asas pemungutan membantu Anda menjelaskan kepada pengguna jasa mengapa suatu pungutan adil. |
| 13 | `final1` | 7 detik | Latihan bab: empat soal | Nah, sekarang kita latihan, ya. Coba kamu jawab latihan berikut ini. |
| 14 | `finish` | 9 detik | Kartu selesai | Bagus, materi kedua selesai. Berikutnya, kita bahas siapa saja yang terlibat, dan bagaimana sistem pemungutan pajaknya. |

Anda boleh memperbaiki kalimat saat merekam, seperti di Bab 1. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
