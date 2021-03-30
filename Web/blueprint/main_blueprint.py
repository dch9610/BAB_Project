from flask import Blueprint
from flask import render_template
from flask import session

from datetime import datetime
# blueprint 객체 생성
main_blue = Blueprint('main', __name__)

# main을 요청하면 호출되는 함수
@main_blue.route('/main')
def main():
    # 날짜 출력
    date = datetime.today().strftime("%Y.%m.%d")
    
    html = render_template('main/main.html', date= date)
    return html