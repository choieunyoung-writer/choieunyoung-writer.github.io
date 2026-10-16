"""한국어 페이지에서 영어판(en/)을 다시 만든다. 기계 번역이 아니라 아래 표에 있는 문구만 바꾼다.
새 한국어 문구가 생기면 M 표에 영어를 더하고 다시 실행: python3 tools/make_en.py
실행 끝에 영어판에 남은 한글을 보여 준다(있으면 표에 추가)."""
import re, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PAGES = sorted(p for p in glob.glob('*.html'))
M = [
 # 긴 문장부터
 ('내밀하고 미세한 감정의 결을 파고들어 현재 가장 뜨거운 문제와 접촉시키는 7편의 감정-사회 소설', '[Publisher’s description — English pending]'),
 ('시간이 지나고 하나의 관계가 끝날 때마다 나는 누가 떠나는 쪽이고 누가 남겨지는 쪽인지 생각했다. 어떤 경우 나는 떠났고, 어떤 경우 남겨졌지만 정말 소중한 관계가 부서졌을 때는 누가 떠나고 누가 남겨지는 쪽인지 알 수 없었다.', '[Excerpt from the book — English translation pending]'),
 ('— 「씬짜오, 씬짜오」에서', '— [source, English pending]'),
 ('미숙했던 지난날의 작은 모서리를 쓰다듬는 부드러운 손길', '[Publisher’s description — English pending]'),
 ('물질은 사라지지 않는다. 변형될 뿐. 산화되어 재만 남는다고 하더라도 보이지 않는 영역에서 물질은 아주 작은 부분도 사라지지 않고 여전히 존재한다. 그 과학적 명제는 어린 나에게 세상 어떤 위로의 말보다도 다정하게 다가왔었다.', '[Excerpt from the book — English translation pending]'),
 ('— 「모래로 지은 집」에서', '— [source, English pending]'),
 ('백 년의 시간을 감싸안으며 이어지는 사랑과 숨의 기록', '[Publisher’s description — English pending]'),
 ('그녀에게는 희망이라는 싹이 있었다. 그건 아무리 뽑아내도 잡초처럼 퍼져나가서 막을 수 없었다. 그녀는 희망을 지배할 수 없었다. 희망이 끌고 가면 그곳이 가시덤불이라도 그저 끌려갈 수밖에 없었다.', '[Excerpt from the book — English translation pending]'),
 ('— 본문에서', '— [source, English pending]'),
 ('여러 나라의 『내게 무해한 사람』', '[English title] around the world'),
 ('내게는 지난 이 년이 성인이 된 이후 보낸 가장 어려운 시간이었다. 그 시간의 절반 동안은 글을 쓰지 못했고 나머지 시간 동안 『밝은 밤』을 썼다. 그 시기의 나는 사람이 아니었던 것 같은데, 누가 툭 치면 쏟아져내릴 물주머니 같은 것이었는데, 이 소설을 쓰는 일은 그런 내가 다시 내 몸을 얻고, 내 마음을 얻어 한 사람이 되어가는 과정이었다.', '[From the author’s afterword — English translation pending the author’s confirmation]'),
 ('— ‘작가의 말’에서', '— from the author’s afterword'),
 ('여러 나라의 『밝은 밤』', '[English title] around the world'),
 ('제11회 젊은작가상', '11th Young Writers’ Award'),
 ('제51회 한국일보문학상', '51st Hankook Ilbo Literary Award'),
 ('제1회 이해조소설문학상', '1st Lee Hae-jo Literary Award for Fiction'),
 ('제24회 김준성문학상', '24th Kim Jun-seong Literary Award'),
 ('최은영은 1984년 경기도 광명에서 태어난 소설가다. 고려대학교 국어국문학과 출신으로, 2013년 『작가세계』 신인상에 중편소설 「쇼코의 미소」가 당선되며 작품 활동을 시작했다.', 'Choi Eunyoung is a novelist born in 1984 in Gwangmyeong, Gyeonggi Province. She studied Korean Language and Literature at Korea University, and made her debut in 2013 when her novella “Shoko’s Smile” won the Writer’s World (Jakga Segye) New Writer’s Award.'),
 ('[작품 세계 소개 — 작가님이 주시거나 확인하신 글로 채웁니다]', '[About her work — from text the author provides or confirms]'),
 ('소설집 『쇼코의 미소』(2016), 『내게 무해한 사람』(2018), 『아주 희미한 빛으로도』(2023), 장편소설 『밝은 밤』(2021), 짧은 소설 『애쓰지 않아도』(2022), 산문집 『백지 앞에서』(2026)를 펴냈다.', 'Her books include the story collections Shoko’s Smile (2016), A Person Harmless to Me (2018) and Even with the Faintest Light (2023), the novel Bright Night (2021), the short fiction Effortless (2022), and the essay collection Before the Blank Page (2026). [English titles pending confirmation]'),
 ('작품은 영어·일본어·중국어·스페인어 등으로 번역되어 출간되었다.', 'Her work has been published in English, Japanese, Chinese, Spanish and other languages.'),
 ('(작가님 확인 전)', '(pending confirmation)'),
 ('[작가님이 덧붙이고 싶은 이야기 — 작가님 확인 후]', '[Anything else the author would like to add — pending confirmation]'),
 ('사진: 문학광장 [촬영자 표기 — 작가님 확인 후]', 'Photo: Munhak Gwangjang [photographer credit pending]'),
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
