from google.appengine.ext import db
from model.person import Person
from model.hospital import Hospital

class imagemodel(db.Model):
    person = db.ReferenceProperty(Person, collection_name='avatars')
    hospital = db.ReferenceProperty(Hospital, collection_name='logos')

    img_blobkey = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
