# parser.py
from urllib.request import urlopen

from requests.packages.idna import unicode

url = 'http://mba.yonsei.ac.kr/recruit.asp?mid=m04_05'
u = urlopen(url)
s = unicode(u.read(), "euc-kr")
print(s)
u.close()