# import package
import urllib

from flask import Flask, escape, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()
