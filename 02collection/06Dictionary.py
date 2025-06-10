""" 
딕셔너리
: 고유키와 값으로 구성된 집합자료형. Key를 통해 저장되므로 자료의
순서는 보장되지 않는다. 선언시 중괄호{}를 사용한다.
"""
# 생성1 : dict() 함수를 이용해서 딕셔너리 생성
dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)

# 생성2 : 중괄호 이용해서 생성
dic2 = {'one':1, 'two':2, 'three':'3'}
print(dic2)

# 딕셔너리 생성 후 반복문을 통해 출력
fruits = {'apple':100, 'grapes':200, 'orange':300, 'peach':400}
print('for문을 이용한 출력')
# 딕셔너리의 Key를 먼저 얻어온 후 인출한다.
for key in fruits:
  val =fruits[key]
  print("%s : %d" % (key, val))
  
print("길이", len(fruits))
# Key를 통해 접근해서 출력하거나 값 변경 가능
print("복숭아", fruits['peach'])

fruits['orange'] = 3500
print("오렌지", fruits['orange'])

# 삭제
del fruits['peach']
print('복숭아삭제', fruits)

""" 
keys() : 딕셔너리의 Key로 구성된 dict_keys 객체를 반환하여 반복문에서
  사용할 수 있다. """
get_keys = fruits.keys()
for k in get_keys:
  print(k)

""" 
values() : 딕셔너리의 Value로 구성된 dict_values 객체를 반환한다. """  
get_values = fruits.values()
for v in get_values:
  print(v)
