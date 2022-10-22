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
