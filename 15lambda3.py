# 람다식과 map, filter, reduce 함수 활용
print(f'{'람다식과 map함수1':-^30}')
# 인수에 2를 곱한 결과를 반환하는 람다식
multiLambda = lambda x : x * 2
list_data = [1, 2, 3, 4, -1, -2, -5, -10]
# 리스트의 요소의 갯수만큼 람다식을 호출하여 얻어진 결과를 리스트로 변환한다.
result = list(map(multiLambda, list_data))
print('결과1', result)  

""" 람다식에서 조건부 표현식(삼항연산자) 사용하기
  형식] 식1 if 조건식 else 식2
    - 조건식이 True일때 식1, False일때 식2
    - if를 사용했다면 반드시 else를 사용해야 함
    - elif는 사용할 수 없음
    - 만약 2개 이상의 조건이 필요하다면 if를 연속으로 사용해야 한다. """
print(f'{'람다식과 map함수2':-^30}')
list_data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 인수가 3으로 나누어지는 경우 '3X'를 반환하고, 아니면 숫자를 그대로 반환한다.
strNumLambda = lambda x : '3X' if x % 3 == 0 else x
result = list(map(strNumLambda, list_data2))
print('결과2', result)

print(f'{'람다식과 filter함수':-^30}')
list_data3 = [1, 4, 6, 19, 25, 46, 64, 81, 100]
result = list(filter(lambda z : z>5 and z<80, list_data3))
print('결과3', result)

print(f'{'람다식과 reduce함수':-^30}')
import functools, operator

# 2개의 요소를 더한 결과를 반환하는 람다식 정의
sum1 = functools.reduce(lambda i, j : i + j,  range(1, 11))
print('결과4-1', sum1)

# operator 모듈에서 제공하는 add함수로 위의 람다식과 동일한 기능을 제공
sum2 = functools.reduce(operator.add, range(1, 11))
print('결과4-2', sum2)