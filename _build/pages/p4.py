LEC = "lecture2024blockchain"
PAGE = {
 'num': '1-04', 'slug': 'contract-and-seal', 'key': '1_04', 'anchor': 'D',
 'tab_title': '계약서와 도장', 'meta_title': '계약서와 도장 — 고치기 어렵게 만드는 장치',
 'description': '숫자·한글 병기와 간인·접인이 위조를 어떻게 드러내는지, 그리고 원본 사본을 잃었을 때 왜 무력해지는지 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.7–8',
 'h1': '계약서와 도장<br>— 고치기 어렵게 만드는 장치', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '숫자와 한글을 함께 적고 도장을 맞찍으면 위조를 막을 수 있을까? 언제 막지 못할까?',
 'lead': '1-03의 각자 장부는 "다르다"는 알아도 "누가 고쳤는지"는 몰랐습니다. 사람들은 고치는 순간 흔적이 남도록 문서에 장치를 더했어요. 숫자와 한글을 함께 적는 병기, 장과 장 사이에 찍는 간인, 두 부를 겹쳐 찍는 접인. 이 장치들을 직접 위조해 보며 강점과 빈틈을 찾습니다.',
 'kpis': [('숫자 + 한글', '금액·날짜 병기로 조작 방지', 'a', [1]), ('간인 · 접인', '도장을 걸쳐 찍어 내용 확인의 증거를 남김', 'g', [1]), ('분실', '한쪽이 잃으면 사실 확인이 어려움', 'r', [1]), ('가짜 도장', '사진 편집 프로그램으로 위조 가능', 'm', [1])],
 'hero': [('doc', 'think', 'doc_e09', '금전 계약, 임대차 계약, 투자 계약 대부분이 이 방식을 따라요. 그만큼 오래 검증된 장치예요. 빈틈은 어디일까요?'),
          ('asst', 'smile', 'asst_e13', '위조범 역할을 해 볼 수 있게 만들었어요. 숫자만 고치기, 둘 다 고치기, 사본 통째로 바꾸기.'),
          ('fly', 'point', 'fly_e08', '도장이 있어도 포토샵 한 번이면 끝 아냐? 그게 궁금해.'),
          ('robo', 'coin', 'robo_e16', '복잡한 장치는 비용이야. 숫자만 또박또박 적으면 충분하지!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '위조를 시도하고 탐지율을 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 빈틈을 찾는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 단순한 문서에 건다.')],
 'why_title': '왜 계약서를 따로 보나',
 'why_lead': '블록체인은 "고치면 드러나게" 만드는 장치를 디지털로 끝까지 밀어붙인 것입니다(2장의 해시). 그 아이디어의 종이 버전이 계약서의 병기와 도장이에요.',
 'why': [('병기', '계약서의 금액·날짜 같은 중요한 사항을 숫자와 한글로 함께 적어 조작의 위험을 막는다. <sup>[1]</sup>'),
         ('간인·접인', '계약 당사자가 도장을 서로 걸쳐 찍어 내용을 확인했다는 증거를 남긴다. 금전·임대차·투자 계약 대부분이 이 방식을 따른다. <sup>[1]</sup>'),
         ('남는 빈틈', '장부나 계약서를 한쪽이 잃어버리면 사실 확인이 어렵고, 가짜 도장으로 위조할 수 있으며, 거짓말을 입증하기 매우 어렵다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 좋은 안전장치는 위조를 불가능하게 하는 게 아니라, 위조하면 흔적이 남게 하는 거예요. 단, 그 흔적을 대조할 무언가가 있어야 해요.'),
 'big_lead': '각자 장부(1-03)에서 한 칸 올라왔습니다. 이번 칸은 문서 안에 "고치면 드러나는" 장치를 넣습니다.',
 'ladder': [('①', '숫자·한글 병기', '한 표기만 고치면 어긋나 흔적이 남는다', '둘 다 같은 금액으로 고치면 통과한다'),
            ('②', '간인·접인 (도장 걸쳐 찍기)', '사본끼리 맞춰 보면 바꿔치기가 드러난다', '대조할 사본이 사라지거나 도장까지 복제하면 막지 못한다 → 1-05 증인')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '병기', 'title': '숫자와 한글을 함께 적는다 — 병기',
   'tags': [('방식: 같은 정보를 두 가지 표기로', 'g'), ('현장: 차용증·계약서의 금액란', '')],
   'left': '<p>"일금 만 원정 (₩10,000)". 숫자 0 하나를 지우면 ₩1,000이 되지만 한글 "만 원"은 그대로라 어긋난다. 위조범은 두 표기를 모두, 서로 맞게 고쳐야 한다.</p>',
   'right': '<p>같은 정보를 두 번 적어 서로 검사하게 하는 것은 블록체인의 아이디어와 닮았다. 블록체인은 내용에서 계산한 짧은 값(해시)을 함께 적어, 내용이 바뀌면 그 값과 어긋나게 한다(2장).</p><p class="lim">해시는 사람이 고쳐 맞출 수 없을 만큼 계산이 복잡하다는 점에서 한글 병기와 다르다. 한글은 누구나 고쳐 쓸 수 있다.</p>',
   'panel': '''<h3>직접 해 보기 — 위조범이 되어 보자</h3>
    <div class="cwrap"><canvas id="c1" aria-label="차용증 한 장. 숫자 금액과 한글 금액, 위조 시도에 따라 어긋남이 표시된다"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">문서 종류</span>
      <button class="bt" data-doc="0" aria-pressed="false">숫자만 적은 차용증</button><button class="bt" data-doc="1" aria-pressed="true">숫자·한글 병기</button></div>
      <div class="group"><span class="glabel">위조</span><button class="bt warn" data-fg="num">숫자만 고치기</button><button class="bt warn" data-fg="both">둘 다 맞게 고치기</button><button class="bt" data-fg="none">원래대로</button></div></div>
    <h3>행동으로 보기 — 위조 문서 20장 분류</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="위조 문서 20장이 들킴과 안 들킴 두 상자로 분류되는 장면"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">위조범이 두 표기를 모두 고치는 비율(예시값)</span><input type="range" id="r1b" min="0" max="100" step="10" value="30" aria-label="두 표기 모두 고치는 비율"><span class="val" id="v1b">30</span>%</div></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 병기는 "서툰 위조"를 잡는다</h4>
    <ol><li>숫자만 고치면 한글과 어긋나 바로 드러난다.</li>
      <li>두 표기를 모두 맞게 고치면 문서 안에서는 모순이 없다. 병기는 이런 "꼼꼼한 위조"를 잡지 못한다.</li>
      <li>그래서 탐지율은 위조범이 얼마나 꼼꼼한지에 달렸다. 꼼꼼한 위조를 잡으려면 문서 <b>밖</b>의 무언가와 대조해야 한다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 둘 다 맞게 고친 위조는 문서 안에서 모순이 없다. → 다른 사본과 대조할 장치가 필요하다(간인·접인).</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '숫자만 고치면 딱 걸려. 근데 한글까지 고쳐 쓰면? 문서 혼자서는 모른다고.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '간인·접인', 'title': '도장을 걸쳐 찍는다 — 간인·접인',
   'tags': [('방식: 두 사본에 걸쳐 찍은 도장으로 짝 확인', 'g'), ('현장: 임대차·금전 계약', '')],
   'left': '<p>계약서 두 부를 겹쳐 놓고 경계에 도장을 찍는다(접인). 여러 장이면 장과 장 사이에도 찍는다(간인). 나중에 두 부를 맞대면 도장 반쪽이 딱 맞아야 한다. 한 부를 새로 써서 바꿔치기하면 도장이 어긋나고, 내용도 다른 사본과 달라진다.</p>',
   'right': '<p>블록체인의 블록은 앞 블록의 값을 담아 서로 "걸쳐" 있다. 한 블록을 바꾸면 이어진 블록과 어긋난다(2장). 그리고 그 사본을 당사자 둘이 아니라 망 전체가 갖는다(1-07). 접인의 약점인 "사본을 잃으면 끝"을 사본 수로 없앤 셈이다.</p>',
   'panel': '''<h3>직접 해 보기 — 사본 바꿔치기</h3>
    <div class="cwrap"><canvas id="c2" aria-label="계약서 두 부가 나란히 있고 경계에 접인 도장이 걸쳐 찍힌 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">위조·사고</span>
      <button class="bt warn" id="b2Rew" aria-pressed="false">A가 자기 사본을 새로 써서 바꾸기</button><button class="bt warn" id="b2Fake" aria-pressed="false">사진 편집으로 도장까지 복제</button><button class="bt warn" id="b2Lose" aria-pressed="false">B가 자기 사본을 잃어버림</button></div></div>
    <h3>행동으로 보기 — 두 사본을 맞대 본다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="두 사본이 가운데로 모여 도장 반쪽과 내용을 맞춰 보는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 도장의 힘은 "다른 사본"에서 나온다</h4>
    <ol><li>B의 사본이 있으면, A가 도장까지 복제해 새로 써도 내용이 B 사본과 달라 드러난다.</li>
      <li>B가 사본을 잃어버리면 A의 사본이 유일한 문서가 된다. A가 전부 새로 쓰고 사진 편집으로 도장을 붙이면 대조할 것이 없다. <sup>[1]</sup></li>
      <li>어느 한쪽이 거짓말을 하더라도 이를 입증하기 매우 어렵다. <sup>[1]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 모든 안전장치가 결국 "당사자 둘이 가진 사본"에 기댄다. 둘 중 하나가 사라지거나 거짓말하면 무너진다. → 당사자가 아닌 제3자, 증인(1-05).</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면</h4><p>전자 문서 시대의 "도장"은 전자 서명이다. 그래도 원칙은 같다. 서명이 맞는지 확인할 원본(공개키, 원본 파일)을 당사자 밖 어딘가에 안전하게 두어야 한다.</p><p class="lim">전자 서명은 사진 편집으로 복제할 수 없다는 점에서 인감과 크게 다르다. 닮은 건 "대조할 원본이 필요하다"는 구조다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', 'B 사본이 있으면 도장까지 복제해도 내용 비교로 걸려요. B 사본이 없으면 같은 위조가 통과해요.')},
 ],
 'duel': {'title': '사본을 잃은 뒤의 위조, 찾아낼 수 있을까?',
  'intro': 'B가 자기 사본을 잃어버렸다. A는 자기 사본을 처음부터 새로 쓰고(숫자·한글을 서로 맞게), 사진 편집으로 도장까지 붙였다. 이런 위조 문서 100장에 대해 <b>위조를 찾아낸 장 수</b>(많을수록 좋음)로 겨룬다. 탐지 규칙은 위 두 실험과 같은 함수다.',
  'fly': ('숫자·한글 병기 + 간인·접인 계약서', '안전장치는 많을수록 좋아. 하나라도 걸리겠지.', '병기 + 도장'),
  'robo': ('숫자만 적은 간단한 차용증', '어차피 위조할 놈은 위조해. 간단하게 가자.', '숫자 한 줄'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>탐지 함수 detect(문서, 대조 사본): (1) 문서 안 숫자·한글이 어긋나면 탐지, (2) 대조 사본이 있으면 내용·도장 반쪽을 비교해 다르면 탐지. 이 대결에서는 대조 사본이 없고(B 분실), 위조범이 두 표기를 맞게 고쳤으므로 두 방식 모두 (1)·(2)에 걸리지 않는다.</p><p class="lim">현실에서는 인감증명, 필적 감정, 종이·잉크 분석처럼 다른 대조 수단이 있을 수 있다. 이 모형은 "당사자 둘의 사본"만 있는 상황으로 좁혔다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>위조 방법</th><th>숫자만 적은 차용증</th><th>병기</th><th>병기 + 접인 (B 사본 있음)</th><th>병기 + 접인 (B 사본 분실)</th></tr></thead><tbody>
   <tr><td>숫자만 고치기</td><td class="r">못 찾음</td><td class="g">찾음</td><td class="g">찾음</td><td class="g">찾음</td></tr>
   <tr><td>둘 다 맞게 고치기</td><td class="r">못 찾음</td><td class="r">못 찾음</td><td class="g">찾음</td><td class="r">못 찾음</td></tr>
   <tr><td>새로 쓰고 도장 복제</td><td class="r">못 찾음</td><td class="r">못 찾음</td><td class="g">찾음 (내용 비교)</td><td class="r">못 찾음</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>"찾음/못 찾음"은 이 모형의 규칙에 따른 결과다. 실제 감정 기술은 더 다양하다.</li><li>표의 마지막 열이 이 편의 핵심이다. 대조할 사본이 사라지면 아무리 정교한 장치도 첫 열과 같아진다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '흔적을 남기는 장치는 대조할 상대가 있어야 의미가 있어요. 그 상대를 당사자 밖에서 구하자, 그게 증인이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('asst', 'smile', 'asst_e13'), ('fly', 'coffee', 'fly_e13'), ('robo', 'meh', 'robo_e18')],
 'outro_alt': '무대 위에 네 캐릭터가 같은 높이로 서 있고, 초파리는 커피잔을, Money-Robo는 일자 눈을 한 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 병기는 서툰 위조를, 접인은 바꿔치기를 드러낸다.<br>· 둘 다 "다른 사본과 대조할 수 있을 때"만 힘을 쓴다.<br>· 사본이 사라지면 정교한 계약서도 숫자 한 줄짜리 차용증과 같다.'),
           ('asst', 'smile', 'asst_e13', '대결은 100장 중 0장 대 0장이었어요. 이번 판은 장치의 차이가 아니라 대조할 사본이 없다는 조건이 결과를 정했어요.'),
           ('fly', 'coffee', 'fly_e13', '안전장치를 아무리 쌓아도 대조할 게 없으면 소용없네. 인정.'),
           ('robo', 'meh', 'robo_e18', '…이겼다고도 졌다고도 못 하겠네. 본전이야.')],
 'kg_hint': '병기, 간인, 접인, 위조…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.7 (계약서의 안전장치: 숫자·한글 병기, 교안의 부동산 전대차 계약서 샘플), p.8 (간인·접인, 분실·가짜 도장 위조, 교안이 인용한 사진 편집 위조 기사: YTN 2015.02.03). PDF 2024-10-18 생성.'],
 'examples': ['차용증 금액 10,000원 (설명용)', '위조범이 두 표기를 모두 고치는 비율 30% (예시값)', '대결: 위조 문서 100장, 모두 "새로 쓰기 + 도장 복제", B 사본 분실 조건'],
 'gloss_keys': [('병기', True), ('간인', True), ('접인', True), ('장부', False), ('블록체인', False)],
 'gloss_anchor': {'병기': '#lv1', '간인': '#lv2', '접인': '#lv2', '장부': '#why', '블록체인': '#why'},
 'quiz': {
  'lv1': [{'q': '"일금 만 원정 (₩10,000)"에서 숫자만 ₩1,000으로 고치면?', 'o': ['한글과 어긋나 위조 흔적이 남는다', '아무도 모른다', '한글이 자동으로 바뀐다', '도장이 지워진다'], 'a': 0, 'why': '같은 정보를 두 번 적었으니 한쪽만 바뀌면 서로 맞지 않아요.', 'hint': '병기의 목적.', 'c': 'lab:method/dual-notation'},
          {'q': '위조범이 두 표기를 모두 고치는 비율이 30%라면, 병기 문서만으로 찾아내는 위조의 비율은? (나머지는 숫자만 고친다고 가정)', 'o': ['30%', '70%', '100%', '0%'], 'a': 1, 'why': '숫자만 고친 70%는 어긋나서 찾고, 둘 다 고친 30%는 못 찾아요.', 'hint': '"못 찾는" 쪽이 30%예요.', 'c': 'lab:limitation/consistent-forgery'}],
  'lv2': [{'q': 'B가 사본을 가지고 있을 때, A가 새로 쓰고 도장까지 복제한 위조는?', 'o': ['B 사본과 내용이 달라 드러난다', '도장이 맞으니 통과한다', '병기가 없으면 통과한다', '판정할 수 없다'], 'a': 0, 'why': '도장을 복제해도 B 사본의 내용(10,000원)과 비교하면 달라요.', 'hint': '대조할 사본이 있어요.', 'c': 'lab:method/cross-seal'},
          {'q': '간인·접인이 무력해지는 조건으로 가장 알맞은 것은?', 'o': ['대조할 상대방 사본이 사라졌을 때', '도장이 빨간색이 아닐 때', '계약서가 두 장 이상일 때', '숫자를 한글로 적었을 때'], 'a': 0, 'why': '도장의 힘은 다른 사본과 맞춰 볼 때 나와요.', 'hint': '표의 마지막 열.', 'c': 'lab:limitation/copy-lost'}]},
 'kgspec': {
  'ladder': ['lab:method/dual-notation', 'lab:method/cross-seal'],
  'about': ['lab:method/dual-notation', 'lab:method/cross-seal', 'lab:limitation/copy-lost'],
  'nodes': [
   ('lab:method/cross-seal', 'Method', '간인·접인 계약서', 'cross-page / cross-copy seals', '#lv2', '도장을 장과 장, 또는 두 사본에 걸쳐 찍어 짝과 내용 확인의 증거를 남기는 방식.', 2, [(LEC, '교안 p.8')]),
   ('lab:limitation/consistent-forgery', 'Limitation', '두 표기를 모두 맞게 고친 위조', 'consistent forgery', '#lv1', '숫자와 한글을 서로 맞게 함께 고치면 문서 안에는 모순이 없어 병기로 찾지 못한다.', 2),
   ('lab:limitation/copy-lost', 'Limitation', '대조할 사본이 사라짐', 'reference copy lost', '#lv2', '상대 사본을 잃으면 남은 사본이 유일한 문서가 되어, 전부 새로 쓴 위조를 찾을 수 없다.', 2, [(LEC, '교안 p.8')]),
   ('lab:concept/fake-seal', 'Concept', '가짜 도장 (사진 편집 위조)', 'forged seal via photo editing', '#lv2', '사진 편집 프로그램으로 도장을 복제해 문서를 위조하는 것.', 2, [(LEC, '교안 p.8')]),
   ('lab:metric/detected-forgeries', 'Metric', '찾아낸 위조 문서 수', 'detected forgeries', '#duel', '위조 문서 중 탐지 규칙으로 찾아낸 장 수.', 2),
   ('lab:method/plain-iou', 'Method', '숫자만 적은 차용증', 'plain IOU with digits only', '#duel', '금액을 숫자로만 적고 별다른 안전장치가 없는 문서.', 1),
   ('lab:analogy/seal-chain', 'Analogy', '걸쳐 찍은 도장 ↔ 앞 블록 값을 담은 블록', 'cross-seal ~ hash-linked blocks', '#lv2', '서로 걸쳐 있어 하나를 바꾸면 이어진 쪽과 어긋난다.', 3),
   ('lab:question/core', 'Question', '병기와 도장으로 위조를 막을 수 있을까? 언제 막지 못할까?', 'Can dual notation and seals stop forgery?', '#top', None, 1),
   ('lab:question/duel', 'Question', '사본을 잃은 뒤의 위조를 찾아낼 수 있을까?', 'Can forgery be detected after the copy is lost?', '#duel', None, 2),
  ],
  'edges': [
   ('lab:method/dual-notation', 'lab:prerequisiteOf', 'lab:method/cross-seal', '#lv2'),
   ('lab:method/dual-notation', 'lab:hasLimitation', 'lab:limitation/consistent-forgery', '#lv1'),
   ('lab:limitation/consistent-forgery', 'lab:addressedBy', 'lab:method/cross-seal', '#lv2'),
   ('lab:method/cross-seal', 'lab:hasLimitation', 'lab:limitation/copy-lost', '#lv2'),
   ('lab:method/cross-seal', 'lab:hasLimitation', 'lab:concept/fake-seal', '#lv2'),
   ('lab:term/ganin', 'lab:partOf', 'lab:method/cross-seal', '#lv2'),
   ('lab:term/jeobin', 'lab:partOf', 'lab:method/cross-seal', '#lv2'),
   ('lab:method/cross-seal', 'lab:contrastsWith', 'lab:method/plain-iou', '#duel'),
   ('lab:method/cross-seal', 'lab:evaluatedBy', 'lab:metric/detected-forgeries', '#duel'),
   ('lab:method/plain-iou', 'lab:evaluatedBy', 'lab:metric/detected-forgeries', '#duel'),
   ('lab:limitation/copy-lost', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/copy-lost', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:analogy/seal-chain', 'lab:analogyOf', 'lab:method/cross-seal', '#lv2'),
   ('lab:method/dual-notation', 'lab:partOf', 'lab:concept/ledger', '#why', 'mid'),
   ('lab:concept/blockchain', 'lab:relatedTo', 'lab:analogy/seal-chain', '#lv2', 'mid'),
  ],
  'claims': [
   ('lab:claim/dual-notation', '계약서의 금액·날짜 등 중요한 사항을 숫자와 한글로 병기해 조작의 위험을 막을 수 있다', '#why', ['lab:method/dual-notation'], [(LEC, '교안 p.7')], 'F01'),
   ('lab:claim/cross-seal-evidence', '계약 당사자가 도장을 서로 찍어(접인) 내용 확인의 증거를 남기며, 금전·임대차·투자 계약 대부분이 이 방식을 따른다', '#why', ['lab:method/cross-seal'], [(LEC, '교안 p.8')], 'F02'),
   ('lab:claim/seal-weakness', '한쪽이 장부나 계약서를 잃으면 사실 확인이 어렵고, 가짜 도장으로 위조할 수 있으며, 거짓말을 입증하기 매우 어렵다', '#lv2', ['lab:limitation/copy-lost', 'lab:concept/fake-seal'], [(LEC, '교안 p.8')], 'F03'),
  ],
  'sims': [('lab:simulation/forge-notation', '병기 위조 실험', '#lv1', ['lab:method/dual-notation']),
           ('lab:simulation/swap-copy', '사본 바꿔치기 실험', '#lv2', ['lab:method/cross-seal']),
           ('lab:simulation/duel-lost-copy', '사본 분실 후 위조 탐지 대결', '#duel', ['lab:metric/detected-forgeries'])],
 },
}
