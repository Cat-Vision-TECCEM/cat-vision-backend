"""
    Routes created for the NUC/Client-side
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import NUC as c

GLOBAL_NUC_BLUEPRINT = Blueprint('GLOBAL_NUC_BLUEPRINT', __name__)


@GLOBAL_NUC_BLUEPRINT.route('/sendData', methods=['POST'])
def sendData():
    """
    Route used by the NUC to send byte-coded data to the backend

    Method:
    * POST

    Parameters:
    * A byte-array containing an encoded JSON

    Format:
    * RAW

    Returns:
    * An exception or a 200 status
    """
    return c.sendData()


@GLOBAL_NUC_BLUEPRINT.route('/get-products', methods=['POST'])
def get_products():
    """
    Route used by the NUC to load all the products of a company from the database

    Method:
    * POST

    Parameters:
    * company_id: numeric id of the company

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.get_products()
