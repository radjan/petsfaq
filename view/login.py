import webapp2
from google.appengine.api import users as gusers

from model import account
from service.account import account_service
from common import share

class RegisterPage(webapp2.RequestHandler):
    def get(self):
        params = {
                'user': None,
                'hi': 'hi!!'
            }
        template = share.jinja_env.get_template('register.html')
        self.response.out.write(template.render(params))

class IdPwdRegister(webapp2.RequestHandler):
    def post(delf):
        userid = self.request.get("myEmail")
        pwd1 = self.request.get("myPassword")
        pwd2 = self.request.get("myPassword2")
        if pwd1 != pwd2:
            self.response.out.write("passwords do not match")
            return
        if not accout_service.exist(userid, account.ACCOUNT_ID_PWD):
            account_service.create_idpwd_accout(userid, pwd1)
            # TODO login session
            self.redirect('/faq')
        else:
            self.response.out.write(userid + ", this id already exists")

class GoogleRegister(webapp2.RequestHandler):
    def get(self):
        user = gusers.get_current_user()
        if user:
            if not account_service.exist(user.user_id(), account.ACCOUNT_GOOGLE):
                account_service.create_google_account(user.user_id(), user.email())
            # TODO login session
            self.redirect('/faq')
        else:
            self.redirect(gusers.create_login_url(self.request.uri))
