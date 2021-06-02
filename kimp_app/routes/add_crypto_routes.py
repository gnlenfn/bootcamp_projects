from flask import Blueprint, request, redirect, url_for, Response
from kimp_app.services import upbit_api
from kimp_app.models import crypto_models, price_models

bp = Blueprint('coin', __name__)


@bp.route('/coin', methods=['POST'])
def show_coins():
    """
    add cryptos to watch
    -  {
            "ticker" : "coin symbol",
            "eng_name" : "crypto english name",
            "kr_name" : "crypto korean name"
            
        }
    """
    
    ticker = request.form.get('ticker')
    try:
        coin_data = upbit_api.get_crypto_info(ticker)
        crypto_models.add_crypto_to_db(coin_data)    
        price_models.add_coin_price(ticker)

    except Exception as e:
        return print(e) #redirect(url_for('crypto.user_index'), code=400)
    
    if not ticker:
        # no username key
        return "Needs crypto name", 400
    
    elif not crypto_models.get_one_coin(ticker):
        # username doesn't exist on Upbit KRW market
        return redirect(url_for('main.user_index'))
    
    else:
        # 
        return redirect(url_for('main.user_index'))


@bp.route('/coin/')
@bp.route('/coin/<string:ticker>')
def delete_user(ticker=None):

    if not ticker:
        return "", 400
    
    elif not crypto_models.get_one_coin(ticker):
        return "", 404
    
    else:    
        crypto_models.del_coin_from_db(ticker)
        return redirect(url_for('main.user_index'))


@bp.route('/update/')
@bp.route('/update/<string:ticker>')
def update_price(ticker=None):  
    price_models.add_coin_price(ticker)
    return redirect(url_for('main.user_index'))
