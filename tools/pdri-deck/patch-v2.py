# Membuat template-v2.html dari template.html (v1) dengan tipe slide "PDF" (halaman modul layar penuh)
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'template.html'), encoding='utf-8').read()

def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:90]); sys.exit(1)
    s = s.replace(a, b, 1)

rep('<title>Memahami dan Menghitung PDRI · Presentasi Interaktif</title>', '<title>Memahami dan Menghitung PDRI · Versi 2 · Modul PDF Layar Penuh</title>')
rep('<small>Outline presentasi</small>', '<small>Versi 2 · Modul PDF layar penuh</small>')
rep('<h3>Editor HTML · presentasi PDRI</h3>', '<h3>Editor HTML · presentasi PDRI v2</h3>')
rep('<script type="application/json" id="deck-data">', '<script type="application/json" id="pages-data">/*__PAGES__*/</script>\n<script type="application/json" id="deck-data">')
rep("const ORIGINAL=document.getElementById('deck-data').textContent;", "const ORIGINAL=document.getElementById('deck-data').textContent;\nconst PAGES=JSON.parse(document.getElementById('pages-data').textContent);")
rep("AGE:'Agenda',SUM:'Ringkasan'};", "AGE:'Agenda',SUM:'Ringkasan',PDF:'Modul PDF'};")
rep("Agenda: tujuh puluh lima langkah dalam delapan kegiatan belajar", "Agenda: delapan kegiatan belajar, tiga bab pertama langsung dari modul PDF layar penuh")
rep("    case 'PER':return rPer(s);", "    case 'PDF':return rPdf(s);\n    case 'PER':return rPer(s);")
rep("<small>${g.items.length} slide</small>", "<small>${g.items.length} slide${g.items.some(x=>x.type==='PDF')?' · modul PDF':''}</small>")
rep("el.className='slide'+(dark?' dark':'');", "el.className='slide'+(dark?' dark':'')+(s.type==='PDF'?' pdf':'');")
rep("a.download='presentasi-pdri.html'", "a.download='presentasi-pdri-v2.html'")
# thumbnail di sidebar
rep("b.innerHTML=`<span class=\"no\">${esc(s.n)}</span><span>${esc(s.title.length>86?s.title.slice(0,84)+'…':s.title)}</span><span class=\"ty\">${s.type==='AGE'?'AGD':s.type==='SUM'?'SUM':s.type}</span>`;",
    "b.innerHTML=`<span class=\"no\">${esc(s.n)}</span>${s.type==='PDF'&&PAGES[s.th]?`<img class=\"th\" src=\"${PAGES[s.th]}\" alt=\"\" loading=\"lazy\">`:''}<span>${esc(s.title.length>86?s.title.slice(0,84)+'…':s.title)}</span><span class=\"ty\">${s.type==='AGE'?'AGD':s.type==='SUM'?'SUM':s.type==='PDF'?'PDF':s.type}</span>`;")
# kunci Z untuk perbesar
rep("else if(k==='n'||k==='N')toggleNotes();", "else if(k==='n'||k==='N')toggleNotes();else if(k==='z'||k==='Z'){const zb=document.querySelector('[data-zoom]');zb&&zb.click()}")
# geser layar tidak berpindah slide saat mode perbesar
rep("if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5)go(", "if(!slideEl.querySelector('.zoomed')&&Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5)go(")

# renderer PDF
rpdf = r'''function rPdf(s){
  const src=PAGES[s.img]||'';
  const ic=d=>`<svg viewBox="0 0 24 24" aria-hidden="true">${d}</svg>`;
  return `<figure class="pgf"><div class="pgw"><img src="${src}" alt="${esc(s.title)}" draggable="false"><i class="shine"></i></div></figure>
  <div class="cap rv" style="--d:3"><span class="tag">${esc(s.tag||'Modul PDF')}</span><b>${esc(s.title)}</b><span class="grow"></span>
  <button class="btn ghost sm" data-zoom aria-label="Perbesar halaman">${ic('<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.3-4.3M11 8v6M8 11h6"/>')}<span>Perbesar</span></button>
  <button class="btn ghost sm" data-notes aria-label="Narasi">${ic('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>')}<span>Narasi</span></button>
  ${s.pdf?`<a class="btn ghost sm" href="${esc(s.pdf)}" target="_blank" rel="noopener" aria-label="Buka PDF bab">${ic('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6"/>')}<span>PDF bab</span></a>`:''}
  <span class="hintp">Ketuk gambar untuk memperbesar, atau putar ponsel ke lanskap.</span></div>`;
}
'''
rep("function rCover(s){", rpdf + "function rCover(s){")

