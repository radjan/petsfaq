from google.appengine.ext import db

class imagemodel(db.Model):
    filename = db.StringProperty()
    full_size_image = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)
