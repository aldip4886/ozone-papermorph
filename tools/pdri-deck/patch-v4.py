# Membuat template-v4.html dari template-v3.html: tanpa header dan footer; navigasi dan tombol Proyeksikan melayang
# (muncul saat kursor digerakkan), panggung 16:9 memenuhi jendela, sidebar menjadi laci di semua lebar.
# Prasyarat: python tools/pdri-deck/patch-v3.py
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'template-v3.html'), encoding='utf-8').read()

def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:110]); sys.exit(1)
    s = s.replace(a, b, 1)

rep('Versi 3 · Slide Materi</title>', 'Versi 4 · Layar Bersih</title>')
rep('Versi 3 · Slide materi beranimasi', 'Versi 4 · Layar bersih tanpa header dan footer')
rep('presentasi PDRI v3</h3>', 'presentasi PDRI v4</h3>')
rep("a.download='presentasi-pdri-v3.html'", "a.download='presentasi-pdri-v4.html'")

# tombol daftar isi di dalam pil navigasi
rep('<button class="nav next" id="next"', '<button class="nav prev" id="fMenu" aria-label="Daftar isi" title="Daftar isi (M)"><svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h10"/></svg></button>\n      <button class="nav next" id="next"')

# sidebar selalu menjadi laci (overlay), supaya panggung tidak berubah ukuran
rep("$('#btnMenu').onclick=()=>{if(innerWidth<=900)app.classList.toggle('drawer');else app.classList.toggle('collapsed')};", "$('#btnMenu').onclick=()=>app.classList.toggle('drawer');")
rep("b.onclick=()=>{go(+b.dataset.i);if(innerWidth<=900)closeDrawer()};", "b.onclick=()=>{go(+b.dataset.i);closeDrawer()};")
rep("else if(m.pm==='menu'){if(innerWidth<=900)app.classList.add('drawer');else app.classList.remove('collapsed')}", "else if(m.pm==='menu'){app.classList.add('drawer')}")

# UI melayang muncul saat pointer bergerak, juga dari dalam adegan (iframe)
rep("addEventListener('mousemove',()=>{if(showOn)wake()});", "addEventListener('mousemove',()=>wake());")
rep("addEventListener('touchstart',()=>{if(showOn)wake()},{passive:true});", "addEventListener('touchstart',()=>wake(),{passive:true});\nwake();")
rep("if(m.pm==='pv-cmd'){pvCmd(m);return}", "if(m.pm==='pv-cmd'){pvCmd(m);return}\n  if(m.pm==='wake'){wake();return}")
rep("/* ================= mulai ================= */", "$('#fMenu').onclick=()=>app.classList.toggle('drawer');\n/* ================= mulai ================= */")

