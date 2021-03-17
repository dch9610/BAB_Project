from flask import Blueprint
from flask import render_template
from flask import session

# blueprint 객체 생성
user_blue = Blueprint('user', __name__)

# 사용자 로그인
@user_blue.route('/user_login')
def user_login() :
    # 응답 결과를 랜더링한다.
    html = render_template('user/login.html')

    return html

# 회원가입
@user_blue.route('/user_join')
def user_join() :

    # 응답 결과를 랜더링한다.
    html = render_template('user/signup.html')
    return html