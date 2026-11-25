"""Map a folder of Google AI Studio takes ("Generated Audio ... .wav") to a chapter's beats by what is said.

    uv run --with faster-whisper python S/map_wavs.py . chNN <wav-folder> <out.json>

Transcribes every WAV (faster-whisper small, id), scores it against every beat text in
content/pdri-mck/chNN/narration.id.json, and assigns beats one-to-one, best match first. Prints the table and
flags weak matches (< 0.6), beats with no take, and takes matching no beat. Writes {beat: wav_path} to out.json.
File names/timestamps are NOT reliable for ordering ("(1)" suffixes, re-takes, takes from other chapters).
"""
import json, re, sys, subprocess, difflib, pathlib
import numpy as np
from faster_whisper import WhisperModel

ROOT, ch, folder, out = pathlib.Path(sys.argv[1]), sys.argv[2], pathlib.Path(sys.argv[3]), pathlib.Path(sys.argv[4])
norm = lambda s: re.sub(r'[^0-9a-z]', '', s.lower())
toks = lambda s: [norm(t) for t in re.split(r'[\s\-]+', re.sub(r'\[\[\w+\]\]', ' ', s)) if norm(t)]
beats = json.loads((ROOT / f'content/pdri-mck/{ch}/narration.id.json').read_text(encoding='utf-8-sig'))['beats']
model = WhisperModel('small', device='cpu', compute_type='int8')
hyp = {}
for f in sorted(folder.glob('*.wav')):
    raw = subprocess.run(['ffmpeg', '-v', 'quiet', '-i', str(f), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    segs, _ = model.transcribe(np.frombuffer(raw, dtype='int16').astype('float32') / 32768, language='id', beam_size=5)
    hyp[f] = toks(' '.join(s.text for s in segs))
    print('transcribed', f.name, ' '.join(hyp[f])[:70], flush=True)
score = {(f, b): difflib.SequenceMatcher(None, toks(t), h, autojunk=False).ratio() for f, h in hyp.items() for b, t in beats.items()}
mapping, used = {}, set()
for (f, b), s in sorted(score.items(), key=lambda kv: -kv[1]):
    if b not in mapping and f not in used:
        mapping[b] = (f, s); used.add(f)
print()
for b in beats:
    if b in mapping:
        f, s = mapping[b]
        print(f'{b:12} {s:.2f} {"WEAK " if s < 0.6 else ""}{f.name}')
    else:
        print(f'{b:12} ---- NO TAKE')
for f in hyp:
    if f not in used:
        best = max(beats, key=lambda b: score[(f, b)])
        print(f'UNUSED {f.name} (closest: {best} {score[(f, best)]:.2f})')
out.write_text(json.dumps({b: str(f) for b, (f, s) in mapping.items()}, ensure_ascii=False, indent=1), encoding='utf-8')
