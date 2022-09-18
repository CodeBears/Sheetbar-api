from routes import *
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

# 建立所有資料表


@app.before_first_request
def create_tables():
    db.create_all()


LogTool.init_logging()


def create_app():
    return app
