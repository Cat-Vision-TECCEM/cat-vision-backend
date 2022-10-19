"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
from flask import request
from Global.Classes.Store import Store

def create_store():
    pass

def get_store_products():
    try:
        store_id = request.args.get('store_id')
        store =  Store({'id':store_id})
        store.get_store_products()
    except Exception as e:
        return {
            'error': str(e)
        }, 400