from kimp_app import db
from kimp_app.services.tweepy_api import get_tweets, get_user
from kimp_app.services.embedding_api import get_embeddings
from kimp_app.models.user_model import get_one_user


class Crypto(db.Model):
    __tablename__ = 'crpyto'
    # id, price, high, low, coin name(eng, kr)
    id = db.Column(db.Integer(), primary_key=True)
    ticker = db.Column(db.String())
    name_eng = db.Columns(db.String())
    name_kor = db.Columns(db.String())
    crypto_id = db.relationship("Price", backref="price.cryptos")

    def __repr__(self):
        return f"Crypto {self.id}"


def add_crypto_to_db(info):
    new_user = Crypto(
        #id = raw_user._json['id'],
        ticker = info['market'].split("-")[1],
        name_eng = info['english_name'],
        name_kor = info['korean_name'],
    )
    
    if not Crypto.query.filter_by(ticker=new_user.ticker).first():
        # if there is no new_user.id
        db.session.add(new_user)
        db.session.commit()
        
def get_coins():
    # return all users in db
    return Crypto.query.all()

def get_one_coin(ticker):
    # return one target user
        return Crypto.query.filter_by(ticker=ticker).first()


def del_user_from_db(ticker):
    target = Crypto.query.filter(Crypto.ticker==ticker).first()
    if target:
        db.session.delete(target)
        db.session.commit()
        