from flask import Blueprint
from flask import render_template
from flask import session

# blueprint 객체 생성
user_blue = Blueprint('user', __name__)

# main을 요청하면 호출되는 함수
@user_blue.route('/user_main')
def user_main() :
    
    html = render_template('boards/orders.html')
    return html