import enum
from datetime import datetime

from flaskapp import db


class AllowedExtensions(enum.Enum):
    mp4 = "mp4"
    jpg = "jpg"
    png = "png"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    files = db.relationship("File", back_populates="user")

    def __repr__(self):
        return "<User {}>".format(self.username)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="files")
    extension = db.Column(db.Enum(AllowedExtensions))
    updated_time = db.Column(db.DateTime, default=datetime.now())
    data = db.Column(db.BLOB)
