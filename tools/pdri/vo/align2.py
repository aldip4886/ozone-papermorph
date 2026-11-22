import json,re,difflib,subprocess,sys
R='/home/user/ozone-papermorph/'
W=json.load(open(sys.argv[1]))
N=json.load(open(R+sys.argv[2]))['beats']
TAIL=0.25
norm=lambda s: re.sub(r'[^0-9a-z]','',s.lower())
def asr_tokens(words):
    out=[]
    for w,s,e in words:
        for p in re.split(r'[\s\-]+',w):
            if norm(p): out.append((norm(p),s,e))
    return out
T={}
for b,text in N.items():
    a=asr_tokens(W[b]['words'])
    # my tokens: (norm, raw, mark_before)
    toks=[]; pend=None
    for m in re.finditer(r'\[\[(\w+)\]\]|(\S+)',text):
        if m.group(1): pend=m.group(1); continue
        raw=m.group(2)
        for k,p in enumerate(re.split(r'-',raw)):
            if norm(p): toks.append([norm(p),None,pend if k==0 else None,raw if k==0 else '']); pend=None
    sm=difflib.SequenceMatcher(None,[t[0] for t in toks],[x[0] for x in a],autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        for i in range(i1,i2):
            if op=='equal': j=j1+i-i1
            elif op=='replace': j=j1+(i-i1)*(j2-j1)//(i2-i1)
            else: j=min(j1,len(a)-1)
            toks[i][1]=a[j][1]
    for i in range(1,len(toks)):  # monotonic
        toks[i][1]=max(toks[i][1],toks[i-1][1])
    dur=float(subprocess.check_output(['ffprobe','-v','quiet','-show_entries','format=duration','-of','csv=p=0',W[b]['file']]))+TAIL
    marks={t[2]:round(t[1],3) for t in toks if t[2]}
    # cues: rebuild from raw words (tokens with raw)
    words=[(t[3],t[1],t[2]) for t in toks if t[3]]
    cues=[];cur=[];st=None
    for k,(raw,s,mk) in enumerate(words):
        if cur and mk and len(' '.join(cur))>40 and not cur[-1].endswith(('.','?','!')) and len(' '.join(cur+[w for w,_,_ in words[k:]]))>95:
            cues.append([round(st,3),' '.join(cur)]);cur=[]
        if not cur: st=max(0.05,s-0.05)
        cur.append(raw)
        if raw.endswith(('.','?','!')) and len(' '.join(cur))>12: cues.append([round(st,3),' '.join(cur)]);cur=[]
    if cur: cues.append([round(st,3),' '.join(cur)])
    # split long cues at the comma nearest the middle
    times={}
    out=[]
    for c0,txt in cues:
        ws=txt.split(' ')
        if len(txt)>100:
            # locate start index of this cue in words
            k0=next(k for k in range(len(words)) if round(max(0.05,words[k][1]-0.05),3)==c0 and words[k][0]==ws[0])
            best=min([i for i,w in enumerate(ws[:-1]) if w.endswith(',')],key=lambda i:abs(len(' '.join(ws[:i+1]))-len(txt)/2),default=None)
            if best is not None:
                out.append([c0,' '.join(ws[:best+1])]); out.append([round(words[k0+best+1][1]-0.05,3),' '.join(ws[best+1:])]); continue
        out.append([c0,txt])
    cues=out
    T[b]={'dur':round(dur,3),'marks':marks,'cues':cues}
    exp=re.findall(r'\[\[(\w+)\]\]',text); assert list(marks)==exp,(b,marks,exp)
js='// Voice: rekaman Google AI Studio dari John (2026-11-22). Marks dan cues diselaraskan dari transkrip Whisper per kata.\nwindow.TIMINGS = '+json.dumps(T,ensure_ascii=False,indent=1)+';\n'
open(R+sys.argv[3],'w').write(js)
for b,v in T.items():
    print(b,v['dur'],v['marks'])
    for c in v['cues']: print('   ',c[0],c[1])
