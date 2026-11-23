/* ================= mode presentasi (proyektor) + tampilan presenter ================= */
let pw=null,showOn=false,blackOn=false,showStart=0,idleT=0;
const htmlEl=document.documentElement;
function pvPost(){
  if(!pw||pw.closed)return;
  const s=flat[cur],n=flat[cur+1];
  try{pw.postMessage({pm:'pv-state',i:cur,n:flat.length,title:s.title,tag:s.tag||s.secLabel||'',type:s.type,notes:s.catatan||'',next:n?n.title:'',show:showOn,black:blackOn,start:showStart},'*')}catch(e){}
}
function pvCmd(m){
  if(m.a==='next')go(cur+1);else if(m.a==='prev')go(cur-1);else if(m.a==='goto')go(m.i);
  else if(m.a==='black')toggleBlack();else if(m.a==='hello')pvPost();
  else if(m.a==='replay'){const fr=slideEl.lastElementChild&&slideEl.lastElementChild.querySelector('iframe');try{fr&&fr.contentWindow.postMessage({pm:'start',mode:MODE},'*')}catch(e){}}
}
function toggleBlack(f){blackOn=f===undefined?!blackOn:f;$('#blk').classList.toggle('on',blackOn);pvPost()}
function remoteKey(m){
  const k=m.key;
  if(['PageDown','ArrowRight','ArrowDown',' ','Enter'].includes(k))go(cur+1);
  else if(['PageUp','ArrowLeft','ArrowUp','Backspace'].includes(k))go(cur-1);
  else if(k==='b'||k==='B'||k==='.')toggleBlack();
  else if(k==='F5')m.shift?startShow({from:cur}):startShow({from:0});
  else if(k==='Home')go(0);else if(k==='End')go(flat.length-1);
}
function wake(){
  htmlEl.classList.add('awake');htmlEl.classList.remove('idle');clearTimeout(idleT);
  idleT=setTimeout(()=>{htmlEl.classList.remove('awake');htmlEl.classList.add('idle')},2600);
}
addEventListener('mousemove',()=>{if(showOn)wake()});
addEventListener('touchstart',()=>{if(showOn)wake()},{passive:true});
async function startShow(o){
  o=o||{};
  closeMenu();
  if(o.presenter){
    try{pw=window.open(location.href.split('#')[0]+'#presenter','pdri-presenter','popup=yes,width=1180,height=760')}catch(e){pw=null}
    if(!pw)toast('Jendela presenter diblokir. Izinkan pop-up untuk halaman ini.');
  }
  showOn=true;showStart=Date.now();htmlEl.classList.add('present');app.classList.add('collapsed');app.classList.remove('drawer');
  if(o.from!=null)go(o.from);
  wake();
  let screenOpt;
  if(o.presenter&&window.getScreenDetails){
    try{
      const d=await getScreenDetails();
      const ext=d.screens.find(s=>s!==d.currentScreen);
      if(ext){screenOpt={screen:ext};try{pw&&pw.moveTo(d.currentScreen.availLeft+40,d.currentScreen.availTop+40)}catch(e){}}
    }catch(e){}
  }
  try{await htmlEl.requestFullscreen(screenOpt)}catch(e){try{await htmlEl.requestFullscreen()}catch(e2){toast('Tekan F11 untuk layar penuh. Jendela ini sudah dalam mode presentasi.')}}
  pvPost();
}
function endShow(){
  if(!showOn)return;
  showOn=false;htmlEl.classList.remove('present','awake','idle');toggleBlack(false);
  if(document.fullscreenElement)document.exitFullscreen().catch(()=>{});
  pvPost();
}
document.addEventListener('fullscreenchange',()=>{if(showOn&&!document.fullscreenElement)endShow()});
/* menu Proyeksikan */
function closeMenu(){$('#pmenu').classList.remove('on')}
$('#btnProject').onclick=e=>{e.stopPropagation();$('#pmenu').classList.toggle('on')};
document.addEventListener('click',e=>{if(!e.target.closest('#pmenu,#btnProject'))closeMenu()});
$('#pmGo').onclick=()=>{
  const from=document.querySelector('input[name=pmFrom]:checked').value==='cur'?cur:0;
  startShow({from,presenter:$('#pmPv').checked});
};
$('#pPrev').onclick=()=>go(cur-1);$('#pNext').onclick=()=>go(cur+1);
$('#pBlack').onclick=()=>toggleBlack();$('#pExit').onclick=endShow;
$('#blk').onclick=()=>toggleBlack(false);
$('#pctl').addEventListener('pointermove',e=>e.stopPropagation());
/* klik di tepi kiri/kanan panggung untuk pindah slide saat presentasi (di atas iframe) */
$('#zL').onclick=()=>go(cur-1);$('#zR').onclick=()=>go(cur+1);

