# register.py
from flask import Blueprint, render_template, request

from models.models import User, add_object, query_object

register_blueprint = Blueprint(
    'register',
    __name__,
    url_prefix='/register',
    template_folder='loginTemplates'
)

@register_blueprint.route('/')
def registe():
    return render_template('register.html')

@register_blueprint.route('/getDate', methods=['POST', 'GET'])
def getRgisterDate():
    username = request.form.get('name')
    password = request.form.get('password')
    passwordConfirmation = request.form.get('password-confirmation')
    msg = 'username:', username, "password", password, 'passwordConfirmation', passwordConfirmation
    if password == passwordConfirmation:
        user = User()
        user.username = username
        user.password = password
        add_object(user)
        return render_template('registerSuccess.html')
    else:
        return render_template('registerError.html')



