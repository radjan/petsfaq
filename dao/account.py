from google.appengine.ext import db

from model import account as model

from common import share

GOOGLE = model.ACCOUNT_GOOGLE
ID_PWD = model.ACCOUNT_ID_PWD

get_root_key = share.party_root_key

class AccountDao():
    def exist(self, acc_id, acc_type):
        return self.get(acc_id, acc_type) != None

    def _get_type(self, acc):
        cls = type(acc)
        if cls is model.Google:
            return GOOGLE
        elif cls is model.IDPWD:
            return ID_PWD
        else:
            raise Exception("unknow type")

    def create(self, acc):
        acc.parent = get_root_key()
        acc.put()

    def get(self, acc_id, acc_type):
        if acc_type == GOOGLE:
            q = model.Google.all()
        elif acc_type == ID_PWD:
            q = model.IDPWD.all()
        else:
            # XXX exception type
            raise Exception("Unsupported Account Type")
        q.filter("userid =", acc_id)
        rets = list(q.run())
        print rets
        if rets:
            if len(rets) >= 2:
                raise Exception("user is not unique! " + acc_type + ": " + acc_id)
            return rets[0]
        return None

account_dao = AccountDao()
