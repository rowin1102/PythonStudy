print(f"{'if문 첫번째 형식':-^30}")
# 4개의 변수 생성 및 초기화
a, b, c, str = 10, 20, 30, 'Python'

if a != b:
  print("a는 b와 다르다.")
if a <= c:
  print("a는 c보다 작거나 같다.")
# 문자열 자체를 조건으로 사용하면 True가 된다. 단 빈 문자열은 False
if str:
  print("문자열은 True를 한다.")
# if a > str: #에러발생
#     print("문자열과 정수는 비교의 대상이 될수없다.")

print(f"{'if문 두번째 형식':-^30}")
if not a > b:
  print("a는 b보다 크지 않습니다.")
else:
  print('a는 b보다 큽니다')
  
if a == b and b != c:
  print("모든 조건을 만족합니다.")
else:
  print('조건중 False가 있습니다.')
  
if a > b or b < c:
  print("조건중 True가 있습니다.")
else:
  print('모든 조건에 만족하지 않습니다.')
  
""" 
2개 이상의 조건식이 있는 경우 elif를 사용한다. """
print(f"{'if문 세번째 형식':-^30}")
age = 33
print(age, '살은 ', end="")
if age >= 35:
  print("중년입니다.")
elif age >= 30:
  print("중년의 시작입니다.")
else:
  print('청년입니다')
  
""" 
파이썬은 중괄호 대신 들여쓰기(Indent)를 통해 블럭을 설정한다.
따라서 들여쓰기의 깊이가 달라지면 에러가 발생되므로 주의해야한다.
"""