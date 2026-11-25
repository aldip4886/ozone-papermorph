"""Align every beat of one chapter from cached ASR words, using pdri-voiceover's align_beat functions."""
import json, sys, pathlib
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / '.claude/skills/pdri-voiceover/scripts'))
import align_beat as ab

asr = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding='utf-8'))
ch = sys.argv[3]
nar_path = ROOT / f'content/pdri-mck/{ch}/narration.id.json'
nar = json.loads(nar_path.read_text(encoding='utf-8-sig'))
tjs = ROOT / f'site/pdri-mck/{ch}/audio/id/timings.js'
ntj = ROOT / f'content/pdri-mck/{ch}/narration.id.timings.json'
# drop BOMs so align_beat (utf-8) and other tools can read these files
for p in (nar_path, ntj):
    if p.exists():
        p.write_text(p.read_text(encoding='utf-8-sig'), encoding='utf-8')
fresh = {}
for bid, text in nar['beats'].items():
    words = asr[ch][bid]['words']
    dur = ab.mp3_duration(ROOT / f'site/pdri-mck/{ch}/audio/id/{bid}.mp3')
    res = ab.align(text, words, dur)
    ab.splice_timings_js(tjs, bid, res)
    fresh[bid] = res
    print(bid, res['dur'], res['marks'])
# rebuild narration timings json in beat order (drops stale entries)
ntj.write_text('{}', encoding='utf-8')
for bid, text in nar['beats'].items():
    ab.update_narration_timings(ntj, bid, text, asr[ch][bid]['words'], ab.mp3_duration(ROOT / f'site/pdri-mck/{ch}/audio/id/{bid}.mp3'))
