import webapp2

from model import person, role
from service.person import person_service
from service.account import account_service
from service.role import role_service
from view import base

from common import share, util

class CreatePersonPage(base.BaseSessionHandler):

    @base.login_required
    def get(self):
        self.render_template('reg_step1.html')

    @base.login_required
    def post(self):
        vet = self.request.get("vet")
        name = self.request.get("name")
        gender = self.request.get("gender")
        birthday = self.request.get("birthday")
        phone = self.request.get("phone")
        email = self.request.get("email")
        kw = {'name': name,
              'gender': gender,}
        util.maybe_add(kw, 'birthday', birthday)
        util.maybe_add(kw, 'email', email)
        util.maybe_add(kw, 'phone', phone)
        p = person.Person(**kw)
        person_service.create(p)
        u = self.session['user']
        acc = account_service.get(u['userid'],
                                  share.acc_key_view2model(u['type']))
        acc.person = p
        account_service.update(acc)
        self.session['user'] = util.get_user(acc)
        next_page = share.REG_STEP2
        if not vet:
            next_page = share.REG_STEP3
        self.redirect(next_page)

class VetDetailPage(base.BaseSessionHandler):
    @base.login_required
    def get(self):
        skip = self.request.get('a')
        if skip == 'skip':
            person = util.get_person(self.session)
            create_role = True
            for r in person.roles:
                if isinstance(r, role.Vet):
                    create_role = False
                    break
            if create_role:
                v = role.Vet(person=person)
                role_service.create(v)
            self.redirect(share.REG_STEP3)
            return
        self.render_template('vet_detail.html')

    @base.login_required
    def post(self):
        person = util.get_person(self.session)
        kw = {'person': person,
              'education': self._gather_list('edu_'),
              'experience': self._gather_list('exp_')}
        util.maybe_add(kw, 'description', self.request.get('description'))
        util.maybe_add(kw, 'specialty', self.request.get('specialty'))
        create_role = True
        for r in person.roles:
            if isinstance(r, role.Vet):
                create_role = False
                v = r
                break
        if create_role:
            v = role.Vet(**kw)
            role_service.create(v)
        else:
            print (dir(v))
            for key, value in kw.items():
                v.__setattr__(key, value)
            role_service.update(v)
        self.redirect(share.REG_STEP3)

    def _gather_list(self, k, tolerance=2):
        miss = 0
        i = 1
        ret = []
        while miss < tolerance:
            v = self.request.get(k + str(i))
            if v:
                miss = 0
                ret.append(v)
            else:
                miss += 1
            i += 1
        return ret

class WorksForPage(base.BaseSessionHandler):
    @base.login_required
    def get(self):
        self.render_template('worksfor.html')

class CreateHospitalPage(base.BaseSessionHandler):
    @base.login_required
    def post(self):
        userid = util.get_userid(self.session)

