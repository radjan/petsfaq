from google.appengine.ext import db

from model import hospital as h_model
from dao import base
from common import share

get_root_key = share.org_root_key
KIND = 'Hospital'

class HospitalDao(base.GeneralDao):
    def __init__(self):
        self.model_cls = h_model.Hospital

    def get(slef, id):
        return db.get(db.Key.from_path(KIND, int(id)))

    def create(self, h):
        h.parent = get_root_key()
        h.put()

    def update(self, h):
        h.put()

    def list(self):
        return h_model.Hospital.all()

hospital_dao = HospitalDao()
