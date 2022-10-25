from flask import request
from Global.Classes.Order import Order


def create_order():
    try:
        params = {
            'company_id': request.json.get('company_id'),
            'store_id': request.json.get('store_id'),
            'products': request.json.get('products')
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