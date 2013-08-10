# -*- coding: utf-8 -*-
from dao.specialty import specialty_dao
from model import specialty as model
from service import base

class SpecialtyService(base.GeneralService):
    def __init__(self, *args, **kw):
        self.dao = specialty_dao

    def create(self, specialty):
        s = self.get_by_value(specialty.species, specialty.category)
        if not s:
            return self.dao.create(specialty)
        return s.get_id()

    def delete(self, s):
        specialty_dao.remove_links(s)
        return specialty_dao.delete(s)

    def get_by_value(self, species='', category=''):
        return self.dao.get_by_value(species, category)

    def ensure_exist(self, species, category=u'一般'):
        s = self.get_by_value(species, category)
        if not s:
            s = model.Specialty(species=species, category=category)
            s.put()
        return s

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

    def add_specialty(self, specialty, note='', hospital=None, vet=None):
        return specialty_dao.link_to_entity(specialty,
                                            note=note,
                                            vet=vet,
                                            hospital=hospital)

    def delete_specialties(self, specialties, hospital=None, vet=None):
        for s in specialties:
            self.delete_specialty(s, hospital=hospital, vet=vet)

    def delete_specialty(self, specialty, hospital=None, vet=None):
        return specialty_dao.unlink(specialty, hospital=hospital, vet=vet)

specialty_service = SpecialtyService()
