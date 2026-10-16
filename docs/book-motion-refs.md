# "책이 펼쳐지는 모션" 참고 사례

작성: 2026-10-17. 이미지 파일은 올리지 않았고 링크와 설명만 적었습니다.
급한 작업이 아니라 나중에 고운대표가 원할 때 고르기 위한 자료입니다.

**먼저 알아둘 점**
- 아래 사례는 **검색으로 찾은 자료이고, 우리 사이트에 넣어 실제로 돌려 보지는 않았습니다.** 무게(용량)는 측정값이 아니라 방식에서 오는 대략적인 추정이라고 적었습니다. 실제로 쓰기로 정하면 그때 용량과 휴대폰 프레임을 직접 재야 합니다.
- 라이선스는 검색 결과(패키지 정보·README)에서 확인한 것만 적었고, 확인이 안 되면 "확인 못함"이라고 적었습니다. 쓰기 전에 각 저장소의 LICENSE 파일을 한 번 더 봐야 합니다.
- 우리 책 목업은 이미 CSS(그라데이션 + 그림자)로 만든 면입니다. 그래서 **CSS 3D transform으로 표지가 열리는 방식이 가장 자연스럽게 이어집니다.**

## 조건 3가지 (모든 방식에 공통)

1. **움직임 줄이기:** `prefers-reduced-motion: reduce`이면 애니메이션을 끄고, 바로 펼쳐진 마지막 모습(또는 표지 그대로)을 정지 상태로 보여 줍니다. 자바스크립트 라이브러리를 쓸 때도 이 조건을 먼저 검사해서 애니메이션 자체를 시작하지 않아야 합니다.
2. **휴대폰에서 버벅이지 않기:** `transform`과 `opacity`만 움직입니다(`box-shadow`·`filter: blur`·`width` 등은 움직이지 않음). `will-change`는 움직이는 동안만. 화면에 들어왔을 때 한 번만 재생(IntersectionObserver)하고, 한 화면에 동시에 여러 권이 움직이지 않게 합니다.
3. **흰 바탕·책별 표지 색과 어울리기:** 열린 속지는 흰색에 가까운 면 + 먹색 `#1F2430` 글자로 하고, 책 색은 표지 바깥면에만 씁니다. 속지 안 글자는 [cover-colors.md](./cover-colors.md)의 "중간색은 글자색으로 쓰지 않는다" 규칙을 따릅니다.

## 사례

### 1. CSS 3D 책 열기 (hover/클릭) — DEV Community 튜토리얼

