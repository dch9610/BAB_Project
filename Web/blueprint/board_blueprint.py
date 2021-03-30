from flask import Blueprint
from flask import render_template
from flask import request
from flask import session

# blueprint 객체 생성
board_blue = Blueprint('board', __name__)

# main을 요청하면 호출되는 함수
@board_blue.route('/board_main')
def board_main() :

    
    html = render_template('boards/board_main.html')
    return html
