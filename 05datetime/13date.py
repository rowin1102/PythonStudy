# 모듈 임포트
import time
from datetime import date, datetime, timedelta

# 오늘 날짜와 년,월,일 출력
today = date.today()
print('오늘날짜', today, today.year, today.month, today.day)

print('='*30) 

# 현재시각
dtime = datetime.now()
print('현재시각', dtime)
print('년/월/일', dtime.year, dtime.month, dtime.day)
print('시/분/초/밀리세컨즈', dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print('='*30) 

# 날짜계산1
one_day = timedelta(days=1)
print('one_day', one_day) # 출력 형식 => 1 day, 0:00:0
# 오늘날짜에서 하루를 더하거나 빼서 날짜를 계산함
yesterday = today - one_day
tomorrow = today + one_day
print('어제와 내일', yesterday, tomorrow)

# 날짜계산2
date_diff = today - yesterday
# 위에서 one_day를 출력했을때와 동일한 값이 출력됨
print('날짜차이', date_diff)

# 날짜형식
date_str = today.strftime('%Y-%m-%d')
print('형식지정', date_str)

# 크리스마스까지 남은 날짜 계산
x_mas_str = f'{today.year}-12-25'
# str -> datetime 타입으로 형식 변환
x_mas_datetime = datetime.strptime(x_mas_str, '%Y-%m-%d')
# datetime -> date 타입으로 형식 변환
x_mas_date = datetime.date(x_mas_datetime)
# 값과 타입 확인하기
print(x_mas_str, x_mas_datetime, x_mas_date)
print(type(x_mas_str), type(x_mas_datetime), type(x_mas_date))
# 크리스마스에서 오늘날짜를 빼면 남은 날짜를 계산할 수 있음
date_diff = x_mas_date - today
print('크리스마스까지1', date_diff)
print('크리스마스까지2', date_diff.days)
