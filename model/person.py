from google.appengine.ext import db

class Person(db.Model):
    name = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

