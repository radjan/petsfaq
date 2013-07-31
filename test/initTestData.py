# -*- encoding: utf8 -*-
import json

SERVER='localhost'
PORT='8080'

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

def import():
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
    v3 = create_vet(v3, person=p3, hospital=h1)

    a1 = create_admin(person=p1, hospital=h1)
    a2 = create_admin(person=p4, hospital=h1)
    a3 = create_admin(person=p3, hospital=h2)

def create_hosiptal(h):
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
if __name__ == "__main__":
    import()
