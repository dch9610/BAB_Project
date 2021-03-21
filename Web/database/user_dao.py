from database import connector

# 사용자 정보 저장
def insertUserData(user_name, user_id, user_pw) :
    # 쿼리문
    sql = '''
            insert into user_table
            (user_name, user_id, user_pw)
            values (%s, %s, %s)
           '''

    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s 부분에 대입될 값을 튜플로 생성한다.
    # 쿼리문의 %s 순서에 맞춰준다.
    data = user_name, user_id, user_pw
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속을 끊어준다.
    conn.close()