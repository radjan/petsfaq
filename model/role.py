from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import hospital
from model import specialty

class Role(polymodel.PolyModel):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    verified = db.BooleanProperty(default=False)

class User(Role):
    pass

class Moderator(Role):
    pass

class Vet(Role):
    hospital = db.RederenceProperty(hospital.Hospital, collection_name='vets')
    specialties = db.ListProperty(specialty.Specialty)
    education = db.ListProperty(str)
    experience = db.ListProperty(str)


class Admin(Role):
    hospital = db.RederenceProperty(hospital.Hospital, collection_name='admins')
