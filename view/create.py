import webapp2

from model import person
from service.person import person_service
from service.account import account_service
from view import base

from common import share

class CreatePersonPage(base.BaseSessionHandler):

    @base.login_required
    def get(self):
        self.render_template('c1.html')

    @base.login_required
    def post(self):
        name = self.request.get("name")
        gender = self.request.get("gender")
        birthday = self.request.get("birthday")
        phone = self.request.get("phone")
        email = self.request.get("email")
        p = person.Person(name=name,
                          gender=gender,
                          birthday=birthday,
                          email=email,
                          phone=phone)
        person_service.create(p)
        u = self.session['user']
        acc = account_service.get(u['userid'],
                                  share.acc_key_view2model(u['type']))
        acc.person = p
        account_service.update(acc)
        self.redirect(share.REG_STEP2)

class CreateRolePage(base.BaseSessionHandler):
    @base.login_required
    def get(self):
        role_type = self.request.get('t')
        template_name = None
        if role_type is None or role_type == "":
            template_name = 'c2_role.html'
        elif role_type == share.VIEW_ROLE_ADM:
            template_name = 'c2_adm.html'
        elif role_type == share.VIEW_ROLE_VET:
            template_name = 'c2_vet.html'
        elif role_type == share.VIEW_ROLE_USER:
            self.redirect(share.HOME)
            return
        else:
            self.response.out.write("unsupported role type")
            return
        self.render_template(template_name)
