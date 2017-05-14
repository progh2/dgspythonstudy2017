# parser.py
import requests as rst
from bs4 import BeautifulSoup as bs
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTP GET Request
s = rst.Session()
req =  s.get('http://reading.ssem.or.kr/r/reading/search/schoolCodeSetting.jsp?schoolCode=24001', verify=False)
req =  s.get('http://reading.ssem.or.kr/r/reading/search/schoolSearchForm.jsp', verify=False)
req =  s.post('http://reading.ssem.or.kr/r/reading/search/schoolSearchResult.jsp?searchPageName=schoolSearchForm&division1=ALL&searchCon1=JAVA&connect1=A&division2=TITL&searchCon2=&connect2=A&division3=PUBL&searchCon3=&dataType=ALL', verify=False)

# HTML 소스 가져오기
html = req.text
#print(html)
# #HTTP Header 가져오기
# header = req.headers
#
# # HTTP Status 가져오기 (200:정상)
# status = req.status_code
#
# # HTTP가 정상적으로 되었는지 확인(True/False)
# is_ok = req.ok
#
# print(is_ok)

# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser를 이용했다.
soup = bs(html, 'html.parser')

# CSS Selector를 통해 html요소들을 찾아낸다.
books = soup.select('div.dataList > table > tbody > tr')

# # my_titles는 list 객체
for book in books:
    tds = book.select('td')
    # Tag안의 텍스트
    print(tds[0].find('a').get('onclick'))
    #print( tds[0].find('a span').text)
    print("저자:"+tds[1].text.strip())
    print("출판사:"+tds[2].text.strip().replace("\t", "").replace("\n(", "("))
    print("코드:"+tds[3].text.strip())
    # Tag의 속성을 가져오기(ex: href속성)
    # print(p.get('src'))
#
#
# data = {}
#
# for p in photos:
#     data[p.get('title')] = p.get('src')
#
# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)