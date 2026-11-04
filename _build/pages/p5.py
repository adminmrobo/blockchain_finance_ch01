LEC, SEOUL = "lecture2024blockchain", "seoul2019perjury"
PAGE = {
 'num': '1-05', 'slug': 'witness-and-notary', 'key': '1_05', 'anchor': 'D',
 'tab_title': '증인과 공증', 'meta_title': '증인과 공증 — 당사자 밖의 확인',
 'description': '증인을 몇 명 세워야 믿을 수 있는지, 증인이 공모하면 어떻게 되는지, 그리고 공증이 왜 생겼는지를 확률로 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.9–10',
 'h1': '증인과 공증<br>— 당사자 밖의 확인', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '당사자가 아닌 사람에게 확인을 맡기면 믿을 수 있을까? 증인은 몇 명이면 될까?',
 'lead': '1-04에서 모든 안전장치가 "당사자 둘의 사본"에 기댄다는 걸 봤습니다. 시나리오 3은 당사자 밖의 사람, 증인을 세웁니다. 그런데 증인도 거짓말을 하거나 한쪽과 짜고 움직일 수 있어요. 그래서 법률상 권한을 가진 사람이 증명하는 공증이 등장합니다.',
 'kpis': [('시나리오 3', '증인이 있는 거래', 'a', [1]), ('3000여 건', '매년 거짓 증언 (교안이 인용한 기사 제목)', 'r', [1, 2]), ('위증죄', '법정의 허위 증언 처벌', 'm', [1]), ('공증', '법률상 권한 있는 사람이 공적으로 증명', 'g', [1])],
 'hero': [('doc', 'think', 'doc_e09', '두 사람의 말이 엇갈릴 때, 옆에서 본 사람이 있으면 좋겠죠. 그런데 그 사람은 얼마나 믿을 수 있을까요?'),
          ('asst', 'smile', 'asst_e13', '증인 수, 거짓말 확률, 공모 확률을 바꿔 가며 틀린 증언이 채택될 확률을 계산해 둘게요.'),
          ('fly', 'point', 'fly_e08', '증인을 셋 세우면 되잖아. 셋이 다 거짓말할 리는 없지?'),
          ('robo', 'coin', 'robo_e16', '사람 셋보다 도장 찍어 주는 공식 기관 하나가 낫지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '확률을 계산하고 발표한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 여럿의 다수결을 믿는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 공적 기관에 건다.')],
 'why_title': '왜 증인과 공증을 보나',
 'why_lead': '블록체인은 "다수의 증인"을 세우는 방식입니다(1-07). 그 전에, 사람 증인이 왜 부족했고 사람들이 그 부족함을 어떻게 메웠는지 봐 둬야 해요.',
 'why': [('증인의 약점', '증인이 장부를 위조하거나 거짓말을 할 수도 있다. 법정에서는 허위 증언에 대한 위증죄로 처벌되는 사례가 적지 않다. <sup>[1]</sup>'),
         ('공모의 위험', '보증인이 범죄에 공모하는 사례도 있다(교안의 부동산 범죄 사례). <sup>[1]</sup> 증인이 한쪽과 짜면 머릿수는 의미가 없다.'),
         ('공증의 등장', '그래서 공증인이나 법원 관련 직원처럼 법률상 공증할 수 있는 사람이, 서류의 내용을 적법한 형식으로 작성하고 서명 날인하는 공증 제도가 생겼다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 증인이 많아야 하는 게 아니라, 증인이 서로 독립이어야 해요. 짜고 움직이는 열 명은 한 명과 같아요.'),
 'big_lead': '계약서(1-04)는 당사자 둘의 사본에 기댔습니다. 이번 칸에서 처음으로 당사자 밖의 확인자가 등장합니다.',
 'ladder': [('①', '증인 (시나리오 3)', '당사자 밖의 사람이 거래를 확인한다', '증인도 거짓말하고 공모할 수 있다'),
            ('②', '공증', '법률상 권한과 책임을 진 사람이 공적으로 증명한다', '결국 한 사람·한 기관을 믿어야 하고 비용이 든다 → 1-06 기관 장부')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '증인', 'title': '증인을 세운다 — 시나리오 3',
   'tags': [('방식: 제3자 여러 명의 다수결', 'g'), ('현장: 돈을 빌릴 때 옆에 선 동료', '')],
   'left': '<p>A가 B에게 돈을 빌릴 때 동료 C를 증인으로 세운다. 나중에 말이 엇갈리면 C에게 물어본다. 증인을 여럿 세우면 다수의 말을 따른다. 하지만 증인이 잘못 기억하거나, 한쪽에 매수되거나, 아예 처음부터 짜고 있을 수 있다.</p>',
   'right': '<p>블록체인은 바로 이 "여러 증인의 다수결"을 극단까지 늘린 구조다. A와 B의 거래 사실이 망 전체에 동시에 기록된다(1-07). 핵심 차이는 증인 수가 아주 많고, 서로 짜기 어렵게 설계한다는 점이다.</p>',
   'panel': '''<h3>직접 해 보기 — 증인 몇 명이면 될까</h3>
    <div class="cwrap"><canvas id="c1" aria-label="증인 수에 따라 틀린 증언이 다수결로 채택될 확률을 보여 주는 막대그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">증인 수</span><input type="range" id="r1n" min="1" max="9" step="2" value="3" aria-label="증인 수"><span class="val" id="v1n">3</span>명</div>
      <div class="group"><span class="glabel">한 명이 거짓말할 확률(예시값)</span><input type="range" id="r1p" min="0" max="40" step="5" value="10" aria-label="거짓말 확률"><span class="val" id="v1p">10</span>%</div>
      <div class="group"><span class="glabel">모두 짜고 움직일 확률(예시값)</span><input type="range" id="r1c" min="0" max="30" step="5" value="5" aria-label="공모 확률"><span class="val" id="v1c">5</span>%</div></div>
    <h3>행동으로 보기 — 법정의 증인석 (재판 20건)</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="재판 20건마다 증인들이 참과 거짓을 말하고 다수결 판정이 나오는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 머릿수와 독립성</h4>
    <ol><li>증인이 서로 독립이면, 늘릴수록 다수가 동시에 틀릴 확률이 빠르게 준다. 거짓말 10%일 때 1명은 10%, 3명이면 2.8%, 5명이면 0.86%.</li>
      <li>하지만 공모 확률은 증인 수로 줄지 않는다. 모두 짜면 몇 명이든 다수가 틀린다. 공모 5%면 틀릴 확률은 5% 밑으로 내려가지 않는다.</li>
      <li>그래서 중요한 건 "몇 명인가"보다 "서로 짜기 어려운가"다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 증인은 거짓말하고 공모할 수 있으며, 그에 대한 책임 장치가 약하다. → 책임과 권한을 진 공적 증명, 공증.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '증인을 9명까지 늘려도 공모 5%는 그대로 남아. 머릿수가 다가 아니네.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '공증', 'title': '권한 있는 사람이 증명한다 — 공증',
   'tags': [('방식: 법률상 권한자가 작성·서명·날인', 'g'), ('현장: 공증 사무소', '')],
   'left': '<p>공증인은 법률이 정한 자격과 책임을 가진 사람이다. 거래 내용을 적법한 형식의 문서로 만들고 서명·날인한다. 거짓으로 증명하면 무거운 책임을 진다. 대신 공증에는 시간과 수수료가 든다.</p>',
   'right': '<p>공증은 "믿을 만한 제3자"를 사람 개인에서 <b>제도</b>로 옮긴 것이다. 블록체인은 이 제3자를 아예 없애는 대신, 망 참여자 전체의 검증과 규칙으로 같은 일을 하려 한다. 1-06은 그 사이 단계, 기관(은행)이다.</p>',
   'panel': '''<h3>직접 해 보기 — 증인 대 공증</h3>
    <div class="cwrap"><canvas id="c2" aria-label="증인 1·3·5명과 공증의 틀릴 확률과 비용을 비교하는 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">공증이 틀릴 확률(예시값)</span><input type="range" id="r2e" min="0" max="5" step="0.5" value="0.5" aria-label="공증 오류 확률"><span class="val" id="v2e">0.5</span>%</div>
      <div class="group"><span class="glabel">공증 수수료(예시값)</span><input type="range" id="r2f" min="0" max="50000" step="5000" value="20000" aria-label="공증 수수료"><span class="val" id="v2f">20000</span>원</div></div>
    <h3>행동으로 보기 — 공증인이 도장을 찍는다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="문서가 공증 사무소를 거쳐 도장이 찍혀 나오는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 책임을 사는 값</h4>
    <ol><li>공증은 법률상 권한과 처벌이라는 책임 장치로 거짓 증명의 확률을 낮춘다(이 모형에서는 0.5%, 예시값).</li>
      <li>그 대가로 수수료를 낸다. 만 원을 빌리는 데 수만 원의 공증 비용을 쓰지는 않는다. 그래서 공증은 큰 거래에 쓰인다.</li>
      <li>공증인이나 기관이 잘못하면? 결국 그 한 사람, 한 기관을 믿어야 한다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 거래마다 사람을 찾아가야 하고 비용이 크며, 결국 한 곳을 믿는다. → 거래 기록을 기관의 전산 장부에 바로 남기는 방식(1-06).</p>''',
   'say': ('asst', 'e10', 'asst_e10', '증인 3명(거짓 10%, 공모 5%)이면 틀릴 확률 7.7%, 공증은 0.5%예요. 대신 공증은 건당 2만 원(예시값)이 들어요.')},
 ],
 'duel': {'title': '증인 셋의 다수결 vs 공증 하나',
  'intro': '빌린 돈을 두고 다툼이 생겼다. 판정 기준은 <b>틀린 기록이 사실로 인정될 확률</b>(낮을수록 좋음). 초파리는 증인 3명의 다수결(각자 거짓말 10%, 모두 공모할 확률 5%), 주판봇은 공증 하나(틀릴 확률 0.5%). 모든 확률은 예시값이고, 계산은 위 두 실험과 같은 식이다.',
  'fly': ('증인 3명의 다수결', '셋이 동시에 거짓말할 리 없어. 머릿수가 답이야.', '거짓 10% · 공모 5%'),
  'robo': ('공증 하나', '책임지는 공식 도장 하나가 사람 셋보다 낫지.', '오류 0.5%'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>증인 n명, 각자 거짓말 확률 p, 공모 확률 c. 틀린 기록이 채택될 확률 = c + (1 − c) × P(거짓말하는 증인 수 &gt; n/2). n=3, p=0.1이면 P = 3p²(1−p) + p³ = 0.028, 전체 = 0.05 + 0.95 × 0.028 = 0.0766. 공증은 오류 확률 e = 0.005.</p><p class="lim">증인들의 거짓말이 서로 독립이라는 가정과 공모를 "전원 공모"로만 본 것은 단순화다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th></th><th>증인 (시나리오 3)</th><th>공증</th></tr></thead><tbody>
   <tr><td>누가 확인하나</td><td>당사자가 고른 사람</td><td>법률상 권한을 가진 사람</td></tr>
   <tr><td>거짓을 막는 장치</td><td>머릿수(다수결), 위증죄</td><td>자격, 적법한 형식, 서명·날인, 책임</td></tr>
   <tr><td>약점</td><td class="r">공모하면 머릿수가 무의미</td><td class="r">비용, 결국 한 사람·한 기관을 믿음</td></tr>
   <tr><td>블록체인과 닮은 점</td><td>다수의 확인</td><td>정해진 형식과 규칙</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>여기서 쓴 거짓말·공모·오류 확률은 모두 예시값이다. 실제 위증 통계나 공증 오류율이 아니다.</li><li>"매년 3000여 건 거짓 증언"은 교안이 인용한 서울신문 기사(2019.06.09) 제목이며, 원 기사는 확인하지 못했다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '증인에서 공증으로, 믿음은 사람에서 제도로 옮겨 갔어요. 다음 편은 그 제도의 끝판, 기관 전체가 증인이 되는 은행이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'coffee', 'fly_e13'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 주판봇이 두 팔을 들고, 초파리 연구원이 커피잔을 든 채 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 증인은 당사자 밖의 확인자지만, 거짓말과 공모에 약하다.<br>· 증인을 늘려도 공모 위험은 줄지 않는다.<br>· 공증은 권한과 책임으로 믿음을 높이고, 그 값을 수수료로 받는다.'),
           ('robo', 'happy', 'robo_e12', '책임지는 도장 하나가 이겼지! 숫자가 말해 줬잖아. 다음에도 여기에 투자.'),
           ('fly', 'coffee', 'fly_e13', '…공모 5%가 발목을 잡았네. 인정. 근데 공증인도 결국 한 사람이야.'),
           ('asst', 'e16', 'asst_e16', '다음은 1-06, 사람 대신 기관 전체가 증인이 되는 은행 장부를 시험해요.')],
 'kg_hint': '증인, 공모, 공증, 위증…',
 'ref_order': [LEC, SEOUL],
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.9 (시나리오 3: 증인이 있는 거래, 보증인의 범죄 공모 사례), p.10 (위증과 공증 제도). PDF 2024-10-18 생성.',
                 '「매년 3000여건 거짓 증언, 사법 정의 흔든다」, 서울신문, 2019.06.09. 교안 p.10의 그림 출처 표기로만 확인했고 원 기사는 확인하지 못함.'],
 'examples': ['증인 거짓말 확률 10%, 공모 확률 5% (예시값)', '공증 오류 확률 0.5%, 공증 수수료 20,000원 (예시값)', '재판 20건 표본, 시드 55 (설명용)'],
 'gloss_keys': [('공증', True), ('위증', True), ('다수결', True), ('중개자', True), ('블록체인', False)],
 'gloss_anchor': {'공증': '#lv2', '위증': '#why', '다수결': '#lv1', '중개자': '#lv2', '블록체인': '#lv1'},
 'quiz': {
  'lv1': [{'q': '각자 거짓말 확률이 10%인 증인 3명(서로 독립, 공모 없음)의 다수가 틀릴 확률에 가장 가까운 것은?', 'o': ['10%', '2.8%', '30%', '0.1%'], 'a': 1, 'why': '2명 이상이 거짓말할 확률 = 3 × 0.1² × 0.9 + 0.1³ = 0.028.', 'hint': '2명 이상이 동시에 거짓말해야 해요.', 'c': 'lab:method/witnesses'},
          {'q': '증인 수를 늘려도 줄지 않는 위험은?', 'o': ['증인 한 명의 착각', '증인 전원이 짜고 움직이는 공모', '증인의 건망증', '증인이 늦게 오는 것'], 'a': 1, 'why': '모두 짜면 몇 명이든 다수가 틀려요. 독립성이 핵심이에요.', 'hint': '공모 슬라이더를 올리고 증인 수를 늘려 보세요.', 'c': 'lab:limitation/witness-collusion'}],
  'lv2': [{'q': '공증이 증인보다 믿을 만한 이유로 가장 알맞은 것은?', 'o': ['법률상 권한과 책임을 진 사람이 적법한 형식으로 증명하기 때문', '공증인은 기억력이 좋기 때문', '공증은 공짜이기 때문', '공증은 블록체인을 쓰기 때문'], 'a': 0, 'why': '맞아요. 자격, 형식, 서명·날인, 책임이 장치예요.', 'hint': '교안 p.10의 정의.', 'c': 'lab:method/notarization'},
          {'q': '만 원을 빌리는 데 공증을 잘 쓰지 않는 이유는?', 'o': ['공증 비용이 거래 금액에 비해 크기 때문', '공증은 불법이기 때문', '만 원은 기록할 필요가 없기 때문', '공증은 은행만 하기 때문'], 'a': 0, 'why': '믿음을 사는 비용(수수료)이 작은 거래에는 맞지 않아요. 백서도 중개 비용이 작은 거래를 막는다고 지적했어요.', 'hint': '수수료 슬라이더.', 'c': 'lab:limitation/notary-cost'}]},
 'kgspec': {
  'ladder': ['lab:method/witnesses', 'lab:method/notarization'],
  'about': ['lab:method/witnesses', 'lab:method/notarization', 'lab:limitation/witness-collusion'],
  'nodes': [
   ('lab:method/witnesses', 'Method', '증인의 다수결', 'witness majority', '#lv1', '당사자 밖의 증인 여럿에게 거래를 확인받고 다툼이 생기면 다수의 말을 따르는 방식 (시나리오 3).', 2, [(LEC, '교안 p.9')]),
   ('lab:limitation/witness-collusion', 'Limitation', '증인의 거짓말과 공모', 'witness lies and collusion', '#lv1', '증인도 위조·거짓말을 할 수 있고, 한쪽과 공모하면 머릿수가 의미 없다.', 2, [(LEC, '교안 p.9–10')]),
   ('lab:limitation/notary-cost', 'Limitation', '공증의 비용과 한 곳에 대한 신뢰', 'notary cost and single trusted party', '#lv2', '거래마다 비용이 들고, 결국 공증인 한 사람·한 기관을 믿어야 한다.', 2),
   ('lab:concept/independence', 'Concept', '증인의 독립성', 'independence of witnesses', '#lv1', '증인들이 서로 짜지 않고 각자 판단하는 성질. 다수결이 힘을 쓰는 조건.', 2),
   ('lab:metric/wrong-accepted', 'Metric', '틀린 기록이 인정될 확률', 'probability a false record is accepted', '#duel', '다툼에서 틀린 기록이 사실로 채택될 확률. 낮을수록 좋다.', 2),
   ('lab:question/core', 'Question', '당사자 밖의 사람에게 확인을 맡기면 믿을 수 있을까?', 'Can third-party witnesses be trusted?', '#top', None, 1),
   ('lab:question/duel', 'Question', '증인 셋의 다수결과 공증 하나 중 무엇이 덜 틀리나?', 'Three witnesses or one notary?', '#duel', None, 2),
  ],
  'edges': [
   ('lab:method/witnesses', 'lab:prerequisiteOf', 'lab:method/notarization', '#lv2'),
   ('lab:method/witnesses', 'lab:hasLimitation', 'lab:limitation/witness-collusion', '#lv1'),
   ('lab:limitation/witness-collusion', 'lab:addressedBy', 'lab:method/notarization', '#lv2'),
   ('lab:method/notarization', 'lab:hasLimitation', 'lab:limitation/notary-cost', '#lv2'),
   ('lab:concept/majority-vote', 'lab:partOf', 'lab:method/witnesses', '#lv1'),
   ('lab:concept/independence', 'lab:prerequisiteOf', 'lab:concept/majority-vote', '#lv1'),
   ('lab:term/perjury', 'lab:partOf', 'lab:limitation/witness-collusion', '#why'),
   ('lab:method/notarization', 'lab:broader', 'lab:concept/trusted-third-party', '#lv2'),
   ('lab:method/witnesses', 'lab:contrastsWith', 'lab:method/notarization', '#duel'),
   ('lab:method/witnesses', 'lab:evaluatedBy', 'lab:metric/wrong-accepted', '#duel'),
   ('lab:method/notarization', 'lab:evaluatedBy', 'lab:metric/wrong-accepted', '#duel'),
   ('lab:metric/wrong-accepted', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/witness-collusion', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:concept/blockchain', 'lab:relatedTo', 'lab:method/witnesses', '#lv1', 'mid'),
  ],
  'claims': [
   ('lab:claim/witness-may-lie', '증인이 장부를 위조하거나 거짓말을 할 수 있고, 법정에서 위증죄로 처벌되는 사례가 적지 않다', '#why', ['lab:limitation/witness-collusion', 'lab:term/perjury'], [(LEC, '교안 p.10')], 'F01'),
   ('lab:claim/guarantor-conspiracy', '보증인이 범죄에 공모하는 사례가 있다 (교안의 부동산 범죄 사례)', '#why', ['lab:limitation/witness-collusion'], [(LEC, '교안 p.9')], 'F02'),
   ('lab:claim/notary-definition', '공증은 특정 사실이나 법률관계를 법률상 권한 있는 사람이 적법한 형식으로 작성하고 서명 날인해 공적으로 증명하는 행위다', '#why', ['lab:method/notarization'], [(LEC, '교안 p.10')], 'F03'),
   ('lab:claim/perjury-3000', '매년 3000여 건의 거짓 증언이 있다는 기사 제목이 교안에 인용되어 있다', '#top', ['lab:term/perjury'], [(LEC, '교안 p.10'), (SEOUL, '기사 제목')], 'F04'),
  ],
  'sims': [('lab:simulation/witness-majority', '증인 다수결 확률 실험', '#lv1', ['lab:method/witnesses']),
           ('lab:simulation/notary-compare', '증인 대 공증 비교', '#lv2', ['lab:method/notarization']),
           ('lab:simulation/duel-witness-notary', '증인 셋 대 공증 대결', '#duel', ['lab:metric/wrong-accepted'])],
 },
}
