# Naskah Voice Over Bab 6 PDRI

Nov 22, 2026 · @John

## Cara kerja

Bab 6 memakai 15 file suara pendek, satu per adegan, sama seperti bab sebelumnya. Gaya bahasanya tetap: "Anda" saat menjelaskan, "kamu" dan "ya" saat mengajak latihan, dan pembuka "Mari kita lanjutkan, ya, sobat".

1. Buka Google AI Studio, menu **Generate speech** (Gemini TTS), mode **Single-speaker audio**.
2. Tempel **prompt gaya** di bawah ke kolom Style instructions, lalu pilih suara yang sama dengan bab sebelumnya.
3. Untuk setiap baris tabel naskah, tempel kolom Teks, klik Run, dengarkan, lalu unduh.
4. Beri nama file berurutan seperti sebelumnya (jam di nama file sudah cukup).
5. Kirim ke-15 file di thread ini. Saya pasang, transkripsi, dan selaraskan subtitle serta animasinya.

Angka di kolom Teks sengaja ditulis dengan kata supaya pelafalannya pasti. Di subtitle, angka tetap tampil sebagai angka.

## Prompt untuk Google AI Studio

Pakai model dan suara yang sama dengan bab sebelumnya. Prompt ini sama dengan Bab 5, ditambah lafal istilah baru di bab ini.

Tempel teks ini ke kolom Style instructions:

```markdown
Bacakan naskah berikut dalam bahasa Indonesia baku dengan logat Indonesia yang netral.
Peran: instruktur Bea dan Cukai yang ramah dan berwibawa, menjelaskan kepada pegawai baru di kelas e-learning.
Nada: tenang, jelas, meyakinkan, sedikit hangat. Saat kalimat mengajak latihan (memakai kata "kamu", "ya", atau "sobat"), nadanya lebih santai dan bersahabat. Bukan gaya iklan, bukan gaya berita.
Tempo: sedang, sedikit lebih lambat dari percakapan biasa, sekitar 140 kata per menit. Saat membacakan tarif, rumus, dan angka rupiah, perlambat sedikit.
Jeda: jeda pendek setelah koma dan titik dua, jeda sekitar setengah detik setelah titik, dan jeda sedikit lebih panjang sebelum hasil perhitungan.
Angka: ucapkan angka persis seperti tertulis dalam kata.
Singkatan dibaca per huruf: PPN (pe-pe-en), PPh (pe-pe-ha), PDRI (pe-de-er-i), PIB (pe-i-be), DJP (de-je-pe), DJBC (de-je-be-ce), PMK (pe-em-ka), PKP (pe-ka-pe), SKB (es-ka-be), UU (u-u), UU PPN (u-u pe-pe-en), CV (se-ve), CIF (si-ai-ef), CBU (si-bi-yu), cc (se-se). PPnBM dibaca pe-pe-en-be-em. API-U dibaca a-pe-i u.
Istilah: regulerend dibaca re-gu-le-rend.
Penekanan: beri tekanan ringan pada "barang mewah", "tidak dapat dikreditkan", "tidak dipungut", "dibebaskan", dan hasil akhir setiap perhitungan.
Jangan menambah, mengurangi, atau mengubah kata apa pun dari naskah.
```

Bila suara terlalu cepat atau datar, ubah satu baris saja (misalnya tempo) lalu ulangi adegan yang sama.

## Naskah per adegan

Total 15 adegan, sekitar 4 menit 50 detik dengan suara draf Ardi. Tempel kolom Teks apa adanya; rekaman Anda boleh sedikit lebih panjang atau pendek karena animasi akan saya selaraskan ulang.

