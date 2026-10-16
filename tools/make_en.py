"""한국어 페이지에서 영어판(en/)을 다시 만든다. 기계 번역이 아니라 아래 표에 있는 문구만 바꾼다.
새 한국어 문구가 생기면 M 표에 영어를 더하고 다시 실행: python3 tools/make_en.py
실행 끝에 영어판에 남은 한글을 보여 준다(있으면 표에 추가)."""
import re, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PAGES = sorted(p for p in glob.glob('*.html'))
M = [
 # 긴 문장부터
 ('시안입니다. 아래 내용은 작가님 확인 전 자리표시이며 실제 정보가 아닙니다.', 'Draft. Content below is placeholder, pending the author’s confirmation.'),
 ('[문의 용도 한두 줄 — 예: 강연·번역·출판 문의. 작가님 확인 후]', '[One or two lines on enquiries — e.g. talks, translation, publishing. Pending confirmation]'),
 ('2013년 『작가세계』 신인상, 중편소설 「쇼코의 미소」 당선', '2013, Writer’s World (Jakga Segye) New Writer’s Award for the novella “Shoko’s Smile”'),
 ('사진: 문학광장 작가정보 [촬영자 표기 — 작가님 확인 후]', 'Photo: Munjang (Literature Plaza) author page [Photographer credit — pending confirmation]'),
 ('[작가 소개 한두 줄 — 작가님이 주신 글로 채웁니다]', '[One or two lines about the author — from the author’s own text]'),
 ('[작가 소개 — 작가님이 주신 글로 채웁니다]', '[Author biography — from the author’s own text]'),
 ('[소개 한두 줄 — 작가님이 주신 내용으로]', '[One or two lines — from the author]'),
 ('[수록작·번역 출간 정보 — 작가님 확인 후]', '[Contents and translations — pending confirmation]'),
 ('[작품 속 문장 한 줄 — 작가님이 고른 것]', '[A line from the book — chosen by the author]'),
 ('[작품 소개 — 작가님·출판사 확인 후]', '[About the book — pending confirmation]'),
 ('[언어 · 출판사 — 작가님 확인 후]', '[Language · publisher — pending confirmation]'),
 ('[작가님 공개 이메일 — 확인 후 기재]', '[Public email — pending confirmation]'),
 ('[전체 수상 목록 — 작가님 확인 후 보완]', '[Full list of awards — pending confirmation]'),
 ('[작가 사진 — 저작권 확인 후]', '[Author photo — pending permission]'),
 ('[링크 — 작가님이 주신 링크]', '[Link — from the author]'),
 ('[매체 인용 — 허락 확인 후]', '[Press quote — pending permission]'),
 ('[서점 링크 — 작가님 확인 후]', '[Bookshop link — pending confirmation]'),
 ('[한 줄 소개 — 작가님 확인 후]', '[One-line description — pending confirmation]'),
 ('[번역 출간 — 작가님 확인 후]', '[Translations — pending confirmation]'),
 ('[수상 내역 — 작가님 확인 후]', '[Awards — pending confirmation]'),
 ('[작가님이 고른 문장 한 줄]', '[A line chosen by the author]'),
 ('[작품 속 문장 한 줄]', '[A line from the book]'),
 ('판본을 누르면 설명이 열립니다.', 'Select an edition to read more.'),
 ('(판본 목록은 작가님 확인 전)', '(List of editions pending confirmation)'),
 ('영어·일본어·중국어·스페인어 등 번역', 'Translated into English, Japanese, Chinese, Spanish and more'),
 ('(작가님 확인 전)', '(pending confirmation)'),
 ('2016년 7월 7일 · 소설집(첫 소설집) · 문학동네', '7 July 2016 · Stories (first collection) · Munhakdongne'),
 ('2026년 4월 30일 · 산문(첫 산문집) · 문학동네', '30 April 2026 · Essays (first essay collection) · Munhakdongne'),
 ('2016년 7월 7일', '7 July 2016'),
 ('2026년 4월 30일', '30 April 2026'),
 ('소설집(첫 소설집)', 'Stories (first collection)'),
 ('산문(첫 산문집)', 'Essays (first essay collection)'),
 ('2026 · 산문 · 문학동네', '2026 · Essays · Munhakdongne'),
 ('2016 · 소설집 · 문학동네', '2016 · Stories · Munhakdongne'),
 (' · 산문 · 문학동네', ' · Essays · Munhakdongne'),
 (' · 소설집 · 문학동네', ' · Stories · Munhakdongne'),
 ('첫 산문집 ', 'First essay collection '),
 ('여러 나라의 『쇼코의 미소』', 'Shoko’s Smile around the world'),
 ('여러 나라의 『백지 앞에서』', '[English title] around the world'),
 ('여러 나라의 『[작품명]』', '[Title] around the world'),
 ('제29회 대산문학상 소설부문', '29th Daesan Literary Award (Fiction)'),
 ('제8회 젊은작가상', '8th Young Writers’ Award'),
 ('제8회 허균문학작가상', '8th Heo Gyun Literary Award for Writers'),
 ('제5회 젊은작가상', '5th Young Writers’ Award'),
 ('작가세계 신인상', 'Writer’s World New Writer’s Award'),
 ('1984년, 경기도 광명', '1984, Gwangmyeong, Gyeonggi Province, South Korea'),
 ('고려대학교 국어국문학과', 'Korea University, Korean Language and Literature'),
 ('[강연·낭독·행사 일정 — 공유 캘린더 연결 후 자동 표시]', '[Talks, readings and events — shown automatically once the shared calendar is connected]'),
 ('일정', 'Events'),
 ('판본 페이지 보기 ↗', 'View this edition ↗'),
 ('[더 있는 판본]', '[More editions]'),
 ('작가님 확인 후', 'Pending confirmation'),
 ('[연도 · 분류 · 출판사]', '[Year · Category · Publisher]'),
 ('[매체 · 제목 링크]', '[Outlet · Title link]'),
 ('[강연·낭독 일정]', '[Talks and readings]'),
 ('[이어지는 소개 문단]', '[Further paragraph]'),
 ('[작가님 확인 후]', '[Pending confirmation]'),
 ('[소설집 · 출판사]', '[Story collection · Publisher]'),
 ('[장편 · 출판사]', '[Novel · Publisher]'),
 ('[산문 · 출판사]', '[Essays · Publisher]'),
 ('[분류 · 출판사]', '[Category · Publisher]'),
 ('출간 연도순 작품', 'Books by year'),
 ('[최근 작품명]', '[Latest title]'),
 ('[번역판 제목]', '[Translated title]'),
 ('[언어/나라]', '[Language/Country]'),
 ('[한국어판]', '[Korean edition]'),
 ('중국어(번체)/대만', 'Chinese (Traditional)/Taiwan'),
 ('스페인어/[나라]', 'Spanish/[Country]'),
 ('일본어/일본', 'Japanese/Japan'),
 ('영어/미국', 'English/US'),
 ('영어/영국', 'English/UK'),
 ('한국어/한국', 'Korean/Korea'),
 ('아주 희미한 빛으로도', '[English title]'),
 ('내게 무해한 사람', '[English title]'),
 ('애쓰지 않아도', '[English title]'),
 ('밝은 밤', '[English title]'),
 ('마음산책', 'Maumsanchaek'),
 ('짧은 소설', 'Short fiction'),
 ('쇼코의 미소', 'Shoko’s Smile'),
 ('백지 앞에서', '[English title]'),
 ('문학동네', 'Munhakdongne'),
 ('전체 서지 보기', 'Full bibliography'),
 ('모든 작품 →', 'All books →'),
 ('← 작품 목록', '← All books'),
 ('출간 연도순', 'By year'),
 ('[작품명]', '[Title]'), ('[연도]', '[Year]'), ('[출간일]', '[Date]'), ('[출판사]', '[Publisher]'),
 ('[번역가]', '[Translator]'), ('[날짜]', '[Date]'), ('[나라]', '[Country]'),
 ('언어/나라', 'Language/Country'),
 ('© 최은영', '© Choi Eunyoung'), ('| 최은영', '| Choi Eunyoung'), ('최은영 | 소설가', 'Choi Eunyoung | Novelist'),
 ('소설가 최은영', 'Novelist Choi Eunyoung'),
 ('주 메뉴', 'Main menu'), ('대표작', 'Selected'), ('새 책', 'New book'), ('소설가', 'Novelist'), ('프로필', 'Profile'),
 ('소설집', 'Stories'), ('장편', 'Novel'), ('산문', 'Essays'), ('전체', 'All'), ('분류', 'Category'),
 ('행사', 'Events'), ('인터뷰', 'Interviews'), ('리뷰', 'Reviews'), ('서평', 'Press'),
 ('출생', 'Born'), ('데뷔', 'Debut'), ('학력', 'Education'), ('사진', 'Photo'), ('수상', 'Awards'),
 ('출판사', 'Publisher'), ('연도', 'Year'), ('번역', 'Translator'),
 ('작품', 'Books'), ('소식', 'News'), ('소개', 'About'), ('연락', 'Contact'),
 ('언어', 'Language'), ('최은영', 'Choi Eunyoung'),
]
def toggle(f, en):
    if en:
        return f'<div class="lang" aria-label="Language"><a href="../{f}" lang="ko" hreflang="ko">한국어</a><span aria-hidden="true">·</span><a href="{f}" aria-current="true" lang="en">EN</a></div>'
    return f'<div class="lang" aria-label="언어"><a href="{f}" aria-current="true" lang="ko">한국어</a><span aria-hidden="true">·</span><a href="en/{f}" lang="en" hreflang="en">EN</a></div>'
