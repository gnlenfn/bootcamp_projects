from dotenv import load_dotenv
import hashlib
import os
import uuid
from urllib.parse import urlencode

import jwt
import requests
import re

load_dotenv(dotenv_path=".env", 
            verbose=True)

ACCESS_KEY = os.getenv('UPBIT_ACCESS_KEY')
SECRET_KEY = os.getenv('UPBIT_SECRET_KEY')
server_url = 'https://api.upbit.com'


def get_candles(ticker, unit="minutes", count='1', time='1'):
    if unit == "days":
        url = f"https://api.upbit.com/v1/candles/{unit}"
    else:
        url = f'https://api.upbit.com/v1/candles/{unit}/{time}'
    
    querystring = {"market": "KRW-"+ticker.upper(), "count": count}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()[0]


def get_crypto_info(ticker):
    ticker = ticker.upper()
    url = "https://api.upbit.com/v1/market/all"

    querystring = {"isDetails":"false"}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    response
    for info in response.json():
        if info['market'] == "KRW-"+ticker:
            return info
        
    return 

a = 1
get_candles("btc")