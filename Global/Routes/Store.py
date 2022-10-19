"""

"""

from urllib import request
from flask import Blueprint
from Global.Controllers import Store as c

GLOBAL_STORE_BLUEPRINT = Blueprint('GLOBAL_STORE_BLUEPRINT', __name__)

@GLOBAL_STORE_BLUEPRINT.route('/create', methods = ['POST'])
def createStore():
    return c.create_store()

@GLOBAL_STORE_BLUEPRINT.route('/getProducts', methods = ['GET'])
def getStoreProducts():
    return c.get_store_products()
