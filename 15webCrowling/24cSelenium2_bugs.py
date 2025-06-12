from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'https://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
songs = soup.select('#CHARTrealtime > table > tbody > tr')

for song in songs:
  title = song.select('th > p > a')[0].text
  singer = song.select('td:nth-child(8) > p > a')[0].text
  album = song.select('td:nth-child(9) > a')[0].text
  
  print(title, singer, album, sep='|')
  song_data.append(['Bugs', rank, title, singer, album])
  rank += 1
  
colums = ['서비스', '순위', '타이틀', '가수', '앨범']
pd_data = pd.DataFrame(song_data, columns=colums)
print(pd_data.head())
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)