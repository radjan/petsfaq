
from model import hospital as h_model
from common import share

get_root_key = share.org_root_key

class HospitalDao:
    def create(self, h):
        h.parent = get_root_key()
        h.put()

    def update(self, h):
        h.put()

    def list(self):
        return h_model.Hospital.all()

hospital_dao = HospitalDao()