os.makedirs('en', exist_ok=True)
for f in PAGES:
    ko = open(f).read()
    # 한국어 쪽: 언어 줄과 hreflang을 이 파일 이름에 맞게
    ko = re.sub(r'<div class="lang".*?</div>', toggle(f, False), ko, flags=re.S)
    if '<div class="lang"' not in ko:
        ko = ko.replace('</nav>\n</header>', '</nav>\n  ' + toggle(f, False) + '\n</header>', 1)
    ko = re.sub(r'<link rel="alternate" hreflang="ko"[^\n]*\n', '', ko)
    ko = ko.replace('<link rel="stylesheet"', f'<link rel="alternate" hreflang="ko" href="https://choieunyoung-writer.github.io/{f}"><link rel="alternate" hreflang="en" href="https://choieunyoung-writer.github.io/en/{f}">\n<link rel="stylesheet"', 1)
    open(f, 'w').write(ko)
    en = ko.replace('<html lang="ko">', '<html lang="en">')
    en = re.sub(r'(href|src)="(?!https?:|#|\.\./|mailto:)(style\.css[^"]*|book-open\.js[^"]*|images/[^"]*)"', r'\1="../\2"', en)
    en = en.replace(toggle(f, False), toggle(f, True))
    en = en.replace('>한국어<', '>@@KO@@<')
    for k, v in M:
        en = en.replace(k, v)
    en = en.replace('>@@KO@@<', '>한국어<')
    open('en/' + f, 'w').write(en)
left = {}
for f in PAGES:
    s = open('en/' + f).read()
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S); s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    l = set(re.findall(r'[가-힣][가-힣 ·]*', s)) - {'한국어'}
    if l: left[f] = l
print('pages:', PAGES); print('leftover Korean in en/:', left or 'none')
