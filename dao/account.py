from google.appengine.ext import db

from model import account as acc_model

from common import share

GOOGLE = acc_model.ACCOUNT_GOOGLE
ID_PWD = acc_model.ACCOUNT_ID_PWD

get_root_key = share.party_root_key

class AccountDao():
    def exist(self, acc_id, acc_type):
        return self.get(acc_id, acc_type) != None

    def _get_type(self, acc):
        cls = type(acc)
        if cls is acc_model.Google:
            return GOOGLE
        elif cls is acc_model.IDPWD:
            return ID_PWD
        else:
            raise Exception("unknow type")

    def create(self, acc):
        acc.parent = get_root_key()
        acc.put()

    def get(self, acc_id, acc_type):
        if acc_type == GOOGLE:
            q = acc_model.Google.all()
        elif acc_type == ID_PWD:
            q = acc_model.IDPWD.all()
        else:
            # XXX exception type
            raise Exception("Unsupported Account Type")
        q.filter("userid =", acc_id)
        rets = list(q.run())
        if rets:
            if len(rets) >= 2:
                raise Exception("user is not unique! " +
                                    acc_type + ": " + acc_id)
            return rets[0]
        return None

    def update(self, acc):
        acc.put()

    def list(self):
        return acc_model.Account.all()

account_dao = AccountDao()
