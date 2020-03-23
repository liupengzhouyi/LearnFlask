# import package
from flask import Flask, escape, url_for, request, render_template

from application.good import good_blueprint
from login.login import login_blueprint
from login.verify import verify_blueprint
# application object
app = Flask(__name__)

# application object register buleprint object
app.register_blueprint(good_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(verify_blueprint)


# tell Flask 触发 function url
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
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
