jinja_env = None

# -----
# web key
WEBAPP2_SESSION_KEY = 'my-little-secret_change-this-before-deploy_secret'

VIEW_GOOGLE = 'g'
VIEW_IDPWD = 'id'

VIEW_ROLE_ADM = 'a'
VIEW_ROLE_VET = 'v'
VIEW_ROLE_USER = 'u'

# -----
# web urls
HOME = '/'
REG_STEP1 = '/reg_step1'
REG_STEP2 = '/reg_step2'
REG_STEP3 = '/reg_step3'

# -----
# model key
ACCOUNT_GOOGLE = 'google'
ACCOUNT_ID_PWD = 'id_pwd'
ACCOUNT_FACEBOOK = 'facebook'

STORE_ROOT_KIND = 'STORE_ROOT'
PARTY_STORE_ROOT = 'PARTY'
ORG_STORE_ROOT = 'STORE'
BLOG_STORE_ROOT = 'BLOG'


from google.appengine.ext import db

class STORE_ROOT(db.Model):
    pass

def party_root_key():
    return db.Key.from_path(STORE_ROOT_KIND, PARTY_STORE_ROOT)

def org_root_key():
    return db.Key.from_path(STORE_ROOT_KIND, ORG_STORE_ROOT)

ACC_V2M_MAP = {VIEW_GOOGLE: ACCOUNT_GOOGLE,
               VIEW_IDPWD: ACCOUNT_ID_PWD,}
def acc_key_view2model(viewkey):
    return ACC_V2M_MAP.get(viewkey, 'unknown')

ACC_M2V_MAP = {ACCOUNT_GOOGLE: VIEW_GOOGLE,
               ACCOUNT_ID_PWD: VIEW_IDPWD,}
def acc_key_model2view(modelkey):
    return ACC_M2V_MAP.get(modelkey, 'unknown')

# XXX init root?
#if not db.get(party_root_key()):
#    STORE_ROOT(key=party_root_key()).put()
#
#if not db.get(org_root_key()):
#    STORE_ROOT(key=org_root_key()).put()

