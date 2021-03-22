from database import connector
from database import user_dao

# 데이터 베이스 접속 테스트
# conn = connector.get_connection()
# print(conn)
# conn.close()

# 사용자 정보 저장 테스트
# user_dao.insertUserData('김민재','123@gmail.com','12345')
# print('저장완료')

# 모든 사용자 정보를 가져오는 테스트
result = user_dao.selectUserDataAll()
print(result)
