#! ../../env/bin/python

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response
from flask import redirect
#from server import auth
from server import db


businesses = Blueprint("businesses", __name__)


@businesses.route("/business", methods=["POST"])
def createBusiness():


    return redirect("/contact")
