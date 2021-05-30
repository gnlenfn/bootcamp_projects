from twit_app import db
from twit_app.services.tweepy_api import get_tweets, get_user
from twit_app.services.embedding_api import get_embeddings
from twit_app.models.user_model import get_one_user


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
    cryptos = db.Columns(db.String(), db.ForeignKey("crypto.ticker"))


    def __repr__(self):
        return f"Price {self.id}"


# def update_user_tweet(username):
#     user_id = get_one_user(target_name=username).id
#     user_tweets = get_tweets(username)
#     tweet_text = [twt.full_text for twt in user_tweets]
#     embedded_text = get_embeddings(tweet_text)
    
#     for text, vec in zip(tweet_text, embedded_text):
#         updated = Tweet(text=text, embedding=vec, user_id=user_id)
#         db.session.add(updated)
#     db.session.commit()

# def add_user_tweet(username):
#     user_id = get_user(username).id
#     user_tweets = get_tweets(username)
#     tweet_text = [twt.full_text for twt in user_tweets]
#     embedded_text = get_embeddings(tweet_text)
    
#     for text, vec in zip(tweet_text, embedded_text):
#         updated = Tweet(text=text, embedding=vec, user_id=user_id)
#         db.session.add(updated)
#     db.session.commit()