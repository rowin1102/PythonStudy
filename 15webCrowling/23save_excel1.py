import pandas as pd

""" 데이터로 사용할 딕셔너리 생성.
  Key는 컬럼으로 사용됨. 각 데이터는 행이 되므로 총 5행짜리 데이터프레임으로 변환. """
data = {
  '이름' : ['강백호', '서태웅', '채치수', '송태섭', '정대만'],
  '국어' : [100, 80, 90, 85, 95],
  '영어' : [80, 75, 60, 90, 80],
  '수학' : [90, 70, 55, 40, 80],
}

# 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(data)
print(df)

# '이름' 컬럼을 인덱스로 지정
df.set_index('이름', inplace=True)
print(df)

# 데이터프레임을 엑셀로 저장
df.to_excel('./saveFiles/slamDuck.xlsx')