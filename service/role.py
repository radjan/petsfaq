from dao.role import role_dao
from service import base

class RoleService(base.GeneralService):
    def __init__(self):
        self.dao = role_dao

role_service = RoleService()
