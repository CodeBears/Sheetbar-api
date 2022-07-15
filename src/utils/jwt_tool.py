from datetime import timedelta, datetime, timezone

import jwt

from utils.error_code import ErrorCode
from utils.errors import ValidationError


class JWTTool:

    @staticmethod
    def encode_jwt(secret_key, exp=0, **kwargs):
        exp = timedelta(seconds=exp)
        payload = {
            'exp': datetime.now(tz=timezone.utc) + exp,
            **kwargs
        }
        return jwt.encode(payload=payload, key=secret_key, algorithm="HS256")

    @staticmethod
    def decode_jwt(secret_key, token):
        try:
            return jwt.decode(jwt=token, key=secret_key, algorithms=['HS256'])
        except jwt.DecodeError:
            raise ValidationError(error_code=ErrorCode.INVALID_TOKEN)
        except jwt.ExpiredSignatureError:
            raise ValidationError(error_code=ErrorCode.EXPIRED_TOKEN)
