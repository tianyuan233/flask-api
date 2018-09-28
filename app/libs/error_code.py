from app.libs.error import APIException

#通过自定义的APIException 将各类情况返回为同一种格式的json
class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'

class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'

class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001

class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0

class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = '服务器错误'
    error_code = 999
