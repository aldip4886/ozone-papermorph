# Membuat template-v3.html dari template.html: adegan modul HTML (dist/pdri/html) dimuat sebagai iframe di dalam shell presentasi.
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'template.html'), encoding='utf-8').read()

def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:100]); sys.exit(1)
    s = s.replace(a, b, 1)

rep('<title>Memahami dan Menghitung PDRI · Presentasi Interaktif</title>', '<title>Memahami dan Menghitung PDRI · Versi 3 · Slide Materi</title>')
rep('<small>Outline presentasi</small>', '<small>Versi 3 · Slide materi beranimasi</small>')
rep('<h3>Editor HTML · presentasi PDRI</h3>', '<h3>Editor HTML · presentasi PDRI v3</h3>')
rep("a.download='presentasi-pdri.html'", "a.download='presentasi-pdri-v3.html'")
rep("AGE:'Agenda',SUM:'Ringkasan'};", "AGE:'Agenda',SUM:'Ringkasan',SCN:'Adegan'};")
rep("    case 'PER':return rPer(s);", "    case 'SCN':return rScn(s);\n    case 'PER':return rPer(s);")
rep("el.className='slide'+(dark?' dark':'');", "el.className='slide'+(dark?' dark':'')+(s.type==='SCN'?' scn':'');")
rep("b.className='it';", "b.className='it'+(s.done?' done':'');")
rep("${s.type==='AGE'?'AGD':s.type==='SUM'?'SUM':s.type}", "${s.type==='AGE'?'AGD':s.type==='SUM'?'SUM':s.type==='SCN'?'▶':s.type}")
rep("Math.round(645241050*e)", "Math.round(1528230000*e)")

rep('<div class="pill">Kemenkeu <i>›</i> DJBC <i>›</i> PBC</div>', '<div class="pill logo"><img alt="Kemenkeu, DJBC, PBC" src="/*__LOGO__*/"></div>')
# teks sintetis
rep("Agenda: tujuh puluh lima langkah dalam delapan kegiatan belajar", "Agenda: tiga bab pertama, materi dalam slide beranimasi")
rep("Jelaskan alur: Pembukaan, Bagian I (KB 1 sampai KB 4), Bagian II (KB 5 sampai KB 8), lalu penutup. Klik kartu untuk melompat.", "Jelaskan alur: tiga bab, tiap bab berisi slide materi beranimasi. Klik kartu untuk melompat.")
rep("Rangkuman akhir: satu rantai hitung menjawab tagihan Rp645 juta", "Rangkuman Bab 1–3: satu angka dasar, satu dasar hukum, satu alur pemungutan")
rep("KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026); PMK 98 Tahun 2025; PMK 131 Tahun 2024; PMK 51 Tahun 2025", "Modul PDRI Bab 1–3; KMK 55/MK/EF.2/2026 (kurs 18 sampai 24 November 2026); PMK 98 Tahun 2025; PMK 51 Tahun 2025")
rep("Tutup pertanyaan pembuka: lebih dari separuh tagihan berasal dari BMTP, bukan dari pajak. BM 10% masih asumsi (cek).", "Tutup tiga bab pertama. Tarif BM 10% masih asumsi latihan (cek BTKI). Berikutnya Bab 4: PPN Impor.")
rep("Delapan JP, delapan kegiatan belajar, dan satu pertanyaan yang memandu semuanya: dari mana angka tagihan Rp645 juta?", "Tiga bab pertama dalam slide materi beranimasi: dari mana angka tagihan Rp645 juta berasal, mengapa negara boleh memungutnya, dan siapa yang memungutnya.")
rep("Delapan kegiatan belajar menuntun Anda dari <mark>nilai impor</mark> sampai menjawab staf importir", "Tiga bab menuntun Anda dari <mark>nilai impor</mark> sampai paham siapa yang memungut pajak")