# teks agenda dan ringkasan untuk Bab 1-5
rep("Agenda: tiga bab pertama, materi dalam slide beranimasi", "Agenda: delapan bab, materi dalam slide beranimasi")
rep("Jelaskan alur: tiga bab, tiap bab berisi slide materi beranimasi.", "Jelaskan alur: delapan bab, tiap bab berisi slide materi beranimasi.")
rep("Rangkuman Bab 1–3: satu angka dasar, satu dasar hukum, satu alur pemungutan", "Rangkuman Bab 1–8: dari satu nilai impor sampai menjawab staf importir")
rep("Modul PDRI Bab 1–3;", "Modul PDRI Bab 1–8;")
rep("Tutup tiga bab pertama.", "Tutup delapan bab.")
rep("Berikutnya Bab 4: PPN Impor.", "Berikutnya post-test 10 soal.")
rep("Tiga bab pertama dalam slide materi beranimasi:", "Delapan bab dalam slide materi beranimasi:")
rep("dan siapa yang memungutnya.</p>\n", "siapa yang memungutnya, cara menghitung PPN Impor, PPh Pasal 22, barang mewah, dan barang kiriman, sampai menjawab staf importir.</p>\n") if "dan siapa yang memungutnya.</p>\n" in s else None
rep("Tiga bab menuntun Anda dari <mark>nilai impor</mark> sampai paham siapa yang memungut pajak", "Delapan bab menuntun Anda dari <mark>nilai impor</mark> sampai <mark>menjawab staf importir</mark>")
rep("Tiga bab pertama selesai: Anda sudah bisa menjelaskan dari mana nilai impor berasal, mengapa negara boleh memungut pajak, dan siapa yang memungutnya.", "Delapan bab selesai: Anda sudah bisa menghitung nilai impor, PPN Impor, PPnBM, PPh Pasal 22, dan barang kiriman, memeriksa fasilitas, serta menjelaskan tagihannya kepada importir.")
rep("dihitung dari nilai impor (Bab 4 dan 5)", "dihitung dari nilai impor (Bab 4 sampai 7)")
rep("['users','Bab 3 · Pihak dan sistem','Importir menghitung sendiri, DJBC meneliti dan memungut, DJP mengadministrasikan pengkreditannya.']];",
    "['users','Bab 3 · Pihak dan sistem','Importir menghitung sendiri, DJBC meneliti dan memungut, DJP mengadministrasikan pengkreditannya.'],\n"
    "           ['file','Bab 4 · PPN Impor','Rp168,1 juta (11%). Dikreditkan sebagai pajak masukan, uangnya tidak hilang.'],\n"
    "           ['coins','Bab 5 · PPh Pasal 22 Impor','Rp38,2 juta (tarif 2,5%). Cicilan di muka, dikreditkan di SPT Tahunan.'],\n"
    "           ['gem','Bab 6 · Barang mewah','PPN 12% penuh ditambah PPnBM 95%; fasilitas mengubah tagihan.'],\n"
    "           ['pack','Bab 7 · Barang kiriman','Nilai FOB dan jenis komoditas menentukan pungutan.'],\n"
    "           ['chat','Bab 8 · Menjawab staf','Rp645,2 juta: 51% BMTP; jelaskan dalam empat langkah.']];")


rep("'Semua PDRI dihitung dari satu angka: nilai pabean + Bea Masuk + bea masuk tambahan. PPN dan PPnBM tidak termasuk.'", "'Semua PDRI dihitung dari satu angka: nilai impor.'")
rep("'Kewajiban pajak ditetapkan dengan undang-undang (Pasal 23A UUD 1945); fungsi, teori, dan asas membantu menjelaskannya.'", "'Pajak ditetapkan dengan undang-undang (Pasal 23A UUD 1945).'")
rep("'Importir menghitung sendiri, DJBC meneliti dan memungut, DJP mengadministrasikan pengkreditannya.'", "'Importir menghitung, DJBC meneliti dan memungut, DJP mengkreditkan.'")

