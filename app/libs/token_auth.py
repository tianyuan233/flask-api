#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/09/26
@file: token_auth.py

"""
from flask import current_app, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

# //TODO HTTPBasicAuth
from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    # token
    pass



def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # request 视图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)