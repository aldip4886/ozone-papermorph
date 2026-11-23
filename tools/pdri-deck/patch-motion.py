# Memperlambat dan menghaluskan animasi di template.html, memperbaiki transisi, dan menambah tombol Animasi.
# Dijalankan sekali pada template.html (v1); setelah itu jalankan patch-v2.py dan build.js / build2.js.
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'template.html')
s = open(p, encoding='utf-8').read()
if 'pdri-motion' in s:
    print('sudah dipatch'); sys.exit(0)

def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:90]); sys.exit(1)
    s = s.replace(a, b, 1)

# ---- 1. gerakan: jangan ikut OS secara diam-diam; pakai tombol Animasi (simpan di localStorage)
rep("@media (prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;animation-delay:0s!important;transition-duration:.01ms!important}.rv,.tile{opacity:1}mark{background-size:100% 100%}}",
    ".no-motion *,.no-motion *:before,.no-motion *:after{animation-duration:.01ms!important;animation-delay:0s!important;animation-iteration-count:1!important;transition-duration:.01ms!important}.no-motion mark{background-size:100% 100%}")
rep("const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;",
    "let reduce=localStorage.getItem('pdri-motion')==='off';\ndocument.documentElement.classList.toggle('no-motion',reduce);")

# ---- 2. durasi lebih lambat
rep(".wipe.go .w1{animation:wipe .8s cubic-bezier(.65,0,.35,1)}", ".wipe.go .w1{animation:wipe 1.3s cubic-bezier(.65,0,.35,1)}")
rep(".wipe.go .w2{animation:wipe .8s cubic-bezier(.65,0,.35,1) .08s}", ".wipe.go .w2{animation:wipe 1.3s cubic-bezier(.65,0,.35,1) .14s}")
rep("animation:hl .7s var(--ease) forwards;animation-delay:calc(var(--base,0s) + .55s)", "animation:hl 1.2s var(--ease) forwards;animation-delay:calc(var(--base,0s) + 1s)")
rep("animation:pop .7s var(--pop) backwards;animation-delay:calc(var(--base,0s) + var(--d,0) * 75ms + .15s)", "animation:pop 1.1s var(--pop) backwards;animation-delay:calc(var(--base,0s) + var(--d,0) * 140ms + .2s)")
rep(".rv{animation:rv .7s var(--ease) backwards;animation-delay:calc(var(--base,0s) + var(--d,0) * 80ms)}", ".rv{animation:rv 1.15s var(--ease) backwards;animation-delay:calc(var(--base,0s) + var(--d,0) * 140ms)}")
rep(".w>span{display:inline-block;animation:wd .75s var(--ease) backwards}", ".w>span{display:inline-block;animation:wd 1.1s var(--ease) backwards}")
rep("${k++*55+90}ms", "${k++*90+150}ms")
rep(".fl{animation:flt 5s ease-in-out infinite}", ".fl{animation:flt 8s ease-in-out infinite}")
rep("(t-t0)/1300)", "(t-t0)/2000)")
rep("rnd(9000,17000)", "rnd(20000,36000)")
rep("v:rnd(.2,.7)", "v:rnd(.08,.28)")
rep("p.ph+=.02;p.x+=Math.sin(p.ph)*.35;", "p.ph+=.006;p.x+=Math.sin(p.ph)*.18;")
rep("translateX(-60px) skewX(4deg)", "translateX(-48px)")
rep("translateX(60px) skewX(-4deg)", "translateX(48px)")
rep("transform:translateY(-8px)}}", "transform:translateY(-6px)}}")

