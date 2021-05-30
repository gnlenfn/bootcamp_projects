from flask import Blueprint, request, redirect, url_for, Response
from kimp_app.services import upbit_api
from kimp_app.models import crypto_models, price_models

bp = Blueprint('user', __name__)


@bp.route('/coin', methods=['POST'])
def add_coins():
    """
    add cryptos to watch
    -  {
            "ticker" : "coin symbol",
            "eng_name" : "crypto english name",
            "kr_name" : "crypto korean name"
            
        }
    """
    
    ticker = request.form.get('ticker')
    coin_list = upbit_api.all_cryptos()
    for token in coin_list:
        crypto_models.add_crypto_to_db(token)
    
    KRW_markets = crypto_models.get_coins()
    if not ticker:
        # no username key
        return "Needs crypto name", 400
    
    elif not crypto_models.get_one_coin(ticker):
        # username doesn't exist on Upbit KRW market
        return redirect(url_for('main.user_index'), code=400) # main.user_index --> 뭘로 바꿔야하냐?
    
    # elif not upbit_api.get_one_user(target_name=ticker):
    #     # username not in db -> add user & add tweets
    #     user_model.add_user_to_db(coin_info)
    #     tweet_model.add_user_tweet(ticker)
    #     return redirect(url_for('main.user_index', msg_code=3), code=200)
    
    # else:
    #     # if there is username in db already
    #     tweet_model.update_user_tweet(username)
    #     return redirect(url_for('main.user_index', msg_code=3), code=200)


@bp.route('/user/')
@bp.route('/user/<int:user_id>')
def delete_user(user_id=None):
    """
    delete_user 함수는 `user_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거해야 합니다.
    요구사항:
      - HTTP Method: `GET`
      - Endpoint: `api/user/<user_id>`
    상황별 요구사항:
      -  `user_id` 값이 주어지지 않은 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `400`
      - `user_id` 가 주어졌지만 해당되는 유저가 데이터베이스에 없는 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `404`
      - 주어진 `username` 값을 가진 유저를 정상적으로 데이터베이스에서 삭제한 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
    """

    if not user_id:
        return "", 400
    
    elif not user_model.get_one_user(target_id=user_id):
        return "", 404
    
    else:    
        user_model.del_user_from_db(user_id)
        return redirect(url_for('main.user_index', msg_code=3), code=200), 200

