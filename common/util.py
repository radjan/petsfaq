import json
from StringIO import StringIO
import collections

from google.appengine.ext import db

from common import share
from service.account import account_service
from sets import Set

GOOGLE = share.VIEW_GOOGLE
IDPWD = share.VIEW_IDPWD

FK_REF = {
        'Person'  :['avatars','questions', 'blogposts', 'roles',
                    'accounts'],
        'Hospital':['logos','blogposts','vets','employees', 'specialties'],
        'Post_Blogpost':['photos','attaches'],
        'Post'    :['replies'],
        'Role_Vet':['specialties'],
        'Attached':['aphotos'],
        }

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

def out_format(data, traced_ids=None):
    ret = None
    if isinstance(data, collections.Iterable):
        ret = []
        for d in data:
            ret.append(out_format(d, traced_ids))
    else:
        ret = _to_dict(data, traced_ids)
    return ret

def _to_dict(domain_obj, traced_ids=None):
    if traced_ids == None:
        traced_ids = Set()
    kind = domain_obj.get_type()
    model_id = domain_obj.get_id()
    tmp = {'kind': kind,
           'id': model_id}

    if model_id not in traced_ids:
        """check if ReferenceProperty-checked already done in previous 
        recursion or add into checking-Set
        """
        traced_ids.add(model_id)
        add_prop_list = FK_REF.get(kind,[])
        for add_prop in add_prop_list:
            fl = [] #foreign key list
            #for x in [v for v in domain_obj.__getattribute__(add_prop) if v.kind() not in traced_ids]:
            for x in domain_obj.__getattribute__(add_prop):
                fl.append(_to_dict(x, traced_ids.copy()))
            #add model type
            tmp[add_prop] = fl

    property_keys = domain_obj.properties().keys()
    for key in property_keys:
        prop = domain_obj.properties()[key]
        v = prop.get_value_for_datastore(domain_obj)
        if type(v) is list:
            l = []
            #for item in [x for x in v if v.kind() not in traced_ids]:
            for item in v:
                l.append(_to_str(item, traced_ids))
            tmp[str(key)] = l
        else:
            tmp[str(key)] = _to_str(v, traced_ids)
    return tmp

def _to_str(obj, traced_ids):
    if isinstance(obj, db.Key):
        if db.get(obj) == None:
            return unicode(None)
        elif db.get(obj).get_id() in traced_ids:
            return unicode(db.get(obj).get_id())
        else:
            return _to_dict(db.get(obj), traced_ids)
    return unicode(obj)

def get_model_properties(model, json_obj):
    kw = {}
    for key, prop in model.properties().items():
        if json_obj.has_key(key):
            kw[key] = _to_proper_type(json_obj[key], prop)
    return kw

def _to_proper_type(value, prop):
    # TODO: different type
    if isinstance(prop, db.ReferenceProperty):
        if isinstance(value, dict):
            # XXX other information dropped
            value = value['id']
        return prop.reference_class.get_by_id(int(value))
    return value

def update_model_properties(modelobj, json_obj):
    kw = get_model_properties(modelobj, json_obj)
    for key, value in kw.items():
        modelobj.__setattr__(key, value)
    return modelobj

