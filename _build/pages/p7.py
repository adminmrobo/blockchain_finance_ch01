LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '1-07', 'slug': 'many-witnesses', 'key': '1_07', 'anchor': 'C',
 'tab_title': '다수의 증인: 분산원장', 'meta_title': '다수의 증인 — 분산원장과 과반의 조건',
 'description': '장부를 모두가 나눠 들고 과반으로 진위를 정하는 분산원장을 직접 공격해 보고, 공격 비용과 투표권 문제까지 따져 보는 1장 마지막 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.12; Nakamoto (2008) 2·4절',
 'h1': '다수의 증인<br>— 분산원장과 과반의 조건', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '은행 한 곳 대신 모두가 장부를 나눠 들면, 위조는 정말 어려워질까? 무엇이 그 조건일까?',
 'lead': '1장의 마지막 칸입니다. 블록체인은 증인을 한 명이 아니라 다수로 세웁니다. A와 B의 거래가 망의 모든 장부에 동시에 적히고, 진위는 망의 데이터를 조회해 정합니다. 위조가 "참"이 되려면 과반의 장부를 동시에 바꿔야 해요. 이 편에서는 그 과반을 직접 공격해 보고, 공격이 언제 손해가 되는지, 그리고 "한 표"를 누구에게 줄지까지 따져 봅니다.',
 'kpis': [('다수', '블록체인이 세우는 증인의 수', 'g', [1]), ('50% 초과', '위조가 "참"이 되려면 바꿔야 할 장부 몫', 'r', [1]), ('비용 > 이익', '과반 해킹이 현실적이지 않은 이유', 'a', [1]), ('CPU 한 표', '백서가 고른 투표 단위', 'm', [2])],
 'hero': [('doc', 'think', 'doc_e09', '증인 셋은 공모하면 끝났어요(1-05). 은행 하나는 뚫리면 끝났고요(1-06). 그럼 증인이 백 명, 천 명이면요?'),
          ('asst', 'smile', 'asst_e13', '장부 수, 공격 장부 수, 공격 비용을 바꿔 가며 위조가 언제 이기는지 계산해 둘게요.'),
          ('fly', 'point', 'fly_e08', '과반만 넘기면 된다며. 그 과반은 누가 세는데? 가짜 장부를 끼워 넣으면?'),
          ('robo', 'coin', 'robo_e16', '과반? 사면 되지. 돈이면 다 돼. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '표를 세고 공격 비용을 계산한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 투표 규칙의 빈틈을 찾는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 오늘은 공격자 역할.')],
 'why_title': '왜 다수의 증인인가',
 'why_lead': '1-03부터 1-06까지 "믿을 대상"은 상대방 → 증인 → 공증인 → 은행으로 바뀌었어요. 이번 칸은 그 대상을 "특정한 누구"가 아니라 "참여자 다수"로 바꿉니다.',
 'why': [('다수의 증인', '블록체인 시스템은 다수의 증인을 세운다. A와 B의 거래가 망에 동시에 기록되어, 진위는 망의 데이터를 조회해 쉽게 판정할 수 있다. <sup>[1]</sup>'),
         ('과반의 벽', '해커가 위조한 데이터가 "참"이 되려면 전체 망 사용자의 50%가 넘는 장부를 동시에 바꿔야 한다. <sup>[1]</sup>'),
         ('비용의 벽', '과반을 동시에 해킹할 능력은 갖추기 매우 어렵고, 성공해도 드는 비용이 얻는 이익보다 크다. 그래서 분산원장 시스템이라고도 한다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 분산원장의 보안은 "불가능"이 아니라 "손해"에서 나와요. 그리고 그 계산은 한 표를 누구에게 주느냐에 달려 있어요.'),
 'big_lead': '은행(1-06)의 "한 곳"을 "다수"로 바꾸는, 이 장의 마지막 칸입니다. 여기서 남는 두 질문(변조를 빨리 알아보는 법, 투표권을 정하는 법)이 2장 「블록체인 기술」로 이어집니다.',
 'ladder': [('①', '다수결 장부 (분산원장)', '과반 미만의 위조는 다수결에서 진다', '과반을 장악하면 위조가 이긴다'),
            ('②', '손익과 투표권', '공격 비용이 이익보다 크게 만든다', '사람(노드) 수로 투표하면 가짜 노드가 싸다 → 2장 해시·작업증명')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '다수결 장부', 'title': '모두가 장부를 든다 — 다수결 장부',
   'tags': [('방식: 장부 N부 + 과반 합의', 'g'), ('장부: 참여자 수만큼의 사본', '')],
   'left': '<p>은행 장부 한 권 대신, 참여자 아홉 명이 똑같은 장부를 한 권씩 든다. 다툼이 생기면 아홉 권을 펼쳐 다수가 적은 내용을 따른다. 한두 권을 몰래 고쳐 봐야 다수결에서 진다.</p>',
   'right': '<p>이것이 <span class="jt" data-t="분산원장">분산원장</span>이다. 위조가 "참"이 되려면 전체의 50%가 넘는 장부를 동시에 바꿔야 한다. <sup>[1]</sup> 백서의 표현으로는, 거래가 없었음을 확인하려면 모든 거래를 알아야 하고, 그래서 거래를 공개적으로 알리고 참여자들이 하나의 순서에 합의해야 한다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 몇 권을 고쳐야 위조가 이기나</h3>
    <div class="cwrap"><canvas id="c1" aria-label="원 모양으로 놓인 장부들. 초록은 원본, 빨강은 위조본. 가운데에 다수결 결과"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">참여 장부 수 N</span><input type="range" id="r1n" min="3" max="21" step="2" value="9" aria-label="참여 장부 수"><span class="val" id="v1n">9</span></div>
      <div class="group"><span class="glabel">공격자가 고친 장부 k</span><input type="range" id="r1k" min="0" max="21" step="1" value="4" aria-label="공격자가 고친 장부 수"><span class="val" id="v1k">4</span></div></div>
    <h3>행동으로 보기 — 장부들이 투표한다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="장부마다 원본과 위조본 중 하나에 표를 던지고 막대가 쌓이는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 과반의 의미</h4>
    <ol><li>N권 중 과반은 ⌊N/2⌋+1권이다. 9권이면 5권, 21권이면 11권.</li>
      <li>공격자가 과반 미만을 고치면 다수결은 원본을 택한다. 증인 셋의 공모(1-05)와 달리, 다수를 동시에 매수해야 한다.</li>
      <li>은행(1-06)은 한 곳만 뚫으면 됐다. 분산원장은 과반을 뚫어야 한다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 공격자가 과반을 장악하면 위조본이 "참"이 된다. 과반이 비싸야 안전하다. → 공격 비용을 따져 보자.</p>''',
   'say': ('asst', 'e10', 'asst_e10', '9권이면 5권을 동시에 바꿔야 해요. 4권까지는 몇 번을 돌려도 원본이 이겼어요.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '손익과 투표권', 'title': '공격은 손해여야 한다 — 손익과 투표권',
   'tags': [('방식: 과반 장악 비용 > 위조 이익', 'g'), ('장부: Money-Robo의 공격 손익 계산서', '')],
   'left': '<p>Money-Robo가 위조로 만 원을 벌려면 장부 다섯 권을 사들여야 한다. 한 권에 3천 원이면 1만 5천 원, 손해다. 그런데 투표 규칙이 "장부를 가진 사람이면 누구나 한 표"라면? 장부를 사들이는 대신 가짜 장부를 잔뜩 만들어 투표장에 들이밀면 된다.</p>',
   'right': '<p>백서는 바로 이 문제를 짚었다. 다수결을 IP 주소 하나당 한 표로 정하면, 많은 IP를 확보할 수 있는 사람이 무너뜨릴 수 있다. 그래서 작업증명, 곧 CPU 하나당 한 표로 정했다. <sup>[2]</sup> 그 방법은 2장에서 다룬다.</p>',
   'panel': '''<h3>직접 해 보기 — 과반을 사는 두 가지 방법</h3>
    <div class="cwrap"><canvas id="c2" aria-label="정직한 장부 수에 따라 진짜 장부를 사들이는 비용과 가짜 노드를 만드는 비용을 위조 이익과 비교하는 그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">진짜 장부 한 권 매수 비용(예시값)</span><input type="range" id="r2c" min="1000" max="10000" step="1000" value="3000" aria-label="진짜 장부 매수 비용"><span class="val" id="v2c">3000</span>원</div>
      <div class="group"><span class="glabel">가짜 노드 하나 만드는 비용(예시값)</span><input type="range" id="r2f" min="0" max="2000" step="100" value="100" aria-label="가짜 노드 비용"><span class="val" id="v2f">100</span>원</div>
      <div class="group"><span class="glabel">투표 규칙</span><button class="bt" data-rule="reg" aria-pressed="true">등록된 참여자만</button><button class="bt" data-rule="open" aria-pressed="false">누구나 노드 하나당 한 표</button></div></div>
    <h3>행동으로 보기 — 투표장에 가짜 장부가 몰려든다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="정직한 장부 9권 앞에 가짜 장부가 줄지어 들어와 표를 던지는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 한 표의 값이 보안을 정한다</h4>
    <ol><li>등록된 참여자만 투표하면, 공격자는 진짜 장부 과반을 사들여야 한다. 장부 수가 늘수록 비용이 커져 이익을 넘는다.</li>
      <li>누구나 노드를 만들어 한 표를 얻으면, 공격자는 가짜 노드를 정직한 장부 수보다 하나 더 만들면 된다. 노드가 싸면 과반도 싸다.</li>
      <li>그래서 열린 망에서는 "한 표"를 쉽게 복제할 수 없는 무언가(계산력, 지분)에 묶어야 한다. 백서의 답은 계산력이었다. <sup>[2]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계 (2장으로):</b> ① 수천 권의 장부 중 어느 것이 몰래 바뀌었는지 빠르게 알아볼 방법(해시와 블록), ② 열린 망에서 한 표를 정하는 방법(작업증명).</p>''',
   'extra': '<div class="bridge gen"><h4>생성 AI로 치면</h4><p>여러 모델의 답을 다수결로 모으는 앙상블이나, 사람 평가자의 다수결로 데이터를 고르는 작업에도 같은 함정이 있다. 같은 모델을 여러 번 복제해 투표시키면 표 수만 늘고 독립성은 없다.</p><p class="lim">AI 앙상블에는 "공격자"가 없는 경우가 많다. 닮은 건 "표가 서로 독립이어야 다수결이 의미 있다"는 조건이다.</p></div>',
   'say': ('fly', 'magnify', 'fly_e07', '가짜 노드가 백 원이면, 과반이 천 원이야. 한 표를 아무나 만들 수 있으면 다수결도 소용없어.')},
 ],
 'duel': {'title': '과반 투표, 위조본이 이길 수 있을까?',
  'intro': '등록된 장부는 9권. Money-Robo(공격자)는 그중 4권을 고쳤다. 과반에 1권 모자라자, 등록되지 않은 가짜 장부 6권을 투표장에 끼워 넣었다. 판정은 <b>표 수</b>(많은 쪽이 기록을 정함)로 하되, 규칙은 "등록된 참여자만 투표한다". 계산은 위 두 실험과 같은 함수다.',
  'fly': ('원본 지지 (정직한 장부)', '등록된 장부끼리만 세. 그게 규칙이야.', '정직한 등록 장부 5권'),
  'robo': ('위조본 지지 (고친 장부 + 가짜 장부)', '표는 표지! 많은 쪽이 이기는 거 아냐?', '고친 4권 + 가짜 6권'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>투표 함수 vote(장부 목록, 규칙): 규칙이 "등록된 참여자만"이면 등록 장부의 표만 센다. 초파리 쪽 표 = 9 − 4 = 5, Money-Robo 쪽 표(모두 셈) = 4 + 6 = 10. Money-Robo의 표 가운데 등록되지 않은 표가 있으므로 규칙 위반(foul)으로 처리한다. 규칙대로 세면 5 대 4로 원본이 이긴다.</p><p class="lim">이 대결은 "투표권을 누구에게 주나"를 보이려는 장치다. 실제 비트코인은 등록 명부 없이 계산력으로 표를 정한다(2장).</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>칸</th><th>믿는 대상</th><th>위조하려면</th><th>약점</th></tr></thead><tbody>
   <tr><td>1-03 기억·각자 장부</td><td>상대방</td><td>내 기록만 바꾸면 됨</td><td>판정 불가</td></tr>
   <tr><td>1-04 계약서·도장</td><td>문서의 장치</td><td>사본 하나 없애고 새로 쓰기</td><td>대조 사본 분실</td></tr>
   <tr><td>1-05 증인·공증</td><td>증인·공증인</td><td>증인 매수·공모</td><td>공모, 비용</td></tr>
   <tr><td>1-06 은행 장부</td><td>기관 하나</td><td>그 한 곳을 뚫기</td><td>표적, 단일 실패 지점</td></tr>
   <tr><td>1-07 분산원장</td><td>참여자 다수</td><td>과반을 동시에</td><td>과반이 싸면 무너짐, 투표권 문제</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>장부 "권수"로 표를 세는 것은 설명용 모형이다. 실제 비트코인은 계산력의 과반으로 다수를 정한다(2장).</li><li>"해킹은 현실적으로 불가능"이라는 강의 자료의 표현은 "이익보다 비싸서 할 이유가 없다"로 읽어야 정확하다. 과반을 가진 공격자는 실제로 기록을 바꿀 수 있다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '1장 끝이에요. 장부를 지키는 힘은 "누가 믿을 만한가"에서 "위조가 얼마나 비싼가"로 옮겨 왔어요. 2장에서는 그 비용을 만드는 기술, 해시와 작업증명을 봐요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'blush', 'robo_e14'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, Money-Robo가 머쓱하게 볼을 붉히는 장면',
 'outro': [('doc', 'front', 'doc_e08', '1장의 세 줄.<br>· 장부를 지키는 방법은 사람 → 문서 → 증인 → 기관 → 다수로 올라왔다.<br>· 분산원장은 과반이 위조하지 않는 한 기록을 지킨다.<br>· 과반이 싸지 않도록 "한 표"를 정하는 일이 남았다. 좋은 연구실에는 의심하는 쪽과 확신하는 쪽이 둘 다 필요하다.'),
           ('fly', 'arms', 'fly_e16', '표를 몇 장 모았냐보다, 그 표가 진짜냐가 먼저야.'),
           ('robo', 'blush', 'robo_e14', '…가짜 장부는 투자가 아니었구나. 2장에서 정정당당하게 본전 찾는다.'),
           ('asst', 'e16', 'asst_e16', '1장 대결 결과는 초파리 3승(실격승 1번 포함), Money-Robo 3승, 무승부 1번이에요. 2장 「블록체인 기술」에서 블록과 해시부터 시작해요.')],
 'kg_hint': '분산원장, 과반, 가짜 노드, 투표…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.12 (블록체인 시스템: 다수의 증인, 블록체인의 합의: 과반수의 동의). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 2절(거래가 없었음을 확인하려면 모든 거래를 알아야 함), 4절(IP 하나당 한 표의 약점, CPU 하나당 한 표). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['장부 수 N, 공격 장부 k, 장부 한 권 매수 비용 3,000원, 가짜 노드 비용 100원, 위조 이익 10,000원 (예시값)', '대결: 등록 장부 9권, 고친 장부 4권, 가짜 장부 6권 (설명용 장면)'],
 'gloss_keys': [('분산원장', True), ('과반', True), ('노드', True), ('가짜 노드', True), ('블록체인', True), ('백서', False)],
 'gloss_anchor': {'분산원장': '#lv1', '과반': '#lv1', '노드': '#lv2', '가짜 노드': '#lv2', '블록체인': '#why', '백서': '#lv2'},
 'quiz': {
  'lv1': [{'q': '장부 15권이 있을 때, 위조본이 다수결에서 이기려면 최소 몇 권을 고쳐야 하나?', 'o': ['7권', '8권', '10권', '15권'], 'a': 1, 'why': '⌊15/2⌋+1 = 8권.', 'hint': '절반을 "넘어야" 해요.', 'c': 'lab:concept/majority-vote'},
          {'q': '은행 장부(1-06)와 비교해 분산원장의 위조가 어려운 이유는?', 'o': ['한 곳이 아니라 과반의 장부를 동시에 바꿔야 해서', '장부가 암호로 쓰여 있어서', '은행보다 직원이 많아서', '수수료가 없어서'], 'a': 0, 'why': '맞아요. 공격 목표가 한 곳에서 과반으로 늘어요.', 'hint': '공격자가 뚫어야 할 곳의 수.', 'c': 'lab:method/distributed-ledger'}],
  'lv2': [{'q': '장부 9권, 한 권 매수 비용 3,000원, 위조 이익 10,000원일 때 과반 매수의 손익은?', 'o': ['+5,000원', '−5,000원', '−17,000원', '0원'], 'a': 1, 'why': '과반 5권 × 3,000 = 15,000원, 이익 10,000원 − 15,000원 = −5,000원.', 'hint': '과반은 몇 권?', 'c': 'lab:metric/attack-cost'},
          {'q': '백서가 "IP 주소 하나당 한 표"를 피한 이유는?', 'o': ['많은 IP를 확보한 사람이 다수결을 무너뜨릴 수 있어서', 'IP 주소가 너무 길어서', '인터넷이 느려서', 'IP는 은행이 관리해서'], 'a': 0, 'why': '한 표를 쉽게 복제할 수 있으면 다수결이 의미 없어요. 그래서 CPU 하나당 한 표(작업증명)로 했어요.', 'hint': '가짜 노드 실험.', 'c': 'lab:concept/sybil'}]},
 'kgspec': {
  'ladder': ['lab:method/distributed-ledger', 'lab:method/costly-vote'],
  'about': ['lab:method/distributed-ledger', 'lab:concept/majority-vote', 'lab:concept/sybil', 'lab:metric/attack-cost'],
  'nodes': [
   ('lab:method/costly-vote', 'Method', '복제하기 어려운 투표권', 'votes tied to a costly resource', '#lv2', '한 표를 쉽게 복제할 수 없는 자원(계산력 등)에 묶어 과반 장악 비용을 높이는 방법.', 3, [(WP, '4절')]),
   ('lab:limitation/majority-takeover', 'Limitation', '과반을 장악하면 위조가 이긴다', 'majority takeover', '#lv1', '공격자가 과반의 장부를 장악하면 위조본이 다수결에서 "참"이 된다.', 3),
   ('lab:limitation/open-questions-ch2', 'Limitation', '변조 탐지와 투표 단위 (2장 과제)', 'tamper detection and vote unit', '#lv2', '많은 사본 중 바뀐 것을 빨리 알아볼 방법과, 열린 망에서 한 표를 정하는 방법이 남았다.', 3),
   ('lab:metric/attack-cost', 'Metric', '공격 손익', 'attack profit', '#lv2', '위조 이익에서 과반 장악 비용을 뺀 값. 음수면 공격이 손해다.', 3),
   ('lab:metric/vote-count', 'Metric', '표 수', 'vote count', '#duel', '다수결에서 각 기록을 지지한 장부의 수.', 3),
   ('lab:concept/voting-rule', 'Concept', '투표 규칙 (누가 한 표를 갖나)', 'voting rule', '#lv2', '다수결에서 투표권을 누구에게 주는지 정한 규칙. 등록 참여자, 노드 수, 계산력 등.', 3),
   ('lab:analogy/nine-ledgers', 'Analogy', '아홉 권의 장부 ↔ 분산원장', 'nine ledgers ~ distributed ledger', '#lv1', '참여자 아홉 명이 같은 장부를 한 권씩 들고 다수가 적은 내용을 따른다.', 2),
   ('lab:question/core', 'Question', '모두가 장부를 나눠 들면 위조는 정말 어려워질까? 무엇이 조건일까?', 'Does a shared ledger make forgery hard? Under what condition?', '#top', None, 3),
   ('lab:question/duel', 'Question', '가짜 장부를 끼워 넣은 과반 투표는 유효한가?', 'Is a majority padded with fake ledgers valid?', '#duel', None, 3),
   ('lab:question/vote-unit', 'Question', '열린 망에서 한 표를 무엇으로 정할까?', 'What should count as one vote in an open network?', '#lv2', None, 4),
  ],
  'edges': [
   ('lab:method/distributed-ledger', 'lab:prerequisiteOf', 'lab:method/costly-vote', '#lv2'),
   ('lab:method/distributed-ledger', 'lab:hasLimitation', 'lab:limitation/majority-takeover', '#lv1'),
   ('lab:limitation/majority-takeover', 'lab:addressedBy', 'lab:method/costly-vote', '#lv2'),
   ('lab:method/costly-vote', 'lab:hasLimitation', 'lab:limitation/open-questions-ch2', '#lv2'),
   ('lab:limitation/open-questions-ch2', 'lab:raises', 'lab:question/vote-unit', '#lv2'),
   ('lab:concept/majority-vote', 'lab:partOf', 'lab:method/distributed-ledger', '#lv1'),
   ('lab:term/node', 'lab:partOf', 'lab:method/distributed-ledger', '#lv2'),
   ('lab:concept/sybil', 'lab:partOf', 'lab:limitation/majority-takeover', '#lv2'),
   ('lab:concept/voting-rule', 'lab:prerequisiteOf', 'lab:method/costly-vote', '#lv2'),
   ('lab:concept/sybil', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:method/distributed-ledger', 'lab:evaluatedBy', 'lab:metric/attack-cost', '#lv2'),
   ('lab:method/distributed-ledger', 'lab:evaluatedBy', 'lab:metric/vote-count', '#duel'),
   ('lab:concept/blockchain', 'lab:broader', 'lab:method/distributed-ledger', '#why'),
   ('lab:analogy/nine-ledgers', 'lab:analogyOf', 'lab:method/distributed-ledger', '#lv1'),
   ('lab:limitation/majority-takeover', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:term/white-paper', 'lab:relatedTo', 'lab:method/costly-vote', '#lv2', 'mid'),
  ],
  'claims': [
   ('lab:claim/many-witnesses', '블록체인 시스템은 다수의 증인을 세워, A·B의 거래 사실이 망에 동시에 기록되고 진위는 망의 데이터 조회로 판정한다', '#why', ['lab:method/distributed-ledger'], [(LEC, '교안 p.12')], 'F01'),
   ('lab:claim/majority-needed', '위조가 "참"이 되려면 전체 망 사용자의 50%가 넘는 장부를 동시에 바꿔야 한다', '#why', ['lab:concept/majority-vote', 'lab:limitation/majority-takeover'], [(LEC, '교안 p.12')], 'F02'),
   ('lab:claim/cost-exceeds-gain', '과반 해킹 능력은 갖추기 어렵고, 성공해도 비용이 이익보다 커 현실적으로 불가능하다(강의 자료의 표현)', '#why', ['lab:metric/attack-cost'], [(LEC, '교안 p.12')], 'F03'),
   ('lab:claim/know-all-transactions', '거래가 없었음을 확인하려면 모든 거래를 알아야 하며, 거래를 공개하고 참여자들이 하나의 순서에 합의해야 한다', '#lv1', ['lab:method/distributed-ledger'], [(WP, '2절')], 'F04'),
   ('lab:claim/one-cpu-one-vote', 'IP 주소 하나당 한 표의 다수결은 많은 IP를 확보한 사람이 무너뜨릴 수 있어, 작업증명은 CPU 하나당 한 표로 한다', '#lv2', ['lab:concept/sybil', 'lab:method/costly-vote'], [(WP, '4절')], 'F05'),
  ],
  'sims': [('lab:simulation/majority-vote', '과반 투표 실험', '#lv1', ['lab:concept/majority-vote']),
           ('lab:simulation/attack-cost', '과반 매수 대 가짜 노드 손익 실험', '#lv2', ['lab:concept/sybil']),
           ('lab:simulation/duel-fake-votes', '가짜 장부 투표 대결', '#duel', ['lab:metric/vote-count'])],
 },
}
