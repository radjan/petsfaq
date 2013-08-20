# -*- encoding: utf8 -*-
import sys
import json
import httplib
import urllib

SERVER='localhost'
PORT=8080
API_PREFIX='/api/v1'

conn = None
def _get_conn():
    global conn, PORT, SERVER
    if conn is None:
        conn = httplib.HTTPConnection(SERVER, PORT)
    return conn

h1 = {"name": "醫院一",
      "description": "這是醫院一",
      "zipcode": "106",
      "county": "台北市",
      "area": "大安區",
      "address": "敦化南路二段216號",
      "phone": "02-87654321",
      "working_hour": "週一至週六 09:00-21:00，週日公休",
      "emergency": True,
      "emergency_phone": "0987654321",
      "emergency_hour": "21:00-09:00",
      "value_added_tax": "87655678",
     }

h2 = {"name": "醫院二",
      "description": "這是醫院二",
      "zipcode": "235",
      "county": "新北市",
      "area": "中和區",
      "address": "中正路100號",
      "phone": "02-87654321",
      "working_hour": "週一至週日 09:00-21:00，週二公休",
      "emergency": False,
      "value_added_tax": "87655678",
     }

p1 = {"name": "獸醫一",
      "gender": "M",
      "birthday": "2010/01/01",
      "email": "vet1@petsfaq.com",
      "phone": "0987123456",
     }

p2 = {"name": "獸醫二",
      "gender": "F",
      "birthday": "2010/02/02",
      "email": "vet2@petsfaq.com",
     }

p3 = {"name": "獸醫三",
      "gender": "M",
      "birthday": "2010/03/03",
      "email": "vet3@petsfaq.com",
      "phone": "02-87878787",
     }

p4 = {"name": "小秘書",
      "gender": "M",
      "birthday": "2010/04/04",
      "email": "s1@petsfaq.com",
     }

s1 = {"species": "貓", "category": "一般"}
s2 = {"species": "貓", "category": "血液"}
s3 = {"species": "兔", "category": "一般"}
s4 = {"species": "兔", "category": "心臟"}
s5 = {"species": "兔", "category": "腫瘤"}
s6 = {"species": "狗", "category": "一般"}

v1 = {"description": "獸醫",
      "education": ["中興獸醫所", "台大獸醫系"],
      "experience": ["醫院一長工",]
     }

v2 = {}

v3 = {"description": "獸醫",
      "education": ["中興獸醫所", "台大獸醫系"],
      "experience": ["醫院一院長", "流浪動物之家志工"]
     }
bp1 = { "title": "test post",
        "content": "test post content",
        "publish": 0
      }

att1 = {
        "title": "test attach",
        "content": "test attach content"
        }


def init_data(PORT=8080):
    global h1, h2, s1, s2, s3, s4, s5, s6, p1, p2, p3, p4, v1, v2, v3, bp1, att1
    h1 = create_hospital(h1)
    h2 = create_hospital(h2)

    s1 = create_specialty(s1)
    s2 = create_specialty(s2)
    s3 = create_specialty(s3)
    s4 = create_specialty(s4)
    s5 = create_specialty(s5)
    s6 = create_specialty(s6)

    add_specialties([s1, s2, s3], hospital=h1)
    add_specialties([s3, s4, s5, s6], hospital=h2)

    p1 = create_person(p1)
    p2 = create_person(p2)
    p3 = create_person(p3)
    p4 = create_person(p4)

    v1 = create_vet(v1, person=p1, hospital=h1)
    v2 = create_vet(v2, person=p2, hospital=h1)

    add_specialties([s1, s2, s3], vet=v1)
    add_specialties([s1, s2, s3, s6], vet=v2)

    v3['specialties'] = [s1, s3, s4, s5, s6]
    v3 = create_vet(v3, person=p3, hospital=h2)

    a1 = create_admin(person=p1, hospital=h1)
    a2 = create_admin(person=p4, hospital=h1)
    a3 = create_admin(person=p3, hospital=h2)


    bp1 = create_blogpost(bp1)
    tt1 = create_attach(att1, blogpost=bp1)
    tt2 = create_attach(att1, blogpost=bp1)
    
    pub = {"publish":1}
    bp1 = complete_post(bp1, pub)



def create_hospital(h):
    response = send_post('/hospital', json.dumps(h))
    h['id'] = json.loads(response)['id']
    return h

def create_person(p):
    response = send_post('/person', json.dumps(p))
    p['id'] = json.loads(response)['id']
    return p

def create_specialty(s):
    response = send_post('/specialty', json.dumps(s))
    s['id'] = json.loads(response)['id']
    return s

def add_specialties(specialties, hospital=None, vet=None):
    if hospital:
        url_path = '/hospital/%s/specialties' % hospital['id']
    else:
        url_path = '/vet/%s/specialties' % vet['id']
    send_post(url_path, json.dumps(specialties))

def create_vet(vet, person=None, hospital=None):
    vet['person'] = person['id']
    vet['hospital'] = hospital['id']
    response = send_post('/vets', json.dumps(vet))
    vet['id'] = json.loads(response)['id']
    return vet

def create_admin(person=None, hospital=None):
    admin = {}
    admin['person'] = person['id']
    admin['hospital'] = hospital['id']
    response = send_post('/admins', json.dumps(admin))
    admin['id'] = json.loads(response)['id']
    return admin

def send_post(url_path, jsonstr):
    headers = {"Content-type": "application/json"}
    conn = _get_conn()
    conn.request("POST", API_PREFIX+url_path, jsonstr, headers)
    r = conn.getresponse()
    assert r.status == 201, 'FAILED: %s, %s' % (url_path, jsonstr)
    res = r.read()
    return res

def send_post_head(url_path,  jsonstr=None):
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}     
    jsonstr = urllib.urlencode(jsonstr)
    conn = _get_conn()
    conn.request("POST", API_PREFIX+url_path, jsonstr, headers)
    r = conn.getresponse()
    assert r.status == 201, 'FAILED: %s, %s' % (url_path, jsonstr)
    res = r.read()
    return res

def send_put(url_path, jsonstr):
    headers = {"Content-type": "application/json"}
    conn = _get_conn()
    conn.request("PUT", API_PREFIX+url_path, jsonstr, headers)
    r = conn.getresponse()
    assert r.status == 200, 'FAILED: %s, %s' % (url_path, jsonstr)
    res = r.read()
    return res

def create_blogpost(bp):
    response = send_post_head('/posts', bp)
    bp['id'] = json.loads(response)['postid']
    return bp

def create_attach(att, blogpost=None):
    bid = blogpost['id']
    response = send_post_head('/post/%s/attaches' % bid,att)
    att['id'] = json.loads(response)['attachedid']
    return att

def complete_post(bp, jsonstr):
    response = send_put('/post/%s' % bp['id'], json.dumps(jsonstr))
    return response


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        PORT = int(sys.argv[1])
    init_data()
