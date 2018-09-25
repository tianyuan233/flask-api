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


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = '服务器错误'
    error_code = 999
