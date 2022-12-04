"""
    Script that handles the received requests
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 24/10/2022
"""

from flask import request
from Global.Classes.NUC import NUC


def sendData():
    """
    Controller for the route /sendData

    Method:
        * POST

    Parameters:
        * A byte-array containing an encoded JSON

    Format:
        * RAW

    Returns:
        * An exception or a 200 status
    """

    try:
        import json
        received_json = request.data.decode('utf-8')
        info = json.loads(received_json)
        return NUC.update_store_items(info)


    except Exception as e:
        return {'error': str(e)}, 400

def get_products():
    """
    Controller for the route /get-products

    Method:
        * POST

    Parameters:
        * company_id: numeric id of the company

    Format:
        * JSON

    Returns:
        * An exception or a 200 status
    """
    try:
        company_id = request.json.get('company_id')
        return NUC.get_products(company_id)

    except Exception as e:
        return {'error': str(e)}, 400
