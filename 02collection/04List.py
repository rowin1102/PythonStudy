""" 
리스트(List)
: 대괄호 [] 안에 콤마로 항목을 구분하며, 대입연산자로 항목을 변경할 수 있는
시퀀스 자료형이다. 서로 다른 자료형의 항목으로 구성할 수 있다.
인덱싱, 슬라이싱, 연결, 반복 등이 가능하다.
"""
# random 모듈을 통해 6~10사이의 난수 생성
import random
rndNum = random.randint(6,10)

# 선언
# 정수로 구성된 리스트
list1 = [1,2,3,4,5,rndNum]
# 문자로 구성된 리스트
list2 = ['Java', 'HTML', 'Python']
# 중첩된 구조의 리스트
list3 = [10, 20, ['Java', 'HTML', 'Python']]

# 출력
# 리스트명을 사용하면 전체 항목을 출력할 수 있다.
print('list1', list1)
print('list2[2]', list2[2])
# 리스트 내부에 정의된 리스트 출력
print('list3[2]', list3[2])

# 슬라이싱
print(f"{'슬라이싱':-^30}")
print('list1[1:4]', list1[1:4]) #인덱스 1~3까지 출력
print('list1[:3]', list1[:3])   #시작이 없으면 0부터
print('list1[1:]', list1[1:])   #종료가 없으면 끝까지

# 리스트 간의 연결이 가능함. 리스트내에 또 다른 리스트가 삽입된다.
print(f"{'리스트연결':-^30}")
all_list = [list1, list2]
print('all_list', all_list)
print('all_list[1][0]', all_list[1][0]) #Java라는 문자가 출력됨


print(f"{'list 관련 메소드':-^30}")
# 11~20사이의 난수 생성
rndNum = random.randint(11,20)

# 항목 추가
list1.append(rndNum)
print(f'append({rndNum})', list1)

# 전체 항목 삭제
list1.clear()
print('clear()', list1)

# 리스트 확장
list1.extend([10, 20, 30, 40, 50])
print('extend()', list1)

# 지정된 인덱스에 요소 삽입
list1.insert(1, 99)
print('insert()', list1)

# 리스트의 마지막 항목 삭제 및 변환
print(list1.pop()) # 삭제된 항목 반환
print('pop()', list1) # 삭제된 결과 출력

# 처음 나오는 항목 99를 삭제
list1.remove(99)
print('remove()', list1)

# 리스트를 뒤집을때 사용
list1.reverse()
print('reverse()', list1)

# 특정 인덱스를 del키워드로 삭제
del list1[0]
print('0번항목삭제후', list1)