# tombol "Buka di editor HTML": VS Code lewat vscode://, Notepad lewat berkas .cmd, atau editor di halaman
rep('<div class="toast" id="toast"></div>', """<div class="pmenu" id="edlg" role="dialog" aria-label="Buka di editor">
  <h4>Buka file HTML ini di</h4>
  <button class="btn gold" id="edVs"><svg viewBox="0 0 24 24"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>Visual Studio Code</button>
  <button class="btn ghost" id="edNp"><svg viewBox="0 0 24 24"><path d="M6 2h9l4 4v16H6zM9 12h7M9 16h7"/></svg>Notepad</button>
  <button class="btn ghost" id="edIn"><svg viewBox="0 0 24 24"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>Editor di halaman ini</button>
  <small id="edNote"></small>
</div>
<div class="toast" id="toast"></div>""")
rep("$('#btnEdit').onclick=openModal;", r"""
/* berkas yang sedang dibuka (hanya diketahui bila halaman dibuka dari komputer: file://) */
function filePath(){
  if(location.protocol!=='file:')return null;
  let p=decodeURIComponent(location.pathname);
  if(/^\/[A-Za-z]:/.test(p))p=p.slice(1);
  return p;
}
function closeEdlg(){$('#edlg').classList.remove('on')}
$('#btnEdit').onclick=e=>{
  e.stopPropagation();
  const fp=filePath();
  $('#edNote').textContent=fp?fp.replace(/\//g,'\\'):'Halaman ini tidak dibuka dari komputer, jadi VS Code dan Notepad tidak bisa dituju. Simpan file lewat Unduh HTML lalu buka dari komputer.';
  $('#edVs').disabled=$('#edNp').disabled=!fp;
  $('#edlg').classList.add('on');
};
$('#edVs').onclick=()=>{const fp=filePath();if(!fp)return;closeEdlg();location.href='vscode://file/'+encodeURI(fp.startsWith('/')?fp.slice(1):fp);toast('Membuka di VS Code. Bila tidak terbuka, pastikan VS Code terpasang dan izinkan peramban membukanya.')};
$('#edNp').onclick=()=>{
  const fp=filePath();if(!fp)return;
  if(!/^[A-Za-z]:/.test(fp)){toast('Notepad hanya tersedia di Windows.');return}
  closeEdlg();
  const win=fp.replace(/\//g,'\\'),cmd='@echo off\r\nstart "" notepad "'+win+'"\r\n';
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([cmd],{type:'application/octet-stream'}));a.download='buka-di-notepad.cmd';a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),2000);
  toast('Jalankan buka-di-notepad.cmd yang baru diunduh untuk membuka file di Notepad.');
};
$('#edIn').onclick=()=>{closeEdlg();openModal()};
document.addEventListener('click',e=>{if(!e.target.closest('#edlg,#btnEdit'))closeEdlg()});
""")

css = r'''/* ---- v4: tanpa header dan footer ---- */
html,body,.app,.main{background:#071E45}
.main{justify-content:center;align-items:center}
.stage{width:min(100vw,calc(100dvh*16/9))!important;margin:0!important;border:0!important;border-radius:0!important;box-shadow:none!important;align-self:center}
.top{position:fixed!important;top:14px;right:14px;left:auto;width:auto;padding:0!important;gap:0;background:none;z-index:70;display:flex!important;opacity:0;transition:opacity .4s}
.top>*:not(#btnProject){display:none!important}
.bar{position:fixed!important;left:50%;bottom:14px;transform:translateX(-50%);width:auto;padding:6px 8px!important;gap:8px;border-radius:99px;background:rgba(7,30,69,.82);backdrop-filter:blur(8px);box-shadow:0 12px 30px rgba(0,0,0,.4);z-index:70;opacity:0;transition:opacity .4s}
.bar .prog{display:none}
.bar .count{color:#fff;min-width:60px;font-size:13px}.bar .count span{color:var(--gold)}
.bar .nav{width:42px;height:42px;border-radius:50%}
.bar .nav.prev{background:rgba(255,255,255,.14);border:0;box-shadow:none}.bar .nav.prev svg{stroke:#fff}
.bar .nav.next{box-shadow:none}
html.awake .top,html.awake .bar,.top:hover,.bar:hover,.top:focus-within,.bar:focus-within{opacity:1}
.app,.app.collapsed{grid-template-columns:minmax(0,1fr)}
.side{position:fixed;left:0;top:0;bottom:0;width:min(86vw,340px);transform:translateX(-102%);transition:transform .4s var(--ease);box-shadow:20px 0 50px rgba(7,30,69,.35);z-index:140}
.app.drawer .side{transform:none}
.scrim{display:block!important;position:fixed;inset:0;background:rgba(7,30,69,.45);z-index:130;opacity:0;pointer-events:none;transition:opacity .3s}
.app.drawer .scrim{opacity:1;pointer-events:auto}
.pmenu{top:62px}
.notes{left:0;right:0}
'''
css += r'''/* penekanan: warna huruf gold, bukan highlight setengah */
mark{background:none!important;background-image:none!important;animation:none!important;padding:0;color:#C8901A!important}
.dark mark,.ans mark{color:#F5B324!important}
.dark .ans mark{color:#C8901A!important}
'''
css += r'''#edlg{left:50%;right:auto;top:50%;transform:translate(-50%,-50%);z-index:160;width:min(380px,calc(100vw - 28px))}#edlg .btn{justify-content:center}#edlg .btn svg{width:18px;height:18px}#edlg .btn:disabled{opacity:.4;pointer-events:none}#edlg small{word-break:break-all}
.sum .q4{grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}.sum .q4 .card{align-items:center;gap:10px;padding:10px 12px}.sum .q4 .card p{font-size:11.5px;line-height:1.35;margin:2px 0 0}.sum .q4 .card b{font-size:12.5px}.sum .q4 .card .tile,.sum .q4 .card svg:first-child{transform:scale(.7);transform-origin:left center}
/* ---- v4: cermin layar peserta di tampilan presenter ---- */
html.mirror .top,html.mirror .bar,html.mirror .side,html.mirror .scrim,html.mirror .cap,html.mirror .toast,html.mirror .zone,html.mirror .pctl,html.mirror .pmenu,html.mirror .notes{display:none!important}
html.mirror,html.mirror body{pointer-events:none;overflow:hidden}
.pvmir{position:relative;width:min(100%,calc(46dvh*16/9));aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:#071E45;border:2px solid rgba(255,255,255,.2);flex:none;align-self:center}
.pvmir iframe{position:absolute;inset:0;width:100%;height:100%;border:0;background:#071E45}
.pvmir .pvblk{position:absolute;inset:0;background:#000;color:#8fa6c8;display:none;place-items:center;font-size:14px;font-weight:600}
.pvmir .pvblk.on{display:grid}
.pvmir .pvlive{position:absolute;left:8px;top:8px;z-index:2;padding:3px 9px;border-radius:99px;background:rgba(7,30,69,.85);color:var(--gold);font-size:10.5px;font-weight:700;letter-spacing:.08em}
'''
rep(".no-motion *,.no-motion *:before", css + ".no-motion *,.no-motion *:before")

