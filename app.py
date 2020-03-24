# import package
from flask import Flask, escape, url_for, request, render_template
from db import db

from application.good import good_blueprint
from login.login import login_blueprint
from login.verify import verify_blueprint
from login.register import register_blueprint

# application object
from models.models import User, add_object
from models.paly import Play, add_object1

app = Flask(__name__)

# application object register buleprint object
app.register_blueprint(good_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(verify_blueprint)
app.register_blueprint(register_blueprint)


# 加载配置信息，其中有数据库的配置信息，包含在SQLALCHEMY_DATABASE_URI中
app.config.from_object('config')

# 初始化db,并创建models中定义的表格
# 添加这一句，否则会报数据库找不到application和context错误
with app.app_context():
    # 初始化db
    db.init_app(app)
    # 创建所有未创建的table
    db.create_all()

# tell Flask 触发 function url
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    play = Play()
    play.playname = 'liupeng01'
    play.password = '1234567'
    add_object1(play)
    return "Index Page"

@app.route('/user/<string:name>')
def paly(name):
    return "hello %s" % name

@app.route('/userid/<float:number>')
def paly00(number):
    return "number: %d" % number

@app.route('/userid/<int:userId>')
def paly01(userId):
    return "userId: %d" % userId

@app.route('/path/<path:subpath>')
def paly02(subpath):
    return "subpath: %s" % escape(subpath)

@app.route('/about/')
def about():
    return "About"

with app.test_request_context():
    print(url_for('index'))

@app.route('/paly04', methods=['GET', 'POST'])
def paly04():
    if request.method == 'POST':
        return index()
    else:
        return hello_world()

if __name__ == '__main__':
    app.run()
