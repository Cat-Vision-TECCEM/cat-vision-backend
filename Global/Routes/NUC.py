"""
    Routes created for the NUC/Client-side
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 24/10/2022
"""

from urllib import request
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



