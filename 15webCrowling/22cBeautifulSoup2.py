import requests
from bs4 import BeautifulSoup

# KBO 타자 기록실
response = requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx?sort=HRA_RT')
# HTML 소스 저장
html = response.text
# Soup 객체로 변환
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 타이틀 크롤링 : HTML 태그 포함
title = soup.select_one('#contents > h4')
# print('title 요소 :', title)

# 태그를 제거하여 순수한 텍스트만 추출
title_txt = title.get_text()
# print('title 텍스트 :', title_txt)

# 타자기록이 있는 <table> 태그 전체를 얻어오기
record_table = soup.select_one('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')
# print('타자기록 요소 :', record_table)

# 타자 기록이 반복되어 출력되는 <tbody>를 얻어온 후 <tr>의 갯수만큼 반복
record_tr = soup.select_one('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody')
repeat_tr = record_tr.select('tr')

for rec in repeat_tr:
  d = []
  for idx in range(1, 20):
    d.append(rec.select_one(f'td:nth-child({idx})').get_text())
  print(d)

