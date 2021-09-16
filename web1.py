# web1.py
from bs4 import BeautifulSoup

#웹페이지를 로딩(유니코드)
#메소드를 연속으로 호출(메서드 체인)
#페이지는 문자열 변수
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색을 잘하는 스프객체 생성(html태그 파싱)
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#<p>태그 몽땅 가져와~~
#print( soup.find_all("p") )
#<a>태그 몽땅 가져와~~
#print( soup.find_all("a") )
#첫번째 <p>태그만 가져오기
#print( soup.find("p") )
#특정 속성을 검색: <p class='outer'>컨텐츠</p>
#print( soup.find_all("p", class_="outer-text") )

#문자열만 가죠오기<p>교육센터</p>
for tag in soup.find_all("p"):
    #태그 안쪽에 문자열: .text 속성
    print( tag.text.strip() )