rep("Refleksikan Paspor Misi Anda: empat pertanyaan kasus sudah terjawab, dan satu rantai hitung kini bisa Anda jelaskan sendiri.", "Tiga bab pertama selesai: Anda sudah bisa menjelaskan dari mana nilai impor berasal, mengapa negara boleh memungut pajak, dan siapa yang memungutnya.")
# rSum diganti untuk Bab 1-3
i0 = s.index("function rSum(s){")
i1 = s.index("function rEnd(s){")
rsum = r'''function rSum(s){
  const total=1528230000;
  const parts=[['Nilai pabean',1089300000,'#D6DEEA','#0A2A5C'],['Bea Masuk',108930000,'#3A9BE1','#fff'],['BMTP',330000000,'#7CC0F2','#0A2A5C']];
  const bar=parts.map(p=>`<i data-w="${(p[1]/total*100).toFixed(2)}" style="background:${p[2]};color:${p[3]}">${p[0]}</i>`).join('');
  const lg=parts.map(p=>`<span><em style="background:${p[2]}"></em>${p[0]} Rp${(p[1]/1e6).toLocaleString('id-ID',{maximumFractionDigits:1})} juta</span>`).join('');
  const q=[['calc','Bab 1 · Nilai impor','Semua PDRI dihitung dari satu angka: nilai pabean + Bea Masuk + bea masuk tambahan. PPN dan PPnBM tidak termasuk.'],
           ['scale','Bab 2 · Dasar memungut','Kewajiban pajak ditetapkan dengan undang-undang (Pasal 23A UUD 1945); fungsi, teori, dan asas membantu menjelaskannya.'],
           ['users','Bab 3 · Pihak dan sistem','Importir menghitung sendiri, DJBC meneliti dan memungut, DJP mengadministrasikan pengkreditannya.']];
  const qh=q.map((x,i)=>`<div class="card rv" data-fx="z" style="--d:${i+6}">${tile(x[0],VNAMES[i%3])}<div><b>${x[1]}</b><p>${x[2]}</p></div></div>`).join('');
  return `<span class="tag rv">Ringkasan</span><h1 class="t rv" style="--d:1">${hl(s.title)}</h1>
  <div class="sum"><div class="chain">
    <div class="cb ar rv" data-fx="z" style="--d:2"><b>Nilai pabean</b>USD 60.000 × kurs</div>
    <div class="cb ar rv" data-fx="z" style="--d:3"><b>+ Bea Masuk + BMTP</b>masuk ke nilai impor</div>
    <div class="cb navy ar rv" data-fx="z" style="--d:4"><b>Nilai impor</b>Rp1.528.230.000</div>
    <div class="cb rv" data-fx="z" style="--d:5"><b>PPN · PPnBM · PPh 22</b>dihitung dari nilai impor (Bab 4 dan 5)</div></div>
  <div class="rv" style="--d:6"><div class="tot">Nilai impor Kasus 1 <span id="totN">Rp0</span></div><div class="stack" id="stack" style="margin-top:10px">${bar}</div><div class="legend">${lg}</div></div>
  <div class="q4">${qh}</div></div>
  <p class="src rv" style="--d:10"><b>Sumber</b> ${esc(s.sumber)}</p>`;
}
'''
s = s[:i0] + rsum + s[i1:]

# renderer adegan (iframe), tanpa tombol pemutar
rscn = r"""function rScn(s){
  const ic=d=>`<svg viewBox="0 0 24 24" aria-hidden="true">${d}</svg>`;
  return `<div class="scnw"><div class="scnf"><iframe src="${esc(s.src)}" title="${esc(s.title)}" allow="autoplay"></iframe><div class="ld"><span class="spin"></span>Memuat adegan…</div></div></div>
  <div class="cap rv" style="--d:3"><span class="tag">${esc(s.tag||'Adegan')}</span><b>${esc(s.title)}</b><span class="grow"></span>
  <button class="btn ghost sm tg" data-an aria-pressed="${AUTONEXT}" title="Auto-lanjut ke adegan berikutnya">${ic('<path d="M5 4l10 8-10 8zM19 5v14"/>')}<span>Auto-lanjut</span></button></div>`;
}
"""
rep("function rCover(s){", rscn + "function rCover(s){")

