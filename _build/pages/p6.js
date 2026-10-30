LAB.start({anchor:'C',init:function(){
/* ① 은행 장부 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),S={n:1000,f:500,hack:false},P=[],R=rng(2);
  slider('r1n',function(v){S.n=v;upd();});slider('r1f',function(v){S.f=v;upd();});
  $('#b1Hack').addEventListener('click',function(){S.hack=!S.hack;this.setAttribute('aria-pressed',S.hack);upd();});
  function drawA(){var W=fit(c1,220),H=220,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var LW=W*0.55;
    for(var i=0;i<8;i++){var a=i/8*Math.PI*2-Math.PI/2,px=LW/2+Math.cos(a)*LW*.36,py=H/2+Math.sin(a)*H*.36;
      x.strokeStyle=S.hack?'rgba(240,96,77,.35)':'rgba(130,184,255,.35)';x.beginPath();x.moveTo(LW/2,H/2);x.lineTo(px,py);x.stroke();x.fillStyle=C.panel2;x.beginPath();x.arc(px,py,11,0,7);x.fill();txt(x,'고객',px,py+24,{a:'center',s:10,c:C.muted});}
    x.fillStyle=S.hack?C.eye:C.info;rr(x,LW/2-30,H/2-20,60,40,8);x.fill();txt(x,S.hack?'해킹됨':'은행 장부',LW/2,H/2+5,{a:'center',w:700,s:12,c:'#13141f'});
    txt(x,'장부 사본: 1부',LW/2,16,{a:'center',s:12,c:C.amber,w:700});
    var X0=LW+20,bw=W-X0-20,day=S.n*S.f,year=day*365,max=5000*2000*365;txt(x,'소비자가 내는 수수료',X0,22,{s:12,c:C.muted});
    [['하루',day],['1년(365일)',year]].forEach(function(b,i){var y=50+i*70,w=Math.max(2,bw*Math.log10(1+b[1])/Math.log10(1+max));x.fillStyle=i?C.stain:C.amber;rr(x,X0,y,w,22,5);x.fill();txt(x,b[0]+' '+fmt(b[1])+'원',X0,y+42,{s:12});});
    txt(x,'(막대 길이는 로그 눈금)',X0,H-10,{s:10,c:C.muted});stamp(x,W,'예시값');}
  function drawB(dt){var W=fit(c1b,190),H=190,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var cx=W/2,cy=H/2,nodes=[];for(var i=0;i<8;i++){var a=i/8*Math.PI*2-Math.PI/2;nodes.push([cx+Math.cos(a)*W*.4,cy+Math.sin(a)*H*.36]);}
    if(dt>0&&R()<S.n/1000*3.6*dt)P.push({s:Math.floor(R()*8),d:Math.floor(R()*8),p:0});
    nodes.forEach(function(n,i){x.strokeStyle='rgba(157,155,184,.2)';x.beginPath();x.moveTo(cx,cy);x.lineTo(n[0],n[1]);x.stroke();drawSprite(x,[SPR.a,SPR.b,SPR.c][i%3],n[0],n[1],2.4);});
    x.fillStyle=S.hack?C.eye:C.info;rr(x,cx-30,cy-18,60,36,8);x.fill();txt(x,S.hack?'멈춤':'은행',cx,cy+5,{a:'center',w:700,s:12,c:'#13141f'});
    P.forEach(function(q){var A=nodes[q.s],B=nodes[q.d],X,Y;if(S.hack&&q.p>=0.5)q.p=0.5;else q.p+=dt*0.6;
      if(q.p<0.5){X=A[0]+(cx-A[0])*q.p*2;Y=A[1]+(cy-A[1])*q.p*2;}else{X=cx+(B[0]-cx)*(q.p-0.5)*2;Y=cy+(B[1]-cy)*(q.p-0.5)*2;}
      if(S.hack&&q.p===0.5){X=cx+((q.s*13)%40-20);Y=cy+30+((q.s*7)%14);}x.fillStyle=S.hack&&q.p===0.5?C.eye:C.amber;x.fillRect(X-4,Y-3,8,6);});
    P=P.filter(function(q){return q.p<1;});if(P.length>60)P.splice(0,P.length-60);
    txt(x,S.hack?'멈춘 거래 꾸러미: '+P.length+'개':'모든 거래가 가운데를 지나간다',12,H-10,{s:12,c:S.hack?C.eye:C.muted});stamp(x,W,'설명용 모형');}
  function upd(){var day=S.n*S.f;kpis($('#k1'),[['1부','장부 사본 수','a'],[fmt(day)+'원','하루 수수료 총액 (예시값)','m'],[fmt(day*365)+'원','1년 총액 (예시값)','m'],[S.hack?'0%':'100%','처리 가능한 거래',S.hack?'r':'g']]);
    $('#eq1').innerHTML='하루 수수료 = <b>'+fmt(S.n)+'건</b> × <i>'+fmt(S.f)+'원</i> = <em>'+fmt(day)+'원</em>';
    var m=[['a','믿음을 기관 한 곳에서 사면, 그 값(보안 투자·인력)은 수수료로 돌아와요.']];
    m.push(S.hack?['r','은행 장부 하나가 뚫리자 모든 거래가 멈췄어요. 장부가 한 곳에만 있으면 그곳이 단일 실패 지점이에요.']:['g','지금은 빠르고 편하고, 다툼이 생겨도 은행 기록으로 바로 판정해요. "은행 장부 해킹"을 눌러 보세요.']);
    ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 가동률 */
function comb(n,k){var r=1;for(var i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
function majUp(n,a){var s=0;for(var k=Math.floor(n/2)+1;k<=n;k++)s+=comb(n,k)*Math.pow(a,k)*Math.pow(1-a,n-k);return s;}
(function(){var c2=$('#c2'),c2b=$('#c2b'),a=0.99,n=7;
  slider('r2a',function(v){a=v/100;upd();});slider('r2n',function(v){n=v;upd();});
  function hrs(p){return (1-p)*8760;}function fmtH(h){return h>=1?h.toFixed(1)+'시간':(h*3600>=1?(h*3600).toFixed(1)+'초':(h*3600).toExponential(1)+'초');}
  function drawA(){var W=fit(c2,210),H=210,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var rows=[['중앙 서버 1대',a,C.info],['노드 '+n+'대 중 과반',majUp(n,a),C.gfp]],L=130,bw=W-L-160;
    rows.forEach(function(r,i){var y=40+i*70,down=hrs(r[1]),w=Math.max(2,bw*Math.min(1,Math.log10(1+down*3600)/Math.log10(1+876*3600)));
      txt(x,r[0],12,y+16,{w:700});x.fillStyle=r[2];rr(x,L,y,w,22,5);x.fill();txt(x,'1년 정지 '+fmtH(down),L+w+8,y+16,{s:12,w:700});txt(x,'가동률 '+(100*r[1]).toFixed(6)+'%',L,y+42,{s:11,c:C.muted});});
    txt(x,'(막대 = 1년 기대 정지 시간, 로그 눈금)',12,H-10,{s:11,c:C.muted});stamp(x,W,'예시값 · 독립 고장 가정');}
  function drawB(){var W=fit(c2b,190),H=190,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var r=rng(66),cols=73,cw=(W-24)/cols;
    [['중앙 서버',function(){return r()<a;}],['과반 방식',function(){var up=0;for(var i=0;i<n;i++)if(r()<a)up++;return up>n/2;}]].forEach(function(row,ri){var down=0;
      txt(x,row[0],12,ri*66+44,{s:12,w:700});for(var d=0;d<365;d++){var ok=row[1](),c=d%cols,rw=Math.floor(d/cols);if(!ok)down++;x.fillStyle=ok?'rgba(94,227,156,.35)':C.eye;x.fillRect(12+c*cw,ri*66+52+rw*7,cw-1,6);}
      txt(x,'멈춘 날 '+down+'일',W-12,ri*66+44,{a:'right',s:12,c:down?C.eye:C.gfp,w:700});});
    stamp(x,W,'예시값');}
  function upd(){var m1=majUp(n,a);kpis($('#k2'),[[fmtH(hrs(a)),'중앙 서버 1년 정지','r'],[fmtH(hrs(m1)),'노드 '+n+'대 과반 방식 1년 정지','g'],[(Math.floor(n/2)+1)+'대','살아 있어야 할 노드','a'],[n+'배','유지할 장비 수 (대략)','m']]);
    $('#eq2').innerHTML='P(과반 살아 있음) = Σ<sub>k&gt;'+(n/2)+'</sub> C('+n+',k) · <i>'+a.toFixed(3)+'</i><sup>k</sup> · (1−'+a.toFixed(3)+')<sup>'+n+'−k</sup> = <b>'+m1.toFixed(9)+'</b>';
    ins($('#ins2'),[['g','같은 성능의 장비라도, 과반만 살아 있으면 되는 방식은 한꺼번에 멈출 확률이 훨씬 작아요.'],['a','대신 장비가 '+n+'배로 늘고, 여러 노드가 서로 확인하느라 처리가 느려질 수 있어요. 그리고 고장이 서로 독립이라는 가정은 현실에서 자주 깨져요.']]);drawA();drawB();}
  addEventListener('resize',upd);upd();})();

function sim(peer){var r=rng(606),ok=0;for(var i=0;i<1000;i++){if(peer){var both=r()<0.94,sloppy=r()<0.7;if(both&&sloppy)ok++;}else{if(r()<0.999)ok++;}}return ok/1000;}
Duel({names:{fly:'초파리 (각자 기록)',robo:'Money-Robo (은행 장부)'},higherIsBetter:true,drawMargin:0.005,
  run:function(){return {fly:sim(true),robo:sim(false)};},bar:function(v){return v;},fmt:function(v){return (100*v).toFixed(1)+'%';},
  lesson:'당사자 밖의 기준 장부가 다툼을 끝낸다',
  say:function(r){return '분쟁 1,000건 중 판정 가능한 비율은 초파리 쪽 '+(100*r.fly).toFixed(1)+'%, Money-Robo 쪽 '+(100*r.robo).toFixed(1)+'%예요. 초파리 쪽은 사본이 사라졌거나 꼼꼼한 위조였던 건을 가리지 못했어요.';}});
}});
