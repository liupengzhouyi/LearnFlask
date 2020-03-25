# login.py
from flask import Blueprint, render_template

todo_blueprint = Blueprint(
    'todo',
    __name__,
    url_prefix='/todo',
    template_folder='todoTemplate'
)

@todo_blueprint.route('/')
def index():
    return render_template('todoIndex.html')