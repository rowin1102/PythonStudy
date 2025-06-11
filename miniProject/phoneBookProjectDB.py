import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', passwd='1234',
                       db='sample_db', charset='utf8', port=3306)
curs = conn.cursor()

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
      conn.close()
      break

def Insert():
  print(f'{'입력기능':-^30}')
  
  sql = f"""insert into phonebooks (username, phoneNum, address)
    values ('{input('성명:')}', '{input('전화:')}', '{input('주소:')}')"""
    
  try:
    curs.execute(sql)
    conn.commit()
    print('주소 입력 완료\n')
  except Exception as e:
    conn.rollback()
    print('쿼리 실행시 오류발생', e)

def Show():
  try:
    sql = 'select * from phonebooks'
    curs.execute(sql)
    rows = curs.fetchall()
    
    print('번호  성명     전화        주소')
    
    for row in rows:
      print('%s   %s   %s    %s' % (row[0], row[1], row[2], row[3]))
  except Exception as e:
    print('쿼리 실행시 오류발생', e)
  
  print()

def Search():
  print(f'{'검색기능':-^30}')
  print('이름을 입력해주세요.')
  
  try:
    sql = "select * from phonebooks where username like '%{0}%'".format(input('이름:'))
    curs.execute(sql)
    rows = curs.fetchall()
    
    print('번호  성명     전화        주소')
    
    for row in rows:
      print('%s   %s   %s    %s' % (row[0], row[1], row[2], row[3]))
  except Exception as e:
    print('쿼리 실행시 오류발생', e)
  
  print()
  
def Update():
  print(f'{'수정기능':-^30}')
  
  sql = "update phonebooks set username='{1}', phoneNum='{2}', address='{3}' where username='{0}'" \
    .format(input('수정할 성명을 입력하세요:'), input('새로운 이름:'), input('새로운 전화번호:'),
            input('새로운 주소:'))
  try:
    curs.execute(sql)
    conn.commit()
    print('연락처가 수정되었습니다.\n')
  except Exception as e:
    conn.rollback()
    print('쿼리 실행시 오류발생', e)

def Deltele():
  deleteName = input('삭제할 성명을 입력하세요:')
  
  sql = f"delete from phonebooks where username={deleteName}"
  
  try:
      curs.execute(sql)
      conn.commit()
      print('정보가 삭제되었습니다.\n')
  except Exception as e:
    conn.rollback()
    print('쿼리 실행시 오류발생', e)

Menu()