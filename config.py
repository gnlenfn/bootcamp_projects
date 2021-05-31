import psycopg2
from sqlalchemy import create_engine

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='fmhvwixr',
    pw='beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh',
    url='arjuna.db.elephantsql.com',
    db='fmhvwixr')
    # SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///dev_db.sqlite3'
    
class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='fmhvwixr',
    pw='beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh',
    url='arjuna.db.elephantsql.com',
    db='fmhvwixr')
    # SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///dev_db.sqlite3'

# # postgre로 바꾸자 sprint2참고(pyfriend part3)
# 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
# 'postgres://fmhvwixr:beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh@arjuna.db.elephantsql.com/fmhvwixr'
# host = 'arjuna.db.elephantsql.com'
# user = 'fmhvwixr'
# password = 'beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh'
# database = 'fmhvwixr'

# connection = psycopg2.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database
# )