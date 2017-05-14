# euc.py
# euc-kr로 된 사이트 가져오는 예제
from urllib.request import urlopen
from requests.packages.idna import unicode


url = 'http://mba.yonsei.ac.kr/recruit.asp?mid=m04_05' # 가져오고자 하는 보기드문 euc-kr로 된 사이트
u = urlopen(url)
s = unicode(u.read(), "euc-kr") # 두번째 인자로 원하는 인자를 지정할 수 있음.
print(s)
u.close()
