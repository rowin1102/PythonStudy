import pymysql

# MriaDB에 연결(포트는 3306이 기본이므로 생략 가능)
conn = pymysql.connect(host='localhost', user='sample_user', passwd='1234',
                       db='sample_db', charset='utf8', port=3306)
# 커서 생성
curs = conn.cursor()

# f-String을 통해 문자열 중간에 {}로 함수 호출문장을 삽입
sql = f"""insert into board (title, content, id, visitcount)
  values ('{input('제목:')}', '{input('내용:')}', 'nakja', 0)"""

try:
  # 쿼리문 실행
  curs.execute(sql)
  # MariaDB에 변경사항을 적용
  conn.commit()
  print('1개의 레코드가 입력됨')
except Exception as e:
  # 오류가 발생되면 롤백 처리
  conn.rollback()
  print('쿼리 실행시 오류발생', e)

# 자원 반납
conn.close()