from google.appengine.ext import db

MALE = 'M'
FEMALE = 'F'

class Person(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)
    gender = db.StringProperty(required=True, choices=[MALE, FEMALE])
    email = db.EmailProperty(required=True)
    phone = db.PhoneNumberProperty()

