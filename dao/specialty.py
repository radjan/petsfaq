from dao import base
from model import specialty as specialty_model

from common import share

get_root_key = share.party_root_key

class SpecialtyDao(base.GeneralDao):
    def __init__(self, *args, **kw):
        self.model_cls = specialty_model.Specialty
        self.get_root_key = share.party_root_key
        self.kind = 'Specialty'

specialty_dao = SpecialtyDao()
