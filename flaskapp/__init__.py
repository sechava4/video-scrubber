from flask import Flask
from flaskapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_class):
    application = Flask(__name__)
    application.config.from_object(config_class)
    db.init_app(application)
    migrate.init_app(application, db)
    ma.init_app(application)

    from .api_v1 import api as api_blueprint

    application.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return application


flaskapp = create_app(Config)

from flaskapp import models
from flaskapp.api_v1 import users
