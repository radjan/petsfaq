# -*- coding: utf-8 -*-
from dao.specialty import specialty_dao
from service import base

class SpecialtyService(base.GeneralService):
    def __init__(self, *args, **kw):
        self.dao = specialty_dao

    def get_by_value(self, species='', category=''):
        return self.dao.get_by_value(species, category)

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

    def add_specialties(self, specialties, vet=None, hospital=None):
        for s in specialties:
            self.add_specialty(s, hospital=hospital, vet=vet)

    def add_specialty(self, specialty, note=None, hospital=None, vet=None):
        return specialty_dao.link_to_entity(specialty,
                                            note=note,
                                            vet=vet,
                                            hospital=hospital)

specialty_service = SpecialtyService()
