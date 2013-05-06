from google.appengine.ext import db

class Specialty(db.Model):
    species = db.StringProperty(default='')
    category = db.StringProperty(default='')

