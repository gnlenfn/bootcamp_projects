class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///dev_db.sqlite3'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///prod_db.sqlite3'

# postgre로 바꾸자 sprint2참고(pyfriend part3)
URI="postgres://fmhvwixr:beZvDcOwfOf-TbCzYEfyHlHRyEFmRNNh@arjuna.db.elephantsql.com/fmhvwixr"