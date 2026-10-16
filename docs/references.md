# 레퍼런스 조사 — 해외 작가 사이트 · GitHub 디자인 (2026-10-16)

고운대표 요청: "경쟁 대상이 편협했다. 전세계적으로 잘 만든 포트폴리오형 홈페이지와 GitHub의 디자인 잘하는 사이트를 보고 따라 하자."

**한계:** 이 클라우드 터미널은 개인 사이트 접속이 막혀 화면을 직접 열어 보지 못했다. 검색 결과, 수상·제작사 사례 페이지, GitHub 공개 소스로만 확인했다. 확인하지 못한 것은 [미검증]으로 적었다.
**원칙:** 기법만 참고하고 다른 사람의 코드·글·이미지는 복사하지 않는다. 우리 사이트 내용은 작가님이 확인한 것만 싣는다.

## 0. 작가님이 처음 보여 준 참고 사이트 (최우선)

- **sonbomi.com** (손보미 작가) — 2026-10-16 고운대표 공유. 작가님이 처음에 "이런 느낌"으로 보여 준 홈페이지. 클라우드 세션은 접속이 막혀 디자인 터미널에 화면 확인 요청 중. [확인 대기]

## 1. 작가·출판 사이트

| 순위 | 사이트 | 확인된 점 | 우리가 가져올 것 |
|---|---|---|---|
| 1 | New York Review of Books (nybooks.com, Athletics 제작, Webby 2021) | 지난 호 표지 색에서 색 짝을 뽑아 홈 상단 "디지털 표지"를 만듦 | 표지 색으로 색 짝을 정해 작품 카드마다 하나씩 배정 |
| 2 | Haruki Murakami (harukimurakami.com, Bluecadet, Communication Arts) | 이미지와 작가 문장을 짝지어 책을 소개. 책 목록을 장편/단편/논픽션으로 나눔 (수상 자료는 2014년경, 현재 화면 [미검증]) | 작품마다 작가님이 고른 문장 한 줄. 소설집/장편/산문 분류 |
| 3 | Craig Mod (craigmod.com/books) | 책을 연도순(최신→과거)으로 정리, 판본 정보 | 연도를 크게 앞세운 작품 연표 |
| 4 | Min Jin Lee (minjinlee.com) | BOOKS / ABOUT / REVIEWS / NEWS / INTERVIEWS / CONTACT로 나눔 | 소식을 행사·인터뷰·리뷰로 나눔 |
| 5 | Ocean Vuong (oceanvuong.com) | 시/소설 페이지 분리, 행사 일정 날짜순 | 행사·낭독 일정 날짜순 목록 |
| 6 | Chimamanda Ngozi Adichie (chimamanda.com) | Books Showcase, Read Online(온라인 글 모음) | "온라인에서 읽기" 링크 모음 |
| 7 | Ann Patchett (annpatchett.com) | 책마다 개별 페이지 | 작품마다 고유 주소(#앵커) |
| 8 | Margaret Atwood (margaretatwood.ca) | 전체 서지 페이지 | 맨 아래 접히는 "전체 서지" |
| 9 | 가와카미 미에코 (mieko.jp) | 일본어·영문 약력 공존 | 번역 출간 표시, 짧은 영문 약력 |
| 상 | Aardvark Book Club (Awwwards SOTD 2026-08-30) | 에디토리얼 타이포, 흰색+옅은 노랑 | 흰 바탕 + 옅은 색 하나의 절제, 표지 호버 살짝 뜨기 |
| 상 | Obys' Design Books (Awwwards SOTD) | 먹색·회색 두 색만 | 글자색은 거의 검정 하나로 통일 |

"표지 목업을 연도순 가로 한 줄"로 보여 주는 해외 작가 사이트는 확인하지 못했다. 우리가 새로 시도하는 형식이다.

## 2. GitHub 디자인 (공개 소스로 확인)

| 순위 | 저장소 | 라이선스 | 기법 |
|---|---|---|---|
| 1 | antfu/antfu.me (★1.1k) | 코드 MIT, 글 CC BY-NC-SA | 자식 요소가 90ms씩 늦게 아래서 떠오르는 페이드인, `prefers-reduced-motion` 배려, 본문 65ch |
| 2 | bchiang7/v4 (★8.3k) | MIT(출처 표기 요청) | 스크롤 시 숨는 반투명 고정 메뉴(`backdrop-filter: blur`), 통일된 이징 `cubic-bezier(.645,.045,.355,1)` |
| 3 | edwardtufte/tufte-css (★6.6k) | MIT | 미색 종이, 좁은 본문 칼럼, 옆주석 — 문학 페이지와 결이 가장 맞음 |
| 4 | chesterhow/tale (★1k) | MIT | 세리프 제목 + 차분한 본문 색 |
| 5 | satnaing/astro-paper (★5.1k) | MIT | 접근성, 스크롤바 색 맞춤, `:focus-visible` |
| 6 | shuding/shud.in | 라이선스 없음 → 기법만 | 본문에 세리프 이탤릭을 포인트로 섞기 |
| 참고 | Josh Comeau "Designing Beautiful Shadows" | 글 | 그림자를 여러 겹, 배경 색조를 섞어 |
| 참고 | raunofreiberg/interfaces | — | 호버·포커스·모션 체크리스트 |

## 3. 우리 사이트에 넣을 것 (결론)

1. 흰 바탕, 글자는 거의 검정 하나. 표지 색(먹색·흐린 파랑·살구·분홍)은 첫 화면의 번지는 빛과 작품 카드 색 짝에만. — 색감은 고운대표 합격.
2. 작품: 연도를 크게 앞세운 가로 책장(스크롤 스냅, 양 끝 흐림), 표지 목업에 층층 그림자와 호버 시 살짝 뜨기. 작품마다 고유 주소, 분류(소설집/장편/산문), 작가님 문장 한 줄 자리.
3. 반투명 고정 메뉴, 화면 폭 따라 변하는 글자 크기, 한글 단어 단위 줄바꿈.
4. 스크롤 시 은은한 페이드인(움직임 끈 사용자에겐 없음).
5. 소식은 행사·인터뷰·리뷰로 나누고, 맨 아래 접히는 전체 서지.

출처: athleticsnyc.com/work/new-york-review-of-books · winners.webbyawards.com (NYRB 2021) · commarts.com/project/23896/haruki-murakami-website · harukimurakami.com/books · craigmod.com/books · minjinlee.com · oceanvuong.com · chimamanda.com/books · annpatchett.com/books · margaretatwood.ca · mieko.jp · awwwards.com/sites/aardvark-book-club · awwwards.com/sites/obys-design-books · github.com/antfu/antfu.me · github.com/bchiang7/v4 · github.com/edwardtufte/tufte-css · github.com/chesterhow/tale · github.com/satnaing/astro-paper · github.com/shuding/shud.in · joshwcomeau.com/css/designing-shadows · github.com/raunofreiberg/interfaces
