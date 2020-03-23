# import package
from flask import Flask

app = Flask(__name__)

# tell Flask 触发 function url
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return "Index Page"

@app.route('/user/<name>')
def paly(name):
    return "hello %s" % name

@app.route('/userid/<int:userId>')
def paly01(userId):
    return "userId: %d" % userId

if __name__ == '__main__':
    app.run()
