# Struktur Output untuk Chapter 3

## Output yang Diminta

1. **SCORM package** - Package SCORM yang siap digunakan
2. **HTML file per scene** - File HTML terpisah untuk setiap scene
3. **PDF fullscreen** - Dokumen PDF dalam format fullscreen

## Struktur Direktori Output

```
ozone-papermorph/
└── site/
    └── pdri-mck/
        └── ch03/
            └── outputs/
                ├── scorm/
                │   ├── imsmanifest.xml
                │   ├── index.html
                │   ├── audio/
                │   ├── lib/
                │   └── ... (semua file SCORM)
                ├── html-per-scene/
                │   ├── scene_01_intro.html
                │   ├── scene_02_ask.html
                │   ├── scene_03_sistem.html
                │   ├── scene_04_alur.html
                │   ├── scene_05_q1.html
                │   ├── scene_06_jenis.html
                │   ├── scene_07_syarat.html
                │   ├── scene_08_rina.html
                │   ├── scene_09_hukum.html
                │   ├── scene_10_hierarki.html
                │   ├── scene_11_peran.html
                │   ├── scene_12_identitas.html
                │   ├── scene_13_q2.html
                │   ├── scene_14_wrap.html
                │   ├── scene_15_final1.html
                │   └── scene_16_finish.html
                └── pdf-fullscreen/
                    └── chapter_3_fullscreen.pdf
```

## Catatan

- SCORM package akan dibuat menggunakan struktur standar SCORM 1.2
- HTML per scene akan diekstrak dari index.html utama
- PDF fullscreen akan dibuat dari konten utama chapter 3

---
*Dokumen ini dibuat untuk memastikan semua output sesuai dengan yang diminta*
