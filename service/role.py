from model import role
from dao.role import role_dao
from dao.specialty import specialty_dao
from service import base

class RoleService(base.GeneralService):
    def __init__(self):
        self.dao = role_dao

    def delete(self, r):
        if isinstance(r, role.Vet):
            for rel in p.specialties:
                specialty_dao.remove_link(rel)
        return role_dao.delete(r)

role_service = RoleService()
