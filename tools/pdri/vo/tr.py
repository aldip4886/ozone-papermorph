import sys, json, glob, os
from faster_whisper import WhisperModel
ids="intro port groups pdri q1 nilai case step1 step2 step3 q2 check wrap final1 finish".split()
up='/root/.claude/uploads/290d5ce8-41a6-5786-aa7c-a654cc30ef6d/'
fs=sorted(glob.glob(up+'*vo-08*.wav'), key=lambda f: f.split('vo-')[1])
m=WhisperModel(sys.argv[1], device='cpu', compute_type='int8')
out={}
for bid,f in zip(ids,fs):
    import subprocess,numpy as np
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','quiet','-i',f,'-f','s16le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(a, language='id', word_timestamps=True, beam_size=5)
    words=[[w.word.strip(), round(w.start,3), round(w.end,3)] for s in segs for w in s.words]
    out[bid]={'file':f,'words':words,'text':' '.join(w[0] for w in words)}
    print(bid, os.path.basename(f), out[bid]['text'], flush=True)
json.dump(out, open('words.json','w'), ensure_ascii=False, indent=1)
