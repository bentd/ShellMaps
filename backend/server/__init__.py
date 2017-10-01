#! ../env/bin/python

import os

from flask import Flask
from flask import g
from flask import Response
from flask import request
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS"))
CORS(app)


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mail = Mail(app)


from server.database.posts import Post
from server.database.schools import School
from server.database.users import User


auth = HTTPBasicAuth()
@auth.verify_password
def verify(identifier, password):

    user = User.verifyUser(identifier, password)
    if user:
        g.user = user
        return True
    return False

from server.routes.accounts import accounts
from server.routes.posts import posts
from server.routes.schools import schools
from server.routes.tokens import tokens

app.register_blueprint(accounts)
app.register_blueprint(posts)
app.register_blueprint(schools)
app.register_blueprint(tokens)


@app.before_request
def before():

    if "case-app-backend.appspot.com" in request.url:
        abort(400)


@app.errorhandler(403)
def forbidden(error):
    return Response(error, status=403)


@app.errorhandler(404)
def lost(error):
    return Response(error, status=404)


@app.errorhandler(500)
def error(error):
    return Response(error, status=500)
