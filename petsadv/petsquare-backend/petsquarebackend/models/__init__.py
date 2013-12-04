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

import datetime
import json

DBSession = scoped_session(sessionmaker(extension=ZTE()))

class ModelMixin(object):
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
    def get_all(cls, filattr=None, session=DBSession, columns=None, offset=None, limit=None, order_by=None, lock_mode  =None, DESC=False):
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
        union_rtn = None
        for id in idlist:
            if hasattr(cls, 'id'):
                scalar = False
                query = session.query(cls)
                query = query.filter(cls.id == id)
                if scalar:
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
            return None
        return union_rtn

    def __json__(self, request):
        obj_dict = self.__dict__
        obj_dict = dict((key, obj_dict[key]) for key in obj_dict if not key.startswith("_"))
        rtn_dict = {}
        for k,value in obj_dict.items():
            #log.debug('key name: %s, value: %s, value type: %s' % (k, value, type(value)))
            if isinstance(value, datetime.datetime):
                value = [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
            rtn_dict[k] = value
        return rtn_dict

Base = declarative_base(cls=ModelMixin)

def main():
    pass

if __name__ == '__main__':
    main()