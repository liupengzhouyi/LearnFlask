# login.py
from flask import Blueprint
from flask import Flask, escape, url_for, request, render_template

verify_blueprint = Blueprint(
    'verify',
    __name__,
    url_prefix='/verify',
    template_folder='loginTemplates'
)

@verify_blueprint.route('/')
def getGoods():
    return render_template('login.html')

@verify_blueprint.route('/verify', methods=['POST'])
def verify():
    username = request.form.get('username')
    password = request.form.get('password')
    print('username:', username, "password", password)
    if username == 'liupeng' and password == '123456':
        return render_template('loginSuccess.html')
    else:
        return render_template('loginError.html')