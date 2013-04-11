from google.appengine.ext import db

from model import account as model

GOOGLE = model.ACCOUNT_GOOGLE
ID_PWD = model.ACCOUNT_ID_PWD

class AccountDao():
    def exist(self, userid, user_type):
        print 'AccountDao.exist', userid, user_type
        if user_type == GOOGLE:
            q = model.Google.all()
        elif user_type == ID_PWD:
            pass
        else:
            # XXX exception type
            raise Exception("Unsupported Account Type")
        q.filter("userid =", userid)
        l = len(list(q.run()))
        if l >= 2:
            raise Exception("user is not unique! " + user_type + ": " + userid)
        return l == 1

    def create_google_account(self, userid, gmail):
        if self.exist(userid, GOOGLE):
            return
        acc = model.Google(userid=userid,
                           gmail=gmail,
                           parent=model.get_root_key())
        acc.put()

account_dao = AccountDao()
