# 검색엔진 등록 준비 (2026-11-16)

플랜짐 예약앱 터미널이 공유한 글(사이트 공개 당일 검색엔진 4곳에 등록) 기준. 아직 **시안 단계라 실제로 등록하지는 않았고, 틀만 준비**해 두었다.

> **중요: 노출(공개)은 작가님 최종 확인 후에만 한다(CLAUDE.md).** 아래 4곳 등록은 noindex를 지우고 정식 공개하는 날 한 번에 처리한다. 지금은 계정 로그인이 필요한 1~2단계까지만 미리 해 둘 수 있다.

## 준비해 둔 것
- `robots.txt`: 지금은 `Disallow: /`로 막아 둠(시안 단계). 공개일에 이 줄을 지우고 `Sitemap:` 줄 주석을 해제.
- `sitemap.xml`: 한국어·영어 페이지 주소 목록. 공개일에 각 검색엔진에 제출.

## 검색엔진 4곳 — 로그인은 고운대표가 직접

| 검색엔진 | 할 일 | 필요한 것 |
|---|---|---|
| 구글 서치콘솔 | [search.google.com/search-console](https://search.google.com/search-console) → 속성 추가 → **URL 접두어** 방식으로 `https://www.choieunyoung.net/` 등록 | HTML 태그 인증 코드(또는 HTML 파일) |
| 네이버 서치어드바이저 | [searchadvisor.naver.com](https://searchadvisor.naver.com) → 사이트 등록 | 사이트 소유 확인용 메타태그 또는 HTML 파일 |
| 빙 웹마스터 도구 | [bing.com/webmasters](https://www.bing.com/webmasters) → 구글 서치콘솔 연동으로 바로 가져오기 가능 | (서치콘솔 연동 시 별도 인증 불필요할 수 있음) |
| 다음(카카오) 웹마스터 도구 | [webmaster.daum.net](https://webmaster.daum.net) → 사이트 등록 | robots.txt에 넣는 PIN 코드 |

## 대표님이 할 일
1. 위 4곳에 로그인해서 사이트 등록을 시작한다.
2. 각 사이트가 주는 **인증 코드**(메타태그 또는 PIN)를 이 세션에 알려 준다.
3. 이 세션이 코드를 각 페이지 `<head>`(메타태그 방식) 또는 `robots.txt`(다음 PIN)에 넣는다.
4. 작가님 최종 확인이 끝나면: noindex 삭제 + `robots.txt`의 `Disallow` 삭제 + `Sitemap` 줄 활성화 + 각 검색엔진에서 "제출/확인" 버튼 누르기(이 버튼은 대표님이 직접 누름).

## 지금 바로 할 수 있는 것
- 로그인·사이트 추가까지는 지금 해도 안전하다(공개되지 않음).
- "확인됨" 상태가 되어도 **색인(검색 노출)은 noindex가 걸려 있으면 안 됨** — 공개일까지는 걱정 없음.
