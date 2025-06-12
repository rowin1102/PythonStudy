import requests
from bs4 import BeautifulSoup

# '파이썬 웹크롤링'으로 검색한 인코딩 처리된 주소(한글로 넣어도 됨)
url = 'https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81'
# requests를 통해 지식인 페이지의 HTML 소스를 읽어옴
response = requests.get(url)

# 응답코드가 200이면 정상적으로 접속된 상태로 판단
if response.status_code == 200:
    # HTML 코드를 변수에 저장
    html = response.text
    # 파싱을 위해 Soup 객체로 변환. HTML이므로 html파서를 적용함.
    soup = BeautifulSoup(html, 'html.parser')
    
    # 셀렉터로 파싱(크롬) : 검색결과에서 첫 번째 제목을 
    title1_1 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a > b')
    # print('추출1_1', title1_1)
    
    # 셀렉터로 추출(파이어폭스) : 셀렉터의 결과는 다르지만 크롤링의 결과는 동일하다.
    title1_2 = soup. \
      select_one('.basic1 > li:nth-child(1) > dl:nth-child(1) > dt:nth-child(1) > a:nth-child(1) > b:nth-child(1)')
    # print('추출1_2', title1_2)
    
    # HTML 태그는 모두 제거하고 텍스트만 파싱
    text = title1_1.get_text()
    # print('추출2:', text)
    
    """ 검색결과 10개를 포함하고 있는 <ul> 태그 하위의 <li>를 한꺼번에 파싱하기
      위해 아래와 같이 작성 """
    ul = soup.select_one('ul.basic1')
    # print('추출3', ul)
    
    print('추출4')
    # 추출3에서 가져온 <ul> 태그 하위에 반복되는 <li>를 얻어온다.
    titles2 = ul.select('li>dl>dt>a')
    # 그리고 갯수만큼 반복해서 파싱한다.
    for tit in titles2:
      # 검색결과의 텍스트만 파싱해서 출력한다.
      print(tit.get_text())
else : 
    print(response.status_code)