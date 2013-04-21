from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import hospital, person

class Role(polymodel.PolyModel):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    verified = db.BooleanProperty(default=False)
    person = db.ReferenceProperty(person.Person, colloection_name='roles', required=True)

class PerOwner(Role):
    pass

class Moderator(Role):
    pass

class Vet(Role):
    hospital = db.RederenceProperty(hospital.Hospital, collection_name='vets')
    specialty = db.TextProperty()
    #specialties = db.ListProperty(specialty.Specialty)
    education = db.ListProperty(str)
    experience = db.ListProperty(str)

class Employee(Role):
    hospital = db.RederenceProperty(hospital.Hospital, collection_name='employees')

class Admin(Employee):
    pass
