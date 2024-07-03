from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import Injector
from config.extension import ExtensionModule
#from internal.extension.database_extension import db

# 导入所有模型类以确保 db.create_all() 能找到它们
app = Flask(__name__)

# 配置数据库 URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgre@192.168.2.112:5432/llmops'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
     injector = Injector([ExtensionModule()])
     db = injector.get(SQLAlchemy)

     db.init_app(app)
     with app.app_context():
        db.create_all()  # 创建所有表

