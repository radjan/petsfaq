from google.appengine.ext import db
from model import base

class Hospital(base.BaseModel, db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    name = db.StringProperty(required=True)
    description = db.TextProperty(required=True)
    zipcode = db.TextProperty(required=True)
    county = db.TextProperty(required=True)
    area = db.TextProperty(required=True)
    address = db.PostalAddressProperty(required=True)
    phone = db.PhoneNumberProperty(required=True)
    working_hour = db.TextProperty() # XXX data structure
    #bookable = db.BooleanProperty(required=True, default=False)
    emergency = db.BooleanProperty(required=True, default=False)
    emergency_phone = db.PhoneNumberProperty()
    emergency_hour = db.TextProperty()
    value_added_tax = db.StringProperty(default='')

    def get_id(self):
        return self.key().id()
