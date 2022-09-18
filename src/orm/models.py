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
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False, comment='譜名')  # TODO 存檔時加亂數
    author = db.Column(db.String(100), nullable=False, comment='作者')
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    instrument = db.Column(db.Integer, db.ForeignKey('instrument.id'), nullable=False)
    view = db.Column(db.Integer, server_default='0', nullable=False, comment='觀看次數')
    download = db.Column(db.Integer, server_default='0', nullable=False, comment='下載次數')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')


class Category(db.Model):
    """
    分類(ex. pop, anime)
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, comment='分類')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')


class Instrument(db.Model):
    __bind_key__ = BIND_KEY
    __tablename__ = 'instrument'
    """
    樂器(ex. piano, violin)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, comment='樂器名')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
