"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""

from flask import request
from Global.Classes.Order import Order
from Global.Utils.sessions import token_valid, company_user_permission


def create_order():
    """
    Controller for the route /create

    Method:
        * POST

    Parameters:
        * company_id: numeric id of the company
        * store_id: numeric id of the store
        * products: a list of dictionaries containing the product's id and the quantity

    Format:
        * JSON

    Returns:
        * An exception or a 200 status
    """

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
        return {'error': str(e)}, 400


def get_sales_product():
    """
    Controller for the route /getSalesProduct

    Method:
        * GET

    Parameters:
        * store_id (optional): numeric id of the store
        * start_month: number of the month
        * start_year
        * end_month(optional): number of the month
        * end_year(optional)

    Format:
        * QueryParams

    Returns:
        * An exception or a 200 status
    """

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
        return {'error': str(e)}, 400


def get_active_orders():
    """
    Controller for the route /getOrders

    Method:
        * GET

    Parameters:
        * store_id (optional): numeric id of the store
        * company_id (optional): numeric id of the company
    
    Format:
        * QueryParams

    Returns:
        * An exception or a 200 status
    """

    try:
        token_valid(request)
        company_user_permission(request)
        params = {
            'store_id': request.args.get('store_id', None),
            'company_id': request.args.get('company_id', None)
        }
        return Order.get_active_orders(params)
    except Exception as e:
        return {'error': str(e)}, 400