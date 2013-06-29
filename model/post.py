from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import person
from model import hospital

TYPE_QUESTION = "Q"
TYPE_ANSWER = "A"
TYPE_REPLY = "R"
TYPE_BLOG = "B"

STATUS_DRAFT = 1
STATUS_PUBLISH = 2
STATUS_EDITED = 3 

class Post(polymodel.PolyModel):
    title = db.StringProperty(required=True)
    post_type = db.StringProperty(required=True,
                  choices=([TYPE_QUESTION, 
                            TYPE_ANSWER, 
                            TYPE_REPLY,
                            TYPE_BLOG]))
    content = db.StringProperty(required=True, multiline=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    def get_id(self):
        return self.key().id()

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
        print 'samuel, kw', kwargs
        print 'samuel, ar', args
        kwargs['post_type'] = TYPE_BLOG
        kwargs['status_code'] = STATUS_DRAFT
        Post.__init__(self, *args, **kwargs)
        #super(Blogpost, self).__init__(*args, **kwargs)


