from flask import request
from Global.Classes.Product import Product
"""
    Script that handles the received requests from the route product
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 26/10/2022
    Last update: 26/10/2022
"""


def create_product():
    try:
        params = {
            'company_id': request.json.get('company_id'),
            'sku': request.json.get('sku'),
            'name': request.json.get('name'),
            'selling_price': request.json.get('selling_price'),
            'image': request.files.get('image')
        }
        product = Product(params, False)
        return f'Product {product.name} created', 200

    except Exception as e:
        return {'error': str(e)}, 400


def get_product():

    try:
        params = {
            'product_id': request.args.get('product_id')
        }
        return Product.obtener_producto(params)
    except Exception as e:
        return {'error': str(e)}, 400