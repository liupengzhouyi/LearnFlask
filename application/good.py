# good.py
from flask import Blueprint

good_blueprint = Blueprint('good', __name__, url_prefix='/api/good')

@good_blueprint.route('/')
def getGoods():
    return "good-1"

@good_blueprint.route('/<int:catagory_id>')
def getGoodsInCatagory(catagory_id):
    return "good-2 %d" % catagory_id