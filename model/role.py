from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import hospital, person

class Role(polymodel.PolyModel):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    verified = db.BooleanProperty(default=False)
    confirmed = db.BooleanProperty(default=False)
    person = db.ReferenceProperty(person.Person, collection_name='roles', required=True)

    def get_id(self):
        return self.key().id()

class PetOwner(Role):
    pass

class Moderator(Role):
    pass

class Vet(Role):
    hospital = db.ReferenceProperty(hospital.Hospital, collection_name='vets')
    description = db.TextProperty(default='')
    specialties = db.ListProperty(db.Key)
    education = db.StringListProperty()
    experience = db.StringListProperty(str)

class Employee(Role):
    hospital = db.ReferenceProperty(hospital.Hospital, collection_name='employees')

class Admin(Employee):
    pass
