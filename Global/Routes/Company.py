"""

"""
from flask import Blueprint
from Global.Controllers import Company as c

GLOBAL_COMPANY_BLUEPRINT = Blueprint('GLOBAL_COMPANY_BLUEPRINT', __name__)


@GLOBAL_COMPANY_BLUEPRINT.route('/create', methods=['POST'])
def create_company():
    return c.create_company()


@GLOBAL_COMPANY_BLUEPRINT.route('/get-all', methods=['GET'])
def get_companies():
    return c.get_companies()
