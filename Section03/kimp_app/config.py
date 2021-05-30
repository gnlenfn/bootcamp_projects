import psycopg2

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG=False

# postgre로 바꾸자 sprint2참고(pyfriend part3)
'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
'postgres://fmhvwixr:beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh@arjuna.db.elephantsql.com/fmhvwixr'
host = 'arjuna.db.elephantsql.com'
user = 'fmhvwixr'
password = 'beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh'
database = 'fmhvwixr'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)