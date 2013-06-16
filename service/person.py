from model import role

from dao.person import person_dao
from service import base

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

person_service = PersonService()
