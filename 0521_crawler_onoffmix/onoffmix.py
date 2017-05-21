##################################
# 2017 장고걸스 파이쓴 스터디 4번째 실습
##################################

# parser.py
import requests     # 리퀘스트 클래스를 사용하기 위해 임포트
from bs4 import BeautifulSoup as bs # 뷰티풀숩 리퀘스트로 가져온 html문서를 조작해서 원하는 내용만 추출하기 위해 사용.


# 로그인할 유저정보를 넣어주자 (모두 문자열)
# 이 내용은 로그인 하려는 사이트의 form을 분석해서 어떤 데이터를 넘겨줘야 할지 찾아낸다
# input 처리된 태그들 중 입력하는 폼과 보이지 않지만 hidden으로 지정된 것들을 모두 넣어주는게 좋다
# 테스트 해봐서 필요 없는 것들은 생략해도 됨
LOGIN_INFO = {
    'email': '__로그인이메일__',
    'pw': '__암호__',
    'proc': 'login',
    'returnUrl': '',
    'witnessMe': '1'
}

# Session 생성, with 구문 안에서 유지
# 세션 흐름이 끊기지 않고 유지되기 때문에 추천
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post(
    	'http://onoffmix.com/account/login',    # 접속 URL
    	data=LOGIN_INFO,                        # 위에서 정의했던 같이 보내줄 값들(POST전송)
    	verify=False,                           # SSL 검증을 하지 않음 한국의 https를 사용하는 SSL인증서 중에서 검증실패 나는 것들이 있어서 false로 놓고 쓰는게 편리하다.
    	headers={                               # User-Agent. 사용자의 브라우져를 알려주는 정보를 수정한다. 그냥 접근하면 막기 때문에 사파리크롬인척 한다
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                },
    	)
    #print(login_req.text)  # 잘 로그인 되는지 확인용 403이 뜬다면 로그인 실패 다른 웹페이지로 리다이렉트 하는 소스가 뜨면 로그인 성공해서 메인으로 이동하는 코드가 나온다.

    # 로그인 성공했으니 신청했던 온오프믹스 내역을 가져와보자
    # 마이 페이지에 신청한 온오프믹스 목록을 가져오는 코드
    event_req = s.get(  # post가 아니라 get을 사용
        'http://onoffmix.com/account/event',    # 온오프믹스 참가 목록 페이지 주소. http로 접속해도 되고 https로 접속해도 된다
        verify=False,                           # SSL 인증서 검증 건너띄기. 아마 실행할 때 워닝 메시지가 나타나지만 문제 없음.
        headers={                               # 위와 동일하게 사파리인척 접속. 어떤 웹서비스는 이 User-Agent정보를 읽어서 모바일용 브라우져면 모바일 웹피이지로 보내기도 한다.
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        },
    )
    #print(event_req.text)      # 잘 접속했는지 확인용

    soup = bs(event_req.content, 'html.parser') # 뷰티플숩을 html을 파싱하는 모드로 지정. xml 등 다른 것들도 처리 가능한 유능한 라이브러리다.
    events = soup.select('li.title > a')        # 웹페이지를 분석해서 찾아낸 온오프믹스 목록 제목을 가져오기 위한 선택자
    for e in events:       # 위에서 찾아낸 모든 목록을 하나씩 뽑아서 e에 넣어준다.
        print(e.text)       # 뽑아낸 정보의 제목을 쩍어준다. 신청한 목록이 나타난다.

