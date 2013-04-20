jinja_env = None

PARTY_STORE_KIND = 'PARTY'
PARTY_STORE_ROOT = 'ROOT'
BLOG_STORE_ROOT = 'BLOG'

WEBAPP2_SESSION_KEY = 'my-little-secret_change-this-before-deploy'

from google.appengine.ext import db
def party_root_key():
    return db.Key.from_path(PARTY_STORE_KIND, PARTY_STORE_ROOT)