# mode cermin: dimuat di dalam jendela presenter, hanya mengikuti slide yang tampil ke peserta
rep("const IS_PV=location.hash==='#presenter';", "const IS_PV=location.hash==='#presenter',IS_MIRROR=location.hash==='#mirror';\nif(IS_MIRROR)document.documentElement.classList.add('mirror');")
rep("  if(m.pm==='wake'){wake();return}", """  if(m.pm==='wake'){wake();return}
  if(m.pm==='mirror'){if(!IS_MIRROR)return;if(m.i!==cur&&m.i!=null)go(m.i);if(m.replay){const f=slideEl.lastElementChild&&slideEl.lastElementChild.querySelector('iframe');try{f&&f.contentWindow.postMessage({pm:'start',mode:MODE},'*')}catch(e){}}return}
  if(IS_MIRROR&&['next','menu','key','done'].includes(m.pm))return;""")
rep('<section class="pvcur"><small id="pvTag">', '<section class="pvcur"><div class="pvmir"><iframe id="pvMir" title="Layar peserta"></iframe><div class="pvblk" id="pvBlk">Layar hitam ditampilkan ke peserta</div><span class="pvlive">LAYAR PESERTA</span></div><small id="pvTag">')
rep("const list=q('pvList');", """const list=q('pvList');
  const mir=q('pvMir');let last={i:0};
  const pushMir=x=>{try{mir.contentWindow.postMessage(Object.assign({pm:'mirror'},last,x||{}),'*')}catch(e){}};
  mir.onload=()=>{pushMir();setTimeout(pushMir,500);setTimeout(pushMir,1500)};
  mir.src=location.href.split('#')[0]+'#mirror';""")
rep("q('pvReplay').onclick=()=>send('replay');", "q('pvReplay').onclick=()=>{send('replay');pushMir({replay:true})};")
rep("const on=list.querySelector('.on');on&&on.scrollIntoView({block:'nearest'});", "const on=list.querySelector('.on');on&&on.scrollIntoView({block:'nearest'});\n    last={i:m.i};pushMir();q('pvBlk').classList.toggle('on',!!m.black);")

open(os.path.join(here, 'template-v4.html'), 'w', encoding='utf-8').write(s)
print('template-v4.html dibuat')
