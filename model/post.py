from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import person
from model import hospital
from model import base
import model.image

TYPE_QUESTION = "Q"
TYPE_ANSWER = "A"
TYPE_REPLY = "R"
TYPE_BLOG = "B"

STATUS_DRAFT = 0
STATUS_PUBLISH = 1
STATUS_EDITED = 2

ATYPE_TEXT = "T"
ATYPE_PHOTO = "P"

class Post(base.BaseModel, polymodel.PolyModel):
    title = db.StringProperty(required=True)
    post_type = db.StringProperty(required=True,
                  choices=([TYPE_QUESTION, 
                            TYPE_ANSWER, 
                            TYPE_REPLY,
                            TYPE_BLOG]))
    content = db.StringProperty(required=True, multiline=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def get_type(self):
        return '_'.join(self._class)

class Questions(Post):
    reply_to = db.ReferenceProperty(Post, collection_name='replies')
    author = db.ReferenceProperty(person.Person, collection_name='questions')

    def __init__(self, *args, **kwargs):
        Post.__init__(self, *args, **kwargs)
        self.post_type = TYPE_QUESTION

class Blogpost(Post):
    author = db.ReferenceProperty(person.Person, collection_name='blogposts')
    hospital = db.ReferenceProperty(hospital.Hospital, collection_name='blogposts')
    status_code = db.IntegerProperty(required=True)

    def __init__(self, *args, **kwargs):
        kwargs['post_type'] = TYPE_BLOG

        if kwargs['status_code'] == None:
           kwargs['status_code'] = STATUS_DRAFT

        Post.__init__(self, *args, **kwargs)

class Attached(base.BaseModel, db.Model):
    blogpost = db.ReferenceProperty(Blogpost, collection_name='attaches')
    title = db.StringProperty(required=True)
    attached_type = db.StringProperty(required=True,
                                      choices=([ATYPE_TEXT, 
                                                ATYPE_PHOTO]))
    content = db.StringProperty(required=True, multiline=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def get_type(self):
        return '_'.join(self._class)

