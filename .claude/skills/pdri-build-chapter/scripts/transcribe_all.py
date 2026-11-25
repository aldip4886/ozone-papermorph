"""Transcribe every beat mp3 of the given PDRI chapters once; save words + a word-diff vs the reference text."""
import json, re, sys, subprocess, difflib, pathlib
import numpy as np
from faster_whisper import WhisperModel

ROOT = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
chs = sys.argv[3:]
model = WhisperModel('small', device='cpu', compute_type='int8')
norm = lambda s: re.sub(r'[^0-9a-z]', '', s.lower())
res = {}
for ch in chs:
    nar = json.loads((ROOT / f'content/pdri-mck/{ch}/narration.id.json').read_text(encoding='utf-8-sig'))['beats']
    res[ch] = {}
    for bid, text in nar.items():
        mp3 = ROOT / f'site/pdri-mck/{ch}/audio/id/{bid}.mp3'
        raw = subprocess.run(['ffmpeg', '-v', 'quiet', '-i', str(mp3), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
        audio = np.frombuffer(raw, dtype='int16').astype('float32') / 32768
        segs, _ = model.transcribe(audio, language='id', word_timestamps=True, beam_size=5)
        words = [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for s in segs for w in s.words]
        ref = [norm(t) for t in re.sub(r'\[\[\w+\]\]', ' ', text).split() if norm(t)]
        hyp = [norm(t) for w in words for t in re.split(r'[\s\-]+', w[0]) if norm(t)]
        sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
        diffs = [(op, ' '.join(ref[i1:i2]), ' '.join(hyp[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
        res[ch][bid] = {'words': words, 'ratio': round(sm.ratio(), 3), 'diffs': diffs}
        print(ch, bid, res[ch][bid]['ratio'], diffs, flush=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
