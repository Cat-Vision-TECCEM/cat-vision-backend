"""
    Routes created for the Product
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import Product as c

GLOBAL_PRODUCT_BLUEPRINT = Blueprint('GLOBAL_PRODUCT_BLUEPRINT', __name__)


@GLOBAL_PRODUCT_BLUEPRINT.route('/create', methods=['POST'])
def create_product():
    """
    Route used to create a new product in the database

    Method:
    * POST

    Parameters:
    * company_id: numeric id of the company
    * sku: sku of the product
    * name: name of the product
    * selling_price: price of the product
    * image: url of the image of the product

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.create_product()


@GLOBAL_PRODUCT_BLUEPRINT.route('/getProduct', methods=['GET'])
def get_product():
    """
    Route used to get the information of a product from the database

    Method:
    * GET

    Parameters:
    * product_id: id of the product

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.get_product()


@GLOBAL_PRODUCT_BLUEPRINT.route('/get-all', methods=['POST'])
def get_all():
    """
    Route used to load all the products of a company from the database

    Method:
    * POST

    Parameters:
    *company_id: numeric id of the company

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.get_all()