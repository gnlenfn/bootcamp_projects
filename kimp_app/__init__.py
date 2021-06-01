from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

def clear_data():
    # meta = db.metadata
    # for table in reversed(meta.sorted_tables):
    #     print('Clear table %s' % table)
    #     session.execute(table.delete())
    # session.commit()
    db.drop_all()
    
def create_app(config=None):
    app = Flask(__name__)
    
    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from kimp_app.routes import (main_routes, add_crypto_routes)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(add_crypto_routes.bp, url_prefix='/api')
    #app.register_blueprint(kimp_routes.bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    clear_data()
    app = create_app()
    app.run(debug=True)