# state global
rep("const ORIGINAL=document.getElementById('deck-data').textContent;", "const ORIGINAL=document.getElementById('deck-data').textContent;\nlet AUTOPLAY=localStorage.getItem('pdri-ap')!=='off',AUTONEXT=localStorage.getItem('pdri-an')==='on';")

# wire(): ukuran adegan 16:9 dan rotasi otomatis di ponsel potret
wirescn = r"""  const fr=root.querySelector('.scnf iframe');
  if(fr){
    const box=root.querySelector('.scnf'),wrap=root.querySelector('.scnw'),ld=root.querySelector('.ld');
    const mq=matchMedia('(max-width:700px) and (orientation:portrait)');
    const fit=()=>{
      const cw=wrap.clientWidth,ch=wrap.clientHeight;if(!cw||!ch)return;
      const rot=false,L=cw,T=ch;
      const w=Math.min(L,T*16/9),h=w*9/16;
      box.style.inset='auto';box.style.margin='0';
      box.style.width=w+'px';box.style.height=h+'px';
      box.style.left=((cw-w)/2)+'px';box.style.top=((ch-h)/2)+'px';
      box.classList.toggle('rot',rot);
      box.style.transform=rot?'rotate(90deg)':'';
      if(rot)box.style.animation='none';
    };
    fit();new ResizeObserver(fit).observe(wrap);
    if(mq.addEventListener)mq.addEventListener('change',fit);
    fr.addEventListener('load',()=>{ld.classList.add('off');try{fr.focus()}catch(e){}});
    const an=root.querySelector('[data-an]');
    an.onclick=()=>{AUTONEXT=!AUTONEXT;localStorage.setItem('pdri-an',AUTONEXT?'on':'off');an.setAttribute('aria-pressed',AUTONEXT);toast('Auto-lanjut '+(AUTONEXT?'hidup':'mati'))};
  }
"""
rep("  root.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>go(+b.dataset.go));", "  root.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>go(+b.dataset.go));\n" + wirescn)

# jeda adegan lama saat berpindah
rep("cur=i;updateChrome();", "cur=i;updateChrome();\n  try{const oi=old&&old.querySelector('iframe');oi&&oi.contentWindow&&oi.contentWindow.postMessage({pm:'pause'},'*')}catch(e){}")

# pesan dari adegan (iframe)
msg = r'''
/* pesan dari adegan: next, menu, ready, done */
addEventListener('message',e=>{
  const m=e.data;if(!m||!m.pm)return;
  const fr=[...slideEl.querySelectorAll('iframe')].find(f=>f.contentWindow===e.source);
  if(!fr)return;
  const cur_=slideEl.lastElementChild;if(!cur_||!cur_.contains(fr))return;
  if(m.pm==='next')go(cur+1);
  else if(m.pm==='menu'){if(innerWidth<=900)app.classList.add('drawer');else app.classList.remove('collapsed')}
  else if(m.pm==='ready'){setTimeout(()=>{try{fr.contentWindow.postMessage({pm:'start'},'*')}catch(e){}},reduce?100:1500)}
  else if(m.pm==='done'){
    const i=cur;flat[i].done=true;
    const b=document.querySelector('.it[data-i="'+i+'"]');b&&b.classList.add('done');
    if(AUTONEXT&&i<flat.length-1){toast('Adegan selesai. Lanjut otomatis…');const t=tok;setTimeout(()=>{if(cur===i&&t===tok&&AUTONEXT)go(i+1)},2600)}
  }
});
'''
rep("/* keyboard + swipe */", msg + "\n/* keyboard + swipe */")
rep("&&!e.target.closest('button:not(.nav)')){e.preventDefault();go(cur+1)}", "&&!e.target.closest('button:not(.nav)')&&!(flat[cur].type==='SCN'&&(k===' '||k==='Enter'))){e.preventDefault();go(cur+1)}")

