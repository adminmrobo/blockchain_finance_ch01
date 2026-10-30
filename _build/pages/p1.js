LAB.start({anchor:'C',init:function(){
/* ① 잔액 장부 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),bal,log,printed,amt=3000,anim=null,t=0,NM=['A','B','C'];
  function reset(){bal=[10000,10000,10000];log=[];printed=0;anim=null;upd();}
  slider('r1a',function(v){amt=v;});
  $$('#lv1 [data-tx]').forEach(function(b){b.addEventListener('click',function(){var p=b.dataset.tx.split(',').map(Number);
    if(bal[p[0]]<amt){log.unshift({t:NM[p[0]]+' 잔액 부족 — 거절',bad:true});upd();return;}
    bal[p[0]]-=amt;bal[p[1]]+=amt;log.unshift({t:NM[p[0]]+' → '+NM[p[1]]+'  '+fmt(amt)+'원'});anim={s:p[0],d:p[1],p:0};upd();});});
  $('#b1Print').addEventListener('click',function(){bal[0]+=2000;printed+=2000;log.unshift({t:'(기록 없음) A 칸 +2,000',bad:true});upd();});
  $('#b1Reset').addEventListener('click',reset);
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var bw=Math.min(70,W*0.1),L=40;NM.forEach(function(n,i){var X=L+i*(bw+30),h=(H-70)*bal[i]/20000;x.fillStyle=[C.info,C.stain,C.gfp][i];rr(x,X,H-30-h,bw,h,6);x.fill();
      txt(x,n,X+bw/2,H-12,{a:'center',w:700});txt(x,fmt(bal[i]),X+bw/2,H-36-h,{a:'center',s:12});});
    var LX=L+3*(bw+30)+10;x.fillStyle='#efe6d2';rr(x,LX,20,W-LX-20,H-40,8);x.fill();txt(x,'장부 기록',LX+12,40,{c:'#3a3040',w:700});
    log.slice(0,6).forEach(function(l,i){txt(x,l.t,LX+12,64+i*24,{c:l.bad?'#c0301f':'#3a3040',s:13});});
    stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c1b,170),H=170,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var P=[[W*.2,110],[W*.5,110],[W*.8,110]];[SPR.a,SPR.b,SPR.c].forEach(function(s,i){drawSprite(x,s,P[i][0],P[i][1],4,i===2);txt(x,NM[i]+' '+fmt(bal[i]),P[i][0],P[i][1]+44,{a:'center',s:12,w:700});});
    if(anim){anim.p=Math.min(1,anim.p+dt*0.8);if(REDUCE)anim.p=1;var a=P[anim.s],b=P[anim.d],ph=anim.p;coin(x,a[0]+(b[0]-a[0])*ph,a[1]-40-Math.sin(ph*Math.PI)*30,10);}
    if(printed){txt(x,'기록 없는 '+fmt(printed)+'원이 생겨났다',W/2,22,{a:'center',c:C.eye,w:700});coin(x,P[0][0]+30,P[0][1]-30+Math.sin(t*6)*3,8);}
    stamp(x,W,'설명용 장면');}
  function upd(){var tot=bal[0]+bal[1]+bal[2];
    kpis($('#k1'),[[fmt(tot)+'원','세 사람 잔액 합계',tot===30000?'g':'r'],[log.filter(function(l){return !l.bad}).length+'줄','정상 송금 기록','a'],[printed?'+'+fmt(printed)+'원':'0원','기록 없이 생긴 돈',printed?'r':'g'],[tot===30000?'보존':'깨짐','총액 보존',tot===30000?'g':'r']]);
    $('#eq1').innerHTML='송금: <b>보내는 칸 − '+fmt(amt)+'</b>, <em>받는 칸 + '+fmt(amt)+'</em> → 합계 변화 <i>0</i>';
    var m=[];if(printed)m.push(['r','기록 없이 A 칸만 고치자 합계가 '+fmt(tot)+'원이 됐어요. 장부를 고칠 수 있는 쪽은 돈을 만들어 낼 수 있어요.']);
    else m.push(['g','송금을 몇 번 해도 합계는 30,000원 그대로예요. 송금은 장부 두 칸의 숫자를 옮기는 일이에요.']);
    ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',drawA);reset();})();

/* ② 이중 지불 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),chk=0,run=null,t=0,res=null;
  $$('#lv2 [data-chk]').forEach(function(b){b.addEventListener('click',function(){chk=+b.dataset.chk;press('#lv2 [data-chk]',b);res=null;run=null;upd();});});
  $('#b2Copy').addEventListener('click',function(){run={p:0};res=chk?[true,false]:[true,true];upd();});
  $('#b2Reset').addEventListener('click',function(){run=null;res=null;upd();});
  function drawA(){var W=fit(c2,220),H=220,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    x.fillStyle=C.amber;rr(x,30,90,70,44,6);x.fill();txt(x,'쿠폰 #0417',65,117,{a:'center',s:12,w:700,c:'#13141f'});txt(x,'원본 파일',65,150,{a:'center',s:11,c:C.muted});
    [[W*.45,50,'사본 1'],[W*.45,150,'사본 2']].forEach(function(c){x.strokeStyle=C.muted;x.setLineDash([4,4]);x.beginPath();x.moveTo(100,112);x.lineTo(c[0],c[1]+20);x.stroke();x.setLineDash([]);
      x.fillStyle='rgba(241,182,70,.7)';rr(x,c[0],c[1],70,40,6);x.fill();txt(x,'#0417',c[0]+35,c[1]+25,{a:'center',s:12,w:700,c:'#13141f'});txt(x,c[2],c[0]+35,c[1]-6,{a:'center',s:11,c:C.muted});});
    ['가게 1','가게 2'].forEach(function(s,i){var X=W*.75,Y=40+i*100;x.fillStyle=C.panel2;rr(x,X,Y,W*.2,50,8);x.fill();txt(x,s,X+W*.1,Y+22,{a:'center',w:700});
      var r=res?(res[i]?'승인':'거절: 이미 사용'):'대기';txt(x,r,X+W*.1,Y+40,{a:'center',s:12,c:res?(res[i]?(i===1?C.eye:C.gfp):C.gfp):C.muted});});
    if(chk){x.fillStyle='#efe6d2';rr(x,W*.75-150,H-50,140,40,6);x.fill();txt(x,'공유 기록부: #0417 '+(res?'사용됨':'미사용'),W*.75-80,H-25,{a:'center',s:11,c:'#3a3040',w:700});}
    stamp(x,W,'설명용 장면');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    drawSprite(x,SPR.d,60,100,4);txt(x,'손님',60,148,{a:'center',s:12});
    [[W*.6,50],[W*.6,120]].forEach(function(s,i){x.fillStyle=C.panel2;rr(x,s[0],s[1]-18,90,36,6);x.fill();txt(x,'가게 '+(i+1),s[0]+45,s[1]+5,{a:'center',w:700});});
    if(run){run.p=Math.min(1,run.p+dt*0.7);if(REDUCE)run.p=1;[[W*.6,50],[W*.6,120]].forEach(function(s,i){var X=80+(s[0]-90)*run.p,Y=100+(s[1]-100)*run.p;x.fillStyle=C.amber;x.fillRect(X,Y-8,22,16);
      if(run.p>=1){txt(x,res[i]?'승인 ✓':'거절 ✗',s[0]+110,s[1]+5,{c:res[i]?(i===1?C.eye:C.gfp):C.gfp,w:700});}});
      if(run.p>=1)txt(x,res[1]?'쿠폰 한 장으로 두 번 결제됨 — 가게 2의 손해':'두 번째 결제는 기록부에서 걸러짐',W/2,22,{a:'center',c:res[1]?C.eye:C.gfp,w:700});}
    else txt(x,'빨간 버튼을 눌러 같은 쿠폰을 두 가게에 동시에 써 보세요',W/2,22,{a:'center',c:C.muted});
    stamp(x,W,'설명용 장면');}
  function upd(){var ok=res?res.filter(Boolean).length:0;
    kpis($('#k2'),[['1장','실제 쿠폰'],[res?ok+'건':'—','받아들여진 결제',res?(ok>1?'r':'g'):'a'],[res?(ok-1)+'건':'—','이중 지불 손해',res?(ok>1?'r':'g'):'a'],[chk?'공유 기록부':'없음','가게의 확인 수단','m']]);
    $('#eq2').innerHTML='통과하는 결제 = <b>'+(chk?'1':'사본 수')+'</b> '+(chk?'(공유 기록부가 두 번째를 거절)':'(파일만 보면 사본도 원본과 같다)');
    var m=[];if(!res)m.push(['a','지금 방식: '+(chk?'결제 전 공유 기록부 확인':'파일만 보고 받기')+'. 빨간 버튼으로 이중 지불을 시도해 보세요.']);
    else if(ok>1)m.push(['r','같은 쿠폰이 두 가게에서 모두 승인됐어요. 디지털 파일은 원본과 사본을 구별할 수 없어요.']);
    else m.push(['g','두 번째 결제가 "이미 사용"으로 거절됐어요. 두 가게가 같은 기록부를 보기 때문이에요.']);
    ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',drawA);upd();})();

/* 대결 */
function sim(check){var r=rng(101),dup=0;for(var i=0;i<100;i++){if(r()<0.3){if(!check)dup++;}}return dup;}
Duel({names:{fly:'초파리 (기록부 확인)',robo:'Money-Robo (즉시 승인)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:sim(true),robo:sim(false)};},bar:function(v){return v/40;},fmt:function(v){return v+'건';},
  lesson:'같은 기록을 확인해야 같은 돈을 두 번 못 쓴다',
  say:function(r){return '가게가 받아 준 중복 결제는 초파리 쪽 '+r.fly+'건, Money-Robo 쪽 '+r.robo+'건이에요. 손님 100명 중 중복 사용을 시도한 '+r.robo+'명이 Money-Robo 방식에서는 전부 통과했어요.';}});
}});
