from model import role
from dao.hospital import hospital_dao as h_dao
from dao.role import role_dao
from dao.specialty import specialty_dao
from service import base

class HospitalService(base.GeneralService):
    def __init__(self):
        self.dao = h_dao

    def delete(self, h):
        if type(h) in (int, long):
            h = self.get(h)
        for rel in h.specialties:
            specialty_dao.remove_link(rel)

        for r in h.vets:
            if isinstance(r, role.Vet):
                # don't delete vet
                r.hospital = None
                role_dao.update(r)

        for r in h.employees:
            if isinstance(r, role.Employee):
                # delete employee roles
                role_dao.delete(r)

        return h_dao.delete(h)


hospital_service = HospitalService()
