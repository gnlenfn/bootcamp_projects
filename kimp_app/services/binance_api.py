from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env",
            verbose=True)

BINANCE_API_KEY = os.getenv("BINANCE_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_SECRET")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

avg_price = client.get_avg_price(symbol='BTCUSDT')


def get_avg_price(ticker):
    return client.get_avg_price(symbol=ticker.upper()+"USDT")

