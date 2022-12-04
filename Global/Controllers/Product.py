"""
    Script that handles the received requests from the route product
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 26/10/2022
    Last update: 26/10/2022
"""

from flask import request
from Global.Classes.Product import Product
from Global.Utils.sessions import token_valid, admin_permission


def create_product():
    """
    Controller for the route /create

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

    try:
        token_valid(request)
        admin_permission(request)
        params = {
            'company_id': request.form.get('company_id'),
            'sku': request.form.get('sku'),
            'name': request.form.get('name'),
            'selling_price': request.form.get('selling_price'),
            'image': request.files.get('image')
        }
        product = Product(params, False)
        return {'success': f'Product {product.name} created'}, 200

    except Exception as e:
        return {'error': str(e)}, 400


def get_product():
    """
    Controller for the route /getProduct

    Method:
        * GET

    Parameters:
        * product_id: numeric id of the product

    Format:
        * QueryParams

    Returns:
        * An exception or a 200 status
    """

    try:
        params = {
            'product_id': request.args.get('product_id')
        }
        return Product.obtener_producto(params)
    except Exception as e:
        return {'error': str(e)}, 400

def get_all():
    """
    Controller for the route /get-all

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
        return Product.get_products(company_id)
    except Exception as e:
        return {'error': str(e)}, 400