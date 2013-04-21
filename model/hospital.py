from google.appengine.ext import db

class Hospital(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    name = db.StringProperty(required=True)
    description = db.TextProperty(required=True)
    specialty = db.TextProperty(required=True) #XXX data structure
    working_hour = db.TextProperty() # XXX data structure
    address = db.PostalAddressProperty(requered=True)
    phone = db.PhoneNumberProperty(required=True)
    bookable = db.BooleanProperty(required=True, default=False)
    emergency = db.BooleanProperty(required=True, default=False)
    emergency_phone = db.PhoneNumberProperty(required=True)
    emergency_condition = db.TextProperty()
    value_added_tax = db.StringNumber()

