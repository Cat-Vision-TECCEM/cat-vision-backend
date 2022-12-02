"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
import re
from flask import request
from Global.Classes.Store import Store


def create_store():
    """
    Controller for the route /create

    Method:
    * POST

    Parameters:
    * name: name of the store
    * state: state where the store is located
    * street: street where the store is located
    * number: street number where the store is located
    * city: city where store is located
    * lat: latitude of the store location
    * lng: longitude of the store location

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    try:
        params = {
            'name': request.json.get('name'),
            'state': request.json.get('state'),
            'street': request.json.get('street'),
            'number': request.json.get('number'),
            'city': request.json.get('city'),
            'lat': request.json.get('lat'),
            'lng': request.json.get('lng'),
            'company_id':request.json.get('company_id')
        }
        store = Store(params, False)
        return {'success': f'Store {store.name} requested'}, 200
    except Exception as e:
        return {'error': str(e)}, 400


def get_store_products():
    """
    Controller for the route /getProducts

    Method:
    * GET

    Parameters:
    * store_id: int - the id of the store we want to get the products

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    try:

        store_id = request.args.get('store_id')
        return Store.get_store_products(store_id)
    except Exception as e:
        return {'error': str(e)}, 400


def get_all_stores():
    """
    Controller for the route /getAll

    Method:
    * GET

    Parameters:
    * Not required

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    try:
        return Store.get_all()
    except Exception as e:
        return {'error': str(e)}, 400
