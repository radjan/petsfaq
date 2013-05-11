# -*- coding: utf-8 -*-
from dao.specialty import specialty_dao
from service import base

class SpecialtyService(base.GeneralService):
    def __init__(self, *args, **kw):
        self.dao = specialty_dao

    def get_by_value(self, species='', category=''):
        ss = self.dao.search({'species': species,
                              'category': category})
        if ss.count() > 0:
            return ss.fetch(1)[0]
        else:
            return None

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
