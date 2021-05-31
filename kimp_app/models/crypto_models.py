from kimp_app import db


class Crypto(db.Model):
    __tablename__ = 'crypto'
    # id, price, high, low, coin name(eng, kr)
    ticker = db.Column(db.String(), primary_key=True)
    name_eng = db.Column(db.String())
    name_kor = db.Column(db.String())
    crypto = db.relationship("Price", backref="price.crypto_ticker",
                                 cascade='all, delete-orphan')


    def __repr__(self):
        return f"Crypto {self.id}"


def add_crypto_to_db(info):
    new_user = Crypto(
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
    return Crypto.query.all().order_by(Crypto.ticker)

def get_one_coin(ticker):
    # return one target user
        return Crypto.query.filter_by(ticker=ticker).first()


def del_coin_from_db(ticker):
    target = Crypto.query.filter(Crypto.ticker==ticker).first()
    if target:
        db.session.delete(target)
        db.session.commit()
        