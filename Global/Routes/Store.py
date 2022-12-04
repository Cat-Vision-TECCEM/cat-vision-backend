"""
    Routes created for the Store
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import Store as c

GLOBAL_STORE_BLUEPRINT = Blueprint('GLOBAL_STORE_BLUEPRINT', __name__)


@GLOBAL_STORE_BLUEPRINT.route('/create', methods=['POST'])
def createStore():
    """
    Route used to create a new store in the database

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
    * password: login password

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.create_store()


@GLOBAL_STORE_BLUEPRINT.route('/getProducts', methods=['GET'])
def getStoreProducts():
    """
    Route used to load all the products of a store from the database

    Method:
    * GET

    Parameters:
    *store_id: numeric id of the store

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    return c.get_store_products()


@GLOBAL_STORE_BLUEPRINT.route('/getAllStores', methods=['GET'])
def getAllStores():
    """
    Route used to load all the stores from the database

    Method:
    * GET

    Parameters:
    * Not required

    Format:
    * None

    Returns:
    * An exception or a 200 status
    """
    return c.get_all_stores()

@GLOBAL_STORE_BLUEPRINT.route('/getAllProducts', methods=['GET'])
def getAllProducts():
    """
    Route used to load all the products from the database

    Method:
    * GET

    Parameters:
    * Not required

    Format:
    * None

    Returns:
    * An exception or a 200 status
    """
    return c.get_all_products()

