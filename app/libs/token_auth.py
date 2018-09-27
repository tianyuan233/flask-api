#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/09/26
@file: token_auth.py

"""
from collections import namedtuple

from flask import current_app, request, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    # token
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    # 是否合法验证
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    # 是否过期验证
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']

    # scope = data['scope']
    # request 视图函数
    # allow = is_in_scope(scope, request.endpoint)
    # if not allow:
    #     raise Forbidden()
    return User(uid, ac_type, '')
