LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '1-02', 'slug': 'central-vs-distributed', 'key': '1_02', 'anchor': 'D',
 'tab_title': '중앙과 분산 네트워크', 'meta_title': '중앙집중식 vs 분산 — 장부를 어디에 둘까',
 'description': '터미널 하나로 모이는 길과 마을끼리 이어진 길을 비교하며, 중앙집중식과 분산 네트워크의 속도와 튼튼함을 직접 재 보는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.5',
 'h1': '중앙집중식 vs 분산<br>— 장부를 어디에 둘까', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '장부를 한 곳에 모으면 빠르고, 여러 곳에 나누면 튼튼하다. 정말 그럴까? 얼마나?',
 'lead': '1-01에서 "모두가 같은 기록을 봐야 한다"는 결론에 닿았습니다. 그 기록을 한 곳에 둘 수도, 모두가 나눠 가질 수도 있어요. 이 편에서는 장부 내용은 잠시 두고, 참여자들이 어떤 모양으로 연결되는지만 비교합니다.',
 'kpis': [('1곳', '중앙집중식: 장부와 처리가 모이는 곳', 'r', [1]), ('모두 동등', '분산: 참여자 연결 방식', 'g', [1]),
          ('빠름', '중앙집중식의 처리 속도', 'a', [1]), ('수수료·보안', '중앙집중식의 약점', 'm', [1])],
 'hero': [('doc', 'think', 'doc_e09', '고속버스 터미널 하나로 모든 노선이 모이는 도시와, 마을끼리 길이 거미줄처럼 이어진 시골. 어느 쪽이 빠르고 어느 쪽이 튼튼할까요?'),
          ('asst', 'smile', 'asst_e13', '마을 12곳으로 두 가지 길을 만들어 놨어요. 평균 몇 번 갈아타는지 제가 세어 볼게요.'),
          ('fly', 'point', 'fly_e08', '터미널이 문 닫으면 어떻게 되는데? 그것부터 보자.'),
          ('robo', 'coin', 'robo_e16', '한 곳에 모으면 효율 최고지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '거리를 재고 숫자를 발표한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 고장 난 뒤를 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 평상시 속도에 건다.')],
 'why_title': '왜 연결 모양부터 보나',
 'why_lead': '장부를 지키는 방법(1-03~1-07)은 결국 "장부가 어디에, 몇 부 있나"의 문제예요. 그 바탕이 되는 연결 모양을 먼저 익혀 둡니다.',
 'why': [('강의 자료의 비교', '블록체인은 데이터를 분산 저장하고 모든 참여자가 동등하게 연결된다. 중앙 집중식은 처리 속도가 빠르지만 수수료와 보안 문제가 있다. <sup>[1]</sup>'),
         ('같은 마을, 다른 길', '마을 12곳(노드)을 두 가지 방식으로 잇는다. 터미널 하나를 거치는 허브형과, 이웃끼리 잇는 그물형.'),
         ('두 가지를 잰다', '평상시 평균 몇 번 건너야 하나(홉), 그리고 어딘가 고장 나면 몇 쌍이 끊기나.')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 빠름과 튼튼함은 같은 길에서 한꺼번에 얻기 어려워요. 이 편은 그 맞바꿈을 숫자로 보는 편이에요.'),
 'big_lead': '1-01이 "모두가 같은 기록을 봐야 한다"를 보였다면, 이 편은 "그 기록을 어디에 두나"의 두 가지 모양을 비교합니다. 1-03부터는 실제 장부 지키기의 역사를 처음부터 따라갑니다.',
 'ladder': [('①', '허브형 (중앙집중식)', '모두가 한 번 갈아타면 닿는다, 빠르다', '허브가 멈추면 전부 끊긴다'),
            ('②', '그물형 (분산)', '어느 한 곳이 멈춰도 길이 남는다', '길이 늘어 느려지고, 모두의 장부를 맞추는 방법이 필요하다 → 1-03~1-07')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '허브형', 'title': '모두 터미널을 거친다 — 허브형',
   'tags': [('구조: 가운데 노드 하나에 모두 연결', 'g'), ('일상: 고속버스 터미널', '')],
   'left': '<p>모든 버스가 터미널 하나로 들어왔다 나간다. 어느 마을에서 어느 마을로 가든 터미널에서 한 번 갈아타면 된다. 대신 터미널이 문을 닫으면 아무 데도 못 간다.</p>',
   'right': '<p><span class="jt" data-t="중앙집중식">중앙집중식</span> 시스템은 장부와 처리를 한 곳(은행, 중앙 서버)에 모은다. 처리 속도가 빠르지만 거래 비용(수수료)과 보안 문제가 있다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 터미널 하나, 마을 11곳</h3>
    <div class="cwrap"><canvas id="c1" aria-label="가운데 허브와 둘레 마을 11곳이 연결된 그림. 고장 난 곳은 회색"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">고장</span>
      <button class="bt warn" id="b1Hub" aria-pressed="false">터미널(허브) 고장</button><button class="bt warn" id="b1Rand" aria-pressed="false">마을 3곳 무작위 고장</button></div></div>
    <h3>행동으로 보기 — 편지가 터미널을 거쳐 간다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="편지가 마을에서 터미널을 거쳐 다른 마을로 가는 애니메이션"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 짧은 길, 하나뿐인 길목</h4>
    <ol><li>마을끼리는 늘 2홉(마을→터미널→마을), 터미널과 마을은 1홉. 12곳 전체 평균은 1.83홉이다.</li>
      <li>마을 몇 곳이 고장 나도 나머지는 멀쩡하다. 하지만 터미널 하나가 멈추면 연결된 쌍이 0이 된다.</li>
      <li>장부도 마찬가지다. 터미널(중앙)에만 장부가 있으면 그곳이 <span class="jt" data-t="단일 실패 지점">단일 실패 지점</span>이 된다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 빠르지만, 한 곳이 멈추면 전부 멈추고 그 한 곳이 공격 목표가 된다. → 길을 여러 갈래로 나누자.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '마을 세 곳 고장은 버텨. 근데 터미널 하나 꺼지니까 전부 끊겼어.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '그물형', 'title': '이웃끼리 잇는다 — 그물형',
   'tags': [('구조: 각 노드가 이웃 여러 곳과 연결', 'g'), ('일상: 마을끼리 이어진 길', '')],
   'left': '<p>마을마다 양옆 이웃 마을들과 직접 길이 나 있다. 터미널은 없다. 어느 마을이 막혀도 돌아갈 길이 있다. 대신 먼 마을까지는 여러 번 건너야 한다.</p>',
   'right': '<p>블록체인은 데이터를 분산 저장하고 모든 참여자가 동등하게 연결되어 데이터를 공유한다. 강의 자료는 이 구조가 중개자 없이 신뢰할 수 있는 거래를 가능하게 하고 해킹에 강하다고 정리한다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 마을 12곳, 이웃과 직접 연결</h3>
    <div class="cwrap"><canvas id="c2" aria-label="마을 12곳이 원 모양으로 놓이고 이웃끼리 연결된 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">양옆으로 잇는 이웃 수</span><input type="range" id="r2k" min="1" max="3" step="1" value="2" aria-label="양옆으로 잇는 이웃 수"><span class="val" id="v2k">2</span></div>
      <div class="group"><button class="bt warn" id="b2Top" aria-pressed="false">가장 바쁜 마을 고장</button><button class="bt warn" id="b2Rand" aria-pressed="false">마을 3곳 무작위 고장</button></div></div>
    <h3>행동으로 보기 — 새 기록이 이웃에서 이웃으로 퍼진다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="한 마을에서 생긴 새 기록이 단계마다 이웃 마을로 퍼져 모든 장부 사본에 적히는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 길은 늘고 길목은 사라진다</h4>
    <ol><li>양옆 2곳씩(이웃 4곳) 이으면 평균 1.91홉. 허브형(1.83홉)보다 조금 길다. 이웃을 3곳씩 이으면 1.45홉으로 짧아지지만 길(연결)이 그만큼 많이 든다.</li>
      <li>어느 마을 하나, 심지어 세 곳이 고장 나도 남은 마을끼리는 대부분 연결된다.</li>
      <li>새 기록은 이웃에서 이웃으로 몇 단계 만에 모든 장부 사본에 퍼진다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 장부 사본이 12부가 됐다. 모두가 같은 내용을 갖게 하려면, 그리고 누군가 자기 사본을 고치면 어떻게 알아내려면 규칙이 필요하다. 그 규칙을 찾는 과정이 1-03~1-07이다.</p>''',
   'extra': '''<div class="bridge field"><h4>현장에 옮기면 — "확장성"은 어느 기준인가</h4><p>강의 자료 5쪽은 블록체인이 "확장성이 높다"고 적었지만, 같은 자료 31쪽의 비교표는 작업증명 방식의 확장성을 "제한적", 처리 속도를 "상대적으로 느림"으로 적는다. <sup>[1]</sup> 참여자를 늘리기 쉽다는 뜻의 확장성과, 초당 처리 건수라는 뜻의 확장성은 다르다. 도입 판단 때는 어느 쪽을 말하는지 먼저 정한다.</p></div>''',
   'say': ('asst', 'e10', 'asst_e10', '이웃 2곳씩이면 평균 1.91홉, 허브형은 1.83홉이에요. 차이는 생각보다 작아요. 대신 고장에는 그물형이 훨씬 버텨요.')},
 ],
 'duel': {'title': '평상시, 거래 한 건이 도착하는 데 몇 번 건너나?',
  'intro': '고장이 없는 평상시. 마을 12곳 사이 모든 쌍의 <b>평균 홉 수</b>(적을수록 빠름)로 겨룬다. 초파리는 이웃 2곳씩 잇는 그물형, 주판봇은 터미널 하나의 허브형. 이 대결은 고장을 따지지 않는다.',
  'fly': ('그물형 (양옆 이웃 2곳씩)', '터미널 없이도 길은 충분해. 빨라 봐야 얼마나 빠르겠어?', '마을 12곳, 연결 24개'),
  'robo': ('허브형 (터미널 하나)', '모든 길은 터미널로! 한 번 갈아타면 끝이야.', '마을 12곳, 연결 11개'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>두 그래프에서 모든 마을 쌍(66쌍)의 최단 경로 길이를 너비 우선 탐색으로 구해 평균을 낸다. 허브형: (11×1 + 55×2)/66 = 1.833. 그물형(이웃 ±1, ±2): 한 마을에서 1홉 4곳, 2홉 4곳, 3홉 3곳 → 21/11 = 1.909.</p><p class="lim">"홉 수 = 속도"는 단순화다. 실제 처리 시간은 각 노드의 계산량, 검증 절차, 합의 규칙에 따라 크게 달라진다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th></th><th>허브형 (중앙집중식)</th><th>그물형 (분산)</th></tr></thead><tbody>
   <tr><td>평상시 평균 홉</td><td class="g">1.83 (빠름)</td><td>1.91 (이웃 2곳씩) · 1.45 (3곳씩)</td></tr>
   <tr><td>허브·바쁜 곳 하나 고장</td><td class="r">연결 0%</td><td class="g">대부분 유지</td></tr>
   <tr><td>필요한 연결 수</td><td>11</td><td>24 (2곳씩) · 36 (3곳씩)</td></tr>
   <tr><td>장부 사본</td><td>1부 (중앙)</td><td>12부 (모두)</td></tr>
   <tr><td>남은 숙제</td><td>중앙을 믿을 수 있나</td><td>12부를 어떻게 똑같이 유지하나</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>버스 길 비유는 "연결 모양"만 보여 준다. 장부 내용이 맞는지, 누가 고쳤는지는 다루지 않는다.</li><li>실제 블록체인 네트워크는 원 모양 격자가 아니라 노드가 무작위에 가깝게 서로 연결된다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '빠름은 중앙, 튼튼함은 분산. 다음 편부터는 장부를 지키는 방법을 가장 단순한 것, 기억부터 다시 올라가요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'coffee', 'fly_e13'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 주판봇이 두 팔을 들고, 초파리 연구원이 커피잔을 든 채 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 허브형은 평상시 빠르고, 허브 하나에 모든 것이 걸린다.<br>· 그물형은 조금 느리지만 어느 한 곳이 멈춰도 버틴다.<br>· 무엇을 고를지는 "평상시"와 "고장 날 때" 중 무엇이 더 비싼지에 달렸다.'),
           ('robo', 'happy', 'robo_e12', '평상시엔 터미널이 이겼지! 숫자가 말해 줬잖아. 다음에도 여기에 투자.'),
           ('fly', 'coffee', 'fly_e13', '…평상시엔 차이가 작았네. 인정. 근데 터미널 꺼지는 날도 와.'),
           ('asst', 'e16', 'asst_e16', '다음은 1-03, 동료에게 만 원을 빌린 날로 돌아가서 기억과 장부를 비교해요.')],
 'kg_hint': '허브, 그물형, 홉, 단일 실패 지점…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.5 (중앙집중식 시스템과 블록체인 시스템 비교), p.31 (비교표의 확장성·처리 속도). PDF 2024-10-18 생성.'],
 'examples': ['마을 12곳, 원형 격자 연결(이웃 ±1~±3), 무작위 고장 시드 7 (설명용 모형)', '홉 수를 속도의 대리 지표로 쓴 것 (단순화)'],
 'gloss_keys': [('중앙집중식', True), ('단일 실패 지점', True), ('노드', True), ('홉', True), ('분산원장', True), ('블록체인', True), ('중개자', False)],
 'gloss_anchor': {'중앙집중식': '#lv1', '단일 실패 지점': '#lv1', '노드': '#why', '홉': '#lv1', '분산원장': '#lv2', '블록체인': '#lv2', '중개자': '#lv2'},
 'quiz': {
  'lv1': [{'q': '허브형(터미널 1 + 마을 11)에서 마을과 마을 사이는 몇 홉인가?', 'o': ['1홉', '2홉', '3홉', '11홉'], 'a': 1, 'why': '마을 → 터미널 → 마을, 2홉이에요.', 'hint': '터미널을 꼭 거쳐요.', 'c': 'lab:method/centralized-network'},
          {'q': '허브형에서 가장 위험한 고장은?', 'o': ['가장자리 마을 하나', '터미널(허브) 하나', '마을 두 곳', '연결 하나'], 'a': 1, 'why': '허브가 멈추면 연결된 쌍이 0이 돼요. 단일 실패 지점이에요.', 'hint': '모든 길이 지나는 곳.', 'c': 'lab:limitation/single-point-of-failure'}],
  'lv2': [{'q': '그물형에서 이웃을 양옆 2곳씩에서 3곳씩으로 늘리면?', 'o': ['평균 홉이 줄고 필요한 연결은 는다', '평균 홉이 늘고 연결은 준다', '둘 다 그대로다', '연결이 끊긴다'], 'a': 0, 'why': '1.91 → 1.45홉, 연결 24 → 36개. 빠름을 연결 비용으로 산 셈이에요.', 'hint': '슬라이더를 3으로 옮겨 보세요.', 'c': 'lab:method/mesh-network'},
          {'q': '강의 자료 5쪽의 "확장성이 높다"와 31쪽 비교표의 "확장성 제한적(작업증명)"이 다른 이유로 가장 알맞은 것은?', 'o': ['확장성이라는 말이 참여자 늘리기와 초당 처리량처럼 다른 뜻으로 쓰일 수 있어서', '한쪽이 오타라서', '블록체인은 확장성과 무관해서', '중앙집중식 이야기라서'], 'a': 0, 'why': '어느 기준의 확장성인지 먼저 정해야 해요.', 'hint': '"현장에 옮기면" 상자.', 'c': 'lab:concept/scalability'}]},
 'kgspec': {
  'ladder': ['lab:method/centralized-network', 'lab:method/mesh-network'],
  'about': ['lab:method/centralized-network', 'lab:method/mesh-network', 'lab:limitation/single-point-of-failure', 'lab:metric/average-hops'],
  'nodes': [
   ('lab:method/mesh-network', 'Method', '그물형 (분산 네트워크)', 'mesh / distributed network', '#lv2', '각 노드가 이웃 여러 곳과 직접 연결되어 중심 없이 데이터를 공유하는 구조.', 2),
   ('lab:limitation/copies-must-agree', 'Limitation', '여러 사본을 똑같이 유지해야 함', 'copies must stay consistent', '#lv2', '장부 사본이 여러 부가 되면, 모두 같은 내용을 갖게 하고 고친 사본을 찾아낼 규칙이 필요하다.', 2),
   ('lab:metric/connected-pairs', 'Metric', '연결 유지 쌍 비율', 'share of connected pairs', '#lv1', '고장 뒤에도 서로 닿을 수 있는 노드 쌍의 비율.', 2),
   ('lab:concept/scalability', 'Concept', '확장성', 'scalability', '#lv2', '시스템이 커질 때(참여자 수, 처리량) 성능을 유지하는 능력. 어느 기준인지에 따라 뜻이 다르다.', 3),
   ('lab:analogy/bus-terminal', 'Analogy', '버스 터미널 ↔ 중앙집중식', 'bus terminal ~ centralized system', '#lv1', '모든 노선이 터미널 하나로 모이는 도시.', 1),
   ('lab:analogy/village-roads', 'Analogy', '마을 길 ↔ 분산 네트워크', 'village roads ~ distributed network', '#lv2', '마을끼리 이웃과 길이 이어진 시골.', 2),
   ('lab:question/core', 'Question', '장부를 한 곳에 모으면 빠르고 나누면 튼튼하다, 얼마나?', 'How much faster is central, how much sturdier is distributed?', '#top', None, 1),
   ('lab:question/duel', 'Question', '평상시 거래 한 건은 몇 번 건너 도착하나?', 'How many hops in normal operation?', '#duel', None, 2),
  ],
  'edges': [
   ('lab:method/centralized-network', 'lab:prerequisiteOf', 'lab:method/mesh-network', '#lv2'),
   ('lab:method/centralized-network', 'lab:hasLimitation', 'lab:limitation/single-point-of-failure', '#lv1'),
   ('lab:limitation/single-point-of-failure', 'lab:addressedBy', 'lab:method/mesh-network', '#lv2'),
   ('lab:method/mesh-network', 'lab:hasLimitation', 'lab:limitation/copies-must-agree', '#lv2'),
   ('lab:limitation/copies-must-agree', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:method/centralized-network', 'lab:contrastsWith', 'lab:method/mesh-network', '#duel'),
   ('lab:method/centralized-network', 'lab:evaluatedBy', 'lab:metric/average-hops', '#duel'),
   ('lab:method/mesh-network', 'lab:evaluatedBy', 'lab:metric/average-hops', '#duel'),
   ('lab:method/mesh-network', 'lab:evaluatedBy', 'lab:metric/connected-pairs', '#lv2'),
   ('lab:method/centralized-network', 'lab:evaluatedBy', 'lab:metric/connected-pairs', '#lv1'),
   ('lab:term/node', 'lab:partOf', 'lab:method/mesh-network', '#why'),
   ('lab:method/distributed-ledger', 'lab:broader', 'lab:method/mesh-network', '#lv2', 'mid'),
   ('lab:concept/blockchain', 'lab:broader', 'lab:method/distributed-ledger', '#lv2'),
   ('lab:concept/trusted-third-party', 'lab:partOf', 'lab:method/centralized-network', '#lv1'),
   ('lab:concept/scalability', 'lab:raises', 'lab:question/core', '#lv2', 'mid'),
   ('lab:analogy/bus-terminal', 'lab:analogyOf', 'lab:method/centralized-network', '#lv1'),
   ('lab:analogy/village-roads', 'lab:analogyOf', 'lab:method/mesh-network', '#lv2'),
   ('lab:metric/average-hops', 'lab:raises', 'lab:question/duel', '#duel'),
  ],
  'claims': [
   ('lab:claim/distributed-storage', '블록체인은 데이터를 분산 저장하며 모든 참여자가 동등하게 연결되어 데이터를 공유한다', '#lv2', ['lab:method/mesh-network', 'lab:concept/blockchain'], [(LEC, '교안 p.5')], 'F01'),
   ('lab:claim/central-fast-but', '중앙 집중식 시스템은 처리 속도가 빠르지만 거래비용(수수료)과 보안 문제가 있다', '#lv1', ['lab:method/centralized-network'], [(LEC, '교안 p.5')], 'F02'),
   ('lab:claim/no-intermediary-trust', '블록체인은 중개자 없이 신뢰할 수 있는 거래를 가능하게 하고 해킹에 강하다(강의 자료의 정리)', '#lv2', ['lab:method/distributed-ledger'], [(LEC, '교안 p.5')], 'F03'),
   ('lab:claim/scalability-conflict', '강의 자료는 p.5에서 확장성이 높다고, p.31 비교표에서 작업증명의 확장성은 제한적이라고 적는다', '#lv2', ['lab:concept/scalability'], [(LEC, '교안 p.5, p.31')], 'F04'),
  ],
  'sims': [('lab:simulation/hub-network', '허브형 고장 실험', '#lv1', ['lab:method/centralized-network']),
           ('lab:simulation/mesh-network', '그물형 고장·전파 실험', '#lv2', ['lab:method/mesh-network']),
           ('lab:simulation/duel-hops', '평균 홉 대결', '#duel', ['lab:metric/average-hops'])],
 },
}
