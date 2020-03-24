# login.py
from flask import Blueprint, render_template

from models.models import User, add_object, query_object

from .register import register_blueprint

login_blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/login',
    template_folder='loginTemplates'
)

@login_blueprint.route('/')
def getGoods():
    return render_template('login.html')

@login_blueprint.route('/add')
def add():
    user = User()
    user.username = 'liupeng012'
    user.password = '1234567'
    add_object(user)
    return render_template('loginSuccess.html')

@login_blueprint.route('/add1')
def add1():
    user = User()
    user.username = 'liupeng012'
    user.password = '1234567'
    r = query_object(user, user.username, user.password)
    print(r)
    return render_template('loginSuccess.html')

