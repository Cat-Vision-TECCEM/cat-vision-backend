from flask import request
from Global.Classes.Order import Order
"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""

def create_order():
    try:
        params = {
            'company_id': request.json.get('company_id'),
            'store_id': request.json.get('store_id'),
            'products': request.json.get('products'),
            'total': request.json.get('total')
        }
        order = Order(params, False)
        return f'Order {order.id} created', 200

    except Exception as e:
        return str(e), 400


def get_sales_product():
    try:
        params = {
            'store_id': request.args.get('store_id', None),
            'start_month': request.args.get('start_month'),
            'start_year': request.args.get('start_year'),
            'end_month': request.args.get('end_month', None),
            'end_year': request.args.get('end_year', None)
        }
        return Order.get_sales_product(params)
    except Exception as e:
        return str(e), 400


def get_active_orders():
    try:
        params = {
            'store_id': request.args.get('store_id', None),
            'company_id': request.args.get('company_id', None)
        }
        return Order.get_active_orders(params)
    except Exception as e:
        return str(e), 400