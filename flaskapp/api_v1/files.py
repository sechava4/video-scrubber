from flask import jsonify, request, abort
from sqlalchemy.orm.attributes import flag_modified

from flaskapp import db
from flaskapp.api_v1 import api
from flaskapp.api_v1.representors import file_schema, files_schema
from flaskapp.models import User, File, AllowedExtensions
from flaskapp.parser import Parser


@api.route("/files/<file_id>")
def get_file_detail(file_id):
    file = File.query.filter(File.id == file_id).first()
    if not file:
        abort(404)
    return file_schema.dump(file)


@api.route("/files/<file_id>", methods=['DELETE'])
def delete_file(file_id):
    File.query.filter(File.id == file_id).delete()
    db.session.commit()
    return jsonify({"message": "File deleted"})


@api.route("/files/<file_id>/meta")
def get_file_metadata(file_id):
    file = File.query.filter(File.id == file_id).first()
    if not file:
        abort(404)
    return jsonify(file.meta)


@api.route("/files/<file_id>/meta", methods=["PATCH"])
def update_metadata(file_id):
    file = File.query.filter(File.id == file_id).first()
    if not file:
        abort(404)
    updated_data = request.json
    file.meta.update(updated_data)
    flag_modified(file, "meta")
    db.session.commit()
    return jsonify(file.meta)


@api.route("/users/<user_id>/files/", methods=["GET"])
def get_files(user_id):
    files = File.query.filter(File.user_id == user_id).all()
    if not files:
        return abort(404)
    return jsonify(files_schema.dump(files))


@api.route("/users/<user_id>/files/", methods=["POST"])
def create_user_file(user_id):
    user = User.query.filter(User.id == user_id).first()
    if not user:
        return abort(404)
    ext = request.content_type.split("/")[1]

    if ext not in [a.value for a in AllowedExtensions]:
        return abort(400)
    parser = Parser()
    meta = parser.get_metadata(ext, request.data)
    file = File(user=user, extension=ext, data=request.data, meta=meta)
    db.session.add(file)
    db.session.commit()
    return file_schema.dump(file)
