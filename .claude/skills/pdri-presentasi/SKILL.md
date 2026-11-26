---
name: pdri-presentasi
description: Build the PDRI (pdri-mck) chapter presentations — one self-contained HTML file per bab that merges all its scene pages into a slide deck WITHOUT voice-over, every animation playing by itself when a slide opens (timing compressed, not synced to VO), with only ‹ › navigation, full screen and a sidebar of scene thumbnails — and verify them. Use when the user asks for "presentasi bab N", "satukan HTML per adegan jadi presentasi", "deck/slide HTML bab N", or to rebuild the presentations after a chapter's index.html, pictures or timings changed.
---

# PDRI presentation per bab (HTML deck, no voice-over)

Output: `dist/pdri/presentasi/babN-<slug-of-title>.html`, one file, offline, ~0.8–1.3 MB (fonts, pictures and
thumbnails inlined; no audio). Approved design (2026-11-26): Bab 1 mockup, then Bab 2–8 the same way.

## What the deck is
- Source: `site/pdri-mck/chNN/index.html` + `site/pdri-mck/lib/*` + `chNN/audio/id/timings.js` (marks only). Same
  per-beat split as `tools/pdri/scenes/build_scenes.py` (one beat = one slide, `lead: false` predecessors pre-run).
- **No voice-over:** every beat's TIMINGS becomes `silent: true` (wall clock), cues emptied, and its marks compressed in
  order: first step ≤ `FIRST` 0.6 s, each next step ≤ `GAP` 1.0 s after the previous, hold ≤ `TAIL` 1.2 s after the last
  mark. Offsets in the chapter code (`m('ask') + 1.4`) stay as written. Tune those three constants in `build_deck.py`
  if the user wants faster/slower.
- Each slide is an `about:srcdoc` iframe whose document is assembled in the browser from shared parts stored once.
  Inside it, the engine's cover, control bar (`#bar`), captions, sound note and home link are hidden, the stage fills
  the frame (`--k` = fit to 1600×900), and the cover is clicked automatically once `boot()` ran → animation starts.
- Engine patches (string `must()` replacements, fail loudly if engine.js changes): volume.js loader removed,
  `new URL('../', location.href)` → constant (srcdoc has no hierarchical URL), and `m()` no longer throws for a beat
  flagged `auto` (below). Also hidden: the finish card's "Semua bab" link (`.finwrap a.btn.quiet`), which led nowhere.
- **Stale timings.js:** a beat in index.html that timings.js lacks (happened once: ch03 `syarat`, `rina`, fixed on main 26 Nov — the site lesson
  itself errors there) gets `{marks: {}, auto: true}`; each mark it asks for is placed, on first use, at
  `FIRST + GAP * n`. The build prints a `warning:` line per such beat — tell the user, the lesson in `site/` needs its
  timings regenerated (skill `pdri-build-chapter`), the deck does not.
- Shell (`tools/pdri/scenes/deck_shell.html`): one bottom bar — chapter + scene name, **‹ n / N ›**, sidebar toggle,
  full screen. Sidebar (left) lists every scene with its end-frame thumbnail. Keys: → / PgDn next, ← / PgUp previous
  (also presenter clickers), G sidebar, F full screen, Esc closes sidebar. While a question is open in a slide, the
  arrows belong to the question (PgDn / the › button still move). `#N` in the URL opens scene N. In full screen the
  bar fades out until the pointer moves.
- Questions (Cek pemahaman, Latihan bab, finish card) stay interactive; those slides end in `waiting`.

## Build
From the repo root (Chromium headless may crash here: use installed Chrome):
```
export PYTHONUTF8=1 PW_CHANNEL=chrome
for n in 1 2 3 4 5 6 7 8; do python tools/pdri/scenes/build_deck.py $n; done      # --no-thumbs to skip screenshots
```
Thumbnails = Playwright screenshot of each slide at `?beat=0&t=999`, 480×270 JPEG.

## Verify (every deck you build)
```
python .claude/skills/pdri-presentasi/scripts/check_deck.py dist/pdri/presentasi/babN-*.html <scratch-dir>
```
Plays every slide to its end; prints `end`, `[t, done, waiting]` per slide; fails on page/console errors, missing
thumbnails, a slide that never starts, or a wrong `#N`. Then **look at** `<scratch-dir>/<name>-sheet.jpg` (end frame of
every slide): no empty slide, nothing clipped, numbers/text present. Slide count must equal the chapter's BEATS count
(`dist/pdri/html/babN` may be older than `site/`; trust `site/`).

## Commit
Stage only `tools/pdri/scenes/build_deck.py`, `tools/pdri/scenes/deck_shell.html`, `dist/pdri/presentasi/*.html`
and this skill. Commit/push only when the user asks; branch first (`claude/pdri-presentasi...`), PR to main.
