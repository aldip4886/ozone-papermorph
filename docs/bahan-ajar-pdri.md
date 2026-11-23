# Bahan Ajar Memahami dan Menghitung Pajak dalam Rangka Impor (PDRI)

Pelatihan untuk Pegawai Baru Direktorat Jenderal Bea dan Cukai

Versi 1, 21 November 2026

## Informasi Bahan Ajar

| Komponen | Keterangan |
| --- | --- |
| Judul | Memahami dan Menghitung Pajak dalam Rangka Impor (PDRI) |
| Sasaran | Pegawai baru DJBC yang akan bertugas di kantor pelayanan dan pelabuhan |
| Durasi | 8 jam pelajaran (JP) x 45 menit, terbagi atas Bagian I (JP 1 sampai 4) dan Bagian II (JP 5 sampai 8) |
| Prasyarat | Materi kepabeanan dasar, Bea Masuk, nilai pabean, dan kurs |
| Dokumen acuan | Outline materi v2, session plan v2, dan analisis arsitektur pengetahuan (folder `docs/`) |
| Status data | Tarif, kurs, dan status peraturan diperiksa per 20 sampai 21 November 2026 |

## Petunjuk Penggunaan

1. Baca bahan ajar ini sesuai urutan kegiatan belajar. Urutan ini mengikuti rantai prasyarat: Anda perlu menguasai nilai impor sebelum menghitung PPN, PPnBM, dan PPh Pasal 22 Impor.
2. Kerjakan setiap contoh hitung dengan kalkulator atau spreadsheet, kemudian cocokkan hasil Anda dengan kunci di bagian akhir.
3. Sebelum menghitung, centang daftar **Cek Dulu Sebelum Hitung**:
   - [ ] Status importir: memiliki API atau tidak, berstatus PKP atau tidak.
   - [ ] Jenis barang: tergolong mewah atau tidak, tercantum dalam lampiran PMK 51/2025 atau tidak.
   - [ ] Aturan dan kurs: peraturan yang dipakai masih berlaku dan kurs sesuai minggu berjalan.
4. Isi Paspor Misi setelah setiap kegiatan belajar. Fasilitator memberi stempel jika Anda sudah menjawab pertanyaan kasus.
5. Angka bertanda **(cek)** masih berupa asumsi untuk keperluan latihan. Sebelum dipakai dalam pekerjaan, cocokkan angka itu dengan BTKI, INSW, atau peraturan yang berlaku.

## Tujuan Pembelajaran

Setelah mengikuti pelatihan, Anda mampu:

1. menghitung nilai impor dari data nilai pabean, Bea Masuk, dan BMTP;
2. menjelaskan dasar negara memungut pajak dengan memakai minimal dua sudut pandang (hukum, fungsi, teori pembenaran, atau asas);
3. membedakan sistem *official assessment*, *self assessment*, dan *withholding*, serta peran DJBC dan DJP dalam PDRI;
4. menjelaskan mekanisme pajak keluaran dan pajak masukan, lalu menghitung PPN Impor barang tidak mewah;
5. menjelaskan PPh Pasal 22 Impor sebagai kredit pajak, memilih tarifnya, dan menghitungnya;
6. menghitung PPN Impor dan PPnBM Impor barang mewah serta menerapkan Surat Keterangan Bebas PPh Pasal 22;
7. menghitung pungutan atas barang kiriman dan membandingkannya dengan impor umum;
8. menemukan kesalahan dalam perhitungan PDRI dan menjelaskan tagihan kepada pengguna jasa secara jelas dan santun.

## Peta Materi

Materi ini memuat tiga jenis pengetahuan, dan masing-masing dipelajari dengan cara yang berbeda.

| Jenis pengetahuan | Isi | Cara Anda mempelajarinya |
| --- | --- | --- |
| Pengetahuan berjenjang | Nilai impor, PPN, PPnBM, PPh Pasal 22, fasilitas, barang kiriman; konsep sistem pemungutan, mekanisme pajak masukan, dan *withholding* | Ikuti urutannya. Kuasai satu langkah sebelum pindah ke langkah berikutnya. |
| Pengetahuan sudut pandang | Pengertian dan fungsi pajak, teori pembenaran, asas pemungutan, perbedaan pajak dengan pungutan lain, peran para pihak | Pakai setiap sudut pandang untuk membaca kasus. Urutannya boleh berbeda. |
| Kecakapan kerja | Menjelaskan tagihan kepada pengguna jasa; kecermatan memeriksa data dan aturan | Latih berulang di setiap kegiatan belajar. |

Rantai perhitungan PDRI yang Anda pelajari:

```
Data dari materi lain: nilai pabean (CIF x kurs), Bea Masuk, BMTP
        ↓
Nilai impor = nilai pabean + Bea Masuk + bea masuk tambahan
        ↓
   ┌────────────┬─────────────┬──────────────┐
PPN Impor    PPnBM Impor   PPh Pasal 22 Impor
   └────────────┴─────────────┴──────────────┘
        ↓
Fasilitas dan pengecualian (SKB, tidak dipungut, dibebaskan)
        ↓
Barang kiriman (ketentuan khusus)
```

## Kasus yang Dipakai

