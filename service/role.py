from dao.role import role_dao

class RoleService:
    def create(self, r):
        return role_dao.create(r)

    def update(self, r):
        return role_dao.update(r)

    def list(self):
        return role_dao.list()

role_service = RoleService()
