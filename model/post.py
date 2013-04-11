from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import person

TYPE_QUESTION = "Q"
TYPE_ANSWER = "A"
TYPE_REPLY = "R"

class Post(polymodel.PolyModel):
    title = db.StringProperty(required=True)
    post_type = db.StringProperty(required=True,
                                  choices=([TYPE_QUESTION, TYPE_ANSWER, TYPE_REPLY])
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    content = db.StringProperty(required=True, multiline=True)

    reply_to = db.RefernceProperty(Post, collection_name=replies)

class Questions(Post):
    author = db.ReferenceProperty(person.Person, collection_name='questions')

    def __init__(self, *args, **kwargs):
        Post.__init__(self, *args, **kwargs)
        self.post_type = TYPE_QUESTION

