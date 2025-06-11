import pymysql

# 삭제를 위한 함수
def delete_record():
  conn = pymysql.connect(host='localhost', user='sample_user', passwd='1234',
                        db='sample_db', charset='utf8', port=3306)
  curs = conn.cursor()
  
  while True:
    iStr = input('삭제할 일련변호(종료 : exit):')
    
    if iStr.lower() == 'exit':
      print('프로그램을 종료합니다.')
      break
    
    sql = f"delete from board where num={iStr}"
    
    try:
      curs.execute(sql)
      conn.commit()
      print('1개의 레코드가 수정됨')
    except Exception as e:
      conn.rollback()
      print('쿼리 실행시 오류발생', e)
  conn.close()

delete_record()