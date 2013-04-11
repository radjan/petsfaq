from google.appengine.ext import db

class Specialty(db.Model):
    animal = db.StringProperty()
    category = db.StringProperty()

