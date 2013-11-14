from model import account as account_model

from dao.account import account_dao as acc_dao
from service import base

from common import share

GOOGLE = share.ACCOUNT_GOOGLE
ID_PWD = share.ACCOUNT_ID_PWD

class AccountService(base.GeneralService):
    def __init__(self):
        self.dao = acc_dao

    def exist(self, acc_id, acc_type):
        return acc_dao.exist(acc_id, acc_type)

    def get_by_userid(self, acc_id, acc_type):
        return acc_dao.get_by_userid(acc_id, acc_type)

account_service = AccountService()
