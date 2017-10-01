#! ../../env/bin/python

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response
from server import auth
from server import db
from server.database.posts import Post
from server.forms import PostForm


primary = Blueprint("site", __name__)


@primary.route("/", methods=["GET")
def main():
    pass

@primary.route("/about", methods=["GET"])
def about():
    pass

@primary.route("/download", methods=["GET"])
def download():
    pass

@primary.route("/register", methods=["POST"])
def register():
    pass
