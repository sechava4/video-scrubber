from flaskapp import ma
from flaskapp.models import User, File


class FileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = File

    id = ma.auto_field()
    user = ma.auto_field()
    _link = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "api.get_file_detail",
                values=dict(file_id="<id>"),
                _external=True,
            ),
            "meta": ma.URLFor(
                "api.get_file_metadata",
                values=dict(file_id="<id>"),
                _external=True,
            ),
        }
    )


file_schema = FileSchema()
files_schema = FileSchema(many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    files = ma.Nested(FileSchema(many=True))
    _link = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "api.get_user_detail", values=dict(user_id="<id>"), external=True
            ),
        }
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
