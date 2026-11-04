LAB.start({anchor:'D',init:function(){
function detect(doc,ref){if(doc.notation&&doc.num!==doc.kor)return '숫자·한글 불일치';
  if(ref){if(doc.num!==ref.num||(doc.notation&&doc.kor!==ref.kor))return '상대 사본과 내용 다름';if(doc.seal&&doc.rewritten&&!doc.fakeSeal)return '도장 반쪽이 맞지 않음';}
  return '';}
function KOR(n){return n===10000?'만':n===1000?'천':n===5000?'오천':n===100000?'십만':n;}
function paper(x,X,Y,w,h,doc,title,o){o=o||{};x.fillStyle=o.lost?'rgba(60,60,80,.4)':'#efe6d2';rr(x,X,Y,w,h,8);x.fill();
  if(o.lost){x.strokeStyle=C.muted;x.setLineDash([5,5]);x.stroke();x.setLineDash([]);txt(x,'분실',X+w/2,Y+h/2,{a:'center',w:700,s:18,c:C.muted});txt(x,title,X+w/2,Y-8,{a:'center',c:C.muted,s:13});return;}
  txt(x,title,X+w/2,Y-8,{a:'center',w:700,s:13});txt(x,'차 용 증',X+w/2,Y+26,{a:'center',c:'#3a3040',w:700,s:15});
  var numBad=o.badNum,korBad=o.badKor;txt(x,'금 ₩'+fmt(doc.num),X+16,Y+56,{c:numBad?'#c0301f':'#3a3040',s:15,w:700});
  if(doc.notation)txt(x,'일금 '+KOR(doc.kor)+' 원정',X+16,Y+80,{c:korBad?'#c0301f':'#3a3040',s:14});
  txt(x,'빌린 사람 A · 빌려준 사람 B',X+16,Y+h-16,{c:'#6a5a50',s:11});}

/* ① 병기 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),notation=true,fg='none',both=0.3;
  $$('#lv1 [data-doc]').forEach(function(b){b.addEventListener('click',function(){notation=b.dataset.doc==='1';press('#lv1 [data-doc]',b);upd();});});
  $$('#lv1 [data-fg]').forEach(function(b){b.addEventListener('click',function(){fg=b.dataset.fg;upd();});});
  slider('r1b',function(v){both=v/100;upd();});
  function make(f){var d={notation:notation,seal:false,num:10000,kor:10000};if(f==='num')d.num=1000;if(f==='both'){d.num=1000;d.kor=1000;}return d;}
  function drawA(){var W=fit(c1,220),H=220,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var d=make(fg),det=detect(d,null);
    var w=Math.min(300,W*.5);paper(x,W/2-w/2,26,w,170,d,fg==='none'?'원본':'위조 시도: '+(fg==='num'?'숫자만':'둘 다'),{badNum:fg!=='none',badKor:fg==='both'});
    if(fg!=='none')txt(x,det?'흔적: '+det:'문서 안에 모순 없음 → 통과',W/2,H-6,{a:'center',w:700,c:det?C.gfp:C.eye});stamp(x,W,'설명용 장면');}
  function batch(){var r=rng(44),L=[];for(var i=0;i<20;i++){var f=r()<both?'both':'num';L.push({f:f,det:!!detect(make(f),null)});}return L;}
  function drawB(){var W=fit(c1b,190),H=190,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=batch(),caught=L.filter(function(l){return l.det}).length;
    var bx=[W*.25,W*.75];['들킴 (흔적 있음)','통과 (흔적 없음)'].forEach(function(s,i){x.strokeStyle=i?C.eye:C.gfp;rr(x,bx[i]-W*.2,40,W*.4,130,10);x.stroke();txt(x,s,bx[i],30,{a:'center',w:700,c:i?C.eye:C.gfp});});
    var ci=[0,0];L.forEach(function(l){var k=l.det?0:1,n=ci[k]++,col=n%10,row=Math.floor(n/10);var X=bx[k]-W*.18+col*(W*.36/10),Y=56+row*40;x.fillStyle=l.f==='both'?'#d9c9a8':'#efe6d2';x.fillRect(X,Y,W*.03,30);x.strokeStyle=l.f==='both'?C.amber:'rgba(0,0,0,.2)';x.strokeRect(X,Y,W*.03,30);});
    txt(x,'20장 중 '+caught+'장 탐지 · 노란 테두리 = 두 표기 모두 고친 위조',12,H-8,{s:12,c:C.muted});stamp(x,W,'예시값');return caught;}
  function upd(){drawA();var caught=drawB(),d=make(fg),det=detect(d,null);
    kpis($('#k1'),[[notation?'병기':'숫자만','문서 종류','a'],[fg==='none'?'—':(det?'있음':'없음'),'위조 흔적',fg==='none'?'a':(det?'g':'r')],[caught+'/20','위조 문서 탐지 (아래 분류)',caught>=14?'g':'r'],[Math.round(100*(notation?1-both:0))+'%','이론상 탐지율','m']]);
    $('#eq1').innerHTML='탐지율 = '+(notation?'<b>숫자만 고친 비율</b> = 1 − <i>'+both.toFixed(1)+'</i> = <em>'+(1-both).toFixed(1)+'</em>':'<b>0</b> (숫자만 적은 문서는 비교할 두 번째 표기가 없다)');
    var m=[];if(!notation)m.push(['r','숫자만 적은 차용증은 숫자를 고쳐도 비교할 표기가 없어 흔적이 남지 않아요.']);
    else if(fg==='both')m.push(['r','두 표기를 서로 맞게 고치면 문서 안에서는 모순이 없어요. 병기는 이런 꼼꼼한 위조를 잡지 못해요.']);
    else m.push(['g','병기 문서에서 숫자만 고치면 한글과 어긋나 흔적이 남아요. 탐지율은 위조범이 얼마나 꼼꼼한지에 달렸어요.']);ins($('#ins1'),m);}
  addEventListener('resize',upd);upd();})();

/* ② 간인·접인 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),rew=false,fake=false,lose=false,t=0;
  $('#b2Rew').addEventListener('click',function(){rew=!rew;this.setAttribute('aria-pressed',rew);upd();});
  $('#b2Fake').addEventListener('click',function(){fake=!fake;this.setAttribute('aria-pressed',fake);upd();});
  $('#b2Lose').addEventListener('click',function(){lose=!lose;this.setAttribute('aria-pressed',lose);upd();});
  function docs(){var A={notation:true,seal:true,num:10000,kor:10000,rewritten:false,fakeSeal:false};if(rew){A.num=5000;A.kor=5000;A.rewritten=true;A.fakeSeal=fake;}var B=lose?null:{num:10000,kor:10000};return {A:A,B:B};}
  function drawA(){var W=fit(c2,230),H=230,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var D=docs(),w=Math.min(250,(W-60)/2);
    paper(x,W/2-w-4,30,w,170,D.A,'A의 사본'+(rew?' (새로 씀)':''),{badNum:rew,badKor:rew});paper(x,W/2+4,30,w,170,{notation:true,num:10000,kor:10000},'B의 사본',{lost:lose});
    var sealOK=!rew||fake;x.strokeStyle='#c0301f';x.lineWidth=2.5;
    x.beginPath();x.arc(W/2-4+(sealOK?0:-6),120,15,Math.PI/2,Math.PI*1.5);x.stroke();if(!lose){x.beginPath();x.arc(W/2+4,120,15,-Math.PI/2,Math.PI/2);x.stroke();}x.lineWidth=1;
    txt(x,'접인',W/2,218,{a:'center',s:11,c:C.muted});stamp(x,W,'설명용 장면');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var D=docs(),det=detect(D.A,D.B);
    var ph=REDUCE?1:Math.min(1,(t%4)/2),gap=(1-ph)*W*.25;
    x.fillStyle='#efe6d2';rr(x,W/2-110-gap,40,100,80,6);x.fill();txt(x,'A: ₩'+fmt(D.A.num),W/2-60-gap,86,{a:'center',c:rew?'#c0301f':'#3a3040',w:700});
    if(D.B){x.fillStyle='#efe6d2';rr(x,W/2+10+gap,40,100,80,6);x.fill();txt(x,'B: ₩10,000',W/2+60+gap,86,{a:'center',c:'#3a3040',w:700});}
    else txt(x,'B 사본 없음 — 맞대 볼 상대가 없다',W/2+80,86,{a:'center',c:C.muted});
    if(ph>=1)txt(x,!rew?'원본끼리 일치 ✓':det?'위조 발견: '+det:'위조를 찾을 방법이 없다',W/2,H-16,{a:'center',w:700,c:!rew?C.gfp:det?C.gfp:C.eye});
    stamp(x,W,'설명용 장면');}
  function upd(){var D=docs(),det=detect(D.A,D.B);
    kpis($('#k2'),[[D.B?'있음':'없음','대조할 B 사본',D.B?'g':'r'],[!rew?'—':(det?'찾음':'못 찾음'),'바꿔치기 탐지',!rew?'a':(det?'g':'r')],[rew?(det||'—'):'—','걸린 이유','m'],[fake?'복제됨':'원본','A 사본의 도장',fake?'r':'a']]);
    $('#eq2').innerHTML='탐지 = <b>문서 안 모순</b> 또는 (<em>B 사본 있음</em> 그리고 (<i>내용 다름</i> 또는 <i>도장 어긋남</i>))';
    var m=[];if(!rew)m.push(['g','지금은 두 사본이 짝이 맞아요. "새로 써서 바꾸기"로 위조를 시도해 보세요.']);
    else if(det)m.push(['g','위조를 찾았어요: '+det+'. B 사본이 있으니 맞대 볼 수 있어요.']);
    else m.push(['r','B 사본이 사라졌고 도장까지 복제됐어요. A 사본 하나만 남아, 어떤 장치로도 위조를 찾을 수 없어요.']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

/* 대결: B 분실 + 새로 쓰기 + 도장 복제, 100장 */
function duelRun(full){var n=0;for(var i=0;i<100;i++){var A={notation:full,seal:full,num:5000,kor:full?5000:5000,rewritten:true,fakeSeal:true};if(detect(A,null))n++;}return n;}
Duel({names:{fly:'초파리 (병기+접인)',robo:'주판봇 (숫자만)'},higherIsBetter:true,drawMargin:0,
  run:function(){return {fly:duelRun(true),robo:duelRun(false)};},bar:function(v){return v/100;},fmt:function(v){return v+'장';},
  lesson:'원본과 대조할 수 없으면 어떤 안전장치도 같다',
  say:function(r){return '위조 문서 100장 중 찾아낸 장 수는 초파리 쪽 '+r.fly+'장, 주판봇 쪽 '+r.robo+'장이에요. B 사본이 없고 위조범이 두 표기를 맞게 고쳐서, 두 방식 모두 걸리는 규칙이 없었어요.';}});
}});
