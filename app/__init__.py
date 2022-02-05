from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models

    from .auth.views import auth_bp
    from .general.general import home_bp
    app.register_blueprint(auth_bp, url_prefix="/login")
    app.register_blueprint(home_bp, url_prefix="/home")

    return app