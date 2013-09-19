from model import person as p_model
from dao import base

from common import share


class PersonDao(base.GeneralDao):
    def __init__(self):
        self.model_cls = p_model.Person
        self.get_root_key = share.party_root_key

person_dao = PersonDao()