css = r'''/* ---- v3: adegan interaktif (iframe) ---- */
.slide.scn>.sc{padding:10px 14px;display:flex;flex-direction:column;gap:10px;overflow:hidden}
.scnw{flex:1;min-height:0;position:relative}
.scnf{position:absolute;inset:0;margin:auto;width:100%;height:100%;border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 22px 52px rgba(10,42,92,.24),0 0 0 2px var(--line);animation:scnIn 1.6s var(--ease) backwards;animation-delay:var(--base,0s)}
@keyframes scnIn{from{opacity:0;transform:scale(.95) translateY(22px);clip-path:inset(0 0 100% 0 round 16px)}to{opacity:1;transform:none;clip-path:inset(0 0 0 0 round 16px)}}
.scnf iframe{width:100%;height:100%;border:0;display:block;background:#fff}
.ld{position:absolute;inset:0;z-index:2;display:grid;place-content:center;justify-items:center;gap:14px;background:linear-gradient(110deg,#fff 30%,#e6f0fc 50%,#fff 70%);background-size:200% 100%;animation:shm 2.2s linear infinite;color:var(--blue);font-weight:600;font-size:14px;transition:opacity .6s}
.ld.off{opacity:0;pointer-events:none}
@keyframes shm{to{background-position:-200% 0}}
.spin{width:40px;height:40px;border-radius:50%;border:5px solid var(--line);border-top-color:var(--gold);animation:spn 1.1s linear infinite}
@keyframes spn{to{transform:rotate(360deg)}}
.cap{display:flex;align-items:center;gap:10px;flex:none;flex-wrap:wrap;padding:2px 4px}
.cap b{font-size:clamp(13px,1.3vw,16px);line-height:1.3;min-width:0}
.cap .grow{flex:1}.cap .tag{flex:none}
a.btn{text-decoration:none;color:inherit}
.btn.sm{padding:8px 13px;font-size:12px;border-radius:12px;box-shadow:none}
.btn.sm svg{width:16px;height:16px}
.btn.ghost.sm:hover{box-shadow:0 4px 0 var(--line)}
.btn.tg[aria-pressed=true]{background:var(--navy);color:#fff;border-color:var(--navy)}
.pill.logo{background:#fff;border:0;padding:4px 16px;display:grid;place-items:center}
.pill.logo img{height:36px;width:auto;display:block}
@media (max-width:700px){.pill.logo{display:none}}
.hintp{display:none;flex-basis:100%;font-size:11.5px;color:#5b7197}
.it.done .no:after{content:" ✓";color:var(--green)}
.it.on.done .no:after{color:var(--gold)}
:fullscreen .top{display:none}
@media (max-width:700px){
  .cap{gap:8px}.cap .tag{font-size:10px;padding:4px 9px}.cap b{flex-basis:100%;order:3}
  .btn.sm span{display:none}.btn.sm{padding:9px 11px}
  .slide.scn>.sc{padding:8px 8px}
  .scnf{border-radius:10px}
}
@media (max-width:700px) and (orientation:portrait){.rotb{display:inline-flex}.hintp{display:block;order:9}}
@media (max-height:500px){.top{display:none}.bar{padding:4px 10px}.nav{width:40px;height:40px}.stage{margin:6px 8px 0}.slide.scn>.sc{padding:6px 8px}.cap{display:none}}
'''
rep(".no-motion *,.no-motion *:before", css + ".no-motion *,.no-motion *:before")

# ---- mode presentasi: elemen tampil tanpa mengikuti beat voice over; transisi diperbarui
rep("AUTONEXT=localStorage.getItem('pdri-an')==='on';", "AUTONEXT=localStorage.getItem('pdri-an')==='on',MODE=localStorage.getItem('pdri-mode')||'build';")
rep('<span class="grow"></span>\n  <button class="btn ghost sm tg" data-an',
    '<span class="grow"></span>\n  <button class="btn ghost sm" data-replay title="Ulangi animasi adegan">${ic(\'<path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/>\')}<span>Ulangi</span></button>\n  <button class="btn ghost sm" data-mode title="Cara elemen tampil: bertahap cepat atau langsung">${ic(\'<path d="M4 6h16M4 12h10M4 18h6"/>\')}<span>${MODE===\'instant\'?\'Langsung\':\'Bangun\'}</span></button>\n  <button class="btn ghost sm tg" data-an')
