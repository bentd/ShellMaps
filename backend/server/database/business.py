import datetime
import json
import random
import string

from itsdangerous import BadSignature
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from server import app
from server import bcrypt
from server import db

class Business(db.Model):

    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)

    def __init__ (self,
                  title,
                  condition,
                  description,
                  price,
                  user_id,
                  school_id,
                  image_url=None):
