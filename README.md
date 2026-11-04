# 블록체인 편 1장 「장부의 진화」

연구실 해설 대시보드 시리즈의 블록체인 편 첫 장입니다. 박사·하루(조수)·초파리 연구원·주판봇이 진행하는 인터랙티브 해설 페이지 7편과 목차로 이루어져 있습니다.

## 보는 법
- `index.html`을 브라우저로 열면 목차가 나옵니다. 설치나 서버가 필요 없습니다.
- GitHub Pages로 공개하려면 저장소 설정에서 Pages를 켜고 루트(`/`)를 고르면 됩니다.
- 외부 요청은 글꼴(Google Fonts) 하나뿐이고, 브라우저 저장소는 쓰지 않습니다.

## 구성
| 파일 | 내용 | 대결 결과 |
|---|---|---|
| `index.html` | 1장 목차, 사다리 한 장 요약, 대결 결산 | — |
| `1-01_money-is-record.html` | 블록체인의 등장 — 돈은 기록이다 (이중 지불) | F 초파리 승 |
| `1-02_central-vs-distributed.html` | 중앙집중식 vs 분산 네트워크 | R 주판봇 승 |
| `1-03_memory-and-ledger.html` | 기억과 장부 (시나리오 1·2) | F 초파리 승 |
| `1-04_contract-and-seal.html` | 계약서와 도장 (병기, 간인·접인) | D 무승부 |
| `1-05_witness-and-notary.html` | 증인과 공증 | R 주판봇 승 |
| `1-06_bank-ledger.html` | 기관 장부: 은행, 중앙 인증 | R 주판봇 승 |
| `1-07_many-witnesses.html` | 다수의 증인: 분산원장, 과반의 비용과 투표권 | X 주판봇 실격 |
| `assets/lab.css` · `assets/lab.js` | 공용 디자인·스크립트 (도우미, 캐릭터, 용어, 퀴즈, 대결, 지식 색인, 꾸러미) | |
| `assets/sprites.js` | 캐릭터 표정 그림 (공식 저장소 팩에서 이 장에 쓰는 것만, 96px + 192px) | |
| `docs/IMG_1-0n_*.md` | 편마다 이미지 제작 명세서 (외부 의뢰 프롬프트 포함) | |
| `docs/IMG_1-00_index.md` | 장 공용 이미지 명세서 | |
| `docs/KG_00_registry.json` | 블록체인 편 지식 그래프 ID 등록부 v0.1 (2·3장이 이어 씀) | |
| `_build/` | 페이지를 만든 생성 스크립트 (참고용, 지워도 페이지는 동작) | |

각 편 맨 끝의 "온톨로지·서지 꾸러미"에서 그 편의 지식 그래프(JSON·JSON-LD·Turtle·CSV)와 참고문헌(CSL-JSON·BibTeX·RIS)을 ZIP으로 내려받을 수 있습니다.

## 자료
- 강의 교안 「4차산업시대의 금융 — 블록체인의 원리 · 블록체인 서비스 사례 · 블록체인과 비트코인」 p.3–13 (저자·연도 표기 없음, PDF 생성일 2024-10-18)
- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.* 1·2·4절
- 서울신문 (2019.06.09) 「매년 3000여건 거짓 증언, 사법 정의 흔든다」 — 교안 인용 표기로만 확인
- 캐릭터 그림: [adminmrobo/fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (ea5da3f)

## 채워 넣을 것
- 라이선스, 공개 주소 (각 편 `page-meta`와 꾸러미의 확인 필요 목록에 빈칸으로 표시됨)
- 대표 배경 그림 8장 (`docs/` 명세서의 외부 의뢰 묶음) — 없어도 페이지는 완성 상태

저자: 안상선 · v1.0 · 2026-10-29
