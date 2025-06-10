import sqlite3
import random

# sqlite 연결 및 DB파일 생성
conn = sqlite3.connect('./saveFiles/biography.db')\
# 커서 생성
curs = conn.cursor()
rnd = random.randint(0, 100)  

# 테이블 생성
""" 테이블은 이미 생성된 경우 예외가 발생되므로 두 번째 실행에서 예외처리를
  하지 않으면 실행이 중지된다. 혹은 if not exist를 쿼리문에 추가해도 된다. """
try:
  tblcmd = 'create table people (name char, job char, pay int)'
  # 쿼리문의 실행은 커서를 사용한다.
  curs.execute(tblcmd)
except Exception as e:
  print('[예외발생] 테이블은 이미 생성되었습니다.', e)
  
# 레코드 1개 삽입. 튜플을 사용하여 인파라미터를 설정
curs.execute('insert into people values (?,?,?)', (f'이순신{rnd}', '장군', 500))

# 레코드 2개 이상 삽입. 튜플로 구성된 리스트 사용.
curs.executemany('insert into people values (?,?,?)',
                [(f'강감찬{rnd}', '장군', 700), (f'홍길동{rnd}', '의적', 800)])

# for문을 이용한 삽입.
rows = [[f'곽재우{rnd}', '의병', 1100], [f'유성룡{rnd}', '재상', 1200],
        [f'임꺽정{rnd}', '의적', 1500]]
# 리스트의 크기만큼 반복해서 입력
for row in rows:
  # 각 루프의 리스트가 인파라미터에 할당되는 형식
  curs.execute('insert into people values (?,?,?)', row) 

# 입력을 마쳤다면 반드시 커밋한다.
conn.commit()
print('레코드 insert 및 commit 완료')  