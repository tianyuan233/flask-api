#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/09/26
@file: scope.py

"""


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    # 运算符重载
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        # allow_api去重
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    allow_module = ['v1.user','v1.gift']
    allow_api = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']


class UserScope(Scope):
    allow_module = ['v1.gift']
    allow_api = ['v1.user+get_user',
                 'v1.user+delete_user']


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
