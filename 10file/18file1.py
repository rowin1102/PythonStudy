""" open() : 파일을 다룰때 사용하는 내장함수로 첫번째 인자인 file경로만 필수사항이고
  나머지는 옵션이다.
  형식] open(파일경로, mode, encoding)
  mode : 파일 열기 모드로 w(쓰기), r(읽기), a(추가)가 있고 b(2진모드),
    t(텍스트모드)로 파일의 형식을 지정할 수 있다. """

print('='*30) 
print('내파일01.txt')
print('='*30) 

# 새로운 파일을 생성하여 반복문으로 내용을 입력. wt이므로 쓰기/텍스트모드로 파일 오픈
f_open = open('./saveFiles/내파일01.txt', mode='wt', encoding='utf-8')
for i in range(1, 21):
  data = '%d번째 줄입니다. \n' % i
  # 파일 내용 입력
  f_open.write(data)
# 반복문을 통해 입력한 후 파일 객체 닫기
f_open.close()
# 여기까지 실행되면 파일이 생성된다.

# 파일을 읽기/텍스트 모드로 오픈. 만약 파일이 없으면 에러 발생
f_read = open('./saveFiles/내파일01.txt', mode='rt', encoding='utf-8')
# 파일의 길이는 알 수 없으므로 무한루프로 구성
while True:
  # 파일의 내용을 할줄씩 읽음
  line = f_read.readline()
  # 더 이상 읽을 내용이 없다면 반복문 탈출
  if not line: break
  print(line)
# 작업을 마쳤다면 자원 해제
f_read.close
# 기존 파일에 내용을 추가하기 위해 추가/텍스트 모드로 오픈
f_add = open('./saveFiles/내파일01.txt', mode='at', encoding='utf-8')
# 한줄을 추가. 개행문자가 없으므로 줄바꿈 처리는 되지 않는다.
f_add.write('추가하는 내용입니다.')
# 필요한 경우 개행문자 추가. 2개 이상의 문자열을 리스트로 추가.
f_add.writelines(['줄바꿈은 되나요?\n', '안되면 개행문자를 넣어주세요.'])
f_add.write('마지막 라인입니다.')
f_add.close()

print('='*30) 
print('내파일02.txt')
print('='*30)

# 자동으로 파일객체를 open/close할 수 있게 with~as를 사용
with open('./saveFiles/내파일02.txt', mode='wt', 
          encoding='utf-8') as myfile:
  # 15줄의 문장을 입력하면 자동으로 close된다.
  for i in range(1, 16):
    data = '%d라인 입력합니다.\n' % i
    myfile.write(data)

# 앞에서 생성된 파일을 읽기모드로 open한 뒤 내용 출력.
with open('./saveFiles/내파일02.txt', mode='rt', 
          encoding='utf-8') as myfile:
  line = None
  while line != '':
    line = myfile.readline()
    print(line.strip('\n'))

# with open('./saveFiles/내파일02.txt', mode='rt', encoding='utf-8') as myfile:
#     for line in myfile:
#         print(line.strip())
