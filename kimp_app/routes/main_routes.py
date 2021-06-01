from re import L
from flask import Blueprint, render_template, request
import pickle
from kimp_app.models import crypto_models, price_models
from kimp_app.services import upbit_api, binance_api, exchange_scrape, predicting



bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
        

@bp.route('/coin')
def user_index():
    all_coins = crypto_models.get_coins()
    prices = price_models.get_prices()
    
    return render_template('coin.html', coin_data=zip(all_coins, prices)) 

@bp.route('/kimp')
def kimp_table():
    # db의 코인들 불러오기
    # upbit,binance에서 현재가격 불러오기
    # 환율 스크래핑
    favorites = crypto_models.get_coins()
    ticker_list = []
    for crypto in favorites:
        ticker_list.append(crypto.ticker)
    
    price = []
    for ticker in ticker_list:
        price.append({
                    "ticker": ticker,
                    "upbit": int(upbit_api.get_candles(ticker)['trade_price']),
                    "binance": round(float(binance_api.get_avg_price(ticker)['price']), 2)
                    })
        #upbit_price.append(int(upbit_api.get_candles(ticker)['trade_price']))
        #binance_price.append(int(binance_api.get_avg_price(ticker)['price']))

    usd = exchange_scrape.get_usd_krw()
    
    return render_template("kimp.html", coin_price=price, dollor=usd)

@bp.route('/predict')
def prediction():
    day = upbit_api.get_candles('btc', 'days')
    features = predicting.features(day)
    with open("xgb_model.pkl", 'rb') as pickle_file:
        model = pickle.load(pickle_file)
        result = model.predict(features)
    
    result = str(result[0])
    return render_template("predict.html", prediction=result)