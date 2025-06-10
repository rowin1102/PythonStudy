# 문자열 바꾸기
print(f'{'replace():':-^30}')
print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('Hello', '안녕')  
print(s)

""" 문자 바꾸기 : maketrans(바꿀문자, 새문자)로 변환테이블을 만든 후 translate()로
  적용한다. 아래 테이블 a는 1, e는 2로 변경한다."""
print(f'{'maketrans()/translate()':-^30}')
str1 = 'apple'
table = str1.maketrans('aeiou', '12345')
print(str1.translate(table))

# '한아언'이 'XYZ'로 각각 변경된다.
str2 = '한글은 아름다운 언어'
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table))

# 문자열 연결 : 리스트로 주어진 요소들을 특정 구분자를 통해 연결한다.
print(f'{'join()':-^30}')
print('-'.join(['010', '7906', '3600']))

""" 공백삭제 혹은 특정 문자 삭제 : lstrip(왼쪽), rstrip(오른쪽), strip(양쪽)
  만약 인수가 없으면 공백(스페이스)를 삭제한다. """
print(f'{'strip()':-^30}')
str = '#^%오늘은 @@ 파이썬 @@ 공부하는날#^%'
print(str.lstrip('#'))
print(str.rstrip('%'))
print(str.rstrip('%').lstrip('#').replace('@', ''))

""" 열 위치 찾기 : find(좌측부터), rfind(우측부터) 문자열을 찾은 후 인덱스를 반환 """
print(f'{'find()':-^30}')
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))

""" 문자열 상세 검사 : 문자열에 숫자, 알파벳, 한글만 있는 경우 True, 그 외의 문자가
  포함되어 있다면 False를 반환한다. """
print(f'{'isalnum()':-^30}')
str = 'python312좋아' 
print(str.isalnum())
str = 'python3.12좋아^^'
print(str.isalnum())

''' 시나리오] 입력한 문자열에 영문대문자, 소문자, 숫자만 포함되어 있다면 True, 
나머지 문자가 하나라도 포함되면 False를 반환하는 프로그램을 작성하시오. '''
print(f'{'시나리오':-^30}')
s = input('문자열을 입력하세요:')
result = True
# 입력받은 문자열을 통해 길이만큼 반복
for char in s:
  # 문자를 하나씩 검사
  if not(char.isupper() or char.islower() or char.isdigit()):
    # 대문자, 소문자, 숫자가 아닌 경우 False를 할당
    result = False
    
print(f'입력한 문자열 : {s}')
print('결과:%s' % result)