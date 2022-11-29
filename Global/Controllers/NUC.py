"""
    Script that handles the received requests
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 24/10/2022
"""

from flask import request
from Global.Classes.NUC import NUC


def sendData():
    try:
        import json
        received_json = request.data.decode('utf-8')
        info = json.loads(received_json)
        return NUC.update_store_items(info)


    except Exception as e:
        return {'error': str(e)}, 400

def get_products():
    try:
        company_id = request.json.get('company_id')
        return NUC.get_products(company_id)

    except Exception as e:
        return {'error': str(e)}, 400
