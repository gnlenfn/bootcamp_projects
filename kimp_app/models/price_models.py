from kimp_app import db
from kimp_app.services import upbit_api


class Price(db.Model):
    __tablename__ = 'price'
    """
    - id: ids, primary key 
    - currnet: current price (1 min bar)
    - high: highest price in 24 hours
    - low: lowest price in 24 hours
    """
    
    id = db.Column(db.Integer(), primary_key=True)
    current = db.Column(db.Float())
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    crypto_ticker = db.Column(db.String(), db.ForeignKey("crypto.ticker"))
    

    def __repr__(self):
        return f"Price {self.id}"


def add_coin_price(ticker):
    ticker = ticker.upper()
    min_candle = upbit_api.get_candles(ticker, "minutes", "1", "1")

    if get_coin_price(ticker):
        del_price_from_db(ticker)
        
    added = Price(
        current = min_candle['trade_price'],
        high = min_candle['high_price'],
        low = min_candle['low_price'],
        crypto_ticker = ticker
    )

    db.session.add(added)
    db.session.commit()
    
def get_coin_price(ticker):
    return Price.query.filter_by(crypto_ticker=ticker).first()

def get_prices():
    return Price.query.order_by(Price.crypto_ticker).all()

def del_price_from_db(ticker):
    target = Price.query.filter(Price.crypto_ticker==ticker).first()
    if target:
        db.session.delete(target)
        db.session.commit()