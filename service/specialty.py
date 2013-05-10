from dao.specialty import specialty_dao
from service import base

class SpecialtyService(base.GeneralService):
    def __init__(self, *args, **kw):
        self.dao = specialty_dao

    def list_species(self):
        specialties = self.dao.list()
        ret = set()
        for s in specialties:
            if s.species:
                ret.add(s.species)
        return ret

    def list_categories(self):
        specialties = self.dao.list()
        ret = set()
        for s in specialties:
            if s.category:
                ret.add(s.category)
        return ret

specialty_service = SpecialtyService()
