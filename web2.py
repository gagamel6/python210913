# web2.py
#웹서버와 통신할 때 사용
import urllib.request
#크롤링할 때 사용
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
#웹페이지 실행결과 받기(문자열)
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체 생성
soup = BeautifulSoup(data, "html.parser")
cartoons = soup.find_all("td", class_="title")
print("검색결과:", len(cartoons) )
#첫번째 결과
title = cartoons[0].find("a").text
print(title)
link = cartoons[0].find("a")["href"]
print(link)
#다중 라인 주석 처리: ctrl + /
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
#파일에 저장
f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
for tag in cartoons:
    title = tag.find("a").text
    print(title.strip())
    f.write(title.strip() + "\n")

f.close()
