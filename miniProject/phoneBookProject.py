def Menu():
  while True:
    print('1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료')
    num = int(input('선택:')) 
    
    if num == 1:
      Insert()
    elif num == 2:
      Show()
    elif num == 3:
      Search()
    elif num == 4:
      Update()
    elif num == 5:
      Deltele()
    elif num == 6:
      print(f'{'종료합니다.':-^30}')
      break
    

info = []

def Insert():
  print(f'{'입력기능':-^30}')
  
  name = input('성명>>>')
  phoneNum = input('전화>>>')
  address = input('주소>>>')
  
  personInfo = {
    'name' : name,
    'phoneNum' : int(phoneNum),
    'address' : address
  }
  
  info.append(personInfo)
  
  print('정보 입력 완료\n')
  
def Show():
  print(f'{'출력기능':-^30}')
  print('번호    성명        전화           주소')
  print(f'{'':-^34}')
  
  for idx, dict in enumerate(info):
    print(f"  {idx+1}     {dict['name']}     {dict['phoneNum']}     {dict['address']}")
  
  print()

def Search():
  print(f'{'검색기능':-^30}')
  print('이름을 입력해주세요.')
  searchName = input('이름:')
  
  for idx, dict in enumerate(info):
    if dict['name'] == searchName:
      print('번호    성명        전화           주소')
      print(f"  {idx+1}     {dict['name']}     {dict['phoneNum']}     {dict['address']}")
      
  print()


def Update():
  print(f'{'수정기능':-^30}')
  updateName = input('수정할 성명을 입력하세요:')
  print('수정할 이름, 연락처, 주소를 입력하세요')
  newName = input('새로운 이름:')
  newPhoneNum = input('새로운 전화번호:')
  newAddress = input('새로운 주소:')
  
  for dict in info:
    if dict['name'] == updateName:
      dict['name'] = newName
      dict['phoneNum'] = int(newPhoneNum)
      dict['address'] = newAddress
  
  print('연락처가 수정되었습니다.\n')
  
def Deltele():
  deleteName = input('삭제할 성명을 입력하세요:')
  
  for dict in info:
    if dict['name'] == deleteName:
      info.remove(dict)
      print('정보가 삭제되었습니다.\n')
    else:
      print('해당하는 정보가 없습니다.\n')
  print()

Menu()