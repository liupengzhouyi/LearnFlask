# __init__.py

from flask import Flask
from db import db


dbApp = Flask(__name__) # 新建app对象

dbApp.config.from_object('config') # 加载配置信息，其中有数据库的配置信息，包含在SQLALCHEMY_DATABASE_URI中

# 初始化db,并创建models中定义的表格

# 添加这一句，否则会报数据库找不到application和context错误
with dbApp.app_context():
    # 初始化db
    db.init_app(dbApp)
    # 创建所有未创建的table
    db.create_all()