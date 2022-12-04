"""
    Routes created for the Company
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import Company as c

GLOBAL_COMPANY_BLUEPRINT = Blueprint('GLOBAL_COMPANY_BLUEPRINT', __name__)


@GLOBAL_COMPANY_BLUEPRINT.route('/create', methods=['POST'])
def create_company():
    """
    Route used to create a new company in the database

    Method:
    * POST

    Parameters:
    * name: name of the company
    * email: email of the company

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.create_company()


@GLOBAL_COMPANY_BLUEPRINT.route('/get-all', methods=['GET'])
def get_companies():
    """
    Route used to load all the companies from the database

    Method:
    * GET

    Parameters:
    * Not required

    Format:
    * None

    Returns:
    * An exception or a 200 status
    """
    return c.get_companies()
