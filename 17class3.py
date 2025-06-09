""" 멤버변수의 정보은닉을 위해 private 대신 __(언더바2개)를 사용한다.
  정보은닉이란 멤버변수의 외부 접근을 차단하고, 클래스 내부에서만 접근하도록
  처리하는 것을 말한다. """
class Computer:
  # 생성자
  def __init__(self, name, passwd):
    # 외부 접근을 허용(public) 멤버변수
    self.name = name
    # 외부 접근을 차단(private) : 멤버변수 앞에 __를 추가
    self.__passwd = passwd
  def hitKeyboard(self):
    return f'{self.name}로 키보드 작업을 합니다.'
  def clickMouse(self):
    print(f'{self.name}에서 마우스로 클릭합니다.')
  def getPasswd(self):
    return self.__passwd
  def setPasswd(self, passwd):
    self.__passwd = passwd
    
myCom = Computer('LG Gram', 'qwer1234')

print(myCom.hitKeyboard())
myCom.clickMouse()

print('컴퓨터이름', myCom.name)

# private이므로 접근할 수 없어 에러 발생
# print('패스워드', myCom.__passwd)

print('패스워드', myCom.getPasswd())

myCom.setPasswd('abcd9876')
print('패스워드 변경 후 1', myCom.getPasswd())

myCom.__passwd = 'xxxxXXXX'
print('패스워드 변경 후 2', myCom.getPasswd())

# 권장되지 않음
# print('맹글링 규칭', myCom.__Computer__passwd)