# ---- 3. tilt halus: tanpa transisi CSS yang bentrok, tanpa translate (penyebab getar di tepi kartu), dilerp lewat rAF
i0 = s.index("function tilt(root){")
i1 = s.index("stage.addEventListener('pointermove'")
i2 = s.index("\n", s.index("stage.addEventListener('pointermove'")) + 1
newtilt = r'''function tilt(root){
  if(!fine||reduce)return;
  root.querySelectorAll('.card,.ck,.ag,.stat,.panel,.ans,.cb').forEach(e=>{
    let tx=0,ty=0,cx=0,cy=0,raf=0,on=false;
    const step=()=>{
      cx+=(tx-cx)*.08;cy+=(ty-cy)*.08;
      if(!on&&Math.abs(cx)+Math.abs(cy)<.02){e.style.transform='';raf=0;return}
      e.style.transform=`perspective(1000px) rotateX(${cy.toFixed(2)}deg) rotateY(${cx.toFixed(2)}deg)`;
      raf=requestAnimationFrame(step);
    };
    e.addEventListener('pointermove',ev=>{const r=e.getBoundingClientRect();tx=((ev.clientX-r.left)/r.width-.5)*7;ty=-((ev.clientY-r.top)/r.height-.5)*5;on=true;if(!raf)raf=requestAnimationFrame(step)});
    e.addEventListener('pointerleave',()=>{tx=ty=0;on=false;if(!raf)raf=requestAnimationFrame(step)});
  });
}
/* parallax ilustrasi: dihaluskan lewat rAF */
let ptx=0,pty=0,pcx=0,pcy=0,pRaf=0;
function pStep(){pcx+=(ptx-pcx)*.06;pcy+=(pty-pcy)*.06;stage.style.setProperty('--px',pcx.toFixed(3));stage.style.setProperty('--py',pcy.toFixed(3));pRaf=(Math.abs(ptx-pcx)+Math.abs(pty-pcy)>.002)?requestAnimationFrame(pStep):0}
stage.addEventListener('pointermove',e=>{if(!fine||reduce)return;const r=stage.getBoundingClientRect();ptx=(e.clientX-r.left)/r.width-.5;pty=(e.clientY-r.top)/r.height-.5;if(!pRaf)pRaf=requestAnimationFrame(pStep)});
'''
s = s[:i0] + newtilt + s[i2:]
# CSS: hilangkan transisi transform pada elemen yang dimiringkan, dan transisi parallax
rep(".art .iso{transform:translate(calc(var(--px,0)*16px),calc(var(--py,0)*11px));transition:transform .25s ease-out}", ".art .iso{transform:translate(calc(var(--px,0)*14px),calc(var(--py,0)*10px))}")
rep(".art .disc,.art .ring{transform:translate(calc(var(--px,0)*-9px),calc(var(--py,0)*-6px));transition:transform .3s ease-out}", ".art .disc,.art .ring{transform:translate(calc(var(--px,0)*-8px),calc(var(--py,0)*-5px))}")
rep("@media (max-width:700px){\n  .top{padding:8px 10px;gap:8px}", ".card,.ck,.ag,.stat,.panel,.ans,.cb{transition:border-color .25s,box-shadow .3s!important}\n@media (max-width:700px){\n  .top{padding:8px 10px;gap:8px}")

# ---- 4. durasi dan jeda transisi antar slide
rep("D=850;const o=", "D=1400;const o=")
rep("D=650;\n    nu.animate([{transform:`translateX(${dir*100}%)`}", "D=1100;\n    nu.animate([{transform:`translateX(${dir*100}%)`}")
rep("D=800;\n    nu.animate([{transform:`perspective(1500px) rotateY(${-dir*75}deg)", "D=1300;\n    nu.animate([{transform:`perspective(1500px) rotateY(${-dir*75}deg)")
rep("D=700;\n    nu.animate([{transform:`translateY(${dir*14}%)", "D=1200;\n    nu.animate([{transform:`translateY(${dir*14}%)")
rep("const base={circle:'.3s',push:'.3s',flip:'.4s',rise:'.2s'}[v];", "const base={circle:'.55s',push:'.5s',flip:'.7s',rise:'.4s'}[v];")
rep("wtimer=setTimeout(()=>{if(my!==tok)return;drop(old);mount(i,'.35s')},420);", "wtimer=setTimeout(()=>{if(my!==tok)return;drop(old);mount(i,'.5s')},680);")
rep("old.animate([{opacity:1},{opacity:0}],{duration:380,delay:120,fill:'forwards'});", "old.animate([{opacity:1},{opacity:0}],{duration:560,delay:180,fill:'forwards'});")

# ---- 5. tombol Animasi di bilah atas
rep('<button class="ib" id="btnNotes"', '<button class="ib" id="btnMotion" aria-label="Animasi aktif/nonaktif" title="Animasi: hidup/mati"><svg viewBox="0 0 24 24"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9zM19 16l.9 2.1L22 19l-2.1.9L19 22l-.9-2.1L16 19l2.1-.9z"/></svg></button>\n      <button class="ib" id="btnNotes"')
mot = r'''
/* tombol animasi: default hidup (tidak ikut pengaturan OS agar transisi selalu terlihat) */
function applyMotion(){document.documentElement.classList.toggle('no-motion',reduce);$('#btnMotion').style.opacity=reduce?.45:1;$('#btnMotion').title=reduce?'Animasi mati (klik untuk menghidupkan)':'Animasi hidup (klik untuk mematikan)'}
$('#btnMotion').onclick=()=>{reduce=!reduce;localStorage.setItem('pdri-motion',reduce?'off':'on');applyMotion();toast(reduce?'Animasi dimatikan':'Animasi dihidupkan')};
applyMotion();
if(matchMedia('(prefers-reduced-motion:reduce)').matches&&!reduce)setTimeout(()=>toast('Animasi tetap aktif. Matikan lewat tombol ✦ di kiri atas.'),1200);
'''
rep("/* ================= mulai ================= */", mot + "\n/* ================= mulai ================= */")

open(p, 'w', encoding='utf-8').write(s)
print('motion dipatch')
