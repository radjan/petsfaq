from google.appengine.ext import db
from model.person import Person
from model.hospital import Hospital
from model.post import Blogpost
from model.post import Attached
from model import base

class imagemodel(base.BaseModel, db.Model):
    person = db.ReferenceProperty(Person, collection_name='avatars')
    hospital = db.ReferenceProperty(Hospital, collection_name='logos')
    blogpost = db.ReferenceProperty(Blogpost, collection_name='photos')
    attached = db.ReferenceProperty(Attached, collection_name='aphotos')

    description =  db.StringProperty()

    img_blobkey = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)

