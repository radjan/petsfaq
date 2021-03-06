from dao import base
from model import specialty as specialty_model

from common import share

get_root_key = share.party_root_key

class SpecialtyDao(base.GeneralDao):
    def __init__(self, *args, **kw):
        self.model_cls = specialty_model.Specialty
        self.get_root_key = share.party_root_key
        self.kind = 'Specialty'

    def get_by_value(self, species='', category=''):
        ss = self.search({'species': species,
                          'category': category})
        if ss.count() > 0:
            return ss.fetch(1)[0]
        else:
            return None

    def link_to_entity(self, specialty, note=None, vet=None, hospital=None):
        if vet is None and hospital is None:
            return None
        model = hospital if hospital else vet
        rels = model.specialties
        for r in rels:
            if specialty.get_id() == r.specialty.get_id():
                return r
        rel = specialty_model.EntitySpecialtyRel(specialty=specialty,
                                                 note=note)
        if vet:
            rel.vet = vet
        elif hospital:
            rel.hospital = hospital
        rel.put()
        return rel

    def unlink(self, specialty, hospital=None, vet=None):
        if vet is None and hospital is None:
            return None
        model = hospital if hospital else vet
        rels = model.specialties
        for r in rels:
            if r.specialty.get_id() == specialty.get_id():
                r.delete()

    def remove_link(self, rel):
        rel.delete()

    def remove_links(self, specialty):
        for rel in specialty.relations:
            self.remove_link(rel)

specialty_dao = SpecialtyDao()
