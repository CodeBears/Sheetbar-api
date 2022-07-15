from sqlalchemy import func, text

from app import db
from config import Config

BIND_KEY = Config.DB_NAME


class Member(db.Model):
    """
    會員
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False, comment='信箱')
    username = db.Column(db.String(100), unique=True, nullable=False, comment='用戶名')
    is_valid = db.Column(db.Boolean, nullable=False, server_default='0', comment='信箱')
    password = db.Column(db.String(100), nullable=False, comment='密碼')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')


class SheetFile(db.Model):
    """
    譜的檔案
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'sheet_file'
    id = db.Column(db.Integer, primary_key=True)
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False, comment='檔名')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')


class Sheet(db.Model):
    """
    譜
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'sheet'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, comment='譜名')  # TODO 存檔時加亂數
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
