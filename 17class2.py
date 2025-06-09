'''
시나리오] 원의 넓이와 둘레를 계산할 수 있는 클래스를 작성한 후 
주어진 코드가 실행될 수 있도록 구현하시오.
circle1 = Circle(5)
print("원의넓이:", circle1.calArea())
print("원의둘레:", circle1.calRound())
'''

import math

# 클래스 정의
class Circle:
  # 생성자 정의
  def __init__(self, radius):
    # 멤버변수 : 반지름
    self.radius = radius
  # 넓이
  def calArea(self):
    return math.pi * (self.radius ** 2)
  # 둘레
  def calRound(self):
    return 2 * math.pi * self.radius
  # 인스턴스 변수 출력시 반환되는 문자열 정의
  def __str__(self):
    return f'원의 반지름은 {self.radius}입니다.'

# 반지름이 5인 인스턴스 생성
circle1 = Circle(5)
print(circle1)
print('원의 넓이 :', circle1.calArea())
print('원의 둘레 :', circle1.calRound())