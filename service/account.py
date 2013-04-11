from model import account as account_model

from dao.account import account_dao as dao

GOOGLE = account_model.ACCOUNT_GOOGLE
ID_PWD = account_model.ACCOUNT_ID_PWD

class AccountService():
    def exist(self, userid, user_type):
        print 'AccountService.exist', userid, user_type
        return dao.exist(userid, user_type)

    def create_google_account(self, userid, gmail):
        return dao.create_google_account(userid, gmail)

account_service = AccountService()
