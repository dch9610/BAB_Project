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

# 모든 회원 정보 반환
def selectUserDataAll():
     # 쿼리문
    sql = '''
            select * from user_table
          '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 대입할 값 지정(없음)
    # 쿼리실행
    cursor.execute(sql)
    result = cursor.fetchall()
    # 데이터베이스 접속 해제
    conn.close()

    return result


# 로그인 처리를 위해 회원 존재 여부를 확인
def check_login_user(user_id, user_pw):
    # 쿼리문 작성
    sql = '''
        select * from user_table
        where user_id = %s and user_pw = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 값 셋팅
    data = (user_id, user_pw)

    # 쿼리 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()

    # 데이터베이스 접속 중지
    conn.close()

    return result