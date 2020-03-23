# good.py
from flask import Blueprint, render_template

login_blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/login',
    template_folder='loginTemplates'
)

@login_blueprint.route('/')
def getGoods():
    return render_template('login.html')