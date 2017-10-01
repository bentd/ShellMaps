
import datetime
import string
import Boolean

from server import db

class Business(db.Model):

    __tablename__ = "businesses"

    type = db.Column(db.String(64))
    name = db.Column(db.String(64))
    address = db.Column(db.String, unique=True)
    ethnicity = db.Column(db.String)
    verified = db.Column(db.Boolean)


    def __init__(self, type, name, address, ethnicity):

        self.type = type
        self.name = name
        self.address = address
        self.ethnicity = etnicity


    @classmethod
    def fromForm(cls, form):

        type = form.type.data
        name = form.name.data
        address = form.address.data
        ethnicity = form.ethnicity.data
        verified = form.verified.data

        
