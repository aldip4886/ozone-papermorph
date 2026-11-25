---
name: pdri-build-chapter
description: Build and verify all deliverables of a PDRI (pdri-mck) chapter for the ozone-papermorph project — check the chapter's voiceover is the final recording (not a draft/sample) and matches the naskah/storyboard, forced-align its timing, then produce the per-chapter SCORM 1.2 + 2004 packages with cmi.interactions tracking, standalone HTML per scene, and the fullscreen PDF, run every check, and commit/push with a handoff doc. Use whenever the user asks to "bangun chapter/bab N", "buat SCORM bab N", "HTML per scene", "PDF fullscreen", "cek apakah VO sudah terbaru", or to rebuild a chapter's outputs after its audio, timing or index.html changed.
---

# PDRI chapter build

The runs that defined this workflow: Bab 3 and 4 (`docs/handoff-bab3-4-build-2026-11-25.md`) and Bab 5 with a
fresh set of takes (`docs/handoff-bab5-build-2026-11-25.md`). Depends on the `pdri-voiceover` skill
(`align_chapter.py` imports its `align_beat.py`).
All commands run from the repo root. Set `PYTHONUTF8=1` for every project script — they read/write without an
explicit encoding and Windows defaults to cp1252. `S` below means this skill's `scripts/` folder.

## 0. Branch

Work on a new branch (`claude/pdri-babN-...`) from `main`. The shared working tree usually holds other people's
unfinished changes: never `git reset`/`clean`, and stage only this job's files (step 6).

## 1. Is the voiceover final and current?

For each chapter N (`chNN`):

1. **Match the user's recording folder against the installed audio.** WAVs from Google AI Studio are
   24 kHz mono 16-bit, so `duration = (bytes - 44) / 48000`. Compare:
   - MD5 of the WAVs vs any staging copies (`dist/chNN-voiceover-staging/*.wav`), and staged MP3 vs
     `site/pdri-mck/chNN/audio/id/*.mp3` (`cmp`);
   - otherwise WAV durations vs MP3 durations (`ffmpeg -i x.mp3 2>&1 | grep Duration`) — identical
     durations mean that MP3 was converted from that WAV.
   Also scan `~/Downloads` root: takes are often saved there, and a take can land in the wrong chapter's folder
   (Bab 3's `new/` held Bab 4's `rina`). Report any WAV that maps to no beat.
   **A fresh folder of takes to install** (e.g. `Downloads/vo_materi_5`): file names/times don't reliably give
   the beat, so map by speech, then convert to the chapter's format (ch04+: 24 kHz/48 kbps; back up the old
   MP3s to scratch first):
   ```
   uv run --with faster-whisper python S/map_wavs.py . chNN <folder> <scratch>/map.json
   ffmpeg -y -v error -i <wav> -ar 24000 -ac 1 -b:a 48k -codec:a libmp3lame site/pdri-mck/chNN/audio/id/<beat>.mp3
   ```
   A weak score (< 0.6) usually means the take follows a newer naskah than `narration.id.json`, or the reader
   added/skipped a phrase — resolve it in step 3. Never overwrite the user's WAVs.
2. **Draft vs real.** A draft (edge-tts, e.g. `id-ID-ArdiNeural`) is 24 kHz/48 kbps with round durations and
   no matching WAV; a beat with `"silent": true` in `timings.js` has no real audio. Missing/draft beats are
   recorded with the `pdri-voiceover` skill — do not build outputs on draft audio without telling the user.
3. **Does the speech match the script?** Transcribe every beat once and diff it against `narration.id.json`:
   ```
   uv run --with faster-whisper python S/transcribe_all.py . <scratch>/asr.json ch03 ch04
   ```
   Expected noise: ASR spellings ("DJBC"→"dgbc", "11/12"→"11x12", "Bu Rina"→"burina"), numbers written vs
   spelled. A real problem is a missing/extra/different phrase. Also confirm `narration.id.json` agrees with
   `docs/naskah-voiceover/babN-naskah-voiceover.md` (Teks column) and, if present,
   `docs/storyboard-pdri/babN-storyboard.md`. Resolving real differences (Bab 5 had all three):
   - take = naskah, but `narration.id.json` is older → update the narration text to the naskah wording,
     keeping every `[[mark]]` (subtitles are built from it);
   - the reader dropped a phrase (Bab 5 `intro` skipped "Mari kita lanjutkan, ya,") → make the narration match
     what is spoken and list it in the handoff as a possible re-take;
   - the reader added something not in the naskah (Bab 5 `alur` began with the on-screen title) → cut it
     from the WAV at a silence (`ffmpeg -af silencedetect=n=-40dB:d=0.25`), using
     `-af "atrim=start=T,asetpts=PTS-STARTPTS,afade=t=in:d=0.05"`. Don't use `-ss` before `-i` on these WAVs —
     it trimmed twice as much. Check the new duration = old − T.
   After any audio/text fix, re-run `transcribe_all.py` before aligning.

   **Pronunciation vs the naskah** (numbers spelled out, abbreviations letter by letter — the naskah's
   style prompt is the rule). Plain ASR writes digits, so it can't show how a number was read. Run:
   ```
   uv run --with faster-whisper python S/check_pronunciation.py . N <scratch>/pron.json   # model medium
   ```
   It transcribes with a prompt in the naskah's spelled style and diffs against the Teks column. Where it
   still writes digits, judge by word timings in `pron.json`: a missing "persen" shows as no `%`/"persen"
   token after the number; "51" said as "lima puluh satu" spans ~0.8 s. For abbreviations that are also
   words (API → "api"), compare the token's duration with the beat's median seconds-per-syllable: letter
   reading (a-pe-i) is 3+ syllables, the word 2. Durations near the boundary can't be settled by ASR — cut
   those spots into one short MP3 for the user to listen to, rather than claiming they're right.
