LEC = "lecture2024blockchain"
PAGE = {
 'num': '1-03', 'slug': 'memory-and-ledger', 'key': '1_03', 'anchor': 'D',
 'tab_title': '기억과 장부', 'meta_title': '기억과 장부 — 만 원을 빌린 날',
 'description': '동료에게 만 원을 빌린 장면(시나리오 1·2)으로 기억과 각자 쓰는 장부의 한계를 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.6–7',
 'h1': '기억과 장부<br>— 만 원을 빌린 날', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '직장 동료끼리 빌린 만 원, 한 달 뒤에도 둘이 같은 금액을 기억할까? 장부를 쓰면 해결될까?',
 'lead': '강의 자료의 시나리오 1·2입니다. 지갑을 두고 온 A가 동료 B에게 점심값과 교통비로 10,000원을 빌립니다. 처음에는 기억으로, 다음에는 각자 장부로 기록해요. 두 방법이 언제 무너지는지 시간을 돌려 가며 확인합니다.',
 'kpis': [('10,000원', '시나리오의 빌린 금액 (점심값·교통비)', 'a', [1]), ('기억', '시나리오 1의 기록 수단', 'r', [1]), ('각자 장부', '시나리오 2의 기록 수단', 'g', [1]), ('서로 확인', '장부 조작을 막으려 생긴 절차', 'm', [1])],
 'hero': [('doc', 'think', 'doc_e09', '만 원은 작은 돈이라 대수롭지 않게 넘기기 쉬워요. 그런데 한 달 뒤에도 둘의 기억이 같을까요?'),
          ('asst', 'smile', 'asst_e13', '날짜를 0일에서 60일까지 돌려 볼 수 있게 해 뒀어요. 기억이 맞을 확률을 제가 계산할게요.'),
          ('fly', 'point', 'fly_e08', '기억은 믿을 게 못 돼. 장부를 써도 잃어버리면 끝 아냐?'),
          ('robo', 'coin', 'robo_e16', '만 원 갖고 장부까지? 기억이면 충분하지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '기억 확률과 장부 보존율을 계산한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 잊어버린 뒤를 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 작은 돈엔 기록이 필요 없다고 본다.')],
 'why_title': '왜 이렇게 작은 장면에서 시작하나',
 'why_lead': '블록체인이 해결하려는 문제는 거창한 금융 사고가 아니라, 이런 작은 거래에서 이미 다 드러나요.',
 'why': [('기억은 흐려진다', '빌린 사실을 기억했다가 가까운 장래에 갚는다. 하지만 기억은 시간이 지날수록 잊혀질 가능성이 높다. <sup>[1]</sup>'),
         ('거짓말할 수도 있다', '경우에 따라서는 A나 B가 의도적으로 거짓말을 할 확률도 있다. <sup>[1]</sup>'),
         ('장부도 완벽하지 않다', '그래서 각자 장부에 쓰지만, 장부는 잃어버릴 수 있고 각자 조작할 위험이 있다. 그래서 서로 장부를 확인하는 절차가 생긴다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 기록의 첫 번째 적은 시간이고, 두 번째 적은 사람의 손이에요.'),
 'big_lead': '1-01·1-02에서 문제와 구조를 봤으니, 여기서부터 장부 지키기의 역사를 처음부터 올라갑니다. 가장 아래 칸은 기억, 그다음은 각자 쓰는 장부예요.',
 'ladder': [('①', '기억 (시나리오 1)', '아무 도구 없이 거래를 기억한다', '시간이 지나면 흐려지고, 거짓말을 가려낼 수 없다'),
            ('②', '각자 장부 (시나리오 2)', '기록이 시간이 지나도 남는다', '분실·조작 위험, 두 장부가 다르면 판정 불가 → 1-04 계약서')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '기억', 'title': '기억으로만 남긴 빚 — 시나리오 1',
   'tags': [('방식: 당사자 둘의 기억', 'g'), ('일상: 동료에게 빌린 점심값', '')],
   'left': '<p>A는 다음 날 갚을 생각이다. B도 금액이 작고 동료 사이라 대수롭지 않게 넘긴다. 둘 다 아무것도 적지 않았다. 일주일, 한 달이 지나면 "얼마였더라?"가 시작된다.</p>',
   'right': '<p>블록체인은 기억이 아니라 <b>기록</b>에 기댄다. 그리고 그 기록을 당사자 둘이 아니라 망 전체가 함께 가진다(1-07). 이 칸은 그 출발점, 기록이 전혀 없는 상태다.</p>',
   'panel': '''<h3>직접 해 보기 — 날짜를 돌려 보자</h3>
    <div class="cwrap"><canvas id="c1" aria-label="지난 날짜에 따라 한 사람과 두 사람 모두 금액을 정확히 기억할 확률이 줄어드는 곡선"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">빌린 뒤 지난 날</span><input type="range" id="r1t" min="0" max="60" step="1" value="7" aria-label="빌린 뒤 지난 날"><span class="val" id="v1t">7</span>일</div>
      <div class="group"><button class="bt warn" id="b1Lie" aria-pressed="false">A가 일부러 적게 말하기</button></div></div>
    <h3>행동으로 보기 — 머릿속 금액이 흐려진다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="A와 B의 생각 풍선 속 금액이 날짜가 지날수록 흐려지는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 둘이 함께 기억할 확률은 더 빨리 준다</h4>
    <ol><li>한 사람이 정확히 기억할 확률을 p라 하면, 두 사람 모두 같은 금액을 기억할 확률은 p × p다. 한 사람이 50%면 둘 다는 25%.</li>
      <li>한쪽이 일부러 적게 말하면, 다른 한쪽의 기억과 엇갈려도 누가 맞는지 증명할 길이 없다.</li>
      <li>이 그래프의 기억 곡선(반감 약 10일)은 원리를 보이려고 정한 예시값이다. 실제 기억은 사람과 상황에 따라 다르다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 기억은 흐려지고, 거짓말을 가려낼 수 없다. → 적어 두자.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '한 달이면 둘 다 정확히 기억할 확률이 거의 없네. 그리고 A가 우기면 끝이야.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '각자 장부', 'title': '각자 장부에 쓴다 — 시나리오 2',
   'tags': [('방식: 당사자가 각자 장부에 기록 + 서로 확인', 'g'), ('일상: 둘의 수첩', '')],
   'left': '<p>A와 B가 각자 수첩에 "10/28 A가 B에게 10,000원 빌림"이라고 적는다. 시간이 지나도 글자는 흐려지지 않는다. 하지만 수첩은 잃어버릴 수 있고, 몰래 고칠 수도 있다. 그래서 가끔 서로 수첩을 맞춰 본다.</p>',
   'right': '<p>"서로 장부를 확인하는 절차"는 블록체인에서 참여자들이 장부를 함께 검증하는 일의 아주 작은 형태다. 둘이 확인하면 <b>다르다</b>는 건 알 수 있지만, <b>누가</b> 고쳤는지는 알 수 없다.</p>',
   'panel': '''<h3>직접 해 보기 — 잃어버림과 고침</h3>
    <div class="cwrap"><canvas id="c2" aria-label="날짜에 따라 장부 두 권이 모두 남아 있을 확률과 기억이 모두 맞을 확률을 비교하는 곡선"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">장부 한 권을 한 달에 잃어버릴 확률(예시값)</span><input type="range" id="r2l" min="0" max="20" step="1" value="3" aria-label="월 분실 확률"><span class="val" id="v2l">3</span>%</div>
      <div class="group"><button class="bt warn" id="b2Forge" aria-pressed="false">A가 자기 장부를 5,000원으로 고치기</button><button class="bt" id="b2Check" aria-pressed="true">서로 장부 확인하기</button></div></div>
    <h3>행동으로 보기 — 두 수첩을 맞춰 본다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="A와 B가 각자 수첩을 펼쳐 금액을 비교하는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 남는 기록, 남는 문제</h4>
    <ol><li>장부는 기억보다 훨씬 오래 남는다. 한 달 분실 확률 3%(예시값)면 30일 뒤 두 권 모두 남아 있을 확률은 약 94%.</li>
      <li>서로 확인하면 한쪽이 고친 것을 "다르다"로 찾아낼 수 있다. 하지만 장부만 봐서는 어느 쪽이 원본인지 모른다.</li>
      <li>한 권을 잃어버리면 남은 한 권이 유일한 기록이 되고, 그 주인이 고쳐도 대조할 상대가 없다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 분실과 조작의 위험, 그리고 "다르다는 건 알지만 누가 맞는지 모른다". → 조작 자체를 어렵게 만드는 장치, 계약서(1-04).</p>''',
   'say': ('asst', 'e10', 'asst_e10', '30일 기준으로 장부 두 권이 모두 남을 확률은 94%, 둘의 기억이 모두 맞을 확률은 약 1.4%예요. 차이가 커요.')},
 ],
 'duel': {'title': '30일 뒤, 빌린 금액이 정확히 남아 있을까?',
  'intro': '같은 상황의 동료 100쌍을 시뮬레이션한다(시드 303). 판정 기준은 <b>30일 뒤 두 사람의 기록이 모두 남아 있고 정확한 쌍의 수</b>(많을수록 좋음). 기억 곡선과 분실 확률은 위 실험의 예시값(반감 약 10일, 월 3%)을 그대로 쓴다.',
  'fly': ('각자 장부에 적기', '만 원이라도 적어. 한 달 뒤의 나는 오늘의 나를 몰라.', '월 분실 3%'),
  'robo': ('기억으로 충분', '만 원 갖고 무슨 장부야. 동료끼리 기억하면 되지.', '기억 반감 약 10일'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>한 사람이 t일 뒤 정확히 기억할 확률 p(t) = e<sup>−t/14</sup> (14일은 예시값, 반감 약 9.7일). 장부 한 권이 t일 뒤 남아 있을 확률 s(t) = 0.97<sup>t/30</sup>. 100쌍마다 두 사람에 대해 난수를 뽑아, 둘 다 정확(남아 있음)한 쌍을 센다.</p><p class="lim">기억과 분실을 서로 독립인 확률로 단순화했다. 실제로는 금액이 클수록 잘 기억하고, 장부를 둔 곳에 따라 분실 위험이 다르다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th></th><th>기억 (시나리오 1)</th><th>각자 장부 (시나리오 2)</th></tr></thead><tbody>
   <tr><td>시간이 지나면</td><td class="r">흐려진다 (30일 뒤 둘 다 정확 약 1.4%)</td><td class="g">남는다 (30일 뒤 둘 다 보존 약 94%)</td></tr>
   <tr><td>한쪽이 거짓말·조작하면</td><td class="r">가려낼 수 없다</td><td>서로 확인하면 "다르다"는 안다</td></tr>
   <tr><td>누가 맞는지</td><td class="r">판정 불가</td><td class="r">판정 불가</td></tr>
   <tr><td>한쪽 기록이 사라지면</td><td>—</td><td class="r">남은 쪽이 고쳐도 모른다</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>기억 곡선과 분실 확률은 예시값이다. 결론(기록 &gt; 기억)은 값을 바꿔도 같지만, 차이의 크기는 값에 따라 달라진다.</li><li>블록체인의 "검증"은 두 사람이 수첩을 맞춰 보는 것보다 훨씬 많은 참여자와 정해진 규칙으로 이루어진다(1-07, 2장).</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '기억보다 장부가 낫다. 하지만 장부도 고칠 수 있다. 다음 편은 고치기 어렵게 만드는 장치, 계약서와 도장이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'blush', 'robo_e14'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, Money-Robo가 머쓱해하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 기억은 시간이 지나면 흐려지고, 거짓말을 가려낼 수 없다.<br>· 장부는 오래 남지만 잃어버리거나 고칠 수 있다.<br>· 서로 확인하면 "다르다"는 알지만 "누가 맞는지"는 모른다.'),
           ('fly', 'arms', 'fly_e16', '적어 두는 게 귀찮아도, 한 달 뒤엔 그 수첩이 유일한 증거야.'),
           ('robo', 'blush', 'robo_e14', '기억에 걸었다가 크게 잃었네… 이번 판은 손절. 다음엔 꼭 적을게.'),
           ('asst', 'e16', 'asst_e16', '다음은 1-04, 숫자와 한글을 함께 적고 도장을 맞찍는 계약서를 시험해요.')],
 'kg_hint': '기억, 장부, 분실, 조작…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.6 (시나리오 1: 기억으로만 기록된 채무 거래), p.7 (시나리오 2: 기록매체(장부)를 이용한 거래). 교안의 그림 출처: 블록체인 소개 snowdeer.info (2017.03.24 인용). PDF 2024-10-18 생성.'],
 'examples': ['기억 곡선 p(t)=e^(−t/14) (반감 약 9.7일) — 설명용 가정', '장부 분실 월 3% — 예시값', '조작 금액 5,000원 — 설명용 장면', '대결: 100쌍, 시드 303'],
 'gloss_keys': [('장부', True), ('중개자', False)],
 'gloss_anchor': {'장부': '#lv2', '중개자': '#summary'},
 'quiz': {
  'lv1': [{'q': '한 사람이 금액을 정확히 기억할 확률이 50%라면, 두 사람 모두 정확히 기억할 확률은? (서로 독립이라고 가정)', 'o': ['50%', '25%', '100%', '75%'], 'a': 1, 'why': '0.5 × 0.5 = 0.25. 둘이 함께 맞아야 하니 더 빨리 줄어요.', 'hint': '두 확률을 곱해요.', 'c': 'lab:method/memory-record'},
          {'q': '기억만으로 남긴 거래에서, 한쪽이 일부러 거짓말을 하면?', 'o': ['다른 쪽 기억이 이긴다', '누가 맞는지 증명할 방법이 없다', '금액이 큰 쪽이 맞다', '자동으로 반반 나눈다'], 'a': 1, 'why': '기록이 없으니 둘의 말만 남아요.', 'hint': '증거가 무엇인가요?', 'c': 'lab:limitation/memory-fades'}],
  'lv2': [{'q': '두 사람이 서로 장부를 확인해서 금액이 다르다는 것을 발견했다. 이것만으로 알 수 있는 것은?', 'o': ['누가 고쳤는지', '두 기록 중 하나가 바뀌었다는 것', '원래 금액', '아무것도 모른다'], 'a': 1, 'why': '맞아요. "다르다"는 알지만, 장부만으로는 어느 쪽이 원본인지 몰라요.', 'hint': '두 장부의 지위는 같아요.', 'c': 'lab:method/personal-ledgers'},
          {'q': '한 달 분실 확률이 3%인 장부 두 권이 30일 뒤 모두 남아 있을 확률에 가장 가까운 것은?', 'o': ['97%', '94%', '91%', '50%'], 'a': 1, 'why': '0.97 × 0.97 ≈ 0.941.', 'hint': '한 권이 남을 확률을 두 번 곱해요.', 'c': 'lab:limitation/ledger-loss-tamper'}]},
 'kgspec': {
  'ladder': ['lab:method/memory-record', 'lab:method/personal-ledgers'],
  'about': ['lab:method/memory-record', 'lab:method/personal-ledgers', 'lab:limitation/ledger-loss-tamper'],
  'nodes': [
   ('lab:method/memory-record', 'Method', '기억으로 남긴 거래', 'memory-only record', '#lv1', '거래를 아무 데도 적지 않고 당사자의 기억에만 맡기는 방식 (시나리오 1).', 1, [(LEC, '교안 p.6')]),
   ('lab:method/personal-ledgers', 'Method', '각자 쓰는 장부', 'separate personal ledgers', '#lv2', '당사자가 각자 장부에 거래를 적고 가끔 서로 확인하는 방식 (시나리오 2).', 1, [(LEC, '교안 p.7')]),
   ('lab:limitation/memory-fades', 'Limitation', '기억은 흐려지고 거짓말을 가려낼 수 없음', 'memory fades and lies cannot be detected', '#lv1', '시간이 지날수록 잊혀지고, 의도적 거짓말을 증명할 방법이 없다.', 1),
   ('lab:limitation/ledger-loss-tamper', 'Limitation', '장부 분실·조작, 누가 맞는지 판정 불가', 'ledger loss, tampering, unresolved disputes', '#lv2', '장부는 잃어버리거나 고칠 수 있고, 두 장부가 다르면 어느 쪽이 원본인지 모른다.', 1),
   ('lab:method/mutual-check', 'Method', '서로 장부 확인', 'mutual ledger check', '#lv2', '당사자가 서로의 장부를 맞춰 보는 절차. 불일치는 찾지만 원본은 가리지 못한다.', 2, [(LEC, '교안 p.7')]),
   ('lab:metric/both-accurate', 'Metric', '두 기록이 모두 정확한 비율', 'both records accurate', '#duel', '두 당사자의 기록(기억)이 모두 남아 있고 정확한 쌍의 비율.', 2),
   ('lab:question/core', 'Question', '한 달 뒤에도 둘이 같은 금액을 기억할까? 장부면 해결될까?', 'Will both remember after a month? Does a ledger solve it?', '#top', None, 1),
   ('lab:question/duel', 'Question', '30일 뒤 빌린 금액이 정확히 남아 있을까?', 'Is the amount still accurate after 30 days?', '#duel', None, 2),
   ('lab:question/who-is-right', 'Question', '두 장부가 다르면 누가 맞는가?', 'If two ledgers differ, which one is right?', '#lv2', None, 2),
  ],
  'edges': [
   ('lab:method/memory-record', 'lab:prerequisiteOf', 'lab:method/personal-ledgers', '#lv2'),
   ('lab:method/memory-record', 'lab:hasLimitation', 'lab:limitation/memory-fades', '#lv1'),
   ('lab:limitation/memory-fades', 'lab:addressedBy', 'lab:method/personal-ledgers', '#lv2'),
   ('lab:method/personal-ledgers', 'lab:hasLimitation', 'lab:limitation/ledger-loss-tamper', '#lv2'),
   ('lab:limitation/ledger-loss-tamper', 'lab:raises', 'lab:question/who-is-right', '#lv2'),
   ('lab:method/mutual-check', 'lab:partOf', 'lab:method/personal-ledgers', '#lv2'),
   ('lab:method/personal-ledgers', 'lab:partOf', 'lab:concept/ledger', '#lv2'),
   ('lab:method/memory-record', 'lab:contrastsWith', 'lab:method/personal-ledgers', '#duel'),
   ('lab:method/memory-record', 'lab:evaluatedBy', 'lab:metric/both-accurate', '#duel'),
   ('lab:method/personal-ledgers', 'lab:evaluatedBy', 'lab:metric/both-accurate', '#duel'),
   ('lab:metric/both-accurate', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/memory-fades', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:question/who-is-right', 'lab:relatedTo', 'lab:concept/trusted-third-party', '#summary', 'mid'),
  ],
  'claims': [
   ('lab:claim/memory-fades', '기억은 시간이 지날수록 잊혀질 가능성이 높고, 당사자가 의도적으로 거짓말을 할 수도 있다', '#why', ['lab:limitation/memory-fades'], [(LEC, '교안 p.6')], 'F01'),
   ('lab:claim/ledger-risks', '장부는 잃어버릴 수 있고 각자 조작할 위험이 있어, 서로 장부를 확인하는 절차가 생긴다', '#why', ['lab:limitation/ledger-loss-tamper', 'lab:method/mutual-check'], [(LEC, '교안 p.7')], 'F02'),
   ('lab:claim/scenario-10000', '시나리오 1은 지갑을 두고 온 A가 동료 B에게 점심값·교통비 10,000원을 빌리는 장면이다', '#top', ['lab:method/memory-record'], [(LEC, '교안 p.6')], 'F03'),
  ],
  'sims': [('lab:simulation/memory-curve', '기억 곡선 실험', '#lv1', ['lab:method/memory-record']),
           ('lab:simulation/ledger-survival', '장부 보존·조작 실험', '#lv2', ['lab:method/personal-ledgers']),
           ('lab:simulation/duel-30days', '30일 뒤 정확도 대결', '#duel', ['lab:metric/both-accurate'])],
 },
}
