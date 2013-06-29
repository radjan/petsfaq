import json
from StringIO import StringIO
import collections

from google.appengine.ext import db

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

def jsonify_response(response, data):
    if isinstance(data, set):
        data = list(data)
    response.headers['Content-Type'] = 'application/json'
    io = StringIO()
    json.dump(data, io)
    response.write(io.getvalue())

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

def get_model_properties(model, json_obj):
    kw = {}
    for key, prop in model.properties().items():
        if json_obj.has_key(key):
            kw[key] = _to_proper_type(json_obj[key], prop)
    return kw

def _to_proper_type(value, prop):
    # TODO: different type
    return value

def update_model_properties(modelobj, json_obj):
    kw = get_model_properties(modelobj, json_obj)
    for key, value in kw.items():
        modelobj.__setattr__(key, value)
    return modelobj

