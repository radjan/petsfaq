from google.appengine.api import users as gusers

def get_cuurent_user():
    user = gusers.get_current_user()
    return user

def get_username(user):
    if user:
        return user.nickname()
    return None

def get_mail(user):
    if user:
        return user.mail()
    return None

def get_userid(user):
    if user:
        return user.user_id()
    return None
