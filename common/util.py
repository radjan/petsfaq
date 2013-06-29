from common import share
from service.account import account_service

import json
from StringIO import StringIO

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

def jsonify_response(response, data):
    if isinstance(data, set):
        data = list(data)
    response.headers['Content-Type'] = 'application/json'
    io = StringIO()
    json.dump(data, io)
    response.write(io.getvalue())

import collections
from google.appengine.ext import db

def out_format(data):
    ret = None
    if isinstance(data, collections.Iterable):
        ret = []
        for d in data:
            ret.append(out_format(d))
    else:
        ret = _to_dict(data)
    return ret

def _to_dict(domain_obj):
    tmp = {}
    property_keys = domain_obj.properties().keys()
    for key in property_keys:
        prop = domain_obj.properties()[key]
        v = prop.get_value_for_datastore(domain_obj)
        if type(v) is list:
            l = []
            for item in v:
                l.append(_to_str(item))
            tmp[str(key)] = l
        else:
            tmp[str(key)] = _to_str(v)
    tmp['id'] = domain_obj.get_id()
    return tmp

def _to_str(obj):
    if isinstance(obj, db.Key):
        return _to_dict(db.get(obj))
    return unicode(obj)

