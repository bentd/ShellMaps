#! ../env/bin/python

import os
import json

from flask import Flask
from flask import g
from flask import Response
from flask import request
# from flask_bcrypt import Bcrypt
#from flask_cors import CORS
#from flask_httpauth import HTTPBasicAuth
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS", "server.config.TestingConfig"))
#CORS(app)


#bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mail = Mail(app)


from server.database.businesses import Business
db.create_all()

with open("businesses.json", "r") as businesses:

    json_text = businesses.read()
    json_list = json.loads(json_text)

    for business in json_list["businesses"]:
        print business
        business_to_add = Business(business["name"], business["owner"], business["type"], business["address"], business["minority"], business["women"], business["verified"])
        db.session.add(business_to_add)
        db.session.commit()


"""
auth = HTTPBasicAuth()
@auth.verify_password
def verify(identifier, password):

    user = User.verifyUser(identifier, password)
    if user:
        g.user = user
        return True
    return False

"""

from server.routes.businesses import businesses
from server.routes.primary import primary

app.register_blueprint(businesses)
app.register_blueprint(primary)


@app.before_request
def before():

    if "appspot.com" in request.url:
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
