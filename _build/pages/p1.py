from template import say
LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '1-01', 'slug': 'money-is-record', 'key': '1_01', 'anchor': 'C',
 'tab_title': '돈은 기록이다', 'meta_title': '블록체인의 등장 — 돈은 기록이다',
 'description': '비트코인 백서가 던진 질문에서 출발해, 돈이 장부의 숫자라는 것과 디지털 돈의 이중 지불 문제를 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.3–4; Nakamoto (2008) 1–2절',
 'h1': '블록체인의 등장<br>— 돈은 기록이다', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '인터넷에서 오가는 돈은 결국 무엇이고, 왜 "장부"가 문제의 한가운데 있을까?',
 'lead': '2008년 10월, 사토시 나카모토라는 필명의 인물이 중앙은행 같은 기관 없이 돌아가는 전자 화폐를 제안했습니다. 그 제안을 이해하려면 먼저 두 가지를 봐야 해요. 돈은 장부에 적힌 숫자라는 것, 그리고 디지털 숫자는 복사된다는 것.',
 'kpis': [('2008. 10', '비트코인 논문 발표', 'a', [1]), ('2009', 'Bitcoin Core 프로그램으로 처음 발행', 'g', [1]),
          ('2가지', '논문의 핵심 주제: 분산원장 · 디지털 화폐', 'm', [1]), ('확인 불가', '필명 저자의 나이·거주지·이름', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '은행 계좌의 돈은 어디에 있을까요? 금고 속 지폐가 아니라 장부의 숫자예요. 오늘은 거기서 시작해요.'),
          ('asst', 'smile', 'asst_e13', '송금을 직접 해 보고, 같은 디지털 쿠폰을 두 번 써 볼 거예요. 숫자는 제가 세어 둘게요.'),
          ('fly', 'point', 'fly_e08', '파일은 복사하면 그만이잖아. 그럼 디지털 돈도 복사되는 거 아냐?'),
          ('robo', 'coin', 'robo_e16', '돈 얘기라면 내가 빠질 수 없지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정. 판정은 숫자대로만 한다.'), ('asst', 'smile', 'asst_e13', '실험을 돌리고 숫자를 발표한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. "정말 그래?"를 끝까지 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 빠르고 큰 쪽에 건다.')],
 'why_title': '왜 비트코인 백서에서 시작하나',
 'why_lead': '이 챕터는 "장부를 누가, 어떻게 지키나"의 역사를 일곱 편에 걸쳐 따라갑니다. 출발점은 그 질문을 정면으로 던진 2008년 논문이에요.',
 'why': [('기관 없는 돈이라는 질문', '논문은 기존 금융 시스템의 문제를 짚고, 국가나 기관의 개입 없이 운영되는 전자 화폐 시스템을 제안했다. <sup>[1]</sup>'),
         ('두 개의 주제', '하나는 기술 기반인 분산원장(블록체인), 다른 하나는 그 위에 만든 디지털 화폐(비트코인)다. <sup>[1]</sup>'),
         ('이 페이지에서 할 일', '돈 = 장부의 숫자임을 확인하고, 디지털 숫자가 복사될 때 생기는 이중 지불을 직접 일으켜 본다.')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 디지털 화폐의 어려움은 "돈을 만드는 것"이 아니라 "같은 돈을 두 번 못 쓰게 하는 것"이에요.'),
 'big_lead': '이 편은 사다리의 출발점입니다. 장부가 왜 필요한지 보이고, 마지막에 "그 장부는 누가 지키나"라는 질문을 다음 편으로 넘깁니다.',
 'ladder': [('①', '장부의 숫자로서의 돈', '송금 = 장부 숫자 옮기기, 총액이 보존된다', '디지털 숫자는 복사할 수 있다'),
            ('②', '쓴 기록을 장부로 확인', '같은 돈을 두 번 쓰는 것을 막는다', '그 장부를 누가 지키고, 누가 믿을 수 있나 → 1-02~1-07')],
 'big_say': ('robo', 'chart', 'robo_e07', '장부 숫자가 곧 돈이라면, 장부를 쥔 쪽이 돈을 쥔 거네? 흥미로운데!'),
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '돈 = 숫자', 'title': '돈은 장부의 숫자다',
   'tags': [('방식: 송금 = 한 칸에서 빼고 다른 칸에 더하기', 'g'), ('장부: 세 사람의 잔액 표', '')],
   'left': '<p>A가 B에게 3,000원을 보내면, 장부에서 A 칸의 숫자가 3,000 줄고 B 칸이 3,000 는다. 지폐는 움직이지 않는다. 장부 전체의 합은 그대로다.</p>',
   'right': '<p>블록체인도 결국 이런 <b>거래 기록</b>을 쌓는 장부다. 차이는 그 장부를 은행 한 곳이 아니라 네트워크 참여자 모두가 함께 저장하고 검증한다는 점이다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 세 사람의 잔액 장부</h3>
    <div class="cwrap"><canvas id="c1" aria-label="A, B, C 세 사람의 잔액 막대와 장부 기록 목록"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">송금</span>
      <button class="bt" data-tx="0,1">A → B</button><button class="bt" data-tx="1,2">B → C</button><button class="bt" data-tx="2,0">C → A</button></div>
      <div class="group"><span class="glabel">금액</span><input type="range" id="r1a" min="1000" max="5000" step="1000" value="3000" aria-label="송금 금액"><span class="val" id="v1a">3000</span>원</div>
      <div class="group"><button class="bt warn" id="b1Print">장부 없이 A 칸 숫자만 고치기</button><button class="bt" id="b1Reset">처음으로</button></div></div>
    <h3>행동으로 보기 — 금화가 칸을 옮겨 간다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="세 사람 사이로 금화가 이동하는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 장부가 돈을 만든다</h4>
    <ol><li>송금은 한 칸에서 빼고 다른 칸에 더하는 두 줄짜리 기록이다. 그래서 총액이 보존된다.</li>
      <li>기록 없이 숫자만 고치면 총액이 늘어난다. 장부를 쥔 쪽은 돈을 "찍어 낼" 수 있다는 뜻이다.</li>
      <li>그래서 장부는 고칠 수 없어야 하고, 누가 고쳤는지 드러나야 한다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 종이 장부의 숫자는 한 곳에만 있지만, 디지털 숫자는 파일이라 그대로 복사된다. → 복사된 돈을 어떻게 막나?</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '총액이 갑자기 늘었어. 기록 없이 숫자를 고치면 돈이 생겨나는구나.'),
   'extra': '<div class="bridge gen"><h4>생성 AI로 치면</h4><p>모델의 "기억"도 결국 숫자(가중치)의 표다. 누가 언제 그 숫자를 바꿨는지 기록하지 않으면, 어떤 버전이 진짜인지 알 수 없다. 모델 버전 관리가 장부 역할을 한다.</p><p class="lim">가중치 표는 돈처럼 "총액 보존" 규칙이 없다. 닮은 건 기록과 검증의 필요성뿐이다.</p></div>'},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '이중 지불', 'title': '디지털 돈은 복사된다 — 이중 지불',
   'tags': [('방식: 쓴 쿠폰을 장부에 표시하고 결제 전에 확인', 'g'), ('장부: 쿠폰 사용 기록부', '')],
   'left': '<p>상품권 한 장을 복사기로 두 장 만들어 두 가게에서 쓴다고 해 보자. 종이라면 위조 방지 무늬가 막지만, 디지털 파일은 원본과 사본이 완전히 같다. 가게가 할 수 있는 일은 "이 일련번호, 이미 쓰였나?"를 <b>장부에서 확인</b>하는 것뿐이다.</p>',
   'right': '<p>백서는 이를 이중 지불 문제로 불렀다. 받는 사람은 앞선 주인이 같은 돈을 두 번 쓰지 않았는지 확인할 수 없고, 흔한 해결책은 모든 거래를 확인하는 믿을 만한 중앙 기관을 두는 것이다. 거래가 <b>없었음</b>을 확인하는 유일한 방법은 모든 거래를 아는 것이다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 쿠폰 한 장, 가게 두 곳</h3>
    <div class="cwrap"><canvas id="c2" aria-label="쿠폰 파일 하나가 복사되어 가게 두 곳으로 가는 그림과 사용 기록부"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">가게의 확인 방식</span>
      <button class="bt" data-chk="0" aria-pressed="true">파일만 보고 받기</button><button class="bt" data-chk="1" aria-pressed="false">결제 전 사용 기록부 확인</button></div>
      <div class="group"><button class="bt warn" id="b2Copy">쿠폰 복사해서 두 가게에 동시에 쓰기</button><button class="bt" id="b2Reset">처음으로</button></div></div>
    <h3>행동으로 보기 — 같은 쿠폰이 두 번 결제될까</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="쿠폰 사본 두 개가 가게 두 곳으로 날아가 받아들여지거나 거절되는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 확인하려면 모든 거래를 알아야 한다</h4>
    <ol><li>파일만 보고 받으면 사본도 원본과 똑같이 통과한다. 쿠폰 한 장이 두 번 쓰인다.</li>
      <li>사용 기록부가 있으면 두 번째 결제는 "이미 사용됨"으로 거절된다.</li>
      <li>단, 두 가게가 <b>같은 기록부</b>를 봐야 한다. 가게마다 따로 기록하면 서로의 사용 내역을 모른다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 모두가 같은 기록부를 봐야 한다면, 그 기록부는 누가 갖고 누가 지키나? 백서 이전의 답은 "믿을 만한 중앙 기관"이었다. <sup>[2]</sup> → 1-02부터 그 답들을 하나씩 시험한다.</p>''',
   'extra': '''<details class="math"><summary>수식으로 보기</summary><p>가게 S개가 각자 기록부를 갖고 있고 공격자가 같은 쿠폰을 S곳에 동시에 쓰면, 받아들여지는 결제 수는 <b>S</b>건(손해 S−1건). 기록부를 하나로 공유하면 <b>1</b>건만 통과한다. 공유 기록부의 핵심은 "모두가 같은 순서의 기록을 본다"는 것이다.</p>
     <p class="lim">이 실험의 쿠폰은 디지털 화폐를 단순화한 비유다. 실제 비트코인은 쿠폰 번호가 아니라 이전 거래의 출력을 쓰는 방식으로 이중 지불을 확인한다.</p></details>''',
   'say': ('asst', 'e10', 'asst_e10', '기록부를 보지 않으면 쿠폰 한 장이 두 번 결제돼요. 기록부를 보면 두 번째는 바로 거절돼요.')},
 ],
 'duel': {'title': '디지털 상품권 100번 결제, 가게의 손해는?',
  'intro': '손님 100명이 디지털 상품권으로 결제한다. 그중 일부(예시값 30%)는 같은 상품권을 다른 가게에서도 동시에 쓰려 한다. 판정 기준은 <b>가게가 받아 준 가짜(중복) 결제 건수</b>(적을수록 좋음). 시드 고정 시뮬레이션.',
  'fly': ('결제 전 공유 사용 기록부 확인', '받기 전에 이미 쓴 건지 보자. 조금 느려도.', '공유 기록부 조회 후 승인'),
  'robo': ('파일만 받으면 바로 승인', '확인하는 시간도 비용이야. 파일 멀쩡하면 OK!', '즉시 승인'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>시드 101로 손님 100명을 만들고, 각자 확률 0.3(예시값)으로 같은 상품권을 두 번째 가게에서도 쓰려 한다. 초파리 방식은 공유 기록부에서 "사용됨"을 확인해 두 번째 결제를 거절하고, Money-Robo 방식은 둘 다 승인한다.</p><p class="lim">공유 기록부가 정직하다고 가정했다. 그 기록부를 누가 지키는지가 이 챕터 나머지의 주제다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>칸</th><th>무엇을 배웠나</th><th>남은 질문</th></tr></thead><tbody>
   <tr><td>① 돈 = 숫자</td><td>송금은 장부 두 칸의 숫자를 옮기는 일, 총액이 보존된다</td><td>기록 없이 숫자를 고치면?</td></tr>
   <tr><td>② 이중 지불</td><td>디지털 돈은 복사되므로, 쓴 기록을 모두가 같은 장부에서 확인해야 한다</td><td>그 장부는 누가 지키나?</td></tr></tbody></table></div>
   <div class="explain"><h4>장부 비유의 한계</h4><ul><li>은행 장부는 "계좌별 잔액"을 적지만, 비트코인은 계좌 잔액 대신 거래의 결과를 이어 붙여 잔액을 계산한다(3장에서 다룬다).</li><li>"공유 기록부"는 아직 누가 운영하는지 정하지 않은 상상의 장치다. 이 챕터는 그 운영자를 사람 → 기관 → 다수로 바꿔 가며 시험한다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '정리하면, 디지털 돈의 문제는 장부의 문제예요. 다음 편에서는 장부를 한 곳에 둘지, 여러 곳에 둘지 구조부터 비교해요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'blush', 'robo_e14'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '회계실 무대 위에 박사, 초파리 연구원, Money-Robo, 하루가 나란히 선 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 돈은 장부의 숫자다.<br>· 디지털 숫자는 복사되므로 같은 돈을 두 번 쓸 수 있다.<br>· 막으려면 모두가 같은 기록을 봐야 하고, 그 기록을 누가 지키느냐가 다음 질문이다.'),
           ('fly', 'arms', 'fly_e16', '확인 한 번이 손해 서른 건을 막았어. 느린 게 아니라 안전한 거야.'),
           ('robo', 'blush', 'robo_e14', '빠른 승인이 곧 손해였네. 이번 판은 손절, 다음 편에서 본전 찾는다.'),
           ('asst', 'e16', 'asst_e16', '다음은 1-02, 장부를 한 곳에 모을지 여러 곳에 나눌지 네트워크 모양부터 비교해요.')],
 'kg_hint': '이중 지불, 장부, 백서…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.3–4 (PDF 45쪽, 2024-10-18 생성). 교안이 인용한 그림 출처는 원 교안을 따른다.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 초록, 1절(금융기관 의존·중개 비용), 2절(이중 지불·중앙 기관·모든 거래를 알아야 함). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['① 잔액 10,000원씩, 송금 1,000~5,000원 (예시값)', '② 쿠폰 한 장, 가게 두 곳 (설명용 장면)', '대결: 손님 100명, 중복 사용 시도 확률 0.3, 시드 101 (예시값)'],
 'gloss_keys': [('장부', True), ('블록체인', True), ('분산원장', True), ('비트코인', True), ('백서', True), ('이중 지불', True), ('중개자', True)],
 'gloss_anchor': {'장부': '#lv1', '블록체인': '#why', '분산원장': '#why', '비트코인': '#top', '백서': '#lv2', '이중 지불': '#lv2', '중개자': '#lv2'},
 'quiz': {
  'lv1': [{'q': 'A가 B에게 3,000원을 보낸 뒤 세 사람 잔액의 합은?', 'o': ['3,000원 줄어든다', '그대로다', '3,000원 늘어난다', '6,000원 줄어든다'], 'a': 1, 'why': '한 칸에서 빼고 다른 칸에 더하므로 총액은 보존돼요.', 'hint': '빼는 줄과 더하는 줄을 함께 생각해 보세요.', 'c': 'lab:concept/money-as-record'},
          {'q': '장부 기록 없이 A 칸 숫자만 2,000 늘리면 무슨 일이 생기나?', 'o': ['총액이 2,000 늘어 돈이 새로 생긴다', 'B 잔액이 자동으로 준다', '아무 일도 없다', '장부가 스스로 고친다'], 'a': 0, 'why': '맞아요. 장부를 고칠 수 있는 쪽은 돈을 찍어 낼 수 있어요.', 'hint': 'KPI의 총액을 보세요.', 'c': 'lab:limitation/digital-copy'}],
  'lv2': [{'q': '가게 3곳이 각자 따로 사용 기록부를 쓸 때, 같은 쿠폰을 3곳에 동시에 쓰면 몇 건이 통과하나?', 'o': ['1건', '2건', '3건', '0건'], 'a': 2, 'why': '각자 기록부는 서로의 사용 내역을 모르니 3곳 모두 통과해요. 공유 기록부라면 1건.', 'hint': '기록부가 하나인지 셋인지가 핵심이에요.', 'c': 'lab:concept/double-spending'},
          {'q': '백서가 말한, 백서 이전의 흔한 이중 지불 해결책은?', 'o': ['모든 거래를 확인하는 믿을 만한 중앙 기관(조폐국)', '쿠폰에 위조 방지 무늬 넣기', '거래를 아예 금지하기', '모든 쿠폰을 종이로 바꾸기'], 'a': 0, 'why': '맞아요. 백서 2절의 표현으로 "trusted central authority, or mint"예요.', 'hint': '백서 2절.', 'c': 'lab:method/shared-ledger-check'}]},
 'kgspec': {
  'ladder': ['lab:concept/money-as-record', 'lab:method/shared-ledger-check'],
  'about': ['lab:concept/money-as-record', 'lab:concept/double-spending', 'lab:concept/bitcoin', 'lab:concept/blockchain'],
  'nodes': [
   ('lab:concept/money-as-record', 'Concept', '장부의 숫자로서의 돈', 'money as ledger entries', '#lv1', '계좌의 돈은 장부에 적힌 숫자이고, 송금은 한 칸에서 빼고 다른 칸에 더하는 기록이다.', 1),
   ('lab:method/shared-ledger-check', 'Method', '공유 사용 기록부 확인', 'checking a shared spending record', '#lv2', '결제 전에 모두가 보는 같은 기록부에서 이미 쓰였는지 확인하는 방법.', 2),
   ('lab:limitation/digital-copy', 'Limitation', '디지털 숫자는 복사된다', 'digital data can be copied', '#lv1', '파일은 원본과 사본이 같아, 기록 없이는 같은 돈이 두 번 쓰일 수 있다.', 1),
   ('lab:limitation/who-keeps-ledger', 'Limitation', '그 장부는 누가 지키나', 'who keeps the ledger', '#lv2', '모두가 같은 기록부를 봐야 하지만, 그 기록부를 운영·보호할 주체가 정해지지 않았다.', 2),
   ('lab:person/satoshi-nakamoto', 'Term', '사토시 나카모토 (필명)', 'Satoshi Nakamoto (pseudonym)', '#top', '비트코인 논문 저자의 필명. 나이·거주지·이름 어느 것도 진위를 확인할 수 없다.', 1, [(LEC, '교안 p.3')]),
   ('lab:metric/accepted-duplicates', 'Metric', '받아 준 중복 결제 건수', 'accepted duplicate payments', '#duel', '가게가 받아 준 이중 지불 결제의 수. 적을수록 좋다.', 2),
   ('lab:method/instant-accept', 'Method', '파일만 보고 즉시 승인', 'instant acceptance without check', '#duel', '기록 확인 없이 받은 디지털 파일을 그대로 결제로 인정하는 방식.', 2),
   ('lab:question/core', 'Question', '인터넷에서 오가는 돈은 무엇이고 왜 장부가 문제의 중심일까?', 'What is online money and why is the ledger central?', '#top', None, 1),
   ('lab:question/duel', 'Question', '디지털 상품권 결제에서 가게의 손해를 줄이려면?', 'How to avoid losses from duplicated vouchers?', '#duel', None, 2),
   ('lab:analogy/voucher-copy', 'Analogy', '복사한 상품권 ↔ 이중 지불', 'copied voucher ~ double-spending', '#lv2', '복사기로 만든 상품권 사본을 두 가게에서 쓰는 장면.', 2),
  ],
  'edges': [
   ('lab:concept/money-as-record', 'lab:prerequisiteOf', 'lab:method/shared-ledger-check', '#lv2'),
   ('lab:concept/money-as-record', 'lab:hasLimitation', 'lab:limitation/digital-copy', '#lv1'),
   ('lab:limitation/digital-copy', 'lab:addressedBy', 'lab:method/shared-ledger-check', '#lv2'),
   ('lab:method/shared-ledger-check', 'lab:hasLimitation', 'lab:limitation/who-keeps-ledger', '#lv2'),
   ('lab:limitation/who-keeps-ledger', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:limitation/digital-copy', 'lab:prerequisiteOf', 'lab:concept/double-spending', '#lv2'),
   ('lab:method/shared-ledger-check', 'lab:solves', 'lab:concept/double-spending', '#lv2'),
   ('lab:concept/money-as-record', 'lab:partOf', 'lab:concept/ledger', '#lv1'),
   ('lab:concept/trusted-third-party', 'lab:relatedTo', 'lab:limitation/who-keeps-ledger', '#lv2', 'mid'),
   ('lab:concept/blockchain', 'lab:broader', 'lab:method/distributed-ledger', '#why'),
   ('lab:concept/bitcoin', 'lab:relatedTo', 'lab:concept/blockchain', '#why'),
   ('lab:term/white-paper', 'lab:partOf', 'lab:concept/bitcoin', '#top'),
   ('lab:person/satoshi-nakamoto', 'lab:partOf', 'lab:term/white-paper', '#top'),
   ('lab:method/shared-ledger-check', 'lab:contrastsWith', 'lab:method/instant-accept', '#duel'),
   ('lab:method/shared-ledger-check', 'lab:evaluatedBy', 'lab:metric/accepted-duplicates', '#duel'),
   ('lab:method/instant-accept', 'lab:evaluatedBy', 'lab:metric/accepted-duplicates', '#duel'),
   ('lab:concept/double-spending', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:analogy/voucher-copy', 'lab:analogyOf', 'lab:concept/double-spending', '#lv2'),
  ],
  'claims': [
   ('lab:claim/bitcoin-2008-2009', '비트코인은 2008년 10월 사토시 나카모토의 논문으로 소개되고 2009년 Bitcoin Core로 처음 발행됐다', '#top', ['lab:concept/bitcoin', 'lab:term/white-paper'], [(LEC, '교안 p.3')], 'F01'),
   ('lab:claim/two-themes', '논문의 핵심 주제는 분산원장(블록체인)과 그 위의 디지털 화폐(비트코인) 두 가지다', '#why', ['lab:concept/blockchain', 'lab:concept/bitcoin'], [(LEC, '교안 p.4')], 'F02'),
   ('lab:claim/no-central-authority', '논문은 국가나 기관의 개입 없이 운영되는 전자 화폐 시스템을 제안했다', '#why', ['lab:concept/bitcoin'], [(LEC, '교안 p.4')], 'F03'),
   ('lab:claim/double-spend-problem', '받는 사람은 앞선 주인이 이중 지불하지 않았는지 확인할 수 없고, 흔한 해결책은 모든 거래를 확인하는 중앙 기관이다', '#lv2', ['lab:concept/double-spending', 'lab:concept/trusted-third-party'], [(WP, '2절')], 'F04'),
   ('lab:claim/know-all-transactions', '거래가 없었음을 확인하는 유일한 방법은 모든 거래를 아는 것이다', '#lv2', ['lab:method/shared-ledger-check'], [(WP, '2절')], 'F05'),
   ('lab:claim/mediation-cost', '중개 비용은 거래 비용을 높여 실용적인 최소 거래 규모를 제한한다', '#why', ['lab:concept/trusted-third-party'], [(WP, '1절')], 'F06'),
  ],
  'sims': [('lab:simulation/balance-ledger', '세 사람 잔액 장부 실험', '#lv1', ['lab:concept/money-as-record']),
           ('lab:simulation/voucher-copy', '쿠폰 복사 실험', '#lv2', ['lab:concept/double-spending']),
           ('lab:simulation/duel-vouchers', '상품권 100번 결제 대결', '#duel', ['lab:method/shared-ledger-check'])],
 },
}
