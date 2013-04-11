# https://developers.google.com/appengine/docs/python/datastore/polymodelclass
# https://developers.google.com/appengine/articles/polymodel

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

from model import person

from common import share

ACCOUNT_GOOGLE = 'google'
ACCOUNT_ID_PWD = 'id_pwd'
ACCOUNT_FACEBOOK = 'facebook'

get_root_key = share.party_root_key

class Account(polymodel.PolyModel):
    login_type = db.StringProperty(required=True,
                                   choices=[ACCOUNT_GOOGLE, ACCOUNT_ID_PWD, ACCOUNT_FACEBOOK])
    userid = db.StringProperty(required=True)
    person = db.ReferenceProperty(person.Person,
                                  collection_name='accounts')


class Google(Account):
    gmail = db.EmailProperty(required=True)

    def __init__(self, *args, **kwargs):
        kwargs['login_type'] = ACCOUNT_GOOGLE
        Account.__init__(self, *args, **kwargs)

class IDPWD(Account):
    password = db.StringProperty(required=True)
    activated = db.BooleanProperty(default=False)
    def __init__(self, *args, **kwargs):
        kwargs['login_type'] = ACCOUNT_ID_PWD
        Account.__init__(self, *args, **kwargs)

# fb account
