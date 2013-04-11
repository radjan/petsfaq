from google.appengine.ext import db

class Hospital(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    description = db.TextProperty(required=True)
    address = db.PostalAddressProperty(requered=True)
    phone = db.PhoneNumberProperty(required=True)
    bookable = db.BooleanProperty(required=True, default=False)
    emergency = db.BooleanProperty(required=True, default=False)
    emergency_condition = db.TextProperty()

