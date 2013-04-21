from model import role as role_model
from common import share

get_root_key = share.party_root_key

class RoleDao():
    def create(self, r):
        r.parent = get_root_key()
        r.put()

    def update(self, r):
        r.put()

    def list(self):
        return role_model.Role.all()

role_dao = RoleDao()