| No | Kode file | Durasi draf | Layar | Teks |
| --- | --- | --- | --- | --- |
| 1 | `intro` | 12 detik | Judul bab; ikon PPnBM di tengah, motor besar, SKB, dan lainnya mengelilinginya | Mari kita lanjutkan, ya, sobat. Pada materi keenam ini, kita menghitung PDRI atas barang mewah, dan melihat bagaimana fasilitas mengubah jumlah yang dibayar. |
| 2 | `ask` | 21 detik | Kartu Kasus 2 CV Roda Jaya; "lebih dari 2× nilai pabean" | Kali ini kita pakai Kasus dua. CV Roda Jaya, importir dengan API-U dan berstatus PKP, mengimpor satu unit sepeda motor CBU seribu cc, dengan nilai CIF dua puluh ribu dolar Amerika. Nanti kita akan lihat, total pungutannya lebih dari dua kali nilai pabeannya. Mengapa bisa sebesar itu? |
| 3 | `mewah` | 23 detik | Kain (beban 11%) dibandingkan motor besar (beban 12%) | Mulai dari PPN. Di materi keempat, kain kita memakai dasar pengenaan sebelas per dua belas dari nilai impor, jadi bebannya sebelas persen. Barang yang tergolong mewah berbeda. PPN-nya dua belas persen dari nilai impor penuh, tanpa sebelas per dua belas. Ini juga diatur dalam PMK seratus tiga puluh satu Tahun dua ribu dua puluh empat. |
| 4 | `ppnbm` | 24 detik | Tiga kartu ciri PPnBM | Selain PPN, barang mewah dikenai PPnBM, atau Pajak Penjualan atas Barang Mewah. UU PPN mengenakan PPnBM atas penyerahan dan impor barang yang tergolong mewah, di samping PPN. PPnBM dikenakan satu kali saja, yaitu saat impor atau saat penyerahan oleh pabrikan. Dan berbeda dengan PPN, PPnBM tidak dapat dikreditkan. |
| 5 | `tarifbm` | 25 detik | Batang tarif PPnBM motor: 60% dan 95% | Tarif dan kelompok barangnya diatur dalam peraturan pelaksanaan. Untuk kendaraan bermotor, berlaku PMK seratus empat puluh satu Tahun dua ribu dua puluh satu, yang diubah dengan PMK empat puluh dua Tahun dua ribu dua puluh dua. Sepeda motor dua ratus lima puluh sampai lima ratus cc dikenai PPnBM enam puluh persen dari nilai impor. Sepeda motor di atas lima ratus cc dikenai sembilan puluh lima persen. |
| 6 | `q1` | 8 detik | Kuis: tarif PPnBM motor Kasus 2 | Sekarang, mari kita cek pemahaman kamu. Berapa tarif PPnBM untuk motor CV Roda Jaya, ya? |
| 7 | `hitung` | 42 detik | Tabel hitung Kasus 2 sampai total pungutan Rp739.997.800 | Mari kita hitung Kasus dua. Nilai pabeannya dua puluh ribu dolar dikali kurs delapan belas ribu seratus lima puluh lima rupiah, yaitu tiga ratus enam puluh tiga koma satu juta rupiah. Bea Masuknya empat puluh persen, jadi seratus empat puluh lima koma dua empat juta. Nilai impornya lima ratus delapan koma tiga empat juta rupiah. Dari nilai impor itu, PPN dua belas persen sebesar enam puluh satu juta, PPnBM sembilan puluh lima persen sebesar empat ratus delapan puluh dua koma sembilan juta, dan PPh Pasal dua puluh dua sepuluh persen sebesar lima puluh koma delapan juta. Total PDRI-nya lima ratus sembilan puluh empat koma delapan juta, dan total pungutannya tujuh ratus empat puluh juta rupiah. |
| 8 | `regul` | 18 detik | Batang nilai pabean vs total pungutan (2,04×); kartu regulerend dan daya pikul | Total pungutan tujuh ratus empat puluh juta rupiah itu lebih dari dua kali nilai pabean motornya. Untuk menjelaskannya, ingat fungsi regulerend: pajak dipakai untuk mengatur konsumsi barang mewah. Dan teori daya pikul: pembeli motor besar dianggap mampu memikul beban pajak yang lebih tinggi. |
| 9 | `fasilitas` | 34 detik | Tiga kartu: SKB PPh 22, PPN tidak dipungut, PPN dibebaskan | Sekarang, fasilitas. Fasilitas mengubah jumlah yang dibayar, jadi periksa dokumennya sebelum menghitung. Surat Keterangan Bebas, atau SKB, PPh Pasal dua puluh dua dari DJP membuat PPh Pasal dua puluh dua tidak dipungut, misalnya karena wajib pajak mengalami kerugian fiskal atau lebih bayar. PPN tidak dipungut berarti PPN tetap terutang tetapi tidak dibayar, dan pajak masukannya tetap dapat dikreditkan. PPN dibebaskan berarti PPN tidak dibayar, tetapi pajak masukannya tidak dapat dikreditkan. |
| 10 | `skb` | 22 detik | Batang PDRI Kasus 1 tanpa fasilitas vs dengan SKB | Contohnya begini. Tanpa fasilitas, PDRI Kasus satu terdiri atas PPN Impor dan PPh Pasal dua puluh dua, totalnya dua ratus enam koma tiga juta rupiah. Kalau PT Kain Prima Nusantara memiliki SKB PPh Pasal dua puluh dua yang berlaku, PDRI-nya hanya PPN Impor, yaitu seratus enam puluh delapan koma satu juta rupiah. |
| 11 | `q2` | 7 detik | Kuis: pajak masukan mana yang dapat dikreditkan | Sekarang, kita cek pemahaman lagi, ya. Pajak masukan mana yang masih dapat dikreditkan? |
| 12 | `jawab` | 22 detik | Pertanyaan Kasus 2 dijawab dalam tiga poin | Jadi, mengapa pungutan motor ini begitu besar? Karena motor ini barang mewah: PPN-nya dua belas persen penuh, ditambah PPnBM sembilan puluh lima persen. PPnBM tidak dapat dikreditkan, jadi benar-benar menjadi beban. Tujuannya mengatur konsumsi barang mewah, sesuai fungsi regulerend dan teori daya pikul. |
| 13 | `wrap` | 19 detik | Tiga kartu rangkuman | Jadi, ini rangkumannya. Untuk barang mewah, PPN-nya dua belas persen dikali nilai impor, ditambah PPnBM sesuai tarifnya. PPnBM tidak dapat dikreditkan. Fasilitas mengubah jumlah yang dibayar, jadi periksa dokumen fasilitas sebelum menghitung. |
| 14 | `final1` | 7 detik | Latihan bab: Temukan Kesalahan, hitung selisih, dan efek SKB | Nah, sekarang kita latihan, ya. Coba kamu temukan kesalahan dalam hitungan berikut ini. |
| 15 | `finish` | 9 detik | Kartu selesai | Bagus, materi keenam selesai. Berikutnya, kita bahas barang kiriman, lewat dua paket belanja daring milik Dita. |

Anda boleh memperbaiki kalimat saat merekam, seperti di bab sebelumnya. Saya akan mentranskripsi rekaman Anda dan menyesuaikan subtitle serta waktu animasi dari suara itu.
