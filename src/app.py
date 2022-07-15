from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from utils.log_tool import LogTool

app = Flask(__name__)

app.config.from_object('config.Config')
config = app.config

CORS(app, send_wildcard=True)  # 允許跨域請求
Compress(app)  # 壓縮

db = SQLAlchemy(app)
from routes import *

LogTool.init_logging()


def create_app():
    return app
