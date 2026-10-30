LAB.start({anchor:'D',init:function(){
var N=12;
function star(){var A=[];for(var i=0;i<N;i++)A.push([]);for(var j=1;j<N;j++){A[0].push(j);A[j].push(0);}return A;}
function lattice(k){var A=[];for(var i=0;i<N;i++){A.push([]);for(var d=1;d<=k;d++){A[i].push((i+d)%N,(i-d+N)%N);}}A.forEach(function(a,i){A[i]=a.filter(function(v,j){return a.indexOf(v)===j;});});return A;}
function stats(A,dead){var alive=[];for(var i=0;i<N;i++)if(!dead[i])alive.push(i);var tot=0,pairs=0,conn=0;
  alive.forEach(function(s){var dist={};dist[s]=0;var q=[s];while(q.length){var u=q.shift();A[u].forEach(function(v){if(dead[v]||dist[v]!==undefined)return;dist[v]=dist[u]+1;q.push(v);});}
    alive.forEach(function(t){if(t<=s)return;pairs++;if(dist[t]!==undefined){conn++;tot+=dist[t];}});});
  return {avg:conn?tot/conn:0,share:pairs?conn/pairs:0,edges:A.reduce(function(a,b){return a+b.length},0)/2,alive:alive.length};}
function randDead(seed,pool){var r=rng(seed),d={},p=pool.slice();for(var i=0;i<3;i++){var j=Math.floor(r()*p.length);d[p[j]]=1;p.splice(j,1);}return d;}
function pos(W,H,i,hub){if(hub&&i===0)return [W/2,H/2];var n=hub?N-1:N,k=hub?i-1:i,a=k/n*Math.PI*2-Math.PI/2,R=Math.min(W*.42,H*.4);return [W/2+Math.cos(a)*R,H/2+Math.sin(a)*R];}
function drawNet(cv,A,dead,hub,H,label){var W=fit(cv,H),x=cv.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
  A.forEach(function(nb,i){nb.forEach(function(j){if(j<i)return;var a=pos(W,H,i,hub),b=pos(W,H,j,hub);x.strokeStyle=(dead[i]||dead[j])?'rgba(157,155,184,.12)':'rgba(130,184,255,.45)';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke();});});
  for(var i=0;i<N;i++){var p=pos(W,H,i,hub),isHub=hub&&i===0;x.fillStyle=dead[i]?'#3a3a4a':isHub?C.info:C.gfp;x.beginPath();x.arc(p[0],p[1],isHub?18:11,0,7);x.fill();
    if(dead[i])txt(x,'✗',p[0],p[1]+5,{a:'center',c:C.eye,w:700});else if(isHub)txt(x,'허브',p[0],p[1]+4,{a:'center',s:11,w:700,c:'#13141f'});}
  txt(x,label,12,H-12,{s:12,c:C.muted});stamp(x,W,'설명용 모형');return W;}

/* ① 허브형 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),A=star(),dead={},hubDown=false,randOn=false,L=[],R=rng(3),t=0;
  function recompute(){dead={};if(hubDown)dead[0]=1;if(randOn){var d=randDead(7,[1,2,3,4,5,6,7,8,9,10,11]);for(var k in d)dead[k]=1;}upd();}
  $('#b1Hub').addEventListener('click',function(){hubDown=!hubDown;this.setAttribute('aria-pressed',hubDown);recompute();});
  $('#b1Rand').addEventListener('click',function(){randOn=!randOn;this.setAttribute('aria-pressed',randOn);recompute();});
  function drawB(dt){t+=dt;var W=fit(c1b,180),H=180,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var hub=[W/2,H/2],leaves=[];for(var i=1;i<N;i++){var X=40+(i-1)*(W-80)/10,Y=i%2?30:H-30;leaves.push([X,Y]);}
    leaves.forEach(function(p,i){x.strokeStyle='rgba(157,155,184,.2)';x.beginPath();x.moveTo(p[0],p[1]);x.lineTo(hub[0],hub[1]);x.stroke();drawSprite(x,dead[i+1]?SPR.d:SPR.a,p[0],p[1],2);});
    x.fillStyle=dead[0]?'#3a3a4a':C.info;rr(x,hub[0]-34,hub[1]-16,68,32,8);x.fill();txt(x,dead[0]?'고장':'터미널',hub[0],hub[1]+5,{a:'center',w:700,s:12,c:'#13141f'});
    if(dt>0&&R()<dt*2.5){var s=Math.floor(R()*11),d=Math.floor(R()*11);if(s!==d&&!dead[s+1])L.push({s:s,d:d,p:0});}
    L.forEach(function(l){var a=leaves[l.s],b=leaves[l.d];if(dead[0]&&l.p>=0.5)l.p=0.5;else l.p+=dt*0.7;
      var X,Y;if(l.p<0.5){X=a[0]+(hub[0]-a[0])*l.p*2;Y=a[1]+(hub[1]-a[1])*l.p*2;}else{X=hub[0]+(b[0]-hub[0])*(l.p-.5)*2;Y=hub[1]+(b[1]-hub[1])*(l.p-.5)*2;}
      if(dead[0]&&l.p===0.5){X=hub[0]-60+((l.s*17)%120);Y=hub[1]+24;}x.fillStyle=dead[0]&&l.p===0.5?C.eye:C.amber;x.fillRect(X-5,Y-3,10,7);});
    L=L.filter(function(l){return l.p<1&&!(dead[l.d+1]&&l.p>0.95);});if(L.length>40)L.splice(0,L.length-40);
    txt(x,dead[0]?'터미널이 멈춰 편지가 쌓인다':'모든 편지가 터미널을 거친다',12,16,{s:12,c:dead[0]?C.eye:C.muted});stamp(x,W,'설명용 모형');}
  function upd(){var s=stats(A,dead);drawNet(c1,A,dead,true,250,'연결 '+s.edges+'개 · 장부 사본 1부(허브)');
    kpis($('#k1'),[[s.avg?s.avg.toFixed(3)+'홉':'—','연결된 쌍의 평균 홉','a'],[(100*s.share).toFixed(0)+'%','서로 닿는 쌍',s.share<0.5?'r':'g'],[s.edges+'개','필요한 연결','m'],[s.alive+'/12','살아 있는 노드','a']]);
    $('#eq1').innerHTML='평균 홉 = (터미널–마을 <b>11쌍 × 1</b> + 마을–마을 <em>55쌍 × 2</em>) ÷ 66 = <i>1.833</i> (고장 없을 때)';
    var m=[];if(dead[0])m.push(['r','터미널 하나가 멈추자 서로 닿는 쌍이 0%가 됐어요. 장부가 터미널에만 있다면 장부도 멈춘 거예요.']);
    else if(randOn)m.push(['a','마을 3곳이 고장 나도 남은 마을끼리는 '+(100*s.share).toFixed(0)+'% 연결돼요. 허브형은 가장자리 고장에는 강해요.']);
    else m.push(['g','고장 없이 평균 1.833홉. 어디서 어디로 가든 한 번만 갈아타면 돼요.']);ins($('#ins1'),m);drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 그물형 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),k=2,A=lattice(2),dead={},top=false,randOn=false,t=0,got={},step=0,timer=0;
  function recompute(){A=lattice(k);dead={};if(top)dead[0]=1;if(randOn){var d=randDead(7,[0,1,2,3,4,5,6,7,8,9,10,11]);for(var q in d)dead[q]=1;}restart();upd();}
  slider('r2k',function(v){k=v;recompute();});
  $('#b2Top').addEventListener('click',function(){top=!top;this.setAttribute('aria-pressed',top);recompute();});
  $('#b2Rand').addEventListener('click',function(){randOn=!randOn;this.setAttribute('aria-pressed',randOn);recompute();});
  function src(){for(var i=0;i<N;i++)if(!dead[(i+3)%N])return (i+3)%N;return 3;}
  function restart(){got={};got[src()]=0;step=0;timer=0;}
  function spread(){var nw=[];Object.keys(got).forEach(function(u){if(got[u]!==step)return;A[u].forEach(function(v){if(!dead[v]&&got[v]===undefined)nw.push(v);});});step++;nw.forEach(function(v){got[v]=step;});return nw.length;}
  var hold=0;function drawB(dt){t+=dt;timer+=dt;if(timer>0.8&&dt>0){timer=0;if(!spread()){hold++;if(hold>2){restart();hold=0;}}}
    if(REDUCE||dt===0&&!Object.keys(got).length){restart();}if(REDUCE)while(spread());
    var W=fit(c2b,190),H=190,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var maxStep=0;for(var i=0;i<N;i++){var X=30+i*(W-60)/11,Y=H/2+(i%2?-30:30);
      var has=got[i]!==undefined;if(dead[i]){x.fillStyle='#3a3a4a';rr(x,X-14,Y-10,28,20,4);x.fill();txt(x,'✗',X,Y+5,{a:'center',c:C.eye,w:700});continue;}
      ledgerIcon(x,X-14,Y-10,28,20,has?'#c9f5dc':'#efe6d2');if(has){maxStep=Math.max(maxStep,got[i]);txt(x,got[i]+'단계',X,Y+28,{a:'center',s:10,c:C.gfp});}}
    var alive=N-Object.keys(dead).length,n=Object.keys(got).length;
    txt(x,'새 기록이 적힌 장부 '+n+'/'+alive+' · '+maxStep+'단계째',12,18,{s:12,c:n===alive?C.gfp:C.amber,w:700});stamp(x,W,'설명용 모형');}
  function upd(){var s=stats(A,dead);drawNet(c2,A,dead,false,250,'연결 '+s.edges+'개 · 장부 사본 '+s.alive+'부');
    kpis($('#k2'),[[s.avg?s.avg.toFixed(3)+'홉':'—','연결된 쌍의 평균 홉','a'],[(100*s.share).toFixed(0)+'%','서로 닿는 쌍',s.share<0.9?'r':'g'],[s.edges+'개','필요한 연결','m'],[s.alive+'부','장부 사본','g']]);
    $('#eq2').innerHTML='이웃 <b>±'+k+'</b>곳씩 → 연결 <em>'+(N*k)+'</em>개, 평균 홉 <i>'+s.avg.toFixed(3)+'</i>';
    var m=[];if(top||randOn)m.push(['g','고장이 나도 남은 마을끼리 '+(100*s.share).toFixed(0)+'% 연결돼요. 돌아갈 길이 있기 때문이에요.']);
    m.push(['a','이웃 ±'+k+'곳씩이면 평균 '+s.avg.toFixed(3)+'홉. 허브형(1.833)과 비교해 보세요. 연결을 늘리면 빨라지지만 길을 더 깔아야 해요.']);ins($('#ins2'),m);drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);restart();upd();})();

Duel({names:{fly:'초파리 (그물형 ±2)',robo:'Money-Robo (허브형)'},higherIsBetter:false,drawMargin:0.01,
  run:function(){return {fly:stats(lattice(2),{}).avg,robo:stats(star(),{}).avg};},bar:function(v){return v/2.5;},fmt:function(v){return v.toFixed(3)+'홉';},
  lesson:'평상시에는 한 곳으로 모으는 쪽이 빠르다',
  say:function(r){return '평균 홉은 초파리 쪽 '+r.fly.toFixed(3)+', Money-Robo 쪽 '+r.robo.toFixed(3)+'이에요. 차이는 '+(r.fly-r.robo).toFixed(3)+'홉, 약 '+Math.round(100*(r.fly/r.robo-1))+'%예요. 고장은 이 대결에서 따지지 않았어요.';}});
}});