rep('<div class="ld"><span class="spin"></span>', '<i class="shine"></i><div class="ld"><span class="spin"></span>')
rep("    const an=root.querySelector('[data-an]');",
    """    const mb=root.querySelector('[data-mode]'),rp=root.querySelector('[data-replay]');
    const send=()=>{try{fr.contentWindow.postMessage({pm:'start',mode:MODE},'*')}catch(e){}};
    mb.onclick=()=>{MODE=MODE==='instant'?'build':'instant';localStorage.setItem('pdri-mode',MODE);mb.lastElementChild.textContent=MODE==='instant'?'Langsung':'Bangun';toast(MODE==='instant'?'Semua elemen langsung tampil':'Elemen muncul bertahap (cepat)');send()};
    rp.onclick=send;
    const an=root.querySelector('[data-an]');""")
rep("fr.contentWindow.postMessage({pm:'start'},'*')", "fr.contentWindow.postMessage({pm:'start',mode:MODE},'*')")

# transisi baru: zoom dan tirai
rep("const VARIANTS=['wipe','circle','push','flip','rise'];", "const VARIANTS=['wipe','circle','zoom','push','curtain','flip','rise'];")
rep("const base={circle:'.55s',push:'.5s',flip:'.7s',rise:'.4s'}[v];", "const base={circle:'.55s',push:'.5s',flip:'.7s',rise:'.4s',zoom:'.55s',curtain:'.55s'}[v];")
rep("  }else{\n    D=1200;\n    nu.animate([{transform:`translateY(${dir*14}%) scale(.95)`",
    """  }else if(v==='zoom'){
    D=1300;
    nu.animate([{transform:`scale(${dir>0?.7:1.3})`,opacity:0,filter:'blur(8px)'},{transform:'none',opacity:1,filter:'blur(0)'}],{duration:D,easing:E});
    old.animate([{transform:'none',opacity:1},{transform:`scale(${dir>0?1.25:.75})`,opacity:0}],{duration:D*.7,easing:'ease-in',fill:'forwards'});
  }else if(v==='curtain'){
    D=1300;
    nu.animate([{clipPath:'inset(0 50% 0 50%)'},{clipPath:'inset(0 0 0 0)'}],{duration:D,easing:'cubic-bezier(.65,0,.35,1)'});
    old.animate([{transform:'none',opacity:1},{transform:'scale(.96)',opacity:.35}],{duration:D,easing:E,fill:'forwards'});
  }else{
    D=1200;
    nu.animate([{transform:`translateY(${dir*14}%) scale(.95)`""")

rep(".no-motion *,.no-motion *:before", """.shine{position:absolute;inset:0;z-index:3;pointer-events:none;background:linear-gradient(105deg,transparent 35%,rgba(255,226,154,.55) 50%,transparent 65%);transform:translateX(-120%);animation:shn 2s ease-out forwards;animation-delay:calc(var(--base,0s) + 1s)}
@keyframes shn{to{transform:translateX(120%)}}
.no-motion *,.no-motion *:before""")

# ---- ukuran seragam, tanpa subtitle, mode presentasi dan tampilan presenter
pvjs = open(os.path.join(here, 'v3-presenter.js'), encoding='utf-8').read()
pvcss = open(os.path.join(here, 'v3-presenter.css'), encoding='utf-8').read()
# bilah keterangan di bawah adegan dihapus: tinggal toolbar melayang
rep('<div class="cap rv" style="--d:3"><span class="tag">${esc(s.tag||\'Adegan\')}</span><b>${esc(s.title)}</b><span class="grow"></span>', '<div class="cap rv" style="--d:3">')
# tombol Proyeksikan di bilah atas
rep('<button class="ib" id="btnMotion"',
    '<button class="btn gold" id="btnProject" title="Proyeksikan ke layar proyektor (F5)"><svg viewBox="0 0 24 24"><path d="M3 4h18v11H3zM8 21h8M12 15v6"/></svg><span class="plbl">Proyeksikan</span></button>\n      <button class="ib" id="btnMotion"')
