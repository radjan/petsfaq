# https://developers.google.com/appengine/docs/python/datastore/polymodelclass
# https://developers.google.com/appengine/articles/polymodel

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import person

from common import share


class Account(polymodel.PolyModel):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    login_type = db.StringProperty(required=True,
                                   choices=[share.ACCOUNT_GOOGLE,
                                            share.ACCOUNT_ID_PWD,
                                            share.ACCOUNT_FACEBOOK])
    userid = db.StringProperty(required=True)
    person = db.ReferenceProperty(person.Person,
                                  collection_name='accounts')

    def get_id(self):
        return self.key().id()

class Google(Account):
    gmail = db.EmailProperty(required=True)

    def __init__(self, *args, **kwargs):
        kwargs['login_type'] = share.ACCOUNT_GOOGLE
        Account.__init__(self, *args, **kwargs)

class IDPWD(Account):
    password = db.StringProperty(required=True)
    activated = db.BooleanProperty(default=False)

    def __init__(self, *args, **kwargs):
        kwargs['login_type'] = share.ACCOUNT_ID_PWD
        Account.__init__(self, *args, **kwargs)

# https://exyr.org/2011/hashing-passwords/
# https://github.com/SimonSapin/snippets/blob/master/hashing_passwords.py
# https://github.com/mitsuhiko/python-pbkdf2/blob/master/pbkdf2.py

# fb account
