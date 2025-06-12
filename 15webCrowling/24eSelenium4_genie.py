import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

# 파싱을 위해 Soup 객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1

# 1~4 페이지까지 반복
for page in range(1, 5):
  print('페이지', page)
  driver.implicitly_wait(2)
  # 각 차트의 순위 반복을 위한 tr요소 선택
  songs = soup.select('tbody > tr')
  for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    song_data.append(['Genie', rank, title, singer])
    rank += 1
  if page < 4:
    # 페이지 하단의 다음 순위 버튼을 클릭한다.
    driver.find_element(By.XPATH, f'//*[@id="body-content"]/div[7]/a[{page+1}]').click()
  driver.implicitly_wait(5)

# 리스트를 데이터프레임으로 변환 및 컬럼 추가
colums = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=colums)
print(pd_data.head())
pd_data.to_excel('./saveFiles/genie_chart.xlsx', index=False)