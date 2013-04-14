import webapp2
from google.appengine.api import users as gusers

from model import account
from service.account import account_service as acc_service
from view import base
from common import share
from thirdparty import hashing_passwords

GOOGLE = 'g'
IDPWD = 'id'

HOME = '/faq'

class LoginPage(base.BaseSessionHandler):
    def get(self):
        if 'user' in self.session:
            self.redirect(HOME)
            return
        params = {}
        template = share.jinja_env.get_template('login.html')
        self.response.out.write(template.render(params))

    def post(self):
        userid = self.request.get("userid")
        password = self.request.get("password")
        acc = acc_service.get(userid, account.ACCOUNT_ID_PWD)
        if acc:
            if hashing_passwords.check_hash(password, acc.password):
                #login
                self.session['user'] = {'name': acc.userid,
                                        'type': IDPWD}
                self.redirect(HOME)
            else:
                self.response.out.write("Wrong password")
        else:
            self.response.out.write("No such user: %s" % userid)

class GoogleLogin(base.BaseSessionHandler):
    def get(self):
        user = gusers.get_current_user()
        if user:
            acc = acc_service.get(user.user_id(), account.ACCOUNT_GOOGLE)
            if acc:
                self.session['user'] = make_google_user(user)
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

class RegisterPage(webapp2.RequestHandler):
    def get(self):
        params = {}
        template = share.jinja_env.get_template('register.html')
        self.response.out.write(template.render(params))

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
        if not acc_service.exist(userid, account.ACCOUNT_ID_PWD):
            acc = account.IDPWD(userid=userid,
                                password=hashing_passwords.make_hash(pwd1))
            acc_service.create(acc)
            #TODO: next step
            self.session['user'] = make_idpwd_user(userid)
            self.redirect(HOME)
        else:
            self.response.out.write(userid + ", this id already exists")

class GoogleRegister(base.BaseSessionHandler):
    def get(self):
        user = gusers.get_current_user()
        if user:
            if not acc_service.exist(user.user_id(),
                                         account.ACCOUNT_GOOGLE):
                acc = account.Google(userid=user.user_id(),
                                     gmail=user.email())
                acc_service.create(acc)
            #TODO: next step
            self.session['user'] = make_google_user(user)
            self.redirect(HOME)
        else:
            self.redirect(gusers.create_login_url(self.request.uri))


def make_idpwd_user(userid):
    return {'name': userid,
            'type': IDPWD}

def make_google_user(user):
    return {'name': user.nickname(),
            'type': GOOGLE}
