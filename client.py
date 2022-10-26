"""
Client for testing purposes of the NUC routes
"""

import requests
import json

# TEST SEND DATA
def sendData():
    url = 'http://127.0.0.1:8080/nuc/sendData'
    jason = {
        "7": 1,
        "9": 5,
        "11": 3,
        "store_id": 3
    }
    print(type(str(jason)))
    obj = bytes(json.dumps(jason), 'utf-8')

    x = requests.post(url, obj)

    print(x.text)
sendData()