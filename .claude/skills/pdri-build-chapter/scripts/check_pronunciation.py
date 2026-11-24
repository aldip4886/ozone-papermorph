"""Check a chapter's recordings against the spelled-out text of the voiceover naskah (numbers as words,
abbreviations letter by letter), beat by beat.

    uv run --with faster-whisper python S/check_pronunciation.py . N <out.json> [--model medium] [--beats a,b]

The naskah (docs/naskah-voiceover/babN-naskah-voiceover.md, "Teks" column) spells numbers out ("dua koma lima
persen") so the voice reads them exactly. Plain ASR writes digits and hides how a number was said, so this
transcribes with an initial prompt in the naskah's own style (numbers in words, "pe-pe-ha", "a-pe-i"), then
diffs word by word against the naskah. Abbreviations are compared in letter-spelled form on both sides.

Report per beat: the differing spans. Read them by hand: ASR spelling noise ("dgbc", "importer") is fine; what
matters is a number said differently (missing "persen", "dua setengah" for "dua koma lima"), a word skipped
or added, or an abbreviation read as a word (API heard as "api" without letters).
"""
import argparse, json, re, subprocess, difflib, pathlib
import numpy as np
from faster_whisper import WhisperModel

# naskah's letter-by-letter readings; applied to both sides so "PPh" and "pe pe ha" compare equal
SPELL = {
    'ppnbm': 'pe pe en be em', 'pph': 'pe pe ha', 'ppn': 'pe pe en', 'pdri': 'pe de er i', 'pib': 'pe i be',
    'djbc': 'de je be ce', 'djp': 'de je pe', 'pmk': 'pe em ka', 'spt': 'es pe te', 'uu': 'u u', 'pt': 'pe te',
    'cv': 'se ve', 'pkp': 'pe ka pe', 'npwp': 'en pe we pe', 'nik': 'en i ka', 'hpp': 'ha pe pe', 'kup': 'ka u pe',
}
LETTER = {'a': 'a', 'b': 'be', 'c': 'ce', 'd': 'de', 'e': 'e', 'f': 'ef', 'g': 'ge', 'h': 'ha', 'i': 'i', 'j': 'je',
          'k': 'ka', 'l': 'el', 'm': 'em', 'n': 'en', 'o': 'o', 'p': 'pe', 'q': 'ki', 'r': 'er', 's': 'es', 't': 'te',
          'u': 'u', 'v': 've', 'w': 'we', 'x': 'eks', 'y': 'ye', 'z': 'zet'}
PROMPT = ('Pe-pe-ha Pasal dua puluh dua Impor, de-je-be-ce, pe-i-be, es-pe-te Tahunan, pe-em-ka lima puluh satu, '
          'a-pe-i u, ber-a-pe-i, dua koma lima persen, nol koma dua lima persen, tujuh koma lima persen, '
          'satu koma lima dua delapan miliar rupiah, tiga puluh delapan juta dua ratus lima ribu tujuh ratus lima puluh rupiah.')


def words(text):
    out = []
    for raw in re.split(r'[\s/]+', text.lower()):
        raw = raw.strip('.,:;?!"“”()')
        if not raw:
            continue
        if raw in ('api', 'api-u', 'api-p', 'ber-api'):        # naskah reads these by letter
            out += {'api': ['a', 'pe', 'i'], 'api-u': ['a', 'pe', 'i', 'u'], 'api-p': ['a', 'pe', 'i', 'pe'],
                    'ber-api': ['ber', 'a', 'pe', 'i']}[raw]
            continue
        for part in re.split(r'-', raw):
            part = re.sub(r'[^0-9a-z]', '', part)
            if not part:
                continue
            if part in SPELL:
                out += SPELL[part].split()
            elif part.isdigit():
                out.append(f'<{part}>')                      # digits in the transcript: the prompt didn't hold
            else:
                out.append(part)
    return out


def naskah_rows(root, n):
    rows = {}
    for l in (root / f'docs/naskah-voiceover/bab{n}-naskah-voiceover.md').read_text(encoding='utf-8-sig').splitlines():
        if re.match(r'^\|\s*\d+\s*\|', l):
            c = [x.strip() for x in l.split('|')[1:-1]]
            rows[c[1].strip('`')] = c[-1]
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('root', type=pathlib.Path); ap.add_argument('chapter', type=int); ap.add_argument('out', type=pathlib.Path)
    ap.add_argument('--model', default='medium'); ap.add_argument('--beats', default='')
    a = ap.parse_args()
    ch = f'ch{a.chapter:02d}'
    rows = naskah_rows(a.root, a.chapter)
    model = WhisperModel(a.model, device='cpu', compute_type='int8')
    report = {}
    for beat, ref in rows.items():
        if a.beats and beat not in a.beats.split(','):
            continue
        mp3 = a.root / f'site/pdri-mck/{ch}/audio/id/{beat}.mp3'
        raw = subprocess.run(['ffmpeg', '-v', 'quiet', '-i', str(mp3), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
        segs, _ = model.transcribe(np.frombuffer(raw, dtype='int16').astype('float32') / 32768, language='id', beam_size=5,
                                   initial_prompt=PROMPT, word_timestamps=True, condition_on_previous_text=False)
        segs = list(segs)
        hyp_text = ' '.join(s.text.strip() for s in segs)
        r, h = words(ref), words(hyp_text)
        sm = difflib.SequenceMatcher(None, r, h, autojunk=False)
        diffs = [(op, ' '.join(r[i1:i2]), ' '.join(h[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
        report[beat] = {'ratio': round(sm.ratio(), 3), 'naskah': ref, 'heard': hyp_text, 'diffs': diffs,
                        'words': [[w.word.strip(), round(w.start, 2), round(w.end, 2)] for s in segs for w in s.words]}
        print(f'\n== {beat} ({sm.ratio():.2f})', flush=True)
        for d in diffs:
            print('  ', d, flush=True)
    a.out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')


if __name__ == '__main__':
    main()
