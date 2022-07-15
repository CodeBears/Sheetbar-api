import os


class Config:
    ENVIRONMENT = os.environ.get('ENVIRONMENT', None)

    # mysql
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['MYSQL_USER']
    DB_PWD = os.environ['MYSQL_PASSWORD']
    DB_HOST = os.environ['MYSQL_HOST']
    DB_PORT = os.environ['MYSQL_PORT']
    SQLALCHEMY_BINDS = {
        DB_NAME: f'mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', None)
    ACCESS_TOKEN_EXPIRE_TIME = 60 * 30  # 30分鐘
    REFRESH_TOKEN_EXPIRE_TIME = 60 * 60 * 24 * 7  # 7天
