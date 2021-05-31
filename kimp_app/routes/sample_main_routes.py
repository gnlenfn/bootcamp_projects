from flask import Blueprint, render_template, request
from twit_app.utils import main_funcs
from twit_app.services import tweepy_api
from twit_app.models import user_model

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/compare', methods=["GET", "POST"])
def compare_index():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "username" : "유저의 유저이름 (username) 이 담긴 문자열"
        }

    prediction 은 다음과 같은 딕셔너리 형태로 넘겨주셔야 합니다:
     -   {
             "result" : "예측 결과를 담은 문자열입니다",
             "compare_text" : "사용자가 넘겨준 비교 문장을 담은 문자열입니다"
         }
    """
    all_users = user_model.User.query.all()
    users = [{"id": user.id, "username": user.username} for user in all_users]
    prediction = {"result": " [USER] ",
                  "compare_text": " [TEXT] "}
    
    if request.method == "POST":
        resp = request.form.to_dict()
        user_1 = user_model.User.query.filter_by(id=resp["user_1"]).first()
        user_2 = user_model.User.query.filter_by(id=resp["user_2"]).first()
        target_text = resp['compare_text']
        
        prediction = {
                "result": main_funcs.predict_text([user_1, user_2], 
                                                target_text),
                "compare_text": target_text
                }

    return render_template('compare_user.html', 
                            users=users, 
                            prediction=prediction), 200
         

@bp.route('/user')
def user_index():
    """
    user_list 에 유저들을 담아 템플렛 파일에 넘겨주세요
    """

    msg_code = request.args.get('msg_code', None)
    
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    user_list = user_model.get_users()

    return render_template('user.html', alert_msg=alert_msg, user_list=user_list)
