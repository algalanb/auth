# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
import datetime


# Define a User model
class User(db.Document):

    date_created  = db.DateTimeField(default=datetime.datetime.now, required=True)
    date_modified = db.DateTimeField(default=datetime.datetime.now, required=True)

    # User Name
    name    = db.StringField(max_length=128, required=True)

    # Identification Data: email & password
    email    = db.EmailField(max_length=128, required=True, unique=True)
    password = db.StringField(max_length=192, required=True)

    # Authorisation Data: role & status
    role     = db.IntField(required=True)
    status   = db.IntField(required=True)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)