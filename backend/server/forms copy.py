from server import db

from server.database.businesses import businesses
from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms.validators import DataRequired as required
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import EqualTo

class BusinessForm(Form):

    type = String 
