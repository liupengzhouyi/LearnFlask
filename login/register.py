# register.py
from flask import Blueprint, render_template

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