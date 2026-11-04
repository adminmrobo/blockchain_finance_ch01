LAB.start({anchor:'C',init:function(){
function kmin(N){return Math.floor(N/2)+1;}
/* 투표 함수: ledgers=[{reg:bool, forged:bool}], rule='reg'|'open' */
function vote(L,rule){var o=0,f=0,illegal=0;L.forEach(function(l){if(rule==='reg'&&!l.reg){illegal++;return;}l.forged?f++:o++;});return {orig:o,forged:f,illegal:illegal};}
function ledgers(N,k,fake){var L=[];for(var i=0;i<N;i++)L.push({reg:true,forged:i<k});for(var j=0;j<fake;j++)L.push({reg:false,forged:true});return L;}

/* ① 다수결 장부 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),N=9,k=4,anim=1;
  function sync(){if(k>N){k=N;$('#r1k').value=k;}$('#r1k').max=N;$('#v1k').textContent=k;$('#v1n').textContent=N;}
  $('#r1n').addEventListener('input',function(){N=+this.value;sync();anim=0;upd();});
  $('#r1k').addEventListener('input',function(){k=+this.value;sync();anim=0;upd();});
  function drawA(){var W=fit(c1,250),H=250,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var cx=W/2,cy=H/2+6,R=Math.min(W*.4,H*.38),v=vote(ledgers(N,k,0),'reg'),forged=v.forged>v.orig;
    for(var i=0;i<N;i++){var a=i/N*Math.PI*2-Math.PI/2,px=cx+Math.cos(a)*R,py=cy+Math.sin(a)*R,bad=i<k;x.fillStyle=bad?'rgba(240,96,77,.85)':'rgba(94,227,156,.85)';rr(x,px-16,py-11,32,22,4);x.fill();txt(x,bad?'1천':'1만',px,py+4,{a:'center',s:10,w:700,c:'#13141f'});}
    x.fillStyle=forged?'rgba(240,96,77,.18)':'rgba(94,227,156,.15)';x.beginPath();x.arc(cx,cy,R*.55,0,7);x.fill();
    txt(x,'다수결 결과',cx,cy-14,{a:'center',s:12,c:C.muted});txt(x,forged?'위조본 1,000원':'원본 10,000원',cx,cy+10,{a:'center',s:16,w:700,c:forged?C.eye:C.gfp});txt(x,'초록 '+v.orig+' : 빨강 '+v.forged,cx,cy+30,{a:'center',s:12});stamp(x,W,'설명용 모형');}
  function drawB(dt){anim=Math.min(1,anim+dt*1.2);if(REDUCE)anim=1;var W=fit(c1b,170),H=170,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=110,bw=W-L-50,h=34,v=vote(ledgers(N,k,0),'reg');
    [['원본에 표',v.orig,C.gfp,40],['위조본에 표',v.forged,C.eye,90]].forEach(function(b){var w=bw*(b[1]/N)*anim;txt(x,b[0],12,b[3]+22,{s:13});x.fillStyle=b[2];rr(x,L,b[3],Math.max(2,w),h,6);x.fill();txt(x,Math.round(b[1]*anim)+'표',L+Math.max(2,w)+8,b[3]+22,{s:13,w:700});});
    var tx=L+bw*0.5;x.strokeStyle=C.amber;x.setLineDash([5,4]);x.beginPath();x.moveTo(tx,28);x.lineTo(tx,140);x.stroke();x.setLineDash([]);txt(x,'과반선 (N/2 = '+(N/2)+')',tx,22,{a:'center',s:11,c:C.amber});stamp(x,W,'설명용 모형');}
  function upd(){var km=kmin(N),forged=k>=km;
    kpis($('#k1'),[[km+'권','위조에 필요한 과반 ⌊N/2⌋+1','a'],[k+'권','공격자가 고친 장부',forged?'r':'m'],[forged?'위조본':'원본','다수결이 "참"으로 정한 기록',forged?'r':'g'],[N+'곳','공격해야 할 후보 (은행은 1곳)','m']]);
    $('#eq1').innerHTML='위조 성공 조건: <b>k = '+k+'</b> ≥ ⌊'+N+'/2⌋+1 = <b>'+km+'</b> → '+(forged?'<em>성립</em>':'불성립');
    ins($('#ins1'),[forged?['r','공격자가 과반('+km+'권 이상)을 동시에 장악하면 위조본이 "참"이 돼요. 분산원장이 막는 건 과반 미만의 공격이에요.']:['g','위조본이 '+k+'권뿐이라 다수결은 원본을 택해요. 위조하려면 '+(km-k)+'권을 더 동시에 바꿔야 해요.']]);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);sync();upd();})();

/* ② 손익과 투표권 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),c=3000,f=100,rule='reg',GAIN=10000,t=0;
  slider('r2c',function(v){c=v;upd();},function(v){return fmt(v);});slider('r2f',function(v){f=v;upd();},function(v){return fmt(v);});
  $$('#lv2 [data-rule]').forEach(function(b){b.addEventListener('click',function(){rule=b.dataset.rule;press('#lv2 [data-rule]',b);upd();});});
  function cost(N){var buy=kmin(N)*c,fake=(N+1)*f;return rule==='open'?Math.min(buy,fake):buy;}
  function drawA(){var W=fit(c2,240),H=240,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=64,R=W-24,T=26,B=H-34,max=Math.max(GAIN*2,kmin(21)*c);
    function X(N){return L+(R-L)*(N-3)/18;}function Y(v){return B-(B-T)*Math.min(1,v/max);}
    x.strokeStyle=C.rule;x.beginPath();x.moveTo(L,T);x.lineTo(L,B);x.lineTo(R,B);x.stroke();
    for(var n=3;n<=21;n+=6)txt(x,n+'권',X(n),B+16,{a:'center',s:10,c:C.muted});txt(x,'정직한 장부 수',R,B+30,{a:'right',s:11,c:C.muted});
    [0,max/2,max].forEach(function(v){txt(x,fmt(v),L-6,Y(v)+4,{a:'right',s:10,c:C.muted});});
    x.strokeStyle=C.amber;x.setLineDash([5,4]);x.beginPath();x.moveTo(L,Y(GAIN));x.lineTo(R,Y(GAIN));x.stroke();x.setLineDash([]);txt(x,'위조 이익 10,000원',L+6,Y(GAIN)-6,{s:11,c:C.amber});
    [['진짜 장부 과반 매수',function(N){return kmin(N)*c},C.gfp,false],['가짜 노드로 과반 만들기',function(N){return (N+1)*f},C.eye,rule!=='open']].forEach(function(s,i){x.strokeStyle=s[2];x.lineWidth=2;x.globalAlpha=s[3]?0.3:1;x.beginPath();
      for(var N=3;N<=21;N+=2){var px=X(N),py=Y(s[1](N));N===3?x.moveTo(px,py):x.lineTo(px,py);}x.stroke();x.globalAlpha=1;x.lineWidth=1;x.fillStyle=s[2];x.fillRect(L+10,T+i*16-6,10,3);txt(x,s[0]+(s[3]?' (이 규칙에선 무효)':''),L+26,T+i*16,{s:11});});
    stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c2b,180),H=180,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    for(var i=0;i<9;i++)ledgerIcon(x,W*.62+(i%3)*44,40+Math.floor(i/3)*36,30,22,i<4?'#f3c2bb':'#c9f5dc');txt(x,'등록 장부 9권',W*.62+66,H-14,{a:'center',s:11,c:C.muted});
    var gx=W*.5;x.fillStyle=rule==='reg'?C.amber:'rgba(157,155,184,.3)';x.fillRect(gx-3,30,6,120);txt(x,rule==='reg'?'등록 확인':'문 열림',gx,22,{a:'center',s:11,w:700,c:rule==='reg'?C.amber:C.muted});
    for(var j=0;j<6;j++){var ph=REDUCE?1:((t*0.25+j*0.15)%1),X0=20+j*10,Xt=rule==='reg'?gx-30-j*8:W*.62+(j%3)*44+150,X=X0+(Xt-X0)*Math.min(1,ph*1.4);
      ledgerIcon(x,X,50+j*16,26,18,'#e9a0a0','rgba(120,40,40,.5)');}
    var v=vote(ledgers(9,4,6),rule);txt(x,rule==='reg'?'가짜 6권은 문 앞에서 멈춤 → 원본 '+v.orig+' : 위조 '+v.forged:'가짜 6권도 투표 → 원본 '+v.orig+' : 위조 '+v.forged,12,H-14,{s:12,w:700,c:v.forged>v.orig?C.eye:C.gfp});stamp(x,W,'설명용 장면');}
  function upd(){var N=9,buy=kmin(N)*c,fake=(N+1)*f,need=cost(N),profit=GAIN-need;
    kpis($('#k2'),[[fmt(buy)+'원','진짜 장부 과반 매수 비용 (N=9)','a'],[rule==='open'?fmt(fake)+'원':'무효','가짜 노드 '+(N+1)+'개 비용',rule==='open'?'r':'g'],[fmt(need)+'원','공격자의 최소 비용',need>GAIN?'g':'r'],[(profit>=0?'+':'')+fmt(profit)+'원','공격 손익',profit<0?'g':'r']]);
    $('#eq2').innerHTML='최소 비용 = '+(rule==='open'?'min(<b>'+kmin(N)+' × '+fmt(c)+'</b>, <em>'+(N+1)+' × '+fmt(f)+'</em>)':'<b>'+kmin(N)+' × '+fmt(c)+'</b>')+' = <i>'+fmt(need)+'원</i> · 손익 = 10,000 − '+fmt(need);
    var m=[];if(rule==='reg')m.push(['g','등록된 참여자만 투표하면 가짜 노드는 소용없어요. 과반 매수에 '+fmt(buy)+'원이 들어 '+(buy>GAIN?'공격이 손해예요.':'아직 공격이 이익이에요. 장부 수나 매수 비용이 더 커야 해요.')]);
    else m.push([fake<GAIN?'r':'a','누구나 노드 하나당 한 표라면, 가짜 노드 '+(N+1)+'개('+fmt(fake)+'원)로 과반을 만들 수 있어요. 한 표가 싸면 과반도 싸요.']);
    m.push(['a','하지만 비트코인 같은 열린 망에는 "등록 명부"가 없어요. 그래서 백서는 한 표를 계산력에 묶었어요(2장).']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (정직한 장부)',robo:'주판봇 (고친+가짜)'},higherIsBetter:true,drawMargin:0,
  run:function(){var all=vote(ledgers(9,4,6),'open'),legal=vote(ledgers(9,4,6),'reg');return {fly:legal.orig,robo:all.forged,foul:legal.illegal>0,legal:legal};},
  bar:function(v){return v/12;},fmt:function(v){return v+'표';},
  lesson:'표는 진짜 참여자의 것이어야 한다',foulRule:'"등록된 참여자만 투표한다"는 규칙',
  say:function(r){return '표 수는 초파리 쪽 '+r.fly+'표, 주판봇 쪽 '+r.robo+'표예요. 그런데 주판봇 표 가운데 '+r.legal.illegal+'표는 등록되지 않은 가짜 장부예요. 규칙대로 세면 '+r.legal.orig+' 대 '+r.legal.forged+'로 원본이 이겨요.';}});
}});
