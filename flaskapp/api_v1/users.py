from flask import request, abort, jsonify

from flaskapp import db
from flaskapp.api_v1 import api
from flaskapp.api_v1.representors import user_schema
from flaskapp.models import User


@api.route("/users/", methods=["POST"])
def create_user():
    username = request.json.get("username")
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)


@api.route("/users/<user_id>")
def get_user_detail(user_id):
    user = User.query.filter(User.id == user_id).first()
    if not user:
        return abort(404)
    return user_schema.dump(user)


@api.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return jsonify({"message": "User deleted"})