- 링크: [CSS perspective and opening book as in 3D](https://dev.to/jsha/css-perspective-and-opening-book-as-in-3d-3985)
- 방식: **CSS 3D transform.** 부모에 `perspective`·`transform-style: preserve-3d`, 표지에 `rotateY`와 척추 쪽 `transform-origin`. 마우스를 올리면 표지가 열림.
- 라이선스: 글에 코드 라이선스 표기를 확인하지 못함. **코드를 복사하지 말고 방식만 참고해 직접 작성**하는 것이 안전합니다.
- 무게: 라이브러리 없음, CSS 몇십 줄. 매우 가벼움(추정).
- 접근성: hover만으로 열면 키보드·터치에서 못 엽니다. **`<button aria-expanded>`로 열고 닫게 바꾸고**, `prefers-reduced-motion`이면 전환 없이 상태만 바꿔야 합니다.
- 우리 사이트 적합도: 높음. 홈의 책 줄에서 책을 눌러 표지가 열리며 상세로 넘어가는 연출에 맞음.

### 2. 3D 책 단계별 만들기 — DEV Community 튜토리얼

- 링크: [Create an animated 3D book in CSS, step by step](https://dev.to/scastiel/create-an-animated-3d-book-in-css-step-by-step-26ic)
- 방식: **CSS 3D transform.** 래퍼에 `perspective`, 책에 `preserve-3d`와 `rotateY`로 책이 돌아서 두께가 보이게 함.
- 라이선스: 코드 라이선스 표기 확인 못함. 1번과 같이 방식만 참고.
- 무게: CSS만, 가벼움(추정). 책등·두께 면을 `div` 몇 개로 만들어 DOM이 조금 늘어남.
- 접근성: 장식 요소라 `aria-hidden`으로 두고, 책 이름·링크는 일반 텍스트로 따로 둡니다. 자동 회전은 하지 않는 것이 좋음.
- 우리 사이트 적합도: 높음. 상세 페이지의 큰 책 목업이 살짝 돌아 두께가 보이는 정도로 쓰기 좋음.

### 3. StPageFlip — 페이지 넘김 라이브러리

- 링크: [Nodlik/StPageFlip](https://github.com/Nodlik/StPageFlip) (npm 이름 `page-flip`)
- 방식: **JS 라이브러리.** 의존성 없이 현실적인 페이지 넘김을 만들고, 이미지·HTML 페이지를 지원. React용 포크(`react-pageflip`)도 있음.
- 라이선스: **MIT**(npm 패키지 정보로 확인). 다만 패키지 건강 점수가 52/100으로 낮게 표시되는 등 관리가 활발하지 않을 수 있어 확인이 필요합니다.
- 무게: 라이브러리 용량 + 페이지 이미지(또는 HTML). 이미지를 많이 넣으면 무거워지므로 **발췌 몇 쪽 이내**로 제한하는 편이 좋음(추정).
- 접근성: 마우스·터치 드래그 중심이라 키보드로 넘기는 버튼을 따로 달아야 함. 본문은 이미지가 아닌 HTML 텍스트로 넣어야 스크린리더가 읽음. `prefers-reduced-motion`이면 넘김 애니메이션을 끄는 옵션(`flippingTime` 단축 등)을 직접 확인해야 함.
- 우리 사이트 적합도: "책 발췌 미리보기" 같은 기능에만 적합. 책 소개용 가벼운 연출로는 과함. 표지·본문 이미지는 출판사 허락이 필요합니다.

### 4. GSAP + ScrollTrigger — 스크롤에 맞춰 열리는 책

- 링크: [GSAP (npm README)](https://cdn.jsdelivr.net/npm/gsap@3.15.0/README.md), 라이선스: [gsap.com/standard-license](https://gsap.com/standard-license)
- 방식: **JS 라이브러리.** 스크롤 위치에 따라 CSS 3D transform 값을 움직이는 스크롤 연동 애니메이션(ScrollTrigger).
- 라이선스: 검색 결과상 Webflow 인수 후 상업용도 무료인 **"standard 'no charge' license"**. **오픈소스(MIT)가 아니므로** 조건은 위 링크에서 직접 확인해야 합니다.
- 무게: 코어 + ScrollTrigger로 수십 KB 규모(추정, 미측정). 책 한 권 연출에는 과함.
- 접근성: 스크롤과 움직임이 묶이면 멀미를 유발하기 쉬움. `gsap.matchMedia()`로 `prefers-reduced-motion: reduce`일 때 애니메이션을 등록하지 않는 방식이 필요합니다. 스크롤 길이를 늘리는 "핀(pin)" 연출은 휴대폰에서 버벅이기 쉬워 권하지 않음.
- 우리 사이트 적합도: 첫 화면 그라데이션이 스크롤에 따라 번지는 연출까지 함께 쓸 때만 고려. 책 펼침만이면 CSS로 충분.

### 5. lottie-web — After Effects 애니메이션 재생

- 링크: [airbnb/lottie-web](https://github.com/airbnb/lottie-web)
- 방식: **JS 라이브러리(JSON 애니메이션 재생).** After Effects로 만든 책 펼침 영상을 벡터 JSON으로 내보내 재생.
- 라이선스: **MIT**(패키지 정보로 확인). 단, 따로 받은 Lottie 애니메이션 파일은 제작자마다 라이선스가 달라 별도 확인 필요.
- 무게: 라이브러리(수십 KB 이상, 추정) + JSON. 복잡한 그라데이션·번짐은 JSON이 커지고 휴대폰에서 느려질 수 있음. 표지 색 번짐 같은 그라데이션 표현에는 불리.
- 접근성: `prefers-reduced-motion`이면 재생하지 않고 정지 프레임을 보여 줌. 자동 반복은 금지, 일시정지 수단 필요.
- 우리 사이트 적합도: 디자이너가 After Effects로 제작해야 해서 부담이 큼. 우리 목업이 이미 CSS라 굳이 쓸 이유는 약함.

### 6. 영상(mp4/webm)으로 만든 책 펼침 — 참고용

- 링크: [Animated book covers – Future of Book Marketing](https://creativeparamita.com/book-cover/future-of-book-marketing/) (애니메이션 표지를 책 마케팅에 쓰는 개념 소개), 판매 템플릿 예: [Envato Elements 책 프로모 템플릿](https://elements.envato.com/book-promo-PCV72YF)(After Effects, 유료)
- 방식: **영상.** 책이 열리는 장면을 미리 렌더링해서 `<video muted playsinline>`으로 재생.
- 라이선스: 템플릿을 쓰면 해당 마켓의 라이선스(유료)를 따름. 직접 제작하면 우리 소유지만 **표지 이미지는 출판사 허락이 필요**합니다.
- 무게: 가장 무거움(몇백 KB~수 MB 추정). 휴대폰 데이터·배터리 부담.
- 접근성: 자동재생은 `prefers-reduced-motion`이면 막고 첫 프레임 이미지(`poster`)만 보여 줌. 자막이 필요한 내용이 아니라면 장식으로 처리.
- 우리 사이트 적합도: 낮음. 책별 표지 색이 CSS로 바뀌는 구조와 안 맞고, 흰 바탕과 영상 배경의 경계를 맞추기 어려움.

### (참고) Turn.js — 비추천

- 링크: [turnjs.com](http://www.turnjs.com/)
- 방식: JS(jQuery 플러그인) 페이지 넘김.
- 라이선스: 검색 결과상 **4판은 유료(상업용), 3판은 개인 용도 무료**라는 설명이 있으나 라이선스 문구는 확인하지 못했습니다. Bower 정보는 라이선스를 "Other"로 표기.
- 판단: 상업용 조건이 불분명하고 jQuery 의존이라 **쓰지 않는 것이 좋습니다.** 같은 용도라면 3번(StPageFlip)이 낫습니다.

## 비교

| # | 방식 | 라이선스 | 무게(추정) | 휴대폰 | 우리 적합도 |
|---|---|---|---|---|---|
| 1 | CSS 3D | 방식만 참고 | 매우 가벼움 | 좋음 | 높음 |
| 2 | CSS 3D | 방식만 참고 | 매우 가벼움 | 좋음 | 높음 |
| 3 | JS 라이브러리 | MIT | 중간 | 이미지 수에 따라 | 발췌 미리보기만 |
| 4 | JS 라이브러리 | no-charge 라이선스 | 중간 | 핀 연출은 위험 | 낮음 |
| 5 | JS(JSON) | MIT | 중간 이상 | 그라데이션에 불리 | 낮음 |
| 6 | 영상 | 마켓/직접 | 무거움 | 데이터 부담 | 낮음 |

## 추천

1. **기본은 1·2번 방식(CSS 3D transform), 라이브러리 없이 직접 작성.** 이미 CSS로 만든 책 목업을 `button`으로 열고 닫게 하면 되고, 무게 증가가 거의 없습니다.
2. 연출은 **한 번만, 화면에 들어올 때** 재생하고, `prefers-reduced-motion`이면 최종 상태를 정지로 보여 줍니다.
3. 본문 발췌를 보여 주고 싶을 때만 3번(StPageFlip)을 별도 페이지에서 검토합니다. 표지·본문 이미지는 출판사 허락 후에 사용합니다.
4. 실제로 만들 때는 첫 구현 후 **저사양 휴대폰 폭(390px)에서 프레임과 용량을 직접 재고**, 가로 스크롤이 없는지 확인합니다.
