from sqlalchemy import or_
from app import db
from orm.models import Member
from utils.auth_tool import AuthTool
from utils.error_code import ErrorCode
from utils.errors import ValidationError
from utils.toolkit import Toolkit
from auth.blacklist import BLACKLIST


class MemberHandler:
    @staticmethod
    def sign_in(email, password):
        member = Member.query.filter(Member.email == email).first()
        if not member or not AuthTool.check_password(password, hashed=member.password):
            raise ValidationError(
                error_code=ErrorCode.USERNAME_OR_PASSWORD_WRONG)
        res = {
            'email': member.email,
            'username': member.username,
            'is_valid': member.is_valid,
        }
        res['access_token'] = AuthTool.get_access_token(**res)

        if member.email in BLACKLIST:
            BLACKLIST.remove(member.email)
        return res

    @staticmethod
    def sign_up(email, username, password):
        member = Member.query.filter(
            or_(
                Member.email == email,
                Member.username == username
            )
        ).first()
        if member:
            raise ValidationError(error_code=ErrorCode.MEMBER_IS_EXIST)
        member = Member(
            email=email,
            username=username,
            password=AuthTool.hash_password(password=password)
        )
        db.session.add(member)
        Toolkit.commit()
        res = {
            'email': member.email,
            'username': member.username,
            'is_valid': member.is_valid,
        }
        res['access_token'] = AuthTool.get_access_token(**res)
        return res

    @staticmethod
    def sign_out(token):
        if AuthTool.block_token(token):
            return {
                "message": "成功登出"
            }
        return {
            "message": "伺服器出現異常 無法成功登出"
        }
