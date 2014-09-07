#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 07, 2014 '
__author__= 'samuel'


def groupfinder(user_id, request):
    if user_id == None:
        return []
    else:
        from petsquarebackend.models.accounts import User_TB
        from petsquarebackend.models import DBSession
        try:
            model = DBSession.query(User_TB)\
                    .filter(User_TB.id == user_id).scalar()
            if model != None:
                return ['group:%s' % user_id]
            else:
                return []
        except Exception, e:
            err_msg = 'groupfinder callback fail: %s' % json.dumps(
                        [str(e), inspect.stack()[0][3],
                         traceback.format_exc()], 
                        indent=1)
            log.error(err_msg)
            return []


def get_user(request):
    from petsquarebackend.models.accounts import User_TB
    from petsquarebackend.models import DBSession
    user_id = request.authenticated_userid

    try:
        model = DBSession.query(User_TB).filter(User_TB.id == user_id).scalar()
        return None if model == None else model
    except Exception, e:
        err_msg = 'get user obj fail: %s' % json.dumps(
                    [str(e), inspect.stack()[0][3],
                     traceback.format_exc()], 
                    indent=1)
        log.error(err_msg)
        return None


def main():
    pass

if __name__ == '__main__':
    main()
