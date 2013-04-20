from model import person as p_model
from common import share

get_root_key = share.party_root_key

class PersonDao():

    def create(self, p):
        p.parent = get_root_key()
        p.put()

    def update(self, p):
        p.put()

    def list(self):
        return p_model.Person.all()

person_dao = PersonDao()
