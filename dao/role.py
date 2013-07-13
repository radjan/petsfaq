from model import role as role_model
from dao import base

from common import share


class RoleDao(base.GeneralDao):
    def __init__(self):
        self.model_cls = role_model.Role
        self.get_root_key = share.party_root_key

role_dao = RoleDao()
