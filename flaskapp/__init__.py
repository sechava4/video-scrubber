from flask import Flask
from flaskapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class):
    application = Flask(__name__)
    application.config.from_object(config_class)
    db.init_app(application)
    migrate.init_app(application, db)

    return application


flaskapp = create_app(Config)

from flaskapp import routes, models
