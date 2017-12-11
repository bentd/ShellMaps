
import datetime
import string
import json

from urllib import urlencode
from urllib2 import urlopen

from server import db

class Business(db.Model):

    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    owner = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    minority = db.Column(db.Boolean, nullable=False)
    women = db.Column(db.Boolean, nullable=False)
    verified = db.Column(db.Boolean)

    def __init__(self, name, owner, type, address, minority, women, verified=None):

        self.name = name
        self.owner = owner
        self.type = type
        self.address = address
        self.minority = minority
        self.women = women
        self.verified = verified

    def coordinates(self):

        print; print self.address; print
        address = urlencode({"address": self.address})
        print; print address; print;
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyCo6s7TH2WBBQWgllw3kXlYxoM1zi7cCww".format(address)
        data = urlopen(url).read()
        data = json.loads(data)
        print; print data; print;
        coord = data["results"][0]["geometry"]["location"]
        return coord

    @classmethod
    def fromForm(cls, form):

        name = form.name.data
        type = form.type.data
        address = form.address.data
        minority = form.minority.data
        women = form.women.data
        verified = form.verified.data

if __name__ == "__main__":

    business = Business("Foo Bar", "Restaurant", "8788 Townsquare Court, Jacksonville, FL 32216", True, True)
