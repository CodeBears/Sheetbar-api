import bcrypt
from flask import request

from config import Config
from orm.models import Member
from utils.error_code import ErrorCode
from utils.errors import ValidationError
from utils.jwt_tool import JWTTool
from auth.blacklist import BLACKLIST


class AuthTool:
    @staticmethod
    def _unicode_to_bytes(unicode_string):
        return bytes(unicode_string, 'utf-8')

    @classmethod
    def hash_password(cls, password):
        password = cls._unicode_to_bytes(password)
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt).decode('utf-8')

    @classmethod
    def check_password(cls, password, hashed):
        password = cls._unicode_to_bytes(password)
        hashed = cls._unicode_to_bytes(hashed)
        return bcrypt.checkpw(password, hashed)

    @classmethod
    def get_access_token(cls, **kwargs):
        res = JWTTool.encode_jwt(
            secret_key=Config.JWT_SECRET_KEY,
            exp=Config.ACCESS_TOKEN_EXPIRE_TIME,
            **kwargs
        )
        return res

    @classmethod
    def check_token(cls):
        prefix = 'Bearer'
        header = request.headers.get('Authorization')
        bearer, _, token = header.partition(' ')
        if bearer != prefix:
            raise ValidationError(error_code=ErrorCode.HEADER_FORMAT_ERROR)
        data = JWTTool.decode_jwt(Config.JWT_SECRET_KEY, token=token)
        email = data.get('email')
        if not email:
            raise ValidationError(error_code=ErrorCode.INVALID_TOKEN)
        member = Member.query.filter_by(email=email).first()
        if not member:
            raise ValidationError(error_code=ErrorCode.MEMBER_IS_NOT_EXIST)
        if email in BLACKLIST:
            raise ValidationError(error_code=ErrorCode.INVALID_TOKEN)

        return member

    @classmethod
    def block_token(cls, token):
        try:
            jti = JWTTool.decode_jwt(Config.JWT_SECRET_KEY, token=token)
            BLACKLIST.add(jti["email"])
            print(BLACKLIST)
            return True
        except:
            return False
