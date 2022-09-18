from functools import wraps

from flask import request
from schema import Schema, Regex, And


class DataValidator:
    @staticmethod
    def validate(schema=None):
        def real_decorator(method, **kwargs):
            @wraps(method)
            def wrapper(*args, **kwargs):
                if request.method in {'GET', 'DELETE'}:
                    payload = request.args
                    payload = dict(payload)
                else:
                    payload = request.get_json(force=True)
                if schema:
                    schema.validate(payload)
                return method(*args, **kwargs, payload=payload)

            return wrapper

        return real_decorator


class DataSchema:
    _EMAIL_PATTERN = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    _USERNAME_PATTERN = r"[A-Za-z\d]{8,20}$"  # 8-20
    _PASSWORD_PATTERN = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$"
    # 8-20 英數混合

    SIGN_IN = Schema({
        'email': Regex(_EMAIL_PATTERN),
        'password': str,
    }, ignore_extra_keys=True)

    SIGN_UP = Schema({
        'email': And(str, Regex(_EMAIL_PATTERN)),
        'username': And(str, Regex(_USERNAME_PATTERN)),
        'password': And(str, Regex(_PASSWORD_PATTERN)),
    }, ignore_extra_keys=True)
