#! ../../env/bin/python

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response
from flask import render_template
#from server import auth
from server import db
from server.database.businesses import Business


primary = Blueprint("primary", __name__)


@primary.route("/", methods=["GET"])
def main():

    #business = Business("Foo Bar", "Bar Foo", "Restaurant", "8788 Townsquare Court, Jacksonville, FL 32216", True, True)
    #business.coordinates()

    #db.session.add(business)
    #db.session.commit()

    businesses = db.session.query(Business).filter_by(verified=True).all()

    return render_template("index.html", verifiedBusinesses=businesses)

@primary.route("/about", methods=["GET"])
def about():

    return render_template("index.html")

@primary.route("/download", methods=["GET"])
def download():

    return render_template("download.html")

@primary.route("/register", methods=["GET"])
def register():

    return render_template("register.html")

@primary.route("/map", methods=["GET"])
def map():

    return render_template("map.html")
