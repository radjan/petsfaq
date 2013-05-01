from model import person as p_model
from dao import base

from common import share

get_root_key = share.party_root_key

class PersonDao(base.GeneralDao):
    def __init__(self):
        self.model_cls = p_model.Person

    def create(self, p):
        p.parent = get_root_key()
        p.put()

    def update(self, p):
        p.put()

    def list(self):
        return p_model.Person.all()

person_dao = PersonDao()