rep('<div class="toast" id="toast"></div>', """<div class="toast" id="toast"></div>
<div class="pmenu" id="pmenu" role="dialog" aria-label="Proyeksikan">
  <h4>Proyeksikan ke layar</h4>
  <label><input type="radio" name="pmFrom" value="start" checked><span><b>Dari awal</b><small>Mulai dari slide pertama (F5)</small></span></label>
  <label><input type="radio" name="pmFrom" value="cur"><span><b>Dari slide ini</b><small>Lanjut dari slide yang sedang tampil (Shift+F5)</small></span></label>
  <label><input type="checkbox" id="pmPv" checked><span><b>Buka tampilan presenter</b><small>Jendela terpisah berisi catatan, slide berikutnya, dan timer. Dengan dua layar, jendela presentasi otomatis ke proyektor bila izin pengelolaan jendela diberikan. Bila tidak, tarik jendela ini ke layar proyektor lebih dulu.</small></span></label>
  <button class="btn gold" id="pmGo"><svg viewBox="0 0 24 24"><path d="M5 3l14 9-14 9z"/></svg>Mulai presentasi</button>
  <small>Keluar dengan Esc. B atau titik = layar hitam. Panah, PageUp/PageDown, atau klik tepi layar untuk pindah slide.</small>
</div>
<div class="pctl" id="pctl"><button id="pPrev" aria-label="Sebelumnya"><svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg></button><span id="pCount"></span><button id="pNext" aria-label="Berikutnya"><svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></button><button id="pBlack" aria-label="Layar hitam"><svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9z"/></svg></button><button id="pExit" aria-label="Keluar"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
<div class="zone" id="zL" aria-hidden="true"></div><div class="zone" id="zR" aria-hidden="true"></div>
<div id="blk"></div>""")
rep("AUTONEXT=localStorage.getItem('pdri-an')==='on',MODE=localStorage.getItem('pdri-mode')||'build';", "AUTONEXT=localStorage.getItem('pdri-an')==='on',MODE=localStorage.getItem('pdri-mode')||'build';\nconst IS_PV=location.hash==='#presenter';")
rep("buildFlat();buildOutline();", "buildFlat();if(IS_PV){initPresenter();return}buildOutline();")
rep("document.title=`${cur+1}/${flat.length} · ${s.title}`;", "document.title=`${cur+1}/${flat.length} · ${s.title}`;\n  const pc=document.getElementById('pCount');if(pc)pc.textContent=(cur+1)+' / '+flat.length;\n  pvPost();")
rep("else if(k==='Home')go(0);else if(k==='End')go(flat.length-1);", "else if(k==='Home')go(0);else if(k==='End')go(flat.length-1);\n  else if(k==='F5'){e.preventDefault();startShow({from:e.shiftKey?cur:0,presenter:false})}else if(k==='b'||k==='B'||k==='.'){toggleBlack()}")
rep("const m=e.data;if(!m||!m.pm)return;", "const m=e.data;if(!m||!m.pm)return;\n  if(m.pm==='pv-cmd'){pvCmd(m);return}")
rep("if(m.pm==='next')go(cur+1);", "if(m.pm==='key')remoteKey(m);\n  else if(m.pm==='next')go(cur+1);")
rep("/* ================= mulai ================= */", pvjs + "\n/* ================= mulai ================= */")
rep(".no-motion *,.no-motion *:before", pvcss + ".no-motion *,.no-motion *:before")

rep("wire(el,s);tilt(el);", "wire(el,s);tilt(el);fitNative(el);")
open(os.path.join(here, 'template-v3.html'), 'w', encoding='utf-8').write(s)
print('template-v3.html dibuat')
