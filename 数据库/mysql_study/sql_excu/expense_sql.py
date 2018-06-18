#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'


EXPENSE_STATUS_NORMAL = '1'
EXPENSE_STATUS_DELETE = '0'

INSERT_INTO_EXPENSE_ALL_COLS = 'insert into expense (person_sn, name, dname, money, expense_date) values (%s,%s,%s,%s,%s)'

INSERT_INTO_EXPENSE_SN_NAME = 'insert into expense (person_sn, name) values (%s,%s)'

GET_ALL_EXPENSE = 'select id, person_sn, name, dname, money, expense_date from expense where status=%s' % EXPENSE_STATUS_NORMAL

GET_ALL_EXPENSE_IS_DELETED = 'select id, person_sn, name, dname, money, expense_date from expense where status=%s' % EXPENSE_STATUS_DELETE

GET_ONE_BY_PERSON_SN = 'select person_sn, name, dname, money, expense_date from expense where status=' + EXPENSE_STATUS_DELETE + ' and person_sn=%s'

GET_ONE_BY_DNAME = 'select person_sn, name, dname, money, expense_date from expense where dname=%s'

DELETE_EXPENSE_BY_ID = 'update expense set status = ' + EXPENSE_STATUS_DELETE + ' where id=%s'
