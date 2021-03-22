from flask import Blueprint
from flask import render_template
from flask import session
from flask.globals import request

from database import user_dao

# blueprint 객체 생성
user_blue = Blueprint('user', __name__)

# 사용자 로그인
@user_blue.route('/user_login')
def user_login() :
    # 응답 결과를 랜더링한다.
    html = render_template('user/login.html')

    return html

# 사용자 로그인 확인
@user_blue.route('/user_login_pro', methods=['post'])
def user_login_pro():
    user_email = request.form.get('user_email')
    user_pw = request.form.get('user_pw')

    print(user_email)
    print(user_pw)

    # 사용자 존재 여부 확인
    result = user_dao.check_login_user(user_email, user_pw)
    print(result)

    # 로그인 실패
    if result == None :
        return '''
                <script>
                    alert('로그인에 실패하였습니다')
                    location.href='user_login?login_fail=true'
                </script>
               '''
    # 로그인 성공
    else :
        return '''
                <script>
                    alert('로그인에 성공하였습니다')
                    location.href='main'
                </script>
               '''

# ---------------------------------------------------------------

# 회원가입
@user_blue.route('/user_join')
def user_join() :

    # 응답 결과를 랜더링한다.
    html = render_template('user/signup.html')
    return html

# 회원가입 처리
@user_blue.route('/user_join_pro', methods=['post'])
def user_join_pro():
 # 브라우저가 전달한 데이터를 추출한다.
    # print(request.form)
    signup_name = request.form.get('signup_name')
    signup_email = request.form.get('signup_email')
    signup_password = request.form.get('signup_password')

    print(signup_name)
    print(signup_email)
    print(signup_password)

    # 데이터 베이스에 저장한다.
    # user_dao.insertUserData(signup_name,signup_email,signup_password)

    return '''
            <script>
                alert('가입이 완료되었습니다')
                location.href = 'user_login'
            </script>
           '''