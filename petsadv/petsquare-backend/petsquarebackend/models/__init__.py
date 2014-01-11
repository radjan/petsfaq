#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

from zope.sqlalchemy import ZopeTransactionExtension as ZTE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
        scoped_session,
        sessionmaker,
      )

from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy.orm.collections import InstrumentedList
import transaction

import datetime
import json

import inspect
import traceback

DBSession = scoped_session(sessionmaker(expire_on_commit=False,
                                        extension=ZTE(keep_session=False)))


def ModelMethod(func):
    def mdl_wrapped(cls, *args, **kwargs):
#        with transaction.manager:
#            try:
#                rtn = func(cls, *args, **kwargs)
#            except Exception, e:
#                rtn = cls.model_exception_rtn(
#                        exp=e,
#                        ins_stk=inspect.stack()[0][3],
#                        tbk=traceback.format_exc())
#        return rtn
        try:
            rtn = func(cls, *args, **kwargs)
        except Exception, e:
            rtn = cls.model_exception_rtn(
                    exp=e,
                    ins_stk=inspect.stack()[0][3],
                    tbk=traceback.format_exc())
        return rtn
    return mdl_wrapped


class ModelMixin(object):
    __public__ = None

    @classmethod
    def get_by_id(cls, id, session=DBSession, columns=None, lock_mode=None):
        if hasattr(cls, 'id'):
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            query = query.filter(cls.id == id)
            if scalar:
                return query.scalar()
            return query.first()
        return None

    @classmethod
    def get_by_attr(cls, attr, value, session=DBSession, columns=None, lock_mode=None):
        if hasattr(cls, attr):
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            query = query.filter(cls.__dict__.get(attr) == value)
            if scalar:
                return query.scalar()
            return query.first()
        return None

    @classmethod
    def get_by_attrs(cls, attrs, session=DBSession, columns=None, lock_mode=None):
        """
        attrs:  [(k,v),(k,v), ... ]

        """
        if len([x for x in attrs if not hasattr(cls, x[0])]) == 0:
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)

            for x in attrs:
                query = query.filter(cls.__dict__.get(x[0]) == x[1])
            if scalar:
                return (True, query.scalar())
            return (True, query.all())
        return (True, None)

    
    @classmethod
    def get_all(cls, filattr=None, session=DBSession, columns=None, offset=None, limit=None, order_by=None, lock_mode=None, DESC=False):
        if columns:
            if isinstance(columns, (tuple, list)):
                query = session.query(*columns)
                query = query.select_from(cls)
            else:
                query = session.query(columns)
                if isinstance(columns, str):
                    query = query.select_from(cls)
        else:
            query = session.query(cls)
        if filattr:
            query = query.filter(cls.__dict__.get(filattr[0]) == filattr[1])
        #add desc
        if order_by is not None:
            if isinstance(order_by, (tuple, list)):
                if DESC:
                    query = query.order_by(desc(*order_by))
                else:
                    query = query.order_by(*order_by)
            else:
                if DESC:
                    query = query.order_by(desc(order_by))
                else:
                    query = query.order_by(order_by)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        if lock_mode:
            query = query.with_lockmode(lock_mode)
        return query.all()

    @classmethod
    def count_all(cls, filattr=None,  session=DBSession, lock_mode=None):
        query = session.query(func.count('*')).select_from(cls)
        if filattr:
            query = query.filter(cls.__dict__.get(filattr[0]) == filattr[1])
        if lock_mode:
            query = query.with_lockmode(lock_mode)
        return query.scalar()

    @classmethod
    def exist(cls, id, session=DBSession, lock_mode=None):
        if hasattr(cls, 'id'):
            query = session.query(func.count('*')).select_from(cls).filter(cls.id == id)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            return query.scalar() > 0
        return False

    @classmethod
    def set_attr(cls, id, attr, value, session=DBSession):
        if hasattr(cls, 'id'):
            session.query(cls).filter(cls.id == id).update({
                attr: value
                })
            session.commit()

    @classmethod
    def set_attrs(cls, id, attrs, session=DBSession):
        if hasattr(cls, 'id'):
            session.query(cls).filter(cls.id == id).update(attrs)
            session.commit()

    @classmethod
    def union_by_ids(cls, idlist, session=DBSession):
        if not hasattr(cls, 'id'):
            return None
        union_rtn = None
        for id in idlist:
            scalar = False
            query = session.query(cls)
            query = query.filter(cls.id == id)
            if scalar:
                # FIXME scalar is never True
                #return query.scalar()
                if union_rtn:
                    union_rtn = union_rtn.union_rtn(query.scalar())
                else:
                    union_rtn = query.scalar()
            #return query.first()
            elif union_rtn:
                union_rtn = union_rtn.union_rtn(query.first())
            else:
                union_rtn = query.first()
        return union_rtn

    @classmethod
    def delete_by_id(cls, id, session=DBSession):
        try:
            model = cls.get_by_attr(attr='id', value=id)
            DBSession.delete(model)
            #DBSession.flush()
            #do not use commit() method manually
            #DBSession.commit()
            rtn = (True, None)
        except Exception, e:
            import traceback
            err_tbk = traceback.format_exc()
            err_exp = str(e)
            #err_msg = err_exp + ', ' + err_tbk
            err_msg = err_exp
            log.debug(err_tbk)
            rtn = (False, err_msg)
        return rtn

    @classmethod
    def model_exception_rtn(cls, exp, ins_stk, tbk):
        rtn = []
        err_info = (cls.__tablename__, ins_stk, tbk)
        log.debug('%s:%s, traceback:\n %s' % err_info)
        rtn.append(False)
        rtn.append({'status':'fail', 'msg':'model error on %s' % ins_stk}) 
        return rtn

    def __json__(self, request, exclude=(), extra=(), exclude_fk=True, max_depth=1):
        log.debug('type: %s, id: %s' % (type(self), self.id))
        obj_dict = self.__dict__
        obj_dict = dict((key, obj_dict[key]) for key in obj_dict if not key.startswith("_"))
        foreignkeys = list(self.__table__.foreign_keys)
        foreignkeys = dict([(x.parent.name, x.column.table.name) for x in foreignkeys])
        #foreignkeys = {fk_name: f_table, ...}

        if exclude_fk:
            exclude = exclude + tuple(foreignkeys.keys())
            #exclude = list(exclude) + foreignkeys.keys()

        public = self.__public__ + extra if self.__public__ else extra
        rtn_pub = [x for x in public if x not in exclude]

        rtn_dict = {}
        for k in rtn_pub:
            if k in exclude:
                continue
            value = self.__getattribute__(k)
            if max_depth == 0 and isinstance(value, (ModelMixin, InstrumentedList)) :
                continue
            if isinstance(value, ModelMixin):
                value = value.__json__(request, exclude, extra, exclude_fk, max_depth-1)
            if isinstance(value, (InstrumentedList, list)):
                value_list = []
                for m in value:
                    if isinstance(m, ModelMixin):
                        m = m.__json__(request, exclude, extra, exclude_fk, max_depth-1)
                    value_list.append(m)
                value = value_list
            elif isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d, %H:%M:%S")
            rtn_dict[k] = value
        return rtn_dict

    #def _retrieve_model(self, request, exclude, extra, exclude_fk, max_depth):
    #    if isinstance(value, ModelMixin):
    #        value = self.__getattribute__(k).__json__(request, exclude, extra, exclude_fk, max_depth-1)

Base = declarative_base(cls=ModelMixin)

def main():
    pass

if __name__ == '__main__':
    main()
