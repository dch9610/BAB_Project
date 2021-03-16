from flask import Blueprint
from flask import render_template
from flask import session

# blueprint 객체 생성
chart_blue = Blueprint('chart', __name__)

# main을 요청하면 호출되는 함수
@chart_blue.route('/chart_main')
def chart_main() :
    
    html = render_template('charts/charts.html')
    return html