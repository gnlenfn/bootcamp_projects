from flask import Blueprint, render_template, request
#from kimp_app.utils import main_funcs
#from kimp_app.services import tweepy_api
#from kimp_app.models import user_model

bp = Blueprint('kimp', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/kimp', methods=["GET", "POST"])
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


