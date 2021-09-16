import os
import exiftool
from datetime import datetime
from flaskapp import flaskapp as app

from flask import jsonify, request


def get_parser():
    et = exiftool.ExifTool("./exiftool(-k).exe")
    et.start()
    return et


@app.route("/users/")
def create_user():
    et = get_parser()
    return "Hello World!"


@app.route("/users/<user_id>/videos/<video_id>")
def get_metadata(user_id, video_id):
    et = get_parser()
    meta = et.get_metadata("video.mp4")
    return jsonify(meta)


@app.route("/users/<user_id>/videos/", methods=["POST"])
def get_user_videos(user_id):
    now = datetime.now()
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, f"{now.strftime('%m_%d_%Y-%H_%M_%S')}.mp4")
    with open(filepath, "w+b") as file:
        file.write(request.data)
    return "created"
