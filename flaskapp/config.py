import os


class Config(object):
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "adljsakldjk72s4e21cjn!Ew@fhfghfghggg4565t@dsa"
    )
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "mysql+pymysql://videoman:some_secret@localhost:3306/videodb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
