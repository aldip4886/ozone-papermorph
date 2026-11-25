---
name: pdri-voiceover
description: Generate real voiceover audio for a PDRI (pdri-mck) chapter beat using the user's own logged-in Google AI Studio session in Chrome, then forced-align it and splice the real timing into the chapter's files. Use this whenever the user asks to "buat voiceover", "generate voiceover", "rekam voiceover", "isi suara yang kosong", or names a bab/chapter + beat that is still silent, for the ozone-papermorph PDRI project. Also use it proactively whenever a chapter's content/pdri-mck/chNN or site/pdri-mck/chNN/audio/id/timings.js shows a beat with "silent": true that needs real audio. Requires claude-in-chrome with the user's browser already open and logged into Google AI Studio.
---

# PDRI voiceover generation

Produces one real, forced-aligned voiceover clip for a PDRI chapter beat (`site/pdri-mck/chNN`)
using Google AI Studio's Generate Speech playground through the user's own Chrome, the way it
was done for `ch04`'s `rina` beat on 2026-11-24. Use this for a single beat or a short list of
beats that are still "silent" (draft/estimated timing, no real recording) — not for bulk-"redo
a whole already-voiced chapter" unless the user explicitly asks for that (re-recording working
beats throws away real audio and is a much bigger ask; confirm first if unsure).

## Before you start

1. Find what actually needs voicing. A beat with `"silent": true` in
   `site/pdri-mck/chNN/audio/id/timings.js` has no real audio yet, even if an mp3 file for it
   exists on disk (old chapters keep a draft TTS mp3 that the engine never plays once `silent`
   is set). Check:
   ```
   python3 -c "
   import json
   d = json.loads(open('site/pdri-mck/chNN/audio/id/timings.js',encoding='utf-8').read().split('=',1)[1].rsplit(';',1)[0])
   for k,v in d.items(): print(k, 'silent=', v.get('silent', False), 'dur=', v.get('dur'))
   "
   ```
2. Get the exact reference text for the beat from `docs/naskah-voiceover/babN-naskah-voiceover.md`
   (the "Teks" column) — that markdown table is the source of truth for what the speaker reads.
   It must also exist, word-for-word, with `[[mark]]` annotations already inserted around the
   points the chapter's animation needs to cue off, in `content/pdri-mck/chNN/narration.id.json`
   under `beats.<beat_id>`. If the beat is brand new (you just added it to the chapter's
   `index.html`), add both — the naskah row and the `[[mark]]`-annotated narration entry — before
   recording anything. The mark names must match the `m('name')` calls the beat's code uses.
3. Load the `claude-in-chrome` skill if its tools aren't already available, then call
   `tabs_context_mcp`. If more than one browser is connected, you must ask the user which one
   (or trigger `switch_browser`) before touching any tab — never guess.

## 1. Set up the Generate Speech playground

Navigate a tab to `https://aistudio.google.com/generate-speech`. If the user said their browser
is "already open and logged in", a fresh navigate in a new MCP tab still carries their session
(cookies are shared across tabs in the same Chrome profile) — you don't need to find their
existing tab.

Click **Create new dialog** to get a single speech block. Open the speaker dropdown
(`Speaker 1 - <default voice>`) and search/select the house voice — **Bodi**, the voice used for
Bab 3 and Bab 4's new beats (`Gemini 3.8 Flash TTS` is normally pre-selected as the model; leave
it). Only use a different voice if the user names one or if a chapter's existing naskah doc says
otherwise — consistency across a chapter's beats matters more than any single voice's quality.

Click the **Style** selector next to the speaker and paste a condensed version of the chapter's
style-instructions block from `docs/naskah-voiceover/babN-naskah-voiceover.md` into the free-text
box (tone, pace ~150 words/min, how to spell out abbreviations relevant to *this* line, which
words to stress). You don't need the full multi-paragraph prompt — a few sentences covering what
actually matters for this specific beat's text is enough.

Click into the main text block, select all (`ctrl+a`) and delete before typing — the block ships
with grey placeholder/example text (`<gasp> That's a great idea! ...`) that is real selectable
content, not a hint, so it must be cleared first. Type the beat's exact text from the naskah
table (no paraphrasing — the naskah is the reference text the alignment step matches against).

Run it (the Run button bottom-right, or Ctrl+Enter). Wait for generation to finish — the
play/pause control and a final duration (e.g. `0:29`) appear once it's done; a few seconds is
normal. Sanity-check the duration against the naskah's estimated "Durasi draf" — they should be
in the same ballpark (TTS at ~150 wpm tracks a word-rate estimate closely).

