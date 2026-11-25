# Papermorph (vendored)

Folder ini adalah salinan sebagian dari [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) (lisensi MIT, lihat `LICENSE`). Salinan ini dipakai untuk membangun buku PDRI, terutama paket SCORM dengan tracking interaksi.

- **Basis upstream:** commit `839a62c` ("Merge pull request #40 from titulartarantula/shown-spoken").
- **Yang disalin:** `engine/`, `.claude/` (skill `papermorph`), `img/readme/`, `README.md`, `AGENTS.md`, `LICENSE`, `.gitattributes`, `.gitignore`.
- **Yang tidak disalin:** `site/` (29 buku demo, ±786 MB), `.github/`, `.opencode/`, dan riwayat git upstream. Ketiganya diabaikan lewat `.gitignore` root.

## Perubahan lokal terhadap upstream

| File | Perubahan |
|---|---|
| `.claude/skills/papermorph/assets/scorm/scorm-bridge.js` | Menghubungkan `window.onInteraction` dari engine ke `cmi.interactions`. Hook dipasang begitu `finishCard` tersedia. Laporan `progress()` ditunda sampai skor bab tercatat, sehingga tidak ada status `failed` palsu. |
| `.claude/skills/papermorph/assets/scorm/scorm-host.js` | Menulis record `cmi.interactions` untuk SCORM 1.2 dan 2004. |
| `.claude/skills/papermorph/assets/scorm/test/check_interactions.py` | File baru: uji end-to-end `cmi.interactions` di mock LMS. |

Buku PDRI memakai engine yang sudah disalin ke `site/pdri-mck/lib/engine.js`. Engine itu memanggil `window.onInteraction`.

## Memperbarui dari upstream

Riwayat git upstream disimpan di luar repo, di `../papermorph-upstream.git` (folder `.git` asli clone ini). Bandingkan dan tarik perubahan dengan:

```sh
G=../papermorph-upstream.git
git --git-dir=$G --work-tree=Papermorph fetch origin
git --git-dir=$G --work-tree=Papermorph diff HEAD origin/main -- engine .claude   # tinjau dulu
git --git-dir=$G --work-tree=Papermorph merge origin/main                         # pertahankan perubahan lokal di atas
```

Kalau folder itu tidak ada (misalnya di mesin lain), clone ulang upstream ke folder terpisah, salin `engine/` dan `.claude/` yang baru, lalu terapkan kembali perubahan lokal di tabel atas. Setelah itu perbarui commit basis di file ini.
