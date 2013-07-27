from google.appengine.ext import db
from model import hospital, role, base

class Specialty(base.BaseModel, db.Model):
    species = db.StringProperty(default='')
    category = db.StringProperty(default='')

class EntitySpecialtyRel(base.BaseModel, db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    hospital = db.ReferenceProperty(hospital.Hospital,
                    collection_name='specialties')
    vet = db.ReferenceProperty(role.Vet,
                    collection_name='specialties')
    specialty = db.ReferenceProperty(Specialty,
                    collection_name='relations')
    note = db.StringProperty(default='')
