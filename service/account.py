from model import account as account_model

from dao.account import account_dao as dao
from common import share

GOOGLE = share.ACCOUNT_GOOGLE
ID_PWD = share.ACCOUNT_ID_PWD

class AccountService():
    def list(self):
        return dao.list()

    def exist(self, acc_id, acc_type):
        return dao.exist(acc_id, acc_type)

    def create(self, acc):
        return dao.create(acc)

    def update(self, acc):
        return dao.update(acc)

    def get(self, acc_id, acc_type):
        return dao.get(acc_id, acc_type)

account_service = AccountService()
