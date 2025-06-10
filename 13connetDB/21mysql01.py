""" 파이썬에서 MySQL(MariaDB)를 사용하려면 PyMySQL을 먼저 설치해야 한다.
  pip install pymysql """
import pymysql

# DB연결 : port의 경우 3306이 디폴트 값이므로 변경되지 않았다면 생략해도 된다.
conn = pymysql.connect(host='localhost', user='sample_user', passwd='1234', port=3306,
                       db='sample_db', charset='utf8')
""" curcorclass = pymysql.cursors.DictCursor : 이 옵션을 사용하면
  레코드 인출시 딕셔너리로 사용할 수 있다. 디폴트값은 튜플로 설정되어 있다. """

curs = conn.cursor()

# SQL 적업을 위해서는 반드시 try~except로 예외처리 해야한다.
try:
  sql = 'select * from board'
  curs.execute(sql)
  
  # select한 모든 레코드 인출
  rows = curs.fetchall()
  print('단순인출', rows)
  
  print(f'{'인출1':-^30}')
  # 행 단위로 하나씩 인출하여 출력
  for row in rows:
    print(row)
    
  print(f'{'인출2':-^30}')
  # 행 단위로 출력하되 각 컬럼의 인덱스를 지정하여 인출
  for row in rows:
    print(row[0], row[1], row[2], end=' ')
    id = row[3]
    pdate = row[4]
    vcnt = row[5]
    # 변수에 저장한 후 서식문자를 이용해서 출력
    print('%s, %s, %s' % (pdate, id, vcnt))
    
  print(f'{'인출3':-^30}')
  # 검색어와 like를 이용해서 검색 결과 인출
  sql = sql + " where title like '%{0}%' ".format(input('검색어 입력:'))
  curs.execute(sql)
  rows = curs.fetchall()
  print(rows)
except Exception as e:
  print('쿼리 실행시 오류발생', e)
  
print('-'*40)
conn.close()
print('자원반납') 