Kurs untuk semua kasus memakai Keputusan Menteri Keuangan Nomor 55/MK/EF.2/2026 yang berlaku 18 sampai 24 November 2026: **Rp18.155 per USD** ([fiskal.kemenkeu.go.id](https://fiskal.kemenkeu.go.id/informasi-publik/kurs-pajak?date=2026-11-20)).

**Kasus 1. Kain tenunan kapas.** PT Kain Prima Nusantara (API-U, PKP) mengimpor 100.000 meter kain tenunan polos dari kapas, berat tidak lebih dari 100 g/m², pos tarif 5208.21.00, dengan nilai CIF USD 60.000. Pos tarif ini dikenai Bea Masuk Tindakan Pengamanan (BMTP) tahun pertama Rp3.300 per meter berdasarkan [PMK 98 Tahun 2025](https://jdih.kemenkeu.go.id/dok/pmk-98-tahun-2025). Tarif Bea Masuk MFN 10% **(cek)**.

**Kasus 2. Sepeda motor besar CBU.** CV Roda Jaya (API-U, PKP) mengimpor 1 unit sepeda motor CBU 1.000 cc, pos 8711.50, dengan nilai CIF USD 20.000. Tarif Bea Masuk MFN 40% **(cek)**, tarif PPh Pasal 22 10% **(cek)**.

**Kasus 3. Paket belanja daring.** Dita, mahasiswi di Bekasi, menerima dua paket melalui Perusahaan Jasa Titipan: earbuds (FOB USD 30, CIF USD 40) dan sepatu sneakers (FOB USD 80, CIF USD 95).

**Skenario pembuka.** Pada hari pertama Anda bertugas di Tanjung Priok, staf PT Kain Prima Nusantara datang ke meja layanan. Perusahaannya baru mengimpor kain senilai sekitar Rp1,09 miliar dan harus membayar pungutan sekitar Rp645 juta. Ia bertanya, "Pak, Bu, hitungan ini dari mana? Pungutannya lebih dari separuh harga kain kami." Selama delapan JP, Anda menyusun jawaban untuk pertanyaan itu.

Empat pertanyaan kasus yang akan Anda jawab:

1. Atas dasar apa negara boleh memungut semua ini? (Kegiatan Belajar 2)
2. Siapa yang memungut, dan dengan cara apa? (Kegiatan Belajar 3)
3. Importir sudah membayar PPN Rp168 juta. Apakah uang itu hilang begitu saja? (Kegiatan Belajar 4)
4. Kain belum terjual, mengapa PPh sudah dipungut di pelabuhan? (Kegiatan Belajar 5)

# BAGIAN I. MEMAHAMI SAMBIL MULAI MENGHITUNG

## Kegiatan Belajar 1. Hari Pertama di Pelabuhan (JP 1)

### Tujuan

Anda mampu menyebutkan komponen pungutan impor dan menghitung nilai impor dari data kasus.

### 1.1 Komponen Pungutan Impor

Saat barang masuk ke daerah pabean, importir membayar dua kelompok pungutan.

Kelompok pertama adalah pungutan kepabeanan: Bea Masuk dan bea masuk tambahan seperti BMTP, bea masuk antidumping, dan bea masuk imbalan. Anda sudah mempelajarinya di materi kepabeanan, jadi di sini angkanya diberikan sebagai data kasus.

Kelompok kedua adalah pajak dalam rangka impor (PDRI), yaitu pajak yang dipungut DJBC pada saat impor:

| Jenis | Dasar hukum utama | Keterangan singkat |
| --- | --- | --- |
| PPN Impor | UU PPN, PMK 131 Tahun 2024 | Dikenakan atas impor Barang Kena Pajak oleh siapa pun |
| PPnBM Impor | UU PPN, PMK 141/PMK.010/2021 (untuk kendaraan bermotor) | Dikenakan hanya atas barang yang tergolong mewah |
| PPh Pasal 22 Impor | UU PPh, PMK 51 Tahun 2025 | Pembayaran di muka atas PPh importir |

Impor barang kena cukai juga dapat menimbulkan cukai, yang dibahas dalam modul tersendiri.

### 1.2 Nilai Impor sebagai Dasar Perhitungan

UU PPN mendefinisikan nilai impor sebagai nilai berupa uang yang menjadi dasar penghitungan bea masuk ditambah pungutan berdasarkan ketentuan peraturan perundang-undangan kepabeanan dan cukai, tidak termasuk PPN dan PPnBM. PMK 51 Tahun 2025 memakai nilai impor yang sama sebagai dasar PPh Pasal 22 Impor.

Rumusnya:

```
Nilai impor = Nilai pabean (Rp) + Bea Masuk + bea masuk tambahan (misalnya BMTP)
```

Kesalahan pada nilai impor terbawa ke PPN, PPnBM, dan PPh Pasal 22, jadi periksa angka ini sebelum menghitung pajak lainnya.

### 1.3 Contoh Hitung: Nilai Impor Kasus 1

| Langkah | Perhitungan | Hasil |
| --- | --- | --- |
| 1. Nilai pabean dalam Rupiah | USD 60.000 x Rp18.155 | Rp1.089.300.000 |
| 2. Bea Masuk MFN **(cek, 10%)** | 10% x Rp1.089.300.000 | Rp108.930.000 |
| 3. BMTP | 100.000 m x Rp3.300 | Rp330.000.000 |
| 4. Nilai impor | Rp1.089.300.000 + Rp108.930.000 + Rp330.000.000 | **Rp1.528.230.000** |

### 1.4 Latihan 1

Hitung nilai impor jika PT Kain Prima Nusantara hanya mengimpor 50.000 meter kain yang sama dengan nilai CIF USD 30.000. Data lain tidak berubah.

### 1.5 Rangkuman

- PDRI terdiri atas PPN Impor, PPnBM Impor, dan PPh Pasal 22 Impor.
- Bea Masuk dan bea masuk tambahan termasuk pungutan kepabeanan dan menjadi bagian dari nilai impor.
- Semua PDRI dihitung dari nilai impor. Periksa nilai impor lebih dahulu.

## Kegiatan Belajar 2. Dasar Negara Memungut Pajak (JP 2)

### Tujuan

Anda mampu menjelaskan dasar pemungutan pajak atas Kasus 1 dengan memakai minimal dua sudut pandang.

### 2.1 Sudut Pandang Hukum

Pasal 23A UUD 1945 menyatakan: "Pajak dan pungutan lain yang bersifat memaksa untuk keperluan negara diatur dengan undang-undang." DPR dan Presiden menetapkan kewajiban pajak dalam undang-undang, sehingga negara berwenang memaksa importir membayar.

Pasal 1 angka 1 UU Ketentuan Umum dan Tata Cara Perpajakan (UU KUP) mendefinisikan pajak sebagai kontribusi wajib kepada negara yang terutang oleh orang pribadi atau badan, bersifat memaksa berdasarkan undang-undang, tanpa imbalan secara langsung, dan digunakan untuk keperluan negara bagi sebesar-besarnya kemakmuran rakyat.

Dari definisi itu, Anda dapat menarik lima unsur pajak:

1. kontribusi wajib kepada negara;
2. terutang oleh orang pribadi atau badan;
3. bersifat memaksa berdasarkan undang-undang;
4. tanpa imbalan secara langsung;
5. digunakan untuk keperluan negara.

### 2.2 Sudut Pandang Fungsi

| Fungsi | Pengertian | Contoh di Kasus 1 |
| --- | --- | --- |
| *Budgetair* (penerimaan) | Pajak mengisi kas negara untuk membiayai belanja negara | PPN dan PPh Pasal 22 atas kain masuk ke kas negara |
| *Regulerend* (mengatur) | Pemerintah memakai pajak dan pungutan untuk mengatur kegiatan ekonomi | BMTP melindungi industri tekstil dalam negeri; tarif PPh Pasal 22 tanpa API (7,5%) lebih tinggi daripada dengan API (2,5%) |

### 2.3 Sudut Pandang Teori Pembenaran

Beberapa teori menjelaskan mengapa negara berhak memungut pajak.

| Teori | Inti pemikiran | Bacaan atas Kasus 1 |
| --- | --- | --- |
| Teori asuransi | Negara melindungi rakyat; pajak menjadi semacam premi | Negara menjaga keamanan jalur perdagangan dan pelabuhan tempat kain masuk |
| Teori kepentingan | Beban pajak dibagi sesuai kepentingan setiap orang atas layanan negara | Importir memakai pelabuhan, jalan, dan layanan kepabeanan |
| Teori daya pikul | Beban pajak disesuaikan dengan kemampuan membayar | Importir yang sanggup membeli kain Rp1 miliar dianggap mampu memikul pajak |
| Teori bakti | Warga membayar pajak sebagai wujud bakti kepada negara | Membayar pajak adalah kewajiban warga negara |
| Teori daya beli | Pajak menarik daya beli dari masyarakat untuk dikembalikan dalam bentuk layanan publik | PPN atas kain pada akhirnya ditanggung pembeli kemeja dan kembali dalam bentuk belanja negara |

### 2.4 Sudut Pandang Asas Pemungutan

Adam Smith dalam *The Wealth of Nations* (1776) mengajukan empat asas:

| Asas | Pengertian | Contoh |
| --- | --- | --- |
| *Equality* | Pajak dikenakan secara adil sesuai kemampuan | Tarif yang sama untuk importir dengan kondisi yang sama |
| *Certainty* | Pajak harus pasti: subjek, objek, tarif, dan waktu pembayaran | Tarif PPh Pasal 22 tercantum dalam PMK 51 Tahun 2025 |
| *Convenience* | Pajak dipungut pada saat yang paling memudahkan wajib pajak | PDRI dibayar bersamaan dengan Bea Masuk |
| *Economy* | Biaya pemungutan harus lebih kecil daripada penerimaan | DJBC memungut PDRI dalam satu dokumen dan satu pembayaran |

Asas lain mengaitkan pajak dengan wilayah dan kewarganegaraan:

- Asas domisili: negara memajaki penduduknya atas seluruh penghasilan, dari dalam maupun luar negeri.
- Asas sumber: negara memajaki penghasilan yang bersumber di wilayahnya, siapa pun penerimanya.
- Asas kebangsaan: negara mengaitkan pengenaan pajak dengan kewarganegaraan.

### 2.5 Sudut Pandang Pembeda Pungutan

| Pungutan | Imbalan | Dasar | Contoh |
| --- | --- | --- | --- |
| Pajak | Tidak langsung | Undang-undang | PPN, PPh |
| Retribusi | Langsung, atas jasa yang diterima | Peraturan daerah | Retribusi parkir |
| Penerimaan Negara Bukan Pajak (PNBP) | Langsung, atas layanan atau pemanfaatan sumber daya | UU PNBP dan peraturan pelaksanaannya | Biaya layanan paspor |
| Bea Masuk | Tidak langsung | UU Kepabeanan | Bea Masuk atas kain |

Cukai juga pungutan negara berdasarkan undang-undang dan dibahas di modul tersendiri.

### 2.6 Aktivitas: Debat Lima Menit

Kelas terbagi menjadi dua kubu. Kubu A mendukung pengenaan BMTP dan PPN atas kain impor. Kubu B menolaknya. Setiap kubu wajib menyebut minimal satu sudut pandang dari Kegiatan Belajar ini.

### 2.7 Latihan 2

1. Sebutkan lima unsur pajak menurut Pasal 1 angka 1 UU KUP.
2. Jelaskan BMTP kain dengan memakai sudut pandang fungsi dan satu asas Adam Smith.
3. PPh Pasal 22 Kasus 1 dengan API sebesar Rp38.205.750. Tanpa API, jumlahnya Rp114.617.250. Fungsi pajak apa yang terlihat dari perbedaan tersebut?

### 2.8 Rangkuman

- Pasal 23A UUD 1945 dan UU KUP menjadi dasar hukum pemungutan pajak.
- Pajak memiliki fungsi *budgetair* dan *regulerend*.
- Teori pembenaran dan asas pemungutan membantu Anda menjelaskan kepada pengguna jasa mengapa suatu pungutan adil.

## Kegiatan Belajar 3. Pihak dan Sistem Pemungutan (JP 3)

### Tujuan

Anda mampu membedakan tiga sistem pemungutan pajak dan menunjukkan peran setiap pihak dalam satu Pemberitahuan Impor Barang (PIB).

### 3.1 Tiga Sistem Pemungutan

| Sistem | Pihak yang menentukan besarnya pajak | Contoh dalam Kasus 1 |
| --- | --- | --- |
| *Official assessment* | Petugas pajak atau fiskus | Pejabat DJBC meneliti PIB dan dapat menetapkan kekurangan pembayaran |
| *Self assessment* | Wajib pajak sendiri | Importir menghitung sendiri Bea Masuk dan PDRI dalam PIB |
| *Withholding* | Pihak ketiga yang ditunjuk undang-undang | DJBC memungut PPh Pasal 22 Impor atas penghasilan importir |

Sistem utama di Indonesia adalah *self assessment*. Dalam impor, ketiganya berjalan bersama: importir menghitung, DJBC meneliti, dan DJBC juga memungut PPh Pasal 22.

### 3.2 Jenis-Jenis Pajak

| Dasar pembagian | Jenis | Contoh |
| --- | --- | --- |
| Lembaga pemungut | Pajak pusat | PPN, PPnBM, PPh, Bea Meterai |
| | Pajak daerah | Pajak kendaraan bermotor, pajak hotel |
| Pihak yang menanggung | Pajak langsung | PPh |
| | Pajak tidak langsung | PPN, PPnBM |
| Sifat | Pajak subjektif | PPh (memperhatikan keadaan wajib pajak) |
| | Pajak objektif | PPN (memperhatikan objeknya) |

### 3.3 Peta Dasar Hukum

| Peraturan | Status per November 2026 |
| --- | --- |
| UU 6/1983 tentang KUP | Terakhir diubah dengan UU 6/2023 tentang Penetapan Perppu 2/2022 tentang Cipta Kerja |
| UU 7/1983 tentang PPh | Terakhir diubah dengan UU 6/2023 |
| UU 8/1983 tentang PPN dan PPnBM | Terakhir diubah dengan UU 6/2023; UU 7/2021 tentang Harmonisasi Peraturan Perpajakan (HPP) menetapkan tarif PPN 12% paling lambat 1 Januari 2025 |
| UU 10/1995 tentang Kepabeanan | Diubah dengan UU 17/2006 |

Urutan peraturan yang Anda temui dalam pekerjaan: Undang-Undang, Peraturan Pemerintah, Peraturan Menteri Keuangan (PMK), lalu Peraturan Direktur Jenderal. Peraturan yang lebih rendah tidak boleh bertentangan dengan peraturan yang lebih tinggi.

### 3.4 Pembagian Peran

| Pihak | Peran dalam PDRI |
| --- | --- |
| Importir | Menghitung dan membayar Bea Masuk dan PDRI, mengisi PIB |
| PPJK | Mengurus pemenuhan kewajiban kepabeanan atas kuasa importir |
| DJBC | Meneliti PIB, memungut PDRI, menetapkan kekurangan pembayaran |
| Bank persepsi atau bank devisa | Menerima pembayaran pungutan negara |
| DJP | Mengadministrasikan pengkreditan PPN dan PPh Pasal 22 dalam SPT importir |
| Konsumen akhir | Menanggung PPN pada akhir rantai penjualan |

Saat melayani, Anda akan sering memeriksa identitas importir: NPWP atau NIK, Angka Pengenal Importir (API-U atau API-P), dan status Pengusaha Kena Pajak (PKP). Data ini terhubung dengan Coretax, sistem administrasi perpajakan DJP.

### 3.5 Aktivitas: Siapa Saya?

Setiap kelompok menerima kartu peran: importir, PPJK, petugas DJBC, bank devisa, DJP, dan konsumen. Pasangkan setiap kartu dengan sistem pemungutan dan instansi yang tepat, lalu presentasikan hasilnya dalam satu menit.

### 3.6 Latihan 3

1. Importir mengisi sendiri nilai PPN dalam PIB, kemudian petugas meneliti PIB tersebut. Sebutkan sistem pemungutan yang bekerja pada setiap langkah.
2. Jelaskan perbedaan peran DJBC dan DJP atas PPN Impor yang dibayar PT Kain Prima Nusantara.

### 3.7 Rangkuman

- Dalam impor, *self assessment*, *official assessment*, dan *withholding* berjalan bersama.
- DJBC memungut PDRI di pelabuhan; DJP mengadministrasikan pengkreditannya.

## Kegiatan Belajar 4. Pajak Pertambahan Nilai Impor (JP 4)

### Tujuan

Anda mampu menjelaskan mekanisme pajak keluaran dan pajak masukan, lalu menghitung PPN Impor barang tidak mewah.

### 4.1 Ciri PPN

- PPN adalah pajak atas konsumsi barang dan jasa di dalam daerah pabean.
- PPN termasuk pajak tidak langsung: penjual atau importir menyetor, konsumen akhir menanggung.
- PPN dikenakan pada setiap tahap penyerahan, tetapi hanya atas pertambahan nilai, sehingga tidak menimbulkan pajak berganda.

### 4.2 Objek dan Subjek

Pasal 4 ayat (1) UU PPN menetapkan impor Barang Kena Pajak sebagai objek PPN. PPN Impor dipungut dari siapa pun yang mengimpor, baik PKP maupun bukan PKP.

Pengusaha Kena Pajak (PKP) adalah pengusaha yang melakukan penyerahan Barang Kena Pajak atau Jasa Kena Pajak yang dikenai pajak berdasarkan UU PPN.

### 4.3 Tarif dan Dasar Pengenaan Pajak

UU HPP menetapkan tarif PPN 12% paling lambat 1 Januari 2025. PMK 131 Tahun 2024 mengatur cara penerapannya:

| Jenis barang | Dasar Pengenaan Pajak (DPP) | Rumus | Beban efektif |
| --- | --- | --- | --- |
| Tidak tergolong mewah | Nilai lain: 11/12 x nilai impor | 12% x 11/12 x nilai impor | 11% |
| Tergolong mewah (dikenai PPnBM) | Nilai impor | 12% x nilai impor | 12% |

Per 10 September 2026, Menteri Keuangan menyatakan belum ada penurunan tarif PPN, sehingga PMK 131 Tahun 2024 masih berlaku saat bahan ajar ini disusun.

### 4.4 Mekanisme Pajak Keluaran dan Pajak Masukan

Pajak keluaran (PK) adalah PPN yang dipungut PKP saat menjual barang. Pajak masukan (PM) adalah PPN yang dibayar PKP saat membeli atau mengimpor barang. Setiap masa pajak, PKP menghitung PK dikurangi PM:

- Jika PK lebih besar daripada PM, PKP menyetor selisihnya (kurang bayar).
- Jika PM lebih besar daripada PK, terjadi lebih bayar, dan PKP dapat meminta pengembalian atau mengompensasikannya.

PIB beserta bukti pembayarannya berkedudukan sama dengan faktur pajak. Importir PKP dapat mengkreditkan PPN Impor sebagai pajak masukan.

### 4.5 Aktivitas: Estafet PPN

Ikuti perjalanan kain Kasus 1 sampai menjadi kemeja. Angka berikut disederhanakan untuk latihan dan memakai beban efektif 11%.

| Pos | Harga jual (sebelum PPN) | PK | PM | Disetor |
| --- | --- | --- | --- | --- |
| Importir kain (impor) | - | - | Rp168.105.300 (PPN Impor) | - |
| Importir menjual ke konveksi | Rp1.800.000.000 | Rp198.000.000 | Rp168.105.300 | Rp29.894.700 |
| Konveksi menjual ke toko | Rp2.500.000.000 | Rp275.000.000 | Rp198.000.000 | Rp77.000.000 |
| Toko menjual ke pembeli | Rp3.200.000.000 | Rp352.000.000 | Rp275.000.000 | Rp77.000.000 |
| **Jumlah yang masuk ke kas negara** | | | | **Rp352.000.000** |

Total setoran sama dengan PPN yang dibayar pembeli akhir (Rp168.105.300 + Rp29.894.700 + Rp77.000.000 + Rp77.000.000 = Rp352.000.000). Pembeli akhir yang menanggung PPN, sedangkan para pengusaha hanya menyetorkannya.

### 4.6 Contoh Hitung: PPN Impor Kasus 1

| Langkah | Perhitungan | Hasil |
| --- | --- | --- |
| Cek dulu | Kain tidak tergolong mewah; importir PKP | DPP nilai lain 11/12 |
| Nilai impor | Lihat Kegiatan Belajar 1 | Rp1.528.230.000 |
| PPN Impor | 12% x 11/12 x Rp1.528.230.000 | **Rp168.105.300** |

### 4.7 Latihan 4

1. Hitung PPN Impor untuk varian 50.000 meter (Latihan 1).
2. Staf importir bertanya, "PPN Rp168 juta ini hilang begitu saja?" Tulis jawaban Anda dalam maksimal tiga kalimat.

### 4.8 Rangkuman

- PPN Impor dikenakan atas impor Barang Kena Pajak oleh siapa pun.
- Barang tidak mewah: 12% x 11/12 x nilai impor. Barang mewah: 12% x nilai impor.
- Importir PKP mengkreditkan PPN Impor sebagai pajak masukan. Konsumen akhir menanggung PPN.

# BAGIAN II. MENGHITUNG, MEMERIKSA, MENJELASKAN

## Kegiatan Belajar 5. Pajak Penghasilan Pasal 22 Impor (JP 5)

### Tujuan

Anda mampu menjelaskan PPh Pasal 22 Impor sebagai kredit pajak, memilih tarif yang tepat, dan menghitungnya.

### 5.1 Pelunasan PPh dalam Tahun Berjalan

Menurut UU PPh, wajib pajak dapat melunasi sebagian PPh sebelum tahun pajak berakhir melalui:

| Jenis | Mekanisme |
| --- | --- |
| PPh Pasal 21 | Pemotongan oleh pemberi kerja atas penghasilan pegawai |
| PPh Pasal 22 | Pemungutan oleh pihak tertentu, termasuk atas impor |
| PPh Pasal 23 | Pemotongan atas dividen, bunga, royalti, sewa, dan jasa tertentu |
| PPh Pasal 25 | Angsuran bulanan oleh wajib pajak sendiri |

Pihak yang membayar penghasilan melakukan pemotongan. Pihak yang ditunjuk atas transaksi tertentu, seperti impor, melakukan pemungutan. Keduanya termasuk *withholding*.

### 5.2 Ketentuan PPh Pasal 22 Impor

Ketentuan terbaru ada dalam [PMK 51 Tahun 2025](https://jdih.kemenkeu.go.id/dok/pmk-51-tahun-2025), berlaku sejak 1 Agustus 2025:

- Pemungut: DJBC dan bank devisa.
- Dasar pemungutan: nilai impor.
- Saat terutang: bersamaan dengan pembayaran Bea Masuk.
- Sifat: tidak final. Importir memperhitungkan PPh Pasal 22 Impor sebagai kredit pajak dalam SPT Tahunan PPh.

### 5.3 Tarif PPh Pasal 22 Impor

| Kondisi | Tarif | Dasar |
| --- | --- | --- |
| Importir memiliki API | 2,5% | Nilai impor |
| Importir tidak memiliki API | 7,5% | Nilai impor |
| Kedelai, gandum, dan tepung terigu, importir memiliki API | 0,5% | Nilai impor |
| Barang tertentu yang tercantum dalam lampiran PMK 51 Tahun 2025 | 10% atau 7,5% sesuai lampiran | Nilai impor |
| Emas batangan | 0,25% | Nilai impor |
| Barang yang tidak dikuasai | 7,5% | Harga jual lelang |

Urutan pemeriksaan tarif:

```
Barang tercantum di lampiran PMK 51/2025? → Ya: pakai tarif lampiran
        ↓ Tidak
Barang kedelai, gandum, terigu, atau emas batangan? → Ya: pakai tarif khusus
        ↓ Tidak
Importir memiliki API? → Ya: 2,5% / Tidak: 7,5%
```

### 5.4 Contoh Hitung: PPh Pasal 22 Impor Kasus 1

| Langkah | Perhitungan | Hasil |
| --- | --- | --- |
| Cek dulu | Pos 52 tidak tercantum dalam daftar tarif 10% lampiran PMK 51/2025; importir memiliki API-U | Tarif 2,5% |
| Nilai impor | Lihat Kegiatan Belajar 1 | Rp1.528.230.000 |
| PPh Pasal 22 Impor | 2,5% x Rp1.528.230.000 | **Rp38.205.750** |

Catatan: daftar tarif 7,5% dalam lampiran PMK 51 Tahun 2025 untuk pos 52 masih perlu dicocokkan **(cek)**.

### 5.5 Alur Uang PPh Pasal 22

```
PIB diajukan → importir membayar PDRI bersama Bea Masuk → dana masuk kas negara
→ DJBC melaporkan hasil pemungutan → importir mengkreditkan PPh Pasal 22 dalam SPT Tahunan
```

### 5.6 Latihan 5: Pilih Tarifmu

Tentukan tarif PPh Pasal 22 Impor untuk setiap skenario.

| No | Skenario |
| --- | --- |
| 1 | PT A (API-U) mengimpor kain kapas |
| 2 | CV B (tanpa API) mengimpor kain kapas |
| 3 | PT C (API-P) mengimpor gandum untuk pabrik tepung |
| 4 | PT D (API-U) mengimpor emas batangan |
| 5 | Barang tidak dikuasai yang dilelang DJBC |
| 6 | PT E (API-U) mengimpor barang yang tercantum dalam daftar 10% lampiran PMK 51/2025 |
| 7 | PT F (API-U) mengimpor kedelai |
| 8 | PT G (tanpa API) mengimpor kedelai |

### 5.7 Rangkuman

- PPh Pasal 22 Impor adalah pembayaran di muka atas PPh importir dan tidak bersifat final.
- Periksa lampiran PMK 51 Tahun 2025 lebih dahulu, kemudian jenis barang khusus, lalu status API.
- Tarif tanpa API lebih tinggi, tetapi importir tetap dapat mengkreditkannya, jadi dampaknya terutama pada arus kas.

## Kegiatan Belajar 6. Barang Mewah dan Fasilitas (JP 6)

### Tujuan

Anda mampu menghitung PDRI atas barang mewah dan menerapkan fasilitas atau pengecualian.

### 6.1 PPN Impor Barang Mewah

Barang yang tergolong mewah dikenai PPN 12% dengan DPP nilai impor, tanpa DPP nilai lain 11/12 (PMK 131 Tahun 2024).

### 6.2 Pajak Penjualan atas Barang Mewah (PPnBM)

- UU PPN mengenakan PPnBM atas penyerahan dan impor barang yang tergolong mewah, selain PPN.
- PPnBM dikenakan satu kali, yaitu saat impor atau saat penyerahan oleh pabrikan.
- PPnBM tidak dapat dikreditkan.
- Tarif dan kelompok barang ditetapkan dalam peraturan pelaksanaan. Untuk kendaraan bermotor berlaku PMK 141/PMK.010/2021 sebagaimana diubah PMK 42/PMK.010/2022:

| Kendaraan | Tarif PPnBM | Dasar |
| --- | --- | --- |
| Sepeda motor 250 cc sampai 500 cc | 60% | Nilai impor |
| Sepeda motor lebih dari 500 cc | 95% | Nilai impor |

### 6.3 Contoh Hitung: Kasus 2

Lembar kerja memuat langkah Kasus 1 sebagai contoh. Kerjakan Kasus 2 berpasangan, lalu cocokkan dengan tabel berikut.

| Langkah | Perhitungan | Hasil |
| --- | --- | --- |
| Cek dulu | Sepeda motor 1.000 cc tergolong mewah; importir API-U, PKP | PPN 12% penuh, PPnBM 95% |
| Nilai pabean | USD 20.000 x Rp18.155 | Rp363.100.000 |
| Bea Masuk **(cek, 40%)** | 40% x Rp363.100.000 | Rp145.240.000 |
| Nilai impor | Rp363.100.000 + Rp145.240.000 | Rp508.340.000 |
| PPN Impor | 12% x Rp508.340.000 | Rp61.000.800 |
| PPnBM Impor | 95% x Rp508.340.000 | Rp482.923.000 |
| PPh Pasal 22 **(cek, 10%)** | 10% x Rp508.340.000 | Rp50.834.000 |
| **Total PDRI** | | **Rp594.757.800** |
| **Total pungutan** | Bea Masuk + PDRI | **Rp739.997.800** |

Total pungutan atas motor ini lebih dari dua kali nilai pabeannya. Untuk menjelaskan angka sebesar itu, pakai fungsi *regulerend* dan teori daya pikul.

### 6.4 Fasilitas dan Pengecualian

| Fasilitas | Pengertian | Akibat dalam PIB |
| --- | --- | --- |
| Surat Keterangan Bebas (SKB) PPh Pasal 22 | DJP membebaskan wajib pajak tertentu dari pemungutan PPh Pasal 22, misalnya karena mengalami kerugian fiskal atau lebih bayar | PPh Pasal 22 tidak dipungut |
| PPN tidak dipungut | PPN terutang, tetapi tidak dipungut berdasarkan ketentuan tertentu | PPN tercatat, tidak dibayar; pajak masukan terkait tetap dapat dikreditkan |
| PPN dibebaskan | Impor dibebaskan dari pengenaan PPN berdasarkan ketentuan tertentu | PPN tidak dibayar; pajak masukan terkait tidak dapat dikreditkan |

Misalnya, jika PT Kain Prima Nusantara memiliki SKB PPh Pasal 22 yang berlaku, PDRI Kasus 1 hanya PPN Impor Rp168.105.300.

### 6.5 Latihan 6: Temukan Kesalahan

Seorang petugas menghitung PPN motor Kasus 2 sebagai berikut: 12% x 11/12 x Rp508.340.000 = Rp55.917.400. Tunjukkan kesalahannya dan hitung selisihnya.

### 6.6 Rangkuman

- Barang mewah: PPN 12% x nilai impor ditambah PPnBM sesuai tarif.
- PPnBM tidak dapat dikreditkan.
- Fasilitas mengubah jumlah yang dibayar, jadi periksa dokumen fasilitas sebelum menghitung.

## Kegiatan Belajar 7. Barang Kiriman (JP 7)

### Tujuan

Anda mampu menghitung pungutan atas barang kiriman dan menjelaskan perbedaannya dengan impor umum.

### 7.1 Dasar Hukum

Barang kiriman diatur dalam PMK 96 Tahun 2023 tentang ketentuan kepabeanan, cukai, dan pajak atas impor dan ekspor barang kiriman, sebagaimana telah beberapa kali diubah, terakhir dengan PMK 4 Tahun 2025 ([JDIH Kemenkeu](https://jdih.kemenkeu.go.id/dok/pmk-4-tahun-2025/summary)). PMK 4 Tahun 2025 antara lain melonggarkan ketentuan untuk barang kiriman jemaah haji dan hadiah perlombaan atau penghargaan internasional.

### 7.2 Ketentuan Pungutan

Ketentuan umum berdasarkan [FAQ barang kiriman Kanwil DJBC Aceh](https://kanwilaceh.beacukai.go.id/mandatory/faq-barang-kiriman.html) dan [laman barang kiriman DJBC](https://www.beacukai.go.id/barangkiriman):

| Nilai FOB per kiriman | Bea Masuk | PPh | PPN |
| --- | --- | --- | --- |
| Sampai USD 3 | Dibebaskan | Dikecualikan | 12% x 11/12 (efektif 11%) |
| Lebih dari USD 3 sampai USD 1.500 | 7,5% | Dikecualikan | 12% x 11/12 (efektif 11%) |
| Lebih dari USD 1.500 | Tarif umum | Tarif umum | Tarif umum |

Delapan kelompok komoditas dikenai tarif yang berbeda dari 7,5%, antara lain tas, produk tekstil, alas kaki, sepeda, jam tangan, kosmetik, besi dan baja, serta buku. Untuk latihan, alas kaki dihitung dengan BM 25% dan PPh 5% **(cek)**. Cocokkan dengan tabel resmi DJBC sebelum kelas.

### 7.3 Perbedaan dengan Impor Umum

| Aspek | Impor umum | Barang kiriman |
| --- | --- | --- |
| Dokumen | PIB | Consignment Note (CN) atau PIBK |
| Pihak yang mengurus | Importir atau PPJK | Perusahaan Jasa Titipan (PJT) atau penyelenggara pos |
| Tarif Bea Masuk | Sesuai BTKI | Tarif tunggal 7,5% untuk FOB lebih dari USD 3 sampai USD 1.500, kecuali komoditas tertentu |
| PPh Pasal 22 | Sesuai PMK 51 Tahun 2025 | Dikecualikan untuk FOB sampai USD 1.500, kecuali komoditas tertentu |

### 7.4 Contoh Hitung: Kasus 3

| Komponen | Paket A: earbuds | Paket B: sepatu sneakers |
| --- | --- | --- |
| FOB / CIF | USD 30 / USD 40 | USD 80 / USD 95 |
| Nilai pabean | USD 40 x Rp18.155 = Rp726.200 | USD 95 x Rp18.155 = Rp1.724.725 |
| Bea Masuk | 7,5% = Rp54.465 | 25% **(cek)** = Rp431.181 |
| Nilai impor | Rp780.665 | Rp2.155.906 |
| PPN (12% x 11/12) | Rp85.873 | Rp237.150 |
| PPh | Dikecualikan | 5% **(cek)** = Rp107.795 |
| **Total pungutan** | **Rp140.338** | **Rp776.126** |

Angka belum dibulatkan. Pembulatan mengikuti ketentuan pengisian dokumen.

### 7.5 Latihan 7

1. Dita bertanya, "Saya beli sepatu sekitar Rp1,7 juta, mengapa tagihannya hampir Rp780 ribu?" Jelaskan dalam tiga kalimat, termasuk kaitannya dengan perlindungan industri alas kaki dalam negeri.
2. Jika Dita hanya membeli tali sepatu dengan FOB USD 2, pungutan apa saja yang ia bayar?

### 7.6 Rangkuman

- Barang kiriman memakai ketentuan khusus berdasarkan nilai FOB dan jenis komoditas.
- Untuk FOB lebih dari USD 3 sampai USD 1.500, berlaku BM 7,5% dan PPh dikecualikan, kecuali komoditas tertentu.
- PPN tetap dipungut dengan beban efektif 11%.

## Kegiatan Belajar 8. Menjawab Staf Importir (JP 8)

### Tujuan

Anda mampu menghitung ulang Kasus 1 beserta variasinya, menemukan kesalahan hitung, dan menjelaskan tagihan kepada pengguna jasa.

### 8.1 Jawaban Lengkap Kasus 1

| Komponen | Perhitungan | Jumlah |
| --- | --- | --- |
| Nilai pabean | USD 60.000 x Rp18.155 | Rp1.089.300.000 |
| Bea Masuk **(cek, 10%)** | 10% x Rp1.089.300.000 | Rp108.930.000 |
| BMTP | 100.000 m x Rp3.300 | Rp330.000.000 |
| Nilai impor | NP + BM + BMTP | Rp1.528.230.000 |
| PPN Impor | 12% x 11/12 x Rp1.528.230.000 | Rp168.105.300 |
| PPh Pasal 22 Impor | 2,5% x Rp1.528.230.000 | Rp38.205.750 |
| **Total PDRI** | PPN + PPh 22 | **Rp206.311.050** |
| **Total pungutan** | BM + BMTP + PDRI | **Rp645.241.050** |

### 8.2 Lomba Hitung: Tiga Variasi

1. Importir ternyata tidak memiliki API.
2. Petugas lupa memasukkan BMTP ke dalam nilai impor.
3. Importir memiliki SKB PPh Pasal 22 yang berlaku.

### 8.3 Kesalahan yang Sering Terjadi

| No | Kesalahan | Contoh | Dampak |
| --- | --- | --- | --- |
| 1 | BM atau BMTP tidak dimasukkan ke nilai impor | Nilai impor Kasus 1 ditulis Rp1.198.230.000 | PPN kurang Rp36.300.000; PPh Pasal 22 kurang Rp8.250.000 |
| 2 | DPP 11/12 dipakai untuk barang mewah | PPN motor Kasus 2 ditulis Rp55.917.400 | PPN kurang Rp5.083.400 |
| 3 | Tarif PPh Pasal 22 salah pilih | Importir tanpa API dikenai 2,5% | PPh Pasal 22 kurang Rp76.411.500 |

### 8.4 Menjelaskan Tagihan kepada Pengguna Jasa

Susun penjelasan Anda dalam empat langkah, maksimal dua menit:

1. Nilai impor: "Pajak dihitung dari nilai impor, yaitu harga kain dalam Rupiah ditambah Bea Masuk dan BMTP, sebesar Rp1,53 miliar."
2. PPN: "PPN Impor Rp168,1 juta. Karena perusahaan Bapak/Ibu PKP, jumlah ini dapat dikreditkan sebagai pajak masukan di SPT Masa PPN."
3. PPh Pasal 22: "PPh Pasal 22 Rp38,2 juta adalah pembayaran di muka atas PPh perusahaan dan dapat dikreditkan di SPT Tahunan."
4. Dasar hukum: "Perhitungan ini berdasarkan PMK 131 Tahun 2024 untuk PPN dan PMK 51 Tahun 2025 untuk PPh Pasal 22."

Kriteria penilaian:

| Aspek | Awal | Berkembang | Cakap | Mahir |
| --- | --- | --- | --- | --- |
| Ketepatan angka | Lebih dari dua komponen salah | Dua komponen salah | Satu komponen salah atau semua benar dengan bantuan | Semua komponen benar tanpa bantuan |
| Dasar hukum | Tidak menyebut dasar hukum | Menyebut setelah diminta | Menyebut PMK 131/2024 dan PMK 51/2025 tanpa diminta | Menjelaskan alasan pemakaian aturan tersebut |
| Kejelasan | Membacakan angka dengan istilah teknis | Urutan benar tetapi berbelit | Selesai dalam dua menit dengan bahasa awam | Menjawab keberatan sebelum ditanyakan |
| Sikap layanan | Defensif atau menghindar | Santun tetapi kaku saat ditanya balik | Tenang dan menjawab keberatan | Tetap tenang saat ditekan; tahu kapan mengarahkan ke DJP |

### 8.5 Refleksi

Tuliskan di Paspor Misi:

1. Satu hal yang paling berguna bagi pekerjaan Anda.
2. Satu kesalahan yang Anda buat hari ini dan cara Anda menghindarinya.

## Kunci Jawaban

**Latihan 1.**

| Komponen | Perhitungan | Hasil |
| --- | --- | --- |
| Nilai pabean | USD 30.000 x Rp18.155 | Rp544.650.000 |
| Bea Masuk | 10% x Rp544.650.000 | Rp54.465.000 |
| BMTP | 50.000 m x Rp3.300 | Rp165.000.000 |
| Nilai impor | | **Rp764.115.000** |

**Latihan 2.**
1. Kontribusi wajib kepada negara; terutang oleh orang pribadi atau badan; bersifat memaksa berdasarkan undang-undang; tanpa imbalan langsung; untuk keperluan negara.
2. Contoh jawaban: BMTP menjalankan fungsi *regulerend* karena pemerintah memakainya untuk melindungi industri tekstil dalam negeri. Dari asas *certainty*, tarif dan jangka waktunya tercantum dalam PMK 98 Tahun 2025.
3. Fungsi *regulerend*: pemerintah mendorong importir memiliki API.

**Latihan 3.**
1. Importir menghitung sendiri: *self assessment*. Petugas meneliti dan dapat menetapkan: *official assessment*.
2. DJBC memungut PPN Impor saat barang masuk. DJP mengadministrasikan pengkreditan PPN tersebut dalam SPT Masa PPN importir.

**Latihan 4.**
1. 12% x 11/12 x Rp764.115.000 = **Rp84.052.650**.
2. Contoh jawaban: "Perusahaan Bapak/Ibu dapat mengkreditkan PPN Impor ini sebagai pajak masukan saat menjual kain. Beban PPN berpindah ke pembeli berikutnya sampai ke konsumen akhir."

**Latihan 5.**

| No | Tarif |
| --- | --- |
| 1 | 2,5% |
| 2 | 7,5% |
| 3 | 0,5% |
| 4 | 0,25% |
| 5 | 7,5% dari harga jual lelang |
| 6 | 10% |
| 7 | 0,5% |
| 8 | 7,5% (tarif 0,5% berlaku hanya bagi importir dengan API) |

**Latihan 6.** Motor tergolong barang mewah, sehingga DPP memakai nilai impor tanpa 11/12. PPN yang benar Rp61.000.800. Selisih kurang pungut **Rp5.083.400**.

**Latihan 7.**
1. Contoh jawaban: "Sepatu termasuk komoditas yang dikenai tarif khusus untuk melindungi industri alas kaki dalam negeri. Bea Masuknya 25% dari nilai pabean, ditambah PPN dan PPh. Pungutan untuk earbuds lebih kecil karena earbuds memakai tarif umum barang kiriman 7,5% tanpa PPh."
2. FOB sampai USD 3: Bea Masuk dibebaskan, PPh dikecualikan, Dita membayar PPN saja.

**Lomba hitung 8.2.**
1. Tanpa API: PPh Pasal 22 = 7,5% x Rp1.528.230.000 = Rp114.617.250. Total PDRI Rp282.722.550.
2. BMTP tidak dimasukkan: nilai impor Rp1.198.230.000; PPN Rp131.805.300 (kurang Rp36.300.000); PPh Pasal 22 Rp29.955.750 (kurang Rp8.250.000).
3. SKB PPh Pasal 22: PDRI hanya PPN Rp168.105.300.

## Glosarium

| Istilah | Pengertian |
| --- | --- |
| API | Angka Pengenal Importir, terdiri atas API-U (umum) dan API-P (produsen) |
| BMTP | Bea Masuk Tindakan Pengamanan, bea masuk tambahan untuk melindungi industri dalam negeri dari lonjakan impor |
| CN | Consignment Note, dokumen pemberitahuan pabean untuk barang kiriman |
| DPP | Dasar Pengenaan Pajak |
| Nilai impor | Nilai pabean ditambah Bea Masuk dan pungutan kepabeanan lain, tidak termasuk PPN dan PPnBM |
| PDRI | Pajak dalam rangka impor: PPN Impor, PPnBM Impor, dan PPh Pasal 22 Impor |
| PIB | Pemberitahuan Impor Barang |
| PJT | Perusahaan Jasa Titipan |
| PKP | Pengusaha Kena Pajak |
| SKB | Surat Keterangan Bebas pemungutan PPh Pasal 22 |

## Daftar Referensi dan Status Keberlakuan

Status diperiksa pada 20 sampai 21 November 2026 melalui JDIH Kemenkeu, laman DJP, laman DJBC, dan laman Badan Kebijakan Fiskal.

| Peraturan atau sumber | Pokok yang dipakai | Status |
| --- | --- | --- |
| UUD 1945 Pasal 23A | Dasar konstitusional pajak | Berlaku |
| UU 6/1983 tentang KUP, terakhir diubah UU 6/2023 | Definisi pajak, *self assessment* | Berlaku |
| UU 7/1983 tentang PPh, terakhir diubah UU 6/2023 | Dasar PPh Pasal 22 | Berlaku |
| UU 8/1983 tentang PPN dan PPnBM, terakhir diubah UU 6/2023 | Objek PPN Impor, PK-PM, PPnBM | Berlaku |
| UU 7/2021 tentang HPP | Tarif PPN 12% | Berlaku |
| [UU 10/1995 tentang Kepabeanan, diubah UU 17/2006](https://jdih.kemenkeu.go.id/dok/uu-17-tahun-2006/summary) | Bea Masuk sebagai unsur nilai impor | Berlaku |
| PMK 131 Tahun 2024 ([ringkasan DJP](https://pajak.go.id/en/node/113453)) | PPN 12%, DPP nilai lain 11/12 | Berlaku sejak 1 Januari 2025 |
| [PMK 51 Tahun 2025](https://jdih.kemenkeu.go.id/dok/pmk-51-tahun-2025) ([DJP](https://www.pajak.go.id/en/node/117217)) | Tarif dan saat terutang PPh Pasal 22 Impor | Berlaku sejak 1 Agustus 2025 |
| [PMK 141/PMK.010/2021](https://peraturan.bpk.go.id/Download/175341/141_PMK.010_2021.pdf), diubah PMK 42/PMK.010/2022 | PPnBM kendaraan bermotor | Berlaku |
| [PMK 98 Tahun 2025](https://jdih.kemenkeu.go.id/dok/pmk-98-tahun-2025) | BMTP kain tenunan kapas (data kasus) | Berlaku 10 Januari 2026 sampai 9 Januari 2029 |
| [PMK 96 Tahun 2023](https://jdih.kemenkeu.go.id/dok/pmk-96-tahun-2023), terakhir diubah [PMK 4 Tahun 2025](https://jdih.kemenkeu.go.id/dok/pmk-4-tahun-2025/summary) | Barang kiriman | Berlaku |
| [PMK 26/PMK.010/2022 (BTKI 2022)](https://jdih.kemenkeu.go.id/dok/26-pmk-010-2022/summary), terakhir diubah PMK 68 Tahun 2026 | Tarif Bea Masuk (data kasus) | Berlaku |
| [KMK 55/MK/EF.2/2026](https://fiskal.kemenkeu.go.id/informasi-publik/kurs-pajak?date=2026-11-20) | Kurs Rp18.155 per USD | Berlaku 18 sampai 24 November 2026 |
| [FAQ barang kiriman Kanwil DJBC Aceh](https://kanwilaceh.beacukai.go.id/mandatory/faq-barang-kiriman.html) | Ketentuan pungutan barang kiriman | Diterbitkan 4 September 2025 |
| [Laman barang kiriman DJBC](https://www.beacukai.go.id/barangkiriman) | Tabel tarif barang kiriman | Laman resmi DJBC |

PMK 160/PMK.04/2010 (nilai pabean) dan PMK 34/PMK.010/2017 beserta perubahannya (tarif PPh Pasal 22) sudah dicabut dan tidak dipakai dalam bahan ajar ini.

### Hal yang Perlu Dicek sebelum Kelas

- [ ] Tarif Bea Masuk MFN pos 5208.21.00 (asumsi 10%) dan 8711.50 (asumsi 40%) melalui INSW atau BTKI.
- [ ] Pencantuman pos 52.08 sampai 52.12 dan 87.11 dalam daftar tarif 7,5% atau 10% lampiran PMK 51 Tahun 2025 (motor diasumsikan 10%).
- [ ] Tarif Bea Masuk dan PPh komoditas alas kaki barang kiriman (asumsi BM 25%, PPh 5%) terhadap PMK 96 Tahun 2023 dan perubahannya.
- [ ] Pasal tarif PPnBM sepeda motor terhadap PMK 42/PMK.010/2022.
- [ ] Naskah UU 1 Tahun 2026 (perubahan ketentuan pidana pajak) dan UU 6 Tahun 2026 di JDIH, untuk memastikan tidak ada perubahan pada ketentuan PDRI yang dipakai.
- [ ] Kurs minggu pelaksanaan kelas di fiskal.kemenkeu.go.id.