Click the download icon (circle with a down-arrow, left of the thumbs-up/down) once. It saves a
`.wav` into the user's Downloads folder as `Generated Audio <date> - <time>.wav` — list
`~/Downloads` sorted by mtime to find it rather than guessing the exact name. If you clicked
Download more than once, you'll have duplicate `.wav`s; keep one and delete the rest.

Close the tab (`tabs_close_mcp`) once you have the file — don't leave scratch tabs open.

## 2. Convert to the chapter's existing mp3 format

Chapters don't all use the same encoding — check a sibling beat that already has real audio
before converting, don't assume:
```
ffmpeg -i site/pdri-mck/chNN/audio/id/<some-other-real-beat>.mp3 2>&1 | grep -E "Duration|Audio:"
```
Match its sample rate and bitrate (ch03's real beats are 44.1 kHz/96 kbps; ch04/ch05's are
24 kHz/48 kbps — Gemini TTS's native rate). Then:
```
ffmpeg -y -v error -i "<downloaded>.wav" -ar <rate> -ac 1 -b:a <bitrate> -codec:a libmp3lame \
  site/pdri-mck/chNN/audio/id/<beat>.mp3
```

## 3. Forced-align and splice in the real timing

Run the bundled script — it transcribes with `faster-whisper` (downloads a small model on first
use, CPU int8, a few seconds for a 30s clip), fuzzy-matches the transcript against the
`[[mark]]`-annotated reference text the same way `tools/pdri/vo/align.py` did for Bab 1–3, and
writes the result straight into `site/pdri-mck/chNN/audio/id/timings.js` (replacing any `silent`
placeholder for that beat in place, dropping the `silent`/`forced` flags) and
`content/pdri-mck/chNN/narration.id.timings.json`:

```
uv run --with faster-whisper python .claude/skills/pdri-voiceover/scripts/align_beat.py <N> <beat_id>
```

Run this from the repo root. It will fail loudly (assertion error) if the transcript's marks
don't match the reference text's `[[mark]]` list — usually means the naskah/narration text and
the code's `m('...')` calls disagree, or the recording skipped/garbled a word badly enough that
sequence-matching lost track. Read the printed transcript in that case before retrying; a model
size bump (`--model medium`) sometimes helps, but a genuine text mismatch needs fixing in
`narration.id.json`/the naskah doc instead, not a bigger model.

Why a real ASR + alignment pass instead of just trusting the word-rate estimate already in
`timings.js`: the `silent: true` entries are a *placeholder* duration/cue estimate written before
any recording exists, used so the chapter plays with subtitles in the meantime. Once real audio
exists, the cues and `m()` marks must reflect where the *actual* voice actor's words land, or
the animation will visibly drift from the narration.

## 4. Verify and update the review artifacts

Rebuild the beat's standalone HTML and screenshot it to catch any layout regression (cards that
now overflow because the real text differs slightly from the draft, etc.) — see
`tools/pdri/scenes/build_scenes.py chNN` and the Playwright screenshot pattern used throughout
this project's chapter work (`#stage` locator screenshot at 1920x1 device scale). Check the
rendered PNG visually before calling it done.

Then:
- Update `docs/naskah-voiceover/babN-naskah-voiceover.md`'s "Durasi draf" cell for this row if
  it now meaningfully differs from the real duration, and the "Total N adegan, sekitar ..."
  summary line.
- Regenerate `books/pdri/review/chNN-mck/storyboard-adegan.jpg` (or `storyboard.jpg`, whichever
  the chapter already uses — check which exists before picking) — the compose script pattern in
  the chapter work earlier in this project tags newly-voiced beats visually.
- Leave a short note for the user naming which beats are still silent in that chapter, if any.

## What NOT to do

- Don't re-record a beat that already has real audio unless the user explicitly asks — that
  throws away a human-approved take.
- Don't invent or guess the voice/style if the chapter's naskah doc specifies one; match it.
- Don't skip the forced-alignment step and hand-wave the timing — a word-rate guess is fine for
  a never-recorded placeholder, but once real audio exists the project's standard is real
  alignment (see `tools/pdri/vo/align.py`, used for Bab 1–3).
- Don't leave MCP browser tabs open after downloading the clip.
- Don't touch `.claude/` conventions outside this skill, and don't commit/push unless asked —
  this whole workflow only touches working-tree files.
