# 블록체인 1장 공용 이미지 명세서 (`IMG_1-00_index.md`)

| 항목 | 내용 |
|---|---|
| 챕터 | 블록체인 편 1장 「장부의 진화」, 페이지 7개 + 목차 |
| 시즌 | 기본 |
| 공용 표정 | 캐릭터 팩 (커밋 ea5da3f), `assets/sprites.js`에 96px + 192px 묶음 · 그림 없음 역할 키: doc_scale, asst_ledger, asst_board |

## 1. 목차·표지 그림
| 키 | 판 | 내용 | 제작 | 우선 |
|---|---|---|---|---|
| bg_ch1_index | F | 장부의 진화를 한 장면에: 왼쪽은 단순, 오른쪽으로 갈수록 수첩 → 계약서 → 공증 도장 → 은행 금고 → 원탁의 장부 아홉 권이 차례로 놓인 긴 회계실 | 외부 | P1 |
| cover_ch1 | J | 넷이 함께: 박사가 가운데에서 사다리처럼 놓인 장부 다섯 단(글자 없음)을 가리키고, 초파리와 Money-Robo가 양쪽에서 올려다보고, 하루가 점수판(빈칸 셋)을 든다 | 외부 | P2 |
| thumb_1_01 ~ thumb_1_07 | I | 각 편 bg를 3:2로 자르기 | 직접 | P2 |

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a long cozy accounting room beside the lab where objects are lined up from left to right like stages of history: a small notebook, a contract with a red seal across two copies, a notary desk with a round seal, a huge round bank vault door, and finally a round table with nine identical leather ledgers, warm golden lamp light growing brighter toward the right, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 2. 페이지별 대표 그림
| 페이지 | 앵커 | bg | outro | 상태 |
|---|---|---|---|---|
| 1-01 | C | bg_1_01 | sc_1_01_outro | bg 의뢰 · outro 합성본 |
| 1-02 | D | bg_1_02 | sc_1_02_outro | bg 의뢰 · outro 합성본 |
| 1-03 | D | bg_1_03 | sc_1_03_outro | bg 의뢰 · outro 합성본 |
| 1-04 | D | bg_1_04 | sc_1_04_outro | bg 의뢰 · outro 합성본 |
| 1-05 | D | bg_1_05 | sc_1_05_outro | bg 의뢰 · outro 합성본 |
| 1-06 | C | bg_1_06 | sc_1_06_outro | bg 의뢰 · outro 합성본 |
| 1-07 | C | bg_1_07 | sc_1_07_outro | bg 의뢰 · outro 합성본 |

## 3. 새 표정 후보 (시리즈 공용, P2)
| 키 | 대신 쓰는 그림 | 쓰는 곳 | 메모 |
|---|---|---|---|
| doc_scale | doc_e13 | 1-04 무승부 판정 | 수평 놋쇠 저울을 두 손으로. 저장소 E25 후보 |
| asst_ledger | asst_e07 | 모든 편 꾸러미 섹션 | 줄무늬 장부를 펼치고 펜. 장부 앵커 챕터라 특히 쓸모 있음 |

## 4. 의뢰 순서 (Genspark 한 세션)
bg_ch1_index → bg_1_01 … bg_1_07 → (선택) cover_ch1 → (선택) sc_1_0n_outro
