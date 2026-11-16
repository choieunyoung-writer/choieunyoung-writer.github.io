# 커스텀 도메인 연결: www.choieunyoung.net (2026-11-16)

도메인은 작가님이 이미 등록하셨어요. 이 문서는 GitHub Pages에 그 도메인을 연결하는 절차예요.

## 1. 저장소 설정 (이 세션에서 완료, 아직 올리지 않음)
- 저장소 루트의 `CNAME` 파일 내용: `www.choieunyoung.net`
- DNS가 연결되기 전에 올리면 GitHub가 도메인을 확인하지 못해 경고가 날 수 있어서, 대표님 확인 후 올려요.

## 2. DNS 설정 (작가님 또는 대표님이 등록 사이트에서)
| 종류 | 이름(호스트) | 값 |
|---|---|---|
| CNAME | www | choieunyoung-writer.github.io |

- 루트 주소(`choieunyoung.net`, www 없는 주소)도 쓰고 싶으면 별도로 정해야 해요. 이 경우 GitHub Pages 문서의 A 레코드 값을 확인해서 넣어요.
- 기존에 `www`에 다른 기록이 있으면 지우고 위 값으로 바꿔요.

## 3. GitHub 설정 (대표님 계정에서)
- 저장소 Settings → Pages → Custom domain에 `www.choieunyoung.net` 입력 → Save
- DNS 확인이 끝나면 "Enforce HTTPS"를 켜요. 인증서 발급에는 시간이 걸릴 수 있어요.

## 4. 확인 후 할 일
- 새 주소로 홈·소개·작품·연락 페이지가 열리는지 확인 (휴대폰·PC)
- 사이트 안의 기존 `choieunyoung-writer.github.io` 주소 표시(검색용 주소·언어 연결)를 새 주소로 바꿀지는 확인 후 결정
- 시안 표시(noindex)는 작가님 최종 확인 후에만 지움
