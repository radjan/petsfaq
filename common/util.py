from common import share

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
