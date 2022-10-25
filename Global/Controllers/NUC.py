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
        print(info)
        return 'Information received', 200

    except Exception as e:
        return str(e), 400