/* ---- tampilan presenter (jendela terpisah) ---- */
function initPresenter(){
  htmlEl.classList.add('pv');
  document.title='Tampilan presenter · PDRI';
  const root=document.createElement('div');root.id='pv';
  root.innerHTML=`<header><b>Tampilan presenter</b><span class="grow"></span><span id="pvClock"></span><span class="pvt" id="pvTimer">00:00</span><button class="btn ghost sm" id="pvReset">Reset timer</button></header>
  <main><section class="pvcur"><small id="pvTag">Menunggu jendela presentasi…</small><h1 id="pvTitle">–</h1><div class="pvnotes" id="pvNotes"></div></section>
  <aside><div class="pvnext"><small>Berikutnya</small><b id="pvNext">–</b></div>
  <div class="pvctl"><button class="btn ghost" id="pvPrev">‹ Sebelumnya</button><button class="btn gold" id="pvNextBtn">Berikutnya ›</button></div>
  <div class="pvctl"><button class="btn ghost sm" id="pvReplay">Ulangi animasi</button><button class="btn ghost sm" id="pvBlack">Layar hitam</button><button class="btn ghost sm" id="pvA1">A−</button><button class="btn ghost sm" id="pvA2">A+</button></div>
  <div class="pvcount" id="pvCount"></div><div class="pvlist" id="pvList"></div></aside></main>`;
  document.body.appendChild(root);
  const q=id=>document.getElementById(id);
  const send=(a,i)=>{try{(window.opener||pw).postMessage({pm:'pv-cmd',a,i},'*')}catch(e){}};
  q('pvPrev').onclick=()=>send('prev');q('pvNextBtn').onclick=()=>send('next');q('pvBlack').onclick=()=>send('black');q('pvReplay').onclick=()=>send('replay');
  let fs=22;const setFs=v=>{fs=Math.max(14,Math.min(48,v));q('pvNotes').style.fontSize=fs+'px'};setFs(22);
  q('pvA1').onclick=()=>setFs(fs-2);q('pvA2').onclick=()=>setFs(fs+2);
  const list=q('pvList');
  flat.forEach((s,i)=>{const b=document.createElement('button');b.dataset.i=i;b.innerHTML=`<span>${esc(String(s.n))}</span>${esc(s.title)}`;b.onclick=()=>send('goto',i);list.appendChild(b)});
  let t0=0;
  q('pvReset').onclick=()=>{t0=Date.now()};
  setInterval(()=>{const d=new Date();q('pvClock').textContent=d.toLocaleTimeString('id-ID',{hour:'2-digit',minute:'2-digit'});if(t0){const s=Math.floor((Date.now()-t0)/1000);q('pvTimer').textContent=String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')}},500);
  addEventListener('message',e=>{
    const m=e.data;if(!m||m.pm!=='pv-state')return;
    if(!t0)t0=m.start||Date.now();
    q('pvTag').textContent=m.tag;q('pvTitle').textContent=m.title;
    q('pvNotes').textContent=m.notes||'Tidak ada catatan untuk slide ini.';
    q('pvNext').textContent=m.next||'Akhir presentasi';
    q('pvCount').textContent='Slide '+(m.i+1)+' dari '+m.n+(m.black?'  ·  layar hitam':'');
    q('pvBlack').classList.toggle('on',!!m.black);
    list.querySelectorAll('button').forEach(b=>b.classList.toggle('on',+b.dataset.i===m.i));
    const on=list.querySelector('.on');on&&on.scrollIntoView({block:'nearest'});
  });
  addEventListener('keydown',e=>{
    if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();send('next')}
    else if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();send('prev')}
    else if(e.key==='b'||e.key==='B'||e.key==='.')send('black');
  });
  send('hello');
}

/* slide native diskalakan dari kanvas tetap bila panggung sempit, supaya selalu 16:9 seperti PowerPoint */
function fitNative(el){
  const sc=el.querySelector('.sc');if(!sc||el.classList.contains('scn'))return;
  const W=stage.clientWidth;
  if(W>=1000){sc.style.cssText='';return}
  const DW=W<700?720:960,DH=DW*9/16,k=W/DW;
  sc.style.cssText=`width:${DW}px;height:${DH}px;inset:auto;left:0;top:0;transform:scale(${k.toFixed(4)});transform-origin:0 0`;
}
new ResizeObserver(()=>slideEl.querySelectorAll('.slide').forEach(fitNative)).observe(stage);
