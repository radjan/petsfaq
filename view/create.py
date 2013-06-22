# -*- coding: utf-8 -*-
import webapp2

from model import person, role, hospital, specialty
from service.person import person_service
from service.account import account_service
from service.role import role_service
from service.hospital import hospital_service
from service.specialty import specialty_service
from view import base

from common import share, util

class CreatePersonPage(base.BaseSessionHandler):

    @base.login_required
    def get(self):
        self.render_template('reg_step1.html')

    @base.login_required
    def post(self):
        vet = self.request.get("isVet")
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
        acc = account_service.get_by_userid(u['userid'],
                                            share.acc_key_view2model(u['type']))
        acc.person = p
        account_service.update(acc)
        self.session['user'] = util.get_user(acc)
        next_page = share.REG_STEP2
        if vet == 'N':
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
            # create an empty role, so we know he/she is a vet
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
              'education': _gather_list(self.request, 'edu_'),
              'experience': _gather_list(self.request, 'exp_')}
        util.maybe_add(kw, 'description', self.request.get('intro'))
        util.maybe_add(kw, 'specialty', self.request.get('specialty'))
        specialties = _get_specialties(self.request)
        v = None
        for r in person.roles:
            if isinstance(r, role.Vet):
                v = r
                break

        if v is None:
            v = role.Vet(**kw)
            for s in specialties:
                k = s.key()
                if k not in v.specialties:
                    v.specialties.append(k)
            role_service.create(v)
        else:
            for key, value in kw.items():
                v.__setattr__(key, value)
            for s in specialties:
                k = s.key()
                if k not in v.specialties:
                    v.specialties.append(k)
            role_service.update(v)
        self.redirect(share.REG_STEP3)


class WorksForPage(base.BaseSessionHandler):
    @base.login_required
    def get(self):
        self.render_template('worksfor.html')

class CreateHospitalPage(base.BaseSessionHandler):
    @base.login_required
    def post(self):
        person = util.get_person(self.session)
        kw = {}
        primary_keys = (('name', 'name'),
                        ('description', 'description'),
                        ('zipcode', 'zipcode'),
                        ('county', 'county'),
                        ('area', 'area'),
                        ('address', 'address'),
                        ('phone', 'phone'),
                       )
        for view_key, model_key in primary_keys:
            kw[model_key] = self.request.get(view_key)
        kw['emergency'] = self.request.get('er') != ""

        opt_keys = (('working_hour', 'working_hour'),
                    ('er_phone', 'emergency_phone'),
                    ('er_hour', 'emergency_hour'),
                   )
        for view_key, model_key in opt_keys:
            util.maybe_add(kw, model_key, self.request.get(view_key))

        h = hospital.Hospital(**kw)

        specialties = _get_specialties(self.request)
        for s in specialties:
            h.specialties.append(s.key())

        hospital_service.create(h)

        for r in person.roles:
            if type(r) is role.Vet:
                r.hospital = h
                role_service.update(r)
        adm = role.Admin(person=person, hospital=h)
        role_service.create(adm)
        self.redirect(share.HOME)

def _gather_list(request, k, tolerance=2):
    miss = 0
    i = 1
    ret = []
    while miss < tolerance:
        curr_key = k + str(i)
        if curr_key in request.POST:
            v = request.get(curr_key)
            miss = 0
            ret.append(v)
            print curr_key, ':', len(v)
        else:
            miss += 1
        i += 1
    return ret

def _get_specialties(request):
    species = _gather_list(request, 'species_')
    categories = _gather_list(request, 'category_')
    specialties = []
    for i in range(len(species)):
        spe = species[i]
        cat = categories[i]
        if not spe or not cat:
            continue
        s = specialty_service.get_by_value(species=spe,
                                           category=cat)
        if s:
            specialties.append(s)
        else:
            s = specialty.Specialty(species=spe,
                                    category=cat)
            specialty_service.create(s)
            specialties.append(s)
    return specialties
