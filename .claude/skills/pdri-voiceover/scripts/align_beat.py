"""Forced-align a just-recorded PDRI beat and splice the real timing into the chapter's files.

What it does, given a chapter number and a beat id that already has a reference text with
[[mark]] annotations in content/pdri-mck/chNN/narration.id.json and a recorded
site/pdri-mck/chNN/audio/id/<beat>.mp3:

1. Transcribes the mp3 with faster-whisper (word-level timestamps, language=id).
2. Fuzzy-matches the transcript against the reference text (difflib, normalized tokens) to
   find where each [[mark]] and each cue (sentence) actually lands in real time -- the same
   approach tools/pdri/vo/align.py used for Bab 1-3.
3. Writes the result into site/pdri-mck/chNN/audio/id/timings.js (replacing any "silent"
   placeholder for that beat, preserving its position) and appends/updates the matching
   entry in content/pdri-mck/chNN/narration.id.timings.json.

Usage:
    uv run --with faster-whisper python .claude/skills/pdri-voiceover/scripts/align_beat.py <chapter_num> <beat_id> [--model small]

Run from the repository root (C:\\Users\\ASUS\\OneDrive - Kemenkeu\\Projects\\ozone-papermorph).
Requires the mp3 to already exist at the expected path -- run the download/convert step first.
"""
import sys, re, json, hashlib, argparse, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]


def norm(s):
    return re.sub(r'[^0-9a-z]', '', s.lower())


def asr_tokens(words):
    out = []
    for w, s, e in words:
        for p in re.split(r'[\s\-]+', w):
            if norm(p):
                out.append((norm(p), s, e))
    return out


def transcribe(mp3_path, model_size):
    from faster_whisper import WhisperModel
    import numpy as np
    model = WhisperModel(model_size, device='cpu', compute_type='int8')
    raw = subprocess.run(
        ['ffmpeg', '-v', 'quiet', '-i', str(mp3_path), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'],
        capture_output=True).stdout
    audio = np.frombuffer(raw, dtype='int16').astype('float32') / 32768
    segs, _ = model.transcribe(audio, language='id', word_timestamps=True, beam_size=5)
    words = [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for seg in segs for w in seg.words]
    return words


def mp3_duration(mp3_path):
    out = subprocess.run(['ffmpeg', '-i', str(mp3_path)], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', out)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def align(text, asr_words, dur, tail=0.25):
    a = asr_tokens(asr_words)
    toks = []  # [norm, time, mark_before_or_None, raw_or_empty]
    pend = None
    for m in re.finditer(r'\[\[(\w+)\]\]|(\S+)', text):
        if m.group(1):
            pend = m.group(1)
            continue
        raw = m.group(2)
        for k, p in enumerate(re.split(r'-', raw)):
            if norm(p):
                toks.append([norm(p), None, pend if k == 0 else None, raw if k == 0 else ''])
                pend = None
    import difflib
    sm = difflib.SequenceMatcher(None, [t[0] for t in toks], [x[0] for x in a], autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        for i in range(i1, i2):
            if op == 'equal':
                j = j1 + i - i1
            elif op == 'replace':
                j = j1 + (i - i1) * (j2 - j1) // max(1, i2 - i1)
            else:
                j = min(j1, len(a) - 1)
            toks[i][1] = a[j][1]
    for i in range(1, len(toks)):
        toks[i][1] = max(toks[i][1], toks[i - 1][1])

    marks = {t[2]: round(t[1], 3) for t in toks if t[2]}
    words = [(t[3], t[1], t[2]) for t in toks if t[3]]
    cues, cur, st = [], [], None
    for k, (raw, s, mk) in enumerate(words):
        if cur and mk and len(' '.join(cur)) > 40 and not cur[-1].endswith(('.', '?', '!')) \
                and len(' '.join(cur + [w for w, _, _ in words[k:]])) > 95:
            cues.append([round(st, 3), ' '.join(cur)]); cur = []
        if not cur:
            st = max(0.05, s - 0.05)
        cur.append(raw)
        if raw.endswith(('.', '?', '!')) and len(' '.join(cur)) > 12:
            cues.append([round(st, 3), ' '.join(cur)]); cur = []
    if cur:
        cues.append([round(st, 3), ' '.join(cur)])

    out = []
    for c0, txt in cues:
        ws = txt.split(' ')
        if len(txt) > 100:
            k0 = next(k for k in range(len(words))
                      if round(max(0.05, words[k][1] - 0.05), 3) == c0 and words[k][0] == ws[0])
            best = min([i for i, w in enumerate(ws[:-1]) if w.endswith(',')],
                       key=lambda i: abs(len(' '.join(ws[:i + 1])) - len(txt) / 2), default=None)
            if best is not None:
                out.append([c0, ' '.join(ws[:best + 1])])
                out.append([round(words[k0 + best + 1][1] - 0.05, 3), ' '.join(ws[best + 1:])])
                continue
        out.append([c0, txt])

    exp = re.findall(r'\[\[(\w+)\]\]', text)
    assert list(marks) == exp, f'mark mismatch: got {list(marks)}, expected {exp}'
    return {'dur': round(dur + tail, 3), 'marks': marks, 'cues': out}


def splice_timings_js(path, beat_id, result):
    txt = path.read_text(encoding='utf-8')
    prefix, body = txt.split('=', 1)
    body = body.rsplit(';', 1)[0]
    data = json.loads(body)
    data[beat_id] = result  # dict insertion keeps original position if the key already existed
    new_body = json.dumps(data, ensure_ascii=False, indent=1)
    path.write_text(prefix + '= ' + new_body + ';\n', encoding='utf-8')


def update_narration_timings(path, beat_id, text, asr_words, dur):
    data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    data[beat_id] = {
        'key': hashlib.sha1(text.encode()).hexdigest(),
        'dur': round(dur, 3),
        'words': [[s, w] for w, s, e in asr_words],
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter', type=int)
    ap.add_argument('beat')
    ap.add_argument('--model', default='small', help='faster-whisper model size (default: small)')
    args = ap.parse_args()

    chdir = f'ch{args.chapter:02d}'
    mp3 = ROOT / 'site/pdri-mck' / chdir / 'audio/id' / f'{args.beat}.mp3'
    narration_path = ROOT / 'content/pdri-mck' / chdir / 'narration.id.json'
    timings_js_path = ROOT / 'site/pdri-mck' / chdir / 'audio/id/timings.js'
    narration_timings_path = ROOT / 'content/pdri-mck' / chdir / 'narration.id.timings.json'

    if not mp3.exists():
        sys.exit(f'Audio not found: {mp3}\nConvert and place the downloaded recording there first.')
    narration = json.loads(narration_path.read_text(encoding='utf-8'))
    text = narration['beats'][args.beat]

    print(f'Transcribing {mp3.name} with faster-whisper ({args.model})...')
    asr_words = transcribe(mp3, args.model)
    print(' ', len(asr_words), 'words:', ' '.join(w for w, _, _ in asr_words)[:120], '...')

    dur = mp3_duration(mp3)
    result = align(text, asr_words, dur)
    print('Aligned:', json.dumps(result, ensure_ascii=False, indent=1))

    splice_timings_js(timings_js_path, args.beat, result)
    update_narration_timings(narration_timings_path, args.beat, text, asr_words, dur)
    print(f'\nUpdated {timings_js_path}')
    print(f'Updated {narration_timings_path}')
    print('\nNext: rebuild + screenshot the beat to check layout, then update the storyboard image.')


if __name__ == '__main__':
    main()
