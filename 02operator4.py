""" 문자에서 여러줄에 걸쳐 문자열을 쓸때는 이와 같이 더블이나 싱글 쿼테이션을 사용하면 된다.
  할당할 변수가 없으면 주석처럼 사용된다. """

str = """ 애래와 같이
여러줄에 걸쳐 문자열을 작성하고 싶으면
이와 같이 더블쿼테이션을 3개 작성한다.
"""

print(str)

# 문자열 변수 생성 및 초기화
head = '나는 헤더 '
bottom = ' 나는 보텀'
# 문자열의 덧셈은 '연결'의 결과를 반환
print(head + bottom)
# 문자열의 곱셈은 '반복'의 결과를 반환
print(head * 3)

# 문자열 슬라이싱
""" 파이썬에서 문자열은 인덱스를 통해 접근할 수 있다. 인덱스는 0부터 시작하고,
  콜론으로 범위를 지정할 수 있다. 범위 사용시 0:10으로 입력했다면 0~9까지를 의미한다.
  즉, 시간은 포함되고, 종료는 미만까지만 지정된다. """
engStr = 'Hello Python Good'
print(engStr[0])
print(engStr[:3])
print(engStr[1:3])
print(engStr[1:])

# 파이썬에서는 한글도 영문과 동일한 슬라이싱이 가능하다.
korStr = '안녕하세요? 파이썬입니다.'
print(korStr[0])
print(korStr[:2])
print(korStr[0:6])

# 정수와 문자는 연결할 수 없다.
# TypeError: can only concatenate str (not "int") to str
print(engStr + 100)
