""" requests : 특정 웹페이지의 html 소스 코드를 읽어올때 사용하는 라이브러리.
  소스보기 했을때 보여지는 html 소스를 그대로 가져와 출력해준다. """

import requests

response1 = requests.get('https://www.naver.com/')
# print(response1.status_code) # 응답코드를 출력
# print(response1.text) # HTML 코드를 출력

# 요청시 파라미터가 필요한 경우 JSON 객체 형식으로 작성
paramJson = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬 웹크롤링'
}
# get 함수의 두 번째 인수로 전달. 그러면 쿼리스트링 형식으로 변화되어 전달되어 페이지의 결과를 얻어올 수 있다.
response2 = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=paramJson)
# print(response2.status_code) # 응답코드를 출력
# print(response2.text) # HTML 코드를 출력


""" BeautifulSoup : requests를 통해 얻어온 HTML 소스에서 필요한 내용을 
  파싱(Parsing)할때 사용되는 라이브러리 """

from bs4 import BeautifulSoup

url = 'http://daum.net/'
response = requests.get(url)

# 요청에 대한 응답이 정상인 경우
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else : 
    print(response.status_code)