from common import share
from service.account import account_service

GOOGLE = share.VIEW_GOOGLE
IDPWD = share.VIEW_IDPWD

def get_user(acc):
    return {'userid': acc.userid,
            'name': acc.person.name,
            'type': share.acc_key_model2view(acc.login_type),}

def temp_idpwd_user(userid):
    return {'userid': userid,
            'name': userid,
            'type': IDPWD}

def temp_google_user(guser):
    return {'userid': guser.user_id(),
            'name': guser.nickname(),
            'type': GOOGLE}

def get_userid(session):
    if 'user' in session:
        return session['user']['userid']
    return None

def get_person(session):
    acc = account_service.get_by_userid(
                get_userid(session),
                share.acc_key_view2model(session['user']['type']))
    return acc.person

def get_current_user(session):
    if 'user' in session:
        return session['user']
    return None

def maybe_add(d, key, value):
    '''
    add to dict d with key if value is not empty
    '''
    if value: d[key] = value
