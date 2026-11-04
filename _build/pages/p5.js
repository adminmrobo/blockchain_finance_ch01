LAB.start({anchor:'D',init:function(){
function binomTail(n,p){var s=0;for(var k=Math.floor(n/2)+1;k<=n;k++){s+=comb(n,k)*Math.pow(p,k)*Math.pow(1-p,n-k);}return s;}
function comb(n,k){var r=1;for(var i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
function wrong(n,p,c){return c+(1-c)*binomTail(n,p);}

/* ① 증인 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),n=3,p=0.1,c=0.05;
  slider('r1n',function(v){n=v;upd();});slider('r1p',function(v){p=v/100;upd();});slider('r1c',function(v){c=v/100;upd();});
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var L=56,B=H-34,T=30,ns=[1,3,5,7,9],bw=(W-L-40)/ns.length,max=Math.max(0.5,wrong(1,p,c));
    x.strokeStyle=C.rule;x.beginPath();x.moveTo(L,T);x.lineTo(L,B);x.lineTo(W-20,B);x.stroke();
    ns.forEach(function(k,i){var v=wrong(k,p,c),vi=binomTail(k,p),h=(B-T)*v/max,X=L+i*bw+bw*.2,w=bw*.6;
      x.fillStyle=k===n?C.eye:'rgba(240,96,77,.35)';rr(x,X,B-h,w,h,4);x.fill();
      var hc=(B-T)*c/max;x.fillStyle='rgba(241,182,70,.55)';x.fillRect(X,B-hc,w,hc);
      txt(x,(100*v).toFixed(1)+'%',X+w/2,B-h-6,{a:'center',s:11,w:k===n?700:500});txt(x,k+'명',X+w/2,B+16,{a:'center',s:11,c:C.muted});});
    x.fillStyle='rgba(241,182,70,.55)';x.fillRect(L+10,T-14,10,8);txt(x,'공모 몫 (증인을 늘려도 그대로)',L+26,T-6,{s:11});
    txt(x,'막대 = 틀린 증언이 채택될 확률',L+230,T-6,{s:11,c:C.muted});stamp(x,W,'예시값');}
  function drawB(){var W=fit(c1b,200),H=200,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var r=rng(55),wrongN=0,cols=10,cw=(W-40)/cols;
    for(var t=0;t<20;t++){var col=t%cols,row=Math.floor(t/cols),X=20+col*cw,Y=30+row*84,coll=r()<c,lies=0;
      for(var i=0;i<n;i++){var lie=coll||r()<p;if(lie)lies++;x.fillStyle=lie?C.eye:C.gfp;x.fillRect(X+6+(i%5)*9,Y+(Math.floor(i/5))*10,7,7);}
      var bad=lies>n/2;if(bad)wrongN++;x.strokeStyle=bad?C.eye:'rgba(94,227,156,.4)';rr(x,X+2,Y-6,cw-6,62,6);x.stroke();
      txt(x,bad?'오판':'바른 판정',X+cw/2-2,Y+44,{a:'center',s:11,c:bad?C.eye:C.gfp,w:700});if(coll)txt(x,'공모',X+cw/2-2,Y+30,{a:'center',s:10,c:C.amber});}
    txt(x,'재판 20건 중 오판 '+wrongN+'건 · 칸 하나 = 증인 한 명 (초록 참, 빨강 거짓)',12,H-8,{s:12,c:C.muted});stamp(x,W,'예시값');return wrongN;}
  function upd(){drawA();var wn=drawB(),v=wrong(n,p,c),vi=binomTail(n,p);
    kpis($('#k1'),[[(100*v).toFixed(2)+'%','틀린 증언이 채택될 확률',v>0.05?'r':'g'],[(100*vi).toFixed(2)+'%','공모가 없을 때',vi>0.05?'r':'g'],[(100*c).toFixed(0)+'%','줄지 않는 공모 몫','a'],[wn+'/20','표본 재판의 오판','m']]);
    $('#eq1').innerHTML='P(틀림) = <i>c</i> + (1 − c) × P(거짓말 &gt; '+n+'/2) = <i>'+c.toFixed(2)+'</i> + '+(1-c).toFixed(2)+' × <b>'+vi.toFixed(4)+'</b> = <em>'+v.toFixed(4)+'</em>';
    var m=[];if(c>0&&n>=5)m.push(['a','증인을 '+n+'명으로 늘려 독립적인 거짓말 위험은 '+(100*vi).toFixed(2)+'%까지 줄었지만, 공모 '+(100*c).toFixed(0)+'%는 그대로 남아요.']);
    else m.push(['m','증인 '+n+'명, 거짓말 '+(100*p).toFixed(0)+'%, 공모 '+(100*c).toFixed(0)+'%일 때 틀린 증언이 채택될 확률은 '+(100*v).toFixed(1)+'%예요.']);
    if(c===0)m.push(['g','공모가 없으면 증인을 늘릴수록 빠르게 안전해져요. 독립성이 다수결의 조건이에요.']);ins($('#ins1'),m);}
  addEventListener('resize',upd);upd();})();

/* ② 공증 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),e=0.005,fee=20000,t=0;
  slider('r2e',function(v){e=v/100;upd();});slider('r2f',function(v){fee=v;upd();},function(v){return fmt(v);});
  function rows(){return [['증인 1명',wrong(1,0.1,0.05),0],['증인 3명',wrong(3,0.1,0.05),0],['증인 5명',wrong(5,0.1,0.05),0],['공증',e,fee]];}
  function drawA(){var W=fit(c2,220),H=220,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var R=rows(),L=90,bw=(W-L-170);
    R.forEach(function(r,i){var y=24+i*46,w=Math.max(2,bw*r[1]/0.15);txt(x,r[0],12,y+16,{s:13,w:700});x.fillStyle=i===3?C.info:C.eye;rr(x,L,y,Math.min(bw,w),22,5);x.fill();
      txt(x,(100*r[1]).toFixed(2)+'%',L+Math.min(bw,w)+8,y+16,{s:12,w:700});txt(x,r[2]?'수수료 '+fmt(r[2])+'원':'수수료 0원',W-12,y+16,{a:'right',s:12,c:C.muted});});
    txt(x,'증인: 거짓 10% · 공모 5% (예시값)',12,H-8,{s:11,c:C.muted});stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var ox=W/2;x.fillStyle=C.panel2;rr(x,ox-70,40,140,90,10);x.fill();txt(x,'공증 사무소',ox,60,{a:'center',w:700});drawSprite(x,SPR.d,ox,100,3);
    var ph=REDUCE?0.99:(t*0.35)%1,X;if(ph<0.4)X=60+(ox-130)*ph/0.4;else if(ph<0.6)X=ox-20;else X=ox+70+(W-ox-130)*(ph-0.6)/0.4;
    x.fillStyle='#efe6d2';rr(x,X,ph<0.4||ph>=0.6?110:70,40,30,4);x.fill();if(ph>=0.5){x.strokeStyle='#c0301f';x.lineWidth=2;x.beginPath();x.arc(X+28,(ph>=0.6?110:70)+15,7,0,7);x.stroke();x.lineWidth=1;}
    txt(x,'건당 '+fmt(fee)+'원 · 만 원 거래라면 수수료가 금액의 '+(fee/100).toFixed(0)+'%',W/2,H-10,{a:'center',s:12,c:fee>=10000?C.eye:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var w3=wrong(3,0.1,0.05);drawA();
    kpis($('#k2'),[[(100*w3).toFixed(2)+'%','증인 3명이 틀릴 확률','r'],[(100*e).toFixed(2)+'%','공증이 틀릴 확률 (예시값)','g'],[fmt(fee)+'원','공증 수수료 (예시값)','a'],[(w3/Math.max(e,1e-9)).toFixed(1)+'배','증인 3명 ÷ 공증','m']]);
    $('#eq2').innerHTML='증인 3명 <em>'+w3.toFixed(4)+'</em> vs 공증 <b>'+e.toFixed(4)+'</b> · 대가: 건당 <i>'+fmt(fee)+'원</i>';
    var m=[['g','공증은 권한과 책임으로 틀릴 확률을 크게 낮춰요(이 모형에서 증인 3명의 약 '+Math.round(w3/Math.max(e,1e-9))+'분의 1).'],['a','대신 건당 '+fmt(fee)+'원이 들어요. 작은 거래에는 믿음의 값이 거래보다 비싸져요.']];ins($('#ins2'),m);drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (증인 3명)',robo:'주판봇 (공증)'},higherIsBetter:false,drawMargin:0.001,
  run:function(){return {fly:wrong(3,0.1,0.05),robo:0.005};},bar:function(v){return v/0.1;},fmt:function(v){return (100*v).toFixed(2)+'%';},
  lesson:'머릿수보다 책임지는 증명이 덜 틀린다',
  say:function(r){return '틀린 기록이 인정될 확률은 초파리 쪽 '+(100*r.fly).toFixed(2)+'%, 주판봇 쪽 '+(100*r.robo).toFixed(2)+'%예요. 초파리 쪽 7.66% 가운데 5%는 공모 몫이라 증인을 늘려도 줄지 않아요.';}});
}});
