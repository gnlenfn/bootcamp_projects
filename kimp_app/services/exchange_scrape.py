from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def get_usd_krw():
    exchange = soup.select_one("div.head_info > span.value").string
    exchange = exchange.replace(",", "")
    return float(exchange)
