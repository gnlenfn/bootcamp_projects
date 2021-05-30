from flask import Blueprint, render_template, request
from kimp_app.utils import main_funcs
from kimp_app.services import tweepy_api
from kimp_app.models import crypto_models
import requests

bp = Blueprint('crpyto', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/price', methods=["GET", "POST"])
def compare_index():
    """
    - 가격 조회를 위한 코인 입력 --> 조회 결과 출력
    - 한글이름, 티커 입력 가능하게
    - 
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