# interaksi zoom di wire()
wirez = r'''  const fg=root.querySelector('.pgf');
  if(fg){
    const zb=root.querySelector('[data-zoom]'),im=fg.querySelector('img');
    const tg=()=>{const on=root.classList.toggle('zoomed');zb.lastElementChild.textContent=on?'Muat layar':'Perbesar';fg.scrollTo(0,0)};
    let dn=false,mv=0,sx=0,sy=0,sl=0,st=0;
    zb.onclick=tg;
    fg.addEventListener('pointerdown',e=>{if(!root.classList.contains('zoomed')||e.pointerType==='touch')return;dn=true;mv=0;sx=e.clientX;sy=e.clientY;sl=fg.scrollLeft;st=fg.scrollTop;fg.setPointerCapture(e.pointerId)});
    fg.addEventListener('pointermove',e=>{if(!dn)return;mv=Math.max(mv,Math.abs(e.clientX-sx)+Math.abs(e.clientY-sy));fg.scrollLeft=sl-(e.clientX-sx);fg.scrollTop=st-(e.clientY-sy)});
    fg.addEventListener('pointerup',()=>{dn=false});
    im.addEventListener('click',()=>{if(mv>6){mv=0;return}tg()});
  }
  root.querySelectorAll('[data-notes]').forEach(b=>b.onclick=()=>toggleNotes());
'''
rep("  root.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>go(+b.dataset.go));", "  root.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>go(+b.dataset.go));\n" + wirez)

css = r'''/* ---- v2: halaman modul PDF layar penuh ---- */
.slide.pdf>.sc{padding:10px 14px 10px;display:flex;flex-direction:column;gap:10px;overflow:hidden}
.pgf{flex:1;min-height:0;container-type:size;display:grid;place-items:center;margin:0}
.pgw{position:relative;width:min(100cqw,177.78cqh);aspect-ratio:16/9;border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 22px 52px rgba(10,42,92,.24),0 0 0 2px var(--line);cursor:zoom-in}
.pgw img{width:100%;height:100%;display:block;user-select:none;-webkit-user-drag:none;animation:pgIn 1.7s var(--ease) backwards;animation-delay:var(--base,0s)}
@keyframes pgIn{from{opacity:0;transform:scale(1.07);clip-path:inset(0 100% 0 0)}to{opacity:1;transform:none;clip-path:inset(0 0 0 0)}}
.shine{position:absolute;inset:0;pointer-events:none;background:linear-gradient(105deg,transparent 35%,rgba(255,226,154,.6) 50%,transparent 65%);transform:translateX(-120%);animation:shn 2.2s ease-out forwards;animation-delay:calc(var(--base,0s) + 1.2s)}
@keyframes shn{to{transform:translateX(120%)}}
.cap{display:flex;align-items:center;gap:10px;flex:none;flex-wrap:wrap;padding:2px 4px}
.cap b{font-size:clamp(13px,1.3vw,16px);line-height:1.3;min-width:0}
.cap .grow{flex:1}
.cap .tag{flex:none}
a.btn{text-decoration:none;color:inherit}
.btn.sm{padding:8px 13px;font-size:12px;border-radius:12px;box-shadow:none}
.btn.sm svg{width:16px;height:16px}
.btn.ghost.sm:hover{box-shadow:0 4px 0 var(--line)}
.hintp{display:none;flex-basis:100%;font-size:11.5px;color:#5b7197}
.slide.zoomed .pgf{overflow:auto;place-items:start;container-type:normal;cursor:grab;border-radius:16px;-webkit-overflow-scrolling:touch}
.slide.zoomed .pgw{width:max(210%,980px);max-width:none;cursor:zoom-out;flex:none}
.it .th{width:64px;height:auto;border-radius:6px;border:1px solid var(--line);flex:none;align-self:flex-start}
.it.on .th{border-color:var(--gold)}
:fullscreen .top{display:none}
:fullscreen .stage{margin:0 8px}
@media (max-width:700px){
  .cap{gap:8px}.cap .tag{font-size:10px;padding:4px 9px}.cap b{flex-basis:100%;order:3}
  .btn.sm span{display:none}.btn.sm{padding:9px 11px}
  .slide.pdf>.sc{padding:8px 8px 8px}
  .pgw{border-radius:10px}
}
@media (max-width:700px) and (orientation:portrait){.hintp{display:block;order:9}}
@media (max-height:500px){.top{display:none}.bar{padding:4px 10px}.nav{width:40px;height:40px}.stage{margin:6px 8px 0}.slide.pdf>.sc{padding:6px 8px}.cap{display:none}}
'''
rep(".no-motion *,.no-motion *:before", css + ".no-motion *,.no-motion *:before")

open(os.path.join(here, 'template-v2.html'), 'w', encoding='utf-8').write(s)
print('template-v2.html dibuat')
