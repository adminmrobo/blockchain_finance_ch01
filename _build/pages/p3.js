LAB.start({anchor:'D',init:function(){
var TAU=14;function pm(t){return Math.exp(-t/TAU);}
function curve(cv,H,fns,tMark,label){var W=fit(cv,H),x=cv.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
  var L=48,R=W-20,T=24,B=H-32;x.strokeStyle=C.rule;x.beginPath();x.moveTo(L,T);x.lineTo(L,B);x.lineTo(R,B);x.stroke();
  [0,0.5,1].forEach(function(v){txt(x,Math.round(v*100)+'%',L-6,B-(B-T)*v+4,{a:'right',s:10,c:C.muted});});
  for(var d=0;d<=60;d+=10)txt(x,d+'일',L+(R-L)*d/60,B+16,{a:'center',s:10,c:C.muted});
  fns.forEach(function(f){x.strokeStyle=f.c;x.lineWidth=2;x.setLineDash(f.dash||[]);x.beginPath();for(var t=0;t<=60;t++){var X=L+(R-L)*t/60,Y=B-(B-T)*f.fn(t);t?x.lineTo(X,Y):x.moveTo(X,Y);}x.stroke();x.setLineDash([]);x.lineWidth=1;
    var Y=B-(B-T)*f.fn(tMark);x.fillStyle=f.c;x.beginPath();x.arc(L+(R-L)*tMark/60,Y,4,0,7);x.fill();});
  x.strokeStyle='rgba(241,182,70,.6)';x.beginPath();x.moveTo(L+(R-L)*tMark/60,T);x.lineTo(L+(R-L)*tMark/60,B);x.stroke();
  var lx=L+10;fns.forEach(function(f,i){x.fillStyle=f.c;x.fillRect(lx,T+i*16-6,10,3);txt(x,f.name,lx+16,T+i*16,{s:11});});stamp(x,W,label);}

/* ① 기억 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),t=7,lie=false;
  slider('r1t',function(v){t=v;upd();});
  $('#b1Lie').addEventListener('click',function(){lie=!lie;this.setAttribute('aria-pressed',lie);upd();});
  function drawB(){var W=fit(c1b,180),H=180,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var ax=W*.3,bx=W*.7,y=130,p=pm(t);drawSprite(x,SPR.a,ax,y,4,false);drawSprite(x,SPR.b,bx,y,4,true);
    [[ax,lie?'5,000원이었지':'10,000원','A의 기억',lie?1:p],[bx,'10,000원','B의 기억',p]].forEach(function(b){x.globalAlpha=Math.max(0.12,b[3]);x.fillStyle=C.panel2;x.beginPath();x.ellipse(b[0],50,90,30,0,0,7);x.fill();
      txt(x,b[1],b[0],56,{a:'center',s:17,w:700,c:lie&&b[2]==='A의 기억'?C.eye:C.text});x.globalAlpha=1;txt(x,b[2],b[0],98,{a:'center',s:11,c:C.muted});});
    txt(x,t+'일 뒤',W/2,24,{a:'center',w:700,c:C.amber});stamp(x,W,'설명용 장면');}
  function upd(){var p=pm(t),both=p*p;curve(c1,230,[{fn:pm,c:C.info,name:'한 사람이 정확히 기억'},{fn:function(d){return pm(d)*pm(d)},c:C.stain,name:'두 사람 모두 정확히 기억'}],t,'설명용 가정 · 기억 반감 약 10일');
    kpis($('#k1'),[[(100*p).toFixed(0)+'%','한 사람이 정확히 기억 (예시값)','a'],[(100*both).toFixed(1)+'%','두 사람 모두 정확',both<0.3?'r':'g'],[lie?'불가':'—','거짓말 가려내기',lie?'r':'a'],['0줄','남은 기록','r']]);
    $('#eq1').innerHTML='p(t) = e<sup>−t/14</sup> = <b>'+p.toFixed(3)+'</b> · 둘 다: p × p = <em>'+both.toFixed(3)+'</em> (t = <i>'+t+'</i>일)';
    var m=[];if(lie)m.push(['r','A가 "5,000원이었지"라고 하면, B의 기억과 엇갈려도 증명할 기록이 없어요.']);
    m.push([both<0.3?'r':'a',t+'일 뒤 두 사람이 같은 금액을 기억할 확률은 약 '+(100*both).toFixed(0)+'%예요. 한 사람 기준('+(100*p).toFixed(0)+'%)보다 빨리 떨어져요.']);ins($('#ins1'),m);drawB();}
  addEventListener('resize',upd);upd();})();

/* ② 각자 장부 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),lam=0.03,forge=false,check=true,T=30;
  slider('r2l',function(v){lam=v/100;upd();});
  $('#b2Forge').addEventListener('click',function(){forge=!forge;this.setAttribute('aria-pressed',forge);upd();});
  $('#b2Check').addEventListener('click',function(){check=!check;this.setAttribute('aria-pressed',check);upd();});
  function surv(t){return Math.pow(1-lam,t/30);}
  function drawB(){var W=fit(c2b,190),H=190,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var bw=Math.min(220,W*.3);[[W*.28,'A의 수첩',forge?'5,000원':'10,000원',forge],[W*.72,'B의 수첩','10,000원',false]].forEach(function(b){var X=b[0]-bw/2;
      x.fillStyle='#efe6d2';rr(x,X,40,bw,110,8);x.fill();x.strokeStyle='rgba(120,100,80,.3)';for(var i=1;i<5;i++){x.beginPath();x.moveTo(X+10,40+i*22);x.lineTo(X+bw-10,40+i*22);x.stroke();}
      txt(x,b[1],b[0],30,{a:'center',w:700});txt(x,'10/28  A가 B에게 빌림',X+12,78,{c:'#3a3040',s:12});txt(x,b[2],X+12,104,{c:b[3]?'#c0301f':'#3a3040',s:17,w:700});});
    if(check){var diff=forge;txt(x,diff?'≠ 다르다! 그런데 누가 고쳤지?':'= 같다',W/2,104,{a:'center',w:700,c:diff?C.eye:C.gfp});}
    stamp(x,W,'설명용 장면');}
  function upd(){var s=surv(T),both=s*s,mem=pm(T)*pm(T);
    curve(c2,230,[{fn:function(d){return surv(d)*surv(d)},c:C.gfp,name:'장부 두 권 모두 남음'},{fn:function(d){return pm(d)*pm(d)},c:C.stain,name:'기억 두 사람 모두 정확',dash:[5,4]}],T,'예시값');
    kpis($('#k2'),[[(100*both).toFixed(1)+'%','30일 뒤 두 권 모두 남음','g'],[(100*mem).toFixed(1)+'%','같은 기간 기억 둘 다 정확','r'],[forge?(check?'발견':'못 봄'):'—','조작 흔적',forge?(check?'a':'r'):'a'],[forge?'불가':'—','누가 맞는지 판정',forge?'r':'a']]);
    $('#eq2').innerHTML='두 권 보존 = (1 − <i>'+(lam*100).toFixed(0)+'%</i>)<sup>30/30</sup> × 같은 값 = <b>'+both.toFixed(3)+'</b>';
    var m=[];m.push(['g','30일 뒤 장부 두 권이 모두 남아 있을 확률 '+(100*both).toFixed(0)+'% — 기억('+(100*mem).toFixed(0)+'%)보다 훨씬 높아요.']);
    if(forge&&check)m.push(['a','서로 확인해서 금액이 다르다는 건 알았어요. 하지만 수첩만으로는 A와 B 중 누가 고쳤는지 정할 수 없어요.']);
    if(forge&&!check)m.push(['r','확인 절차가 없으면 A가 고친 사실조차 드러나지 않아요.']);ins($('#ins2'),m);drawB();}
  addEventListener('resize',upd);upd();})();

function sim(ledger){var r=rng(303),ok=0;for(var i=0;i<100;i++){var a=r(),b=r();var p=ledger?Math.pow(0.97,1):pm(30);if(a<p&&b<p)ok++;}return ok;}
Duel({names:{fly:'초파리 (각자 장부)',robo:'주판봇 (기억)'},higherIsBetter:true,drawMargin:0,
  run:function(){return {fly:sim(true),robo:sim(false)};},bar:function(v){return v/100;},fmt:function(v){return v+'쌍';},
  lesson:'한 달 뒤의 기억은 기록을 이기지 못한다',
  say:function(r){return '30일 뒤 두 사람 기록이 모두 정확한 쌍은 초파리 쪽 '+r.fly+'쌍, 주판봇 쪽 '+r.robo+'쌍이에요. 100쌍 중이에요. 시드는 303으로 고정했어요.';}});
}});