4. **Is the timing aligned?** `content/pdri-mck/chNN/narration.id.timings.json` must have one entry per beat
   with `dur` equal to the MP3 length and ASR words; `timings.js` `dur` = MP3 + 0.25 s. If not (e.g. cues
   were only scaled proportionally), align every beat from the cached transcripts:
   ```
   python S/align_chapter.py . <scratch>/asr.json chNN
   ```
   It reuses `pdri-voiceover/scripts/align_beat.py`'s `align()`, rewrites both timing files, and strips UTF-8
   BOMs from the narration JSONs (align_beat can't read them). An assertion error means the `[[mark]]` list
   and the recording disagree — read the transcript, fix the text, don't force it.
5. Update `narration.id.json` `voice`/`rate`/`note` if they still describe a draft voice, and
   `CHAPTER.minutes` in `site/pdri-mck/chNN/index.html` if the total audio length rounds differently.

## 2. Chapter checks

`tools/pdri/e2e_mck_chNN.py` (playback, replay, quiz layout, answers, finish). If it doesn't exist, copy the
ch03 one and set `URL` and `ANSWERS` from the chapter's `quiz(...)` blocks (choice index of `right`, `=value`
for `blanks` — compute it from the constants, `#a;b;c` for grids). No local server is needed:
```
URL="file:///<repo-path-url-encoded>/site/pdri-mck/chNN/index.html" python tools/pdri/e2e_mck_chNN.py
```

## 3–4. Build SCORM, HTML per scene, PDF

```
python S/build_outputs.py N            # or --only scorm / --only scenes
```
It does, and stops on the first failure:
- `tools/pdri/scorm/stage_chapter.py` → a one-chapter book in `dist/pdri/stage/chNN`;
- Papermorph `scorm.py` → `dist/pdri/chNN-scorm12.zip` and `-scorm2004.zip` (mastery 70, title
  "PDRI: Pajak dalam Rangka Impor (Bab N)" — keep these the same as earlier chapters);
- `check_scorm.py` (session, folder link, finish card, objective, resume) and `check_interactions.py`
  (`window.onInteraction` installed, `cmi.interactions` ids/format, no refused SetValue, no false `failed`);
- `tools/pdri/scenes/build_scenes.py` → standalone `NN-<beat>.html` per scene, `S/shoot_scenes.py`
  screenshots (Python port of `shoot_scenes.js`), `pack_scenes.py` → `00-daftar-adegan.html` and
  `babN-<slug>-fullscreen.pdf` (PageMode FullScreen);
- replaces `dist/pdri/html/babN/*.html` (stale files removed — numbering shifts when beats are added) and
  copies the PDF to `dist/pdri/pdf/`.

`check_interactions.py` answers generically (first option, "0" in boxes), so a wrong fill-in answer can stop
it before later practice questions — fewer records than questions is not by itself a failure. Confirm every
question reports by answering them all:
```
python S/check_all_interactions.py "file:///.../site/pdri-mck/chNN/index.html" <fill-in answer, e.g. 84.052.650>
```

Then **look at the screenshots** (the build prints the png folder; a 4×4 contact sheet is quickest) for
overflow, clipped text or empty scenes.

## 5. Handoff

Write `docs/handoff-babN[-M]-build-<date>.md` (Indonesian, like the existing handoffs): VO findings (what
matched, stray files), alignment done, output table with paths and sizes, every check and its result, rebuild
commands, tooling changes, and what's left (listening review, real-LMS/SCORM Cloud test, storyboard image,
naskah "Durasi draf", uncommitted leftovers).

## 6. Commit, push, PR

- Stage only: `site/pdri-mck/chNN/index.html`, `site/pdri-mck/chNN/audio`, `content/pdri-mck/chNN`,
  `dist/pdri/html/babN`, `dist/pdri/chNN-scorm*.zip`, the handoff, touched naskah/storyboard docs and tools,
  and `site/pdri-mck/lib/engine.js` if changed. Never junk like `chNN/outputs/`, `scorm_package/`,
  `*_SUMMARY.md`, `dist/pdri/stage/`, `dist/pdri/unz/`.
- `*.pdf` is gitignored: `git add -f dist/pdri/pdf/babN-*.pdf`.
- Check `git diff --cached --name-only` for anything pre-staged by someone else (e.g. deletions) and
  `git restore --staged` it.
- A zero-byte `.git/index.lock` with no running git process is stale — check the process list before removing.
- `gh` may not be installed; then push and give the user
  `https://github.com/aldip4886/ozone-papermorph/pull/new/<branch>` with a ready PR description.

## Known gotchas

- `Papermorph/` is vendored in this repo (engine + skill, with the interaction-tracking `scorm-bridge.js`/
  `scorm-host.js` and `check_interactions.py`); see `Papermorph/UPSTREAM.md` for the upstream base and how to
  update. Its demo books (`Papermorph/site/`) are not in the repo. If
  `Papermorph/.claude/skills/papermorph/assets/scorm/scorm-bridge.js` has no `onInteraction`, stop and tell the
  user — packages built without it don't report answers. Never re-add a nested `Papermorph/.git`: git would
  then store only a pointer, not the files.
- The local HTTP server may be blocked in this environment; use `file://` URLs (everything here works with them).
- Ch03 MP3s are 44.1 kHz/96 kbps (per-scene HTML ~1 MB each); ch04+ are 24 kHz/48 kbps.
