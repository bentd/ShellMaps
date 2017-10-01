
import datetime
import string

from urllib import urlencode
from urllib2 import urlopen

from server import db

class Business(db.Model):

    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    type = db.Column(db.String(16), nullable=False)
    address = db.Column(db.String(128), unique=True, nullable=False)
    minority = db.Column(db.Boolean, nullable=False)
    women = db.Column(db.Boolean, nullable=False)
    verified = db.Column(db.Boolean)

    def __init__(self, name, type, address, minority, women, verified=None):

        self.name = name
        self.type = type
        self.address = address
        self.minority = minority
        self.women = women
        self.verified = verified

    def coordinates(self):

        address = urlencode({"address": self.address})
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyCo6s7TH2WBBQWgllw3kXlYxoM1zi7cCww".format(address)
        json = urlopen(url).read()
        print json


    @classmethod
    def fromForm(cls, form):

        type = form.type.data
        name = form.name.data
        address = form.address.data
        minority = form.minority.data

        verified = form.verified.data

if __name__ == "__main__":

    business = Business("Foo Bar", "Restaurant", "8788 Townsquare Court, Jacksonville, FL 32216", True, True)
