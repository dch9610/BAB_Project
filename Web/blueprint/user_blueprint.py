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
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    print(user_name)
    print(user_id)
    print(user_pw)