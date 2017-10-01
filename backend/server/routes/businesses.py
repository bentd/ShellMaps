#! ../../env/bin/python

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response
from server import auth
from server import db
from server.database.posts import Post
from server.forms import PostForm


businesses = Blueprint("businesses", __name__)


@businesses.route("/post", methods=["POST"])
