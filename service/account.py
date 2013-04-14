from model import account as account_model

from dao.account import account_dao as dao

GOOGLE = account_model.ACCOUNT_GOOGLE
ID_PWD = account_model.ACCOUNT_ID_PWD

class AccountService():
    def exist(self, acc_id, acc_type):
        return dao.exist(acc_id, acc_type)

    def create(self, acc):
        return dao.create(acc)

    def get(self, acc_id, acc_type):
        return dao.get(acc_id, acc_type)

account_service = AccountService()
