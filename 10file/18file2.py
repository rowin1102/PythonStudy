import pickle

# 여러가지 형식의 데이터 준비
name='개발자'
age=99
address='서울시 중구 세종대로'
times={'Java':20, 'HTML':2, 'Oracle':10, 'Python':3}

# with~as로 파일 오픈. 쓰기/바이너리 모드로 설정
with open('./saveFiles/developer.p', 'wb') as file:
  pickle.dump(name, file)
  pickle.dump(age ,file)
  pickle.dump(address ,file)
  pickle.dump(times ,file)
  
# 읽기/바이너리 모드로 설정
with open('./saveFiles/developer.p', 'rb') as file:
  # load함수로 내용 읽기
  name = pickle.load(file)
  age = pickle.load(file)
  address = pickle.load(file)
  times = pickle.load(file)

  print('이름', name)
  print('나이', age)
  print('주소', address)
  print('배당시간', times)