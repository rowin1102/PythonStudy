# 파이썬은 문장의 끝에 세미콜론을 사용하지 않는다.
a = 'Hello Pyhon'
print(a, id(a))
print('한줄에'); print('여러줄 쓰려면 '); print('세미콜론이 필요함')

# 변수 선언시 별도의 키워드가 없음
a = 100
print(a, id(a))

# 정수형
i = 200
print(i, type(i))

# 실수형
i = 3.14
print(i, type(i))

# Bool형
i = True
print(i, type(i))

# 문자형
i = '안녕'
print(i, type(i))

# 변수와 할당을 여러개 할때는 콤마로 좌측, 우측을 구분하여 작성
r, g, b = 'Red', 'Green', 'Blue'
print(r, g, b)
