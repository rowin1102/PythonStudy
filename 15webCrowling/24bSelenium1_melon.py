from selenium import webdriver

# 크롬 드라이버 로드. 이때 웹브라우저가 실행됨.
driver = webdriver.Chrome()
""" 셀레니움은 크롬 브라우저를 이용해서 크롤링할 페이지를 띄운 후 데이터를 가져온다. 
  이때 비동기통신을 통해 데이터를 로드하는 경우 조금 늦게 로딩되는 경우가 있으므로, 
  셀레니움에서는 '암묵적대기'가 필요한 경우가 있다. 이런 경우 5초까지는 대기하겠다는 의미이다."""
driver.implicitly_wait(5)

""" time모둘을 사용하는 경우에는 로딩과 상관없이 무조건 5초를 대기한다. 
  따라서 반드시 필요한 경우에만 사용하는 것이 좋다. """
# import time
# time.sleep(5)

# 셀레니움을 통해 접속한 후 페이지의 정보(HTML소스)를 얻어옴
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

# BeautifulSoup을 임포트한 후 얻어온 정보를 Soup객체로 변환
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보를 저장할 리스트 생성
song_data = []
rank = 1
songs = soup.select('tbody > tr')

for song in songs:
  title = song.select('div.ellipsis.rank01 > span > a')[0].text
  singer = song.select('div.ellipsis.rank02 > a')[0].text
  favo = song.select('td:nth-child(8) > div > button > span.cnt')[0].text
  
  print(title, singer, favo, sep='|')
  # 파싱한 정보를 리스트에 추가
  song_data.append(['Melon', rank, title, singer, favo])
  rank += 1
  
import pandas as pd

# 데이터프레임으로 변환시 상단에 컬럼명을 추가
colums = ['서비스', '순위', '타이틀', '가수', '좋아요']
pd_data = pd.DataFrame(song_data, columns=colums)
# 데이터프레임의 상위 5개 행을 출력해서 확인
print(pd_data.head())
# 엑셀로 저장
pd_data.to_excel('./saveFiles/melon_chart.xlsx', index=False)