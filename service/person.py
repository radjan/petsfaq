from model import role

from dao.person import person_dao
from dao.specialty import specialty_dao
from service import base

from common import serviceFactory

class PersonService(base.GeneralService):
    def __init__(self):
        self.dao = person_dao

    def search_vets(self, params):
        people = self.dao.search(params)
        ret = []
        for p in people:
            vet_role = self._extract_vet(p)
            if vet_role:
                #XXX not model properties
                p.vet = vet_role
                ret.append(p)
        return ret

    def _extract_vet(self, person):
        for r in person.roles:
            if isinstance(r, role.Vet):
                return r
        return None

    def delete(self, p):
        if type(p) == int:
            p = self.get(p)
        role_service = serviceFactory.get_service(serviceFactory.ROLE)
        for r in p.roles:
            role_service.delete(r)
        for img in p.avatars:
            #XXX image dao, delete blog
            img.delete()
        person_dao.delete(p)

person_service = PersonService()
