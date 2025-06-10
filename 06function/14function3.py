""" Built - in Function(내장함수) :내장함수는 외부 모듈과 달리 import가
  필요하지 않으므로 별도의 설정없이 바로 사용할 수 있다. """

print(f'{'기본 내장 함수':-^30}')
# range함수를 통해 1~10까지를 생성하여 List로 정의함.
data1 = list(range(1, 11))
print(data1)
print('len=', len(data1))
print('sum=', sum(data1))
print('max=', max(data1))
print('min=', min(data1))

print(f'{'enumerate()':-^30}')
""" 순서가 있는 자료형(리스트, 튜플, 문자열 등)을 전달받아 인덱스를 포함하는 객체를
  반환한다. """
for i, v in enumerate(data1):
  # 리스트를 인덱스와 함께 값 출력
  print(i, v, end=', ')
print()

# 딕셔너리 생성
data2 = dict(birth=1970, name='홍길동', size='100cm')
# 딕셔너리를 통해 반복하면 Index와 Key를 반환
for i, v in enumerate(data2):
  print(i, v, data2[v], end=', ')
print()

print(f'{'eval()':-^30}') 
# 실행 가능한 문자열을 입력받아 결과값을 반환한다.
print(eval('1+2')) # 합의 결과 3 반환
print(eval("'hi' + 'a'")) # 문자열을 연결하여 반환

print(f'{'sorted()':-^30}')
# 입력값을 정렬한 후 리스트로 반환한다.
numbers = (8, 7, 6, 8, 4, 9, 7, 5, 3, 2, 7, 4, 9, 8, 2, 6, 5)
print(sorted(numbers))

print(f'{'이터레이터(iterator)':-^30}') 
""" 값을 차례대로 꺼낼 수 있는 객체.
  for i in range(100): 과 같이 작성하면 파이썬은 0부터 99까지의 값을
  차례대로 꺼낼 수 있는 이터레이터를 생성하여 숫자를 생성하게 된다.
  
  iter() : 반복을 끝낼 값(Sentinel)을 지정하면 특정 값이 나올때 반복을 종료하는 함수.
    형식] iter(반복가능한 객체, 반복을 끝낼 값)"""
it = iter([1, 2, 3, 4, 5, 99])
while it:
  row = next(it)
  # 99가 되면 break를 통해 반복문 탈출
  if row == 99:
    break
  print(row, end=', ')
""" 위 while문은 더 이상 출력할 항목이 없을 경우 next()에서 예외가 발생되면서 실행이 중지된다.
  이 부분은 예외처리에서 학습할 예정이다. """
print()

# 난수 생성을 위해 모듈 임포트
import random
count = 0
# iter()함수를 통해 반복. 2가 나올때까지 반복된다.
for i in iter(lambda : random.randint(0, 10), 2):
  print(i, end=', ')
  count += 1
else:
  print('\n난수 2가 생성되어 종료')
print(f'반복횟수:{count}')