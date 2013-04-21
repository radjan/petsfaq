import webapp2
from google.appengine.api import users as gusers

from model import account
from service.account import account_service as acc_service
from view import base
from common import share, util
from thirdparty import hashing_passwords

HOME = share.HOME
REG_STEP1 = share.REG_STEP1

class LoginPage(base.BaseSessionHandler):
    def get(self):
        if 'user' in self.session:
            self.redirect(HOME)
            return
        self.render_template('login.html')

    def post(self):
        userid = self.request.get("userid")
        password = self.request.get("password")
        acc = acc_service.get(userid, share.ACCOUNT_ID_PWD)
        if acc:
            if hashing_passwords.check_hash(password, acc.password):
                #login
                self.session['user'] = util.get_user(acc)
                self.redirect(HOME)
            else:
                self.response.out.write("Wrong password")
        else:
            self.response.out.write("No such user: %s" % userid)

class GoogleLogin(base.BaseSessionHandler):
    def get(self):
        user = gusers.get_current_user()
        if user:
            acc = acc_service.get(user.user_id(), share.ACCOUNT_GOOGLE)
            if acc:
                self.session['user'] = util.get_user(acc)
                self.redirect(HOME)
            else:
                self.redirect('register_google')
        else:
            self.redirect(gusers.create_login_url(self.request.uri))


class LogoutPage(base.BaseSessionHandler):
    def get(self):
        user = self.session['user'] if 'user' in self.session else None
        if user and user['type'] == 'g':
            self.redirect(gusers.create_logout_url(HOME))
        else:
            self.redirect(HOME)
        for k in self.session.keys():
            del self.session[k]

class RegisterPage(base.BaseSessionHandler):
    def get(self):
        self.render_template('register.html')

class IdPwdRegister(base.BaseSessionHandler):
    def post(self):
        userid = self.request.get("myEmail")
        pwd1 = self.request.get("myPassword")
        pwd2 = self.request.get("myPassword2")
        if not userid or not pwd1:
            self.response.out.write("empty field")
            return
        if pwd1 != pwd2:
            self.response.out.write("passwords do not match")
            return
        if not acc_service.exist(userid, share.ACCOUNT_ID_PWD):
            acc = account.IDPWD(userid=userid,
                                password=hashing_passwords.make_hash(pwd1))
            acc_service.create(acc)
            self.session['user'] = util.temp_idpwd_user(userid)
            self.redirect(REG_STEP1)
        else:
            self.response.out.write(userid + ", this id already exists")

class GoogleRegister(base.BaseSessionHandler):
    def get(self):
        user = gusers.get_current_user()
        if user:
            if not acc_service.exist(user.user_id(),
                                         share.ACCOUNT_GOOGLE):
                acc = account.Google(userid=user.user_id(),
                                     gmail=user.email())
                acc_service.create(acc)
            self.session['user'] = util.temp_google_user(user)
            self.redirect(REG_STEP1)
        else:
            self.redirect(gusers.create_login_url(self.request.uri))


