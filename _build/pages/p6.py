LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '1-06', 'slug': 'bank-ledger', 'key': '1_06', 'anchor': 'C',
 'tab_title': '기관 장부: 은행', 'meta_title': '기관 장부 — 은행이 증인이 될 때',
 'description': '은행 전산 장부가 분쟁을 끝내는 힘과, 그 대가인 수수료·해킹 표적·단일 실패 지점을 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.11, p.13; Nakamoto (2008) 1절',
 'h1': '기관 장부<br>— 은행이 증인이 될 때', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '사람 대신 기관 전체가 증인이 되면 다툼은 끝날까? 그 대가는 무엇일까?',
 'lead': 'A와 B의 거래가 은행 전산 장부에 남으면 따로 증인을 세울 필요가 없습니다. 기관 전체가 증거를 위조할 가능성은 매우 낮으니까요. 오늘날 대부분의 거래가 이 방식입니다. 그런데 중요한 정보가 한 곳에 모이면 그곳이 표적이 되고, 지키는 비용은 수수료로 돌아옵니다.',
 'kpis': [('기관', '증인이 되는 제3자', 'a', [1]), ('해킹 표적', '중요 정보가 모인 곳의 위험', 'r', [1]), ('수수료', '보안·인력 비용을 소비자가 부담', 'm', [1]), ('중개 비용', '작은 거래를 어렵게 만든다 (백서)', 'g', [2])],
 'hero': [('doc', 'think', 'doc_e09', '지금 우리가 송금할 때 증인을 세우나요? 아니죠. 은행 장부가 증인이에요. 이 편은 그 편리함의 값을 따져 봐요.'),
          ('asst', 'smile', 'asst_e13', '앞 편들의 숫자를 이어서 쓸게요. 장부 보존 94%, 꼼꼼한 위조 30%. 은행 장부와 비교해요.'),
          ('fly', 'point', 'fly_e08', '은행이 털리면? 은행 서버가 멈추면? 다들 그날은 송금 못 하잖아.'),
          ('robo', 'coin', 'robo_e16', '은행만큼 믿을 데가 어딨어. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '판정 가능 비율과 가동률을 계산한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 기관이 멈추는 날을 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 기관에 건다.')],
 'why_title': '왜 은행 장부를 따로 보나',
 'why_lead': '백서가 정면으로 겨냥한 상대가 바로 "믿을 만한 제3자로서의 금융기관"이었어요. 블록체인을 이해하려면 이 방식이 무엇을 잘하고 무엇을 비싸게 하는지 알아야 해요.',
 'why': [('기관이 증인', '증인을 사람이 아니라 믿을 만한 기관으로 하면, 기관 전체가 증거를 위조할 가능성은 매우 낮아 신뢰성이 높다. <sup>[1]</sup>'),
         ('표적과 비용', '기관이 중요한 정보를 가지므로 해킹의 목표가 되기 쉽고, 보안 기술 투자와 인력 비용은 서류 발급·계좌 수수료로 소비자에게 돌아간다. <sup>[1]</sup>'),
         ('백서의 문제 제기', '인터넷 상거래는 거의 전적으로 금융기관에 기대고, 중개 비용은 거래 비용을 높여 실용적인 최소 거래 규모를 제한한다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 기관 장부는 다툼을 끝내는 데는 최고예요. 문제는 다툼이 아니라 그 기관이 멈추거나 뚫리는 날이에요.'),
 'big_lead': '공증(1-05)에서 한 걸음 더, 이제 거래 기록 자체를 기관의 전산 장부에 남깁니다. 이 칸이 오늘날의 표준이고, 다음 칸(1-07)이 블록체인의 출발점입니다.',
 'ladder': [('①', '기관 장부 (은행이 증인)', '모든 거래가 한 장부에 남아 다툼을 바로 판정한다', '해킹 표적, 단일 실패 지점, 수수료'),
            ('②', '중앙 인증 (공인인증서·OTP)', '기관 서버가 신원과 비밀번호를 확인한다', '인증도 특정 기관·서버에 집중된다 → 1-07 분산원장')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '은행 장부', 'title': '기관이 증인이 된다 — 은행 전산 장부',
   'tags': [('방식: 거래 기록을 기관 장부 한 곳에', 'g'), ('장부: 은행 전산 원장', '')],
   'left': '<p>A가 B에게 보낸 돈은 은행 원장에 "A −10,000, B +10,000"으로 남는다. 다툼이 생기면 은행 기록을 보면 끝이다. 대신 모든 손님의 거래가 이 한 장부를 지나고, 은행은 이 장부를 지키는 데 큰돈을 쓴다.</p>',
   'right': '<p>이것이 블록체인이 대신하려는 "믿을 만한 제3자"다. 블록체인은 이 장부 한 권을 참여자 모두가 한 부씩 갖는 분산원장으로 바꾸고, 기관 대신 망의 규칙으로 기록을 지키려 한다(1-07).</p>',
   'panel': '''<h3>직접 해 보기 — 수수료와 해킹</h3>
    <div class="cwrap"><canvas id="c1" aria-label="고객 8명이 은행 장부 하나를 거쳐 거래하는 그림과 누적 수수료 막대"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">하루 거래 수</span><input type="range" id="r1n" min="100" max="5000" step="100" value="1000" aria-label="하루 거래 수"><span class="val" id="v1n">1000</span></div>
      <div class="group"><span class="glabel">건당 수수료(예시값)</span><input type="range" id="r1f" min="0" max="2000" step="100" value="500" aria-label="건당 수수료"><span class="val" id="v1f">500</span>원</div>
      <div class="group"><button class="bt warn" id="b1Hack" aria-pressed="false">은행 장부 해킹</button></div></div>
    <h3>행동으로 보기 — 모든 거래가 가운데를 지나간다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="거래 꾸러미가 고객에서 은행 장부를 거쳐 다른 고객에게 가는 애니메이션"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 다툼은 끝내고, 위험은 모은다</h4>
    <ol><li>은행 장부가 있으면 개인 장부·계약서·증인 없이도 다툼을 판정할 수 있다. 1-03~1-05의 문제가 한 번에 풀린다.</li>
      <li>그 대신 모든 거래 정보가 한 곳에 모여 해킹의 목표가 되고, 그곳이 멈추면 모든 거래가 멈춘다.</li>
      <li>보안 투자와 인력 비용은 수수료로 소비자가 낸다. <sup>[1]</sup> 백서는 이 중개 비용이 작은 거래를 어렵게 만든다고 지적했다. <sup>[2]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 장부가 한 곳에 있어 표적이 되고, 비용은 소비자에게 돌아온다.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면</h4><p>"은행 = 장부 한 권"은 단순화다. 실제 은행은 백업, 이중화, 재해 복구 센터로 장비 고장에 대비한다. 그래도 관리 주체가 하나라는 점, 그 주체의 내부 사고나 정책 결정이 모든 고객에게 미친다는 점은 같다.</p></div>',
   'say': ('robo', 'e20', 'robo_e20', '잠깐, 이 막대 전부 수수료야? 장부 하나 지키는 값이 이렇게 새고 있었다니…')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '중앙 인증', 'title': '인증도 한 곳에 — 공인인증서와 OTP',
   'tags': [('방식: 기관 서버가 신원·비밀번호 확인', 'g'), ('장부: 인증 기관의 사용자 정보 저장소', '')],
   'left': '<p>은행 앱에 들어갈 때 쓰는 인증서와 일회용 비밀번호도 결국 기관 서버가 "이 사람이 맞다"고 확인해 주는 장치다. 장부뿐 아니라 "누가 누구인가"를 확인하는 일까지 특정 기관에 모여 있다.</p>',
   'right': '<p>강의 자료는 공인인증서와 OTP가 모두 중앙 관리 시스템에 의존하고, 블록체인 방식은 참여자들의 동의로 인증해 단일 실패 위험을 줄인다고 정리한다. 다만 분산 처리로 속도가 느릴 수 있다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 한 서버 vs 여러 노드의 과반</h3>
    <div class="cwrap"><canvas id="c2" aria-label="중앙 서버 하나의 가동률과, 여러 노드 중 과반이 살아 있을 확률을 비교하는 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">서버(노드) 한 대의 가동률(예시값)</span><input type="range" id="r2a" min="95" max="99.9" step="0.1" value="99" aria-label="한 대의 가동률"><span class="val" id="v2a">99</span>%</div>
      <div class="group"><span class="glabel">분산 노드 수</span><input type="range" id="r2n" min="3" max="15" step="2" value="7" aria-label="분산 노드 수"><span class="val" id="v2n">7</span></div></div>
    <h3>행동으로 보기 — 1년 365일 달력</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="1년 365일을 칸으로 그려 중앙 서버와 분산 방식 각각이 멈춘 날을 표시한 달력"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 과반이 동시에 멈출 확률</h4>
    <ol><li>중앙 서버 하나의 가동률이 99%면 1년에 약 3.65일(87.6시간)은 멈춘다(예시값).</li>
      <li>같은 성능의 노드 7대 중 과반(4대)만 살아 있으면 되는 방식이라면, 과반이 동시에 멈출 확률은 훨씬 작다.</li>
      <li>대신 여러 노드가 서로 확인하느라 한 건을 처리하는 데 시간이 더 걸릴 수 있다. <sup>[1]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 장부도 인증도 한 기관에 모여 있다. 기관을 없애고 참여자 다수가 장부를 함께 지키면 어떨까? → 1-07 분산원장.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>노드 n대가 각자 확률 a로 살아 있고 서로 독립이면, 과반(⌊n/2⌋+1대 이상)이 살아 있을 확률 = Σ<sub>k&gt;n/2</sub> C(n,k) a<sup>k</sup>(1−a)<sup>n−k</sup>.</p><p class="lim">현실의 장애는 독립이 아닐 때가 많다(같은 소프트웨어 결함, 같은 지역 정전). 독립 가정은 분산 쪽을 실제보다 유리하게 보이게 할 수 있다.</p></details>',
   'say': ('asst', 'e10', 'asst_e10', '한 대 99%면 1년에 87.6시간 멈춰요. 7대 중 과반 방식이면 1년 기대 정지 시간이 약 11초예요. 고장이 서로 독립이라는 가정이에요.')},
 ],
 'duel': {'title': '1년간 분쟁 1,000건, 몇 건을 판정할 수 있나?',
  'intro': '돈 거래 분쟁 1,000건(시드 606). 판정 기준은 <b>기록만으로 누가 맞는지 판정한 비율</b>(높을수록 좋음). 초파리는 1-03·1-04의 방식(각자 장부 + 병기 계약서), Money-Robo는 은행 장부. 앞 편의 예시값을 그대로 이어 쓴다: 두 사본이 모두 남을 확률 94%, 위조범이 꼼꼼할 확률 30%, 은행 기록 유실 0.1%.',
  'fly': ('각자 장부 + 병기 계약서', '은행 없이도 우리끼리 기록하면 돼.', '사본 보존 94% · 꼼꼼한 위조 30%'),
  'robo': ('은행 장부', '다툼? 은행 기록 한 번 보면 끝이지.', '기록 유실 0.1%'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>분쟁 하나마다: 초파리 방식은 두 사본이 모두 남아 있고(0.94) 위조가 서툴러 흔적이 남을 때(0.7)만 판정 가능 → 기대 65.8%. Money-Robo 방식은 은행 기록이 남아 있으면(0.999) 판정 가능 → 기대 99.9%. 시드 606으로 1,000건을 뽑아 센다.</p><p class="lim">은행 기록 자체가 틀렸거나 내부자가 고친 경우는 이 대결에 넣지 않았다. 그 위험이 다음 편의 출발점이다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th></th><th>각자 장부·계약서 (1-03·1-04)</th><th>증인·공증 (1-05)</th><th>은행 장부 (1-06)</th></tr></thead><tbody>
   <tr><td>다툼 판정</td><td class="r">자주 불가</td><td>대체로 가능</td><td class="g">거의 항상 가능</td></tr>
   <tr><td>비용</td><td>거의 없음</td><td>건마다 큼</td><td>수수료로 상시</td></tr>
   <tr><td>믿어야 하는 대상</td><td>상대방</td><td>증인·공증인</td><td>기관 하나</td></tr>
   <tr><td>약점</td><td>분실·조작</td><td>공모·비용</td><td class="r">해킹 표적, 단일 실패 지점</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>가동률·수수료·유실률은 예시값이다. 실제 은행 시스템의 가동률은 이보다 훨씬 높게 관리된다.</li><li>공인인증서·OTP 그림은 강의 자료의 구조도를 말로 옮긴 것이다. 세부 절차는 기관마다 다르다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '기관 장부는 다툼을 끝냈어요. 남은 건 "그 기관을 믿어야 한다"는 한 가지. 다음 편은 그 한 곳을 다수로 바꿔요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'cry', 'fly_e21'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 Money-Robo가 두 팔을 들고, 초파리 연구원이 폭포 눈물을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 기관 장부는 증인·공증 없이도 다툼을 판정한다.<br>· 대신 모든 정보가 한 곳에 모여 표적이 되고, 지키는 비용은 수수료가 된다.<br>· 인증까지 한 곳에 모이면, 그곳이 멈추는 날 모두가 멈춘다.'),
           ('robo', 'happy', 'robo_e12', '판정률 99.9%! 숫자가 말해 줬잖아. 다음에도 여기에 투자.'),
           ('fly', 'cry', 'fly_e21', '…우리끼리 기록으로는 3분의 1을 못 가렸어. 인정. 근데 은행이 틀리면 누가 가려?'),
           ('asst', 'e16', 'asst_e16', '다음은 1-07, 이 챕터의 마지막. 은행 한 곳 대신 다수의 증인이 장부를 나눠 들어요.')],
 'kg_hint': '은행, 수수료, 해킹, 가용성…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.11 (기관이 증인인 경우: 은행, 수수료 및 해킹), p.13 (공인인증서·OTP와 블록체인 인증 비교). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 1절(금융기관 의존, 중개 비용과 최소 거래 규모). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['하루 거래 수, 건당 수수료 500원 (예시값)', '서버 한 대 가동률 99%, 노드 7대, 독립 고장 가정 (예시값)', '대결: 분쟁 1,000건, 시드 606, 사본 보존 94%·꼼꼼한 위조 30%·은행 유실 0.1% (예시값, 앞 편 값 이어 씀)'],
 'gloss_keys': [('중개자', True), ('수수료', True), ('단일 실패 지점', True), ('공인인증서', True), ('OTP', True), ('가용성', True), ('분산원장', True)],
 'gloss_anchor': {'중개자': '#why', '수수료': '#lv1', '단일 실패 지점': '#lv1', '공인인증서': '#lv2', 'OTP': '#lv2', '가용성': '#lv2', '분산원장': '#lv1'},
 'quiz': {
  'lv1': [{'q': '하루 2,000건, 건당 수수료 500원(예시값)이면 하루 수수료 총액은?', 'o': ['10만 원', '50만 원', '100만 원', '1,000만 원'], 'a': 2, 'why': '2,000 × 500 = 1,000,000원.', 'hint': '거래 수 × 건당 수수료.', 'c': 'lab:concept/fee'},
          {'q': '은행 장부 방식이 1-03~1-05의 문제를 한 번에 푸는 이유는?', 'o': ['모든 거래가 기관의 한 장부에 남아 그것을 기준으로 판정하기 때문', '은행 직원이 기억력이 좋기 때문', '수수료가 없기 때문', '장부가 여러 권이기 때문'], 'a': 0, 'why': '맞아요. 대조할 기준 장부가 당사자 밖에 하나 있어요.', 'hint': '대조할 사본이 어디 있나요?', 'c': 'lab:method/bank-ledger'}],
  'lv2': [{'q': '가동률 99%인 서버 하나는 1년(8,760시간)에 약 몇 시간 멈추나?', 'o': ['8.8시간', '87.6시간', '876시간', '0.9시간'], 'a': 1, 'why': '8,760 × 0.01 = 87.6시간.', 'hint': '멈춘 비율 1%.', 'c': 'lab:metric/availability'},
          {'q': '강의 자료가 블록체인 인증 방식의 단점으로 함께 적은 것은?', 'o': ['분산 처리로 속도가 느릴 수 있다', '위조가 쉽다', '중앙 기관이 필요하다', '거래 기록이 비공개다'], 'a': 0, 'why': '맞아요. 단일 실패 위험은 줄지만 속도가 느릴 수 있어요.', 'hint': '교안 p.13.', 'c': 'lab:method/central-auth'}]},
 'kgspec': {
  'ladder': ['lab:method/bank-ledger', 'lab:method/central-auth'],
  'about': ['lab:method/bank-ledger', 'lab:method/central-auth', 'lab:limitation/single-point-of-failure', 'lab:concept/fee'],
  'nodes': [
   ('lab:method/bank-ledger', 'Method', '기관 장부 (은행 전산 원장)', 'institutional ledger (bank)', '#lv1', '거래 기록을 믿을 만한 기관의 전산 장부 한 곳에 남기고, 그 장부를 기준으로 다툼을 판정하는 방식.', 2, [(LEC, '교안 p.11')]),
   ('lab:method/central-auth', 'Method', '중앙 인증 (공인인증서·OTP)', 'centralized authentication', '#lv2', '신원과 비밀번호 확인을 특정 기관·서버가 맡는 인증 방식.', 3, [(LEC, '교안 p.13')]),
   ('lab:limitation/target-and-cost', 'Limitation', '해킹 표적과 수수료', 'attack target and fees', '#lv1', '중요 정보가 한 곳에 모여 해킹 목표가 되고, 보안 비용이 수수료로 소비자에게 돌아온다.', 2, [(LEC, '교안 p.11')]),
   ('lab:limitation/auth-centralized', 'Limitation', '인증도 한 곳에 집중', 'authentication is centralized', '#lv2', '인증 정보의 생성과 검증이 특정 기관이나 서버에 집중되어 있다.', 3, [(LEC, '교안 p.13')]),
   ('lab:metric/resolved-disputes', 'Metric', '판정 가능한 분쟁 비율', 'share of resolvable disputes', '#duel', '기록만으로 누가 맞는지 판정할 수 있는 분쟁의 비율.', 2),
   ('lab:method/peer-records', 'Method', '각자 장부 + 병기 계약서', 'peer records with contract', '#duel', '1-03·1-04의 방식. 당사자 둘의 장부와 계약서로만 다툼을 판정한다.', 2),
   ('lab:question/core', 'Question', '기관 전체가 증인이 되면 다툼은 끝날까? 대가는?', 'Does an institutional witness end disputes? At what cost?', '#top', None, 2),
   ('lab:question/duel', 'Question', '분쟁 1,000건 중 몇 건을 판정할 수 있나?', 'How many disputes can be resolved?', '#duel', None, 2),
   ('lab:question/bank-wrong', 'Question', '은행 기록이 틀리거나 내부자가 고치면 누가 가리나?', 'Who checks the bank if its record is wrong?', '#outro', None, 3, None, None, 'mid'),
  ],
  'edges': [
   ('lab:method/bank-ledger', 'lab:prerequisiteOf', 'lab:method/central-auth', '#lv2'),
   ('lab:method/bank-ledger', 'lab:hasLimitation', 'lab:limitation/target-and-cost', '#lv1'),
   ('lab:method/bank-ledger', 'lab:hasLimitation', 'lab:limitation/single-point-of-failure', '#lv1'),
   ('lab:limitation/target-and-cost', 'lab:addressedBy', 'lab:method/central-auth', '#lv2', 'mid'),
   ('lab:method/central-auth', 'lab:hasLimitation', 'lab:limitation/auth-centralized', '#lv2'),
   ('lab:limitation/auth-centralized', 'lab:addressedBy', 'lab:method/distributed-ledger', '#lv2', 'mid'),
   ('lab:method/certificate-auth', 'lab:broader', 'lab:method/central-auth', '#lv2'),
   ('lab:method/otp', 'lab:broader', 'lab:method/central-auth', '#lv2'),
   ('lab:method/bank-ledger', 'lab:broader', 'lab:concept/trusted-third-party', '#lv1'),
   ('lab:concept/fee', 'lab:partOf', 'lab:limitation/target-and-cost', '#lv1'),
   ('lab:method/central-auth', 'lab:evaluatedBy', 'lab:metric/availability', '#lv2'),
   ('lab:method/bank-ledger', 'lab:contrastsWith', 'lab:method/peer-records', '#duel'),
   ('lab:method/bank-ledger', 'lab:evaluatedBy', 'lab:metric/resolved-disputes', '#duel'),
   ('lab:method/peer-records', 'lab:evaluatedBy', 'lab:metric/resolved-disputes', '#duel'),
   ('lab:metric/resolved-disputes', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:method/bank-ledger', 'lab:raises', 'lab:question/bank-wrong', '#outro'),
   ('lab:limitation/target-and-cost', 'lab:raises', 'lab:question/core', '#lv1'),
  ],
  'claims': [
   ('lab:claim/institution-witness', '거래 내역이 은행 전산 장부에 남으면 증인 없이 안전한 거래가 가능하고, 기관 전체가 증거를 위조할 가능성은 매우 낮다', '#why', ['lab:method/bank-ledger'], [(LEC, '교안 p.11')], 'F01'),
   ('lab:claim/target-fees', '기관이 중요한 정보를 가져 해킹 목표가 되기 쉽고, 보안·인력 비용은 서류발급·계좌 수수료로 소비자가 부담한다', '#why', ['lab:limitation/target-and-cost', 'lab:concept/fee'], [(LEC, '교안 p.11')], 'F02'),
   ('lab:claim/auth-central', '공인인증서와 OTP는 모두 중앙 관리 시스템에 의존하며 인증 정보의 생성과 검증이 특정 기관·서버에 집중되어 있다', '#lv2', ['lab:limitation/auth-centralized'], [(LEC, '교안 p.13')], 'F03'),
   ('lab:claim/blockchain-auth', '블록체인 방식 인증은 단일 실패 위험을 줄이지만 분산 처리로 속도가 느릴 수 있다(강의 자료의 정리)', '#lv2', ['lab:method/distributed-ledger'], [(LEC, '교안 p.13')], 'F04'),
   ('lab:claim/commerce-relies', '인터넷 상거래는 거의 전적으로 금융기관에 의존하며, 중개 비용이 거래 비용을 높여 최소 거래 규모를 제한한다', '#why', ['lab:concept/trusted-third-party', 'lab:concept/fee'], [(WP, '1절')], 'F05'),
  ],
  'sims': [('lab:simulation/bank-fees', '은행 수수료·해킹 실험', '#lv1', ['lab:method/bank-ledger']),
           ('lab:simulation/uptime', '중앙 대 과반 가동률 실험', '#lv2', ['lab:method/central-auth']),
           ('lab:simulation/duel-disputes', '분쟁 판정률 대결', '#duel', ['lab:metric/resolved-disputes'])],
 },
}
