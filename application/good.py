# good.py
from flask import Blueprint, render_template

good_blueprint = Blueprint(
    'good',
    __name__,
    url_prefix='/api/good',
    template_folder='application_templates'
)

@good_blueprint.route('/')
def getGoods():
    return "good-1"

@good_blueprint.route('/<int:catagory_id>')
def getGoodsInCatagory(catagory_id):
    return "good-2 %d" % catagory_id

@good_blueprint.route('/index/<string:name>')
def index(name):
    return render_template('index.html', name=name)