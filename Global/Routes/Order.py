"""
    Routes created for the Order
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import Order as c

GLOBAL_ORDER_BLUEPRINT = Blueprint('GLOBAL_ORDER_BLUEPRINT', __name__)


@GLOBAL_ORDER_BLUEPRINT.route('/create', methods=['POST'])
def create_order():
    """
    Route used to create a new order in the databse

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
    return c.create_order()


@GLOBAL_ORDER_BLUEPRINT.route('/getSalesProduct', methods=['GET'])
def get_sales_product():
    """
    Route that obtains how many times a product has been ordered, the total of the ordered products and the total income
    in a certain interval of time.

    If a store_id is not given, then it is assumed that global statistics are requested.
    If an end date is not given, then it is assumed that the desired end date is the actual date.

    Method:
    * GET

    Parameters:
    * store_id (optional)
    * start_month
    * start_year
    * end_month(optional)
    * end_year(optional)

    Returns:
    * A JSON containing the requested information or an exception
    """
    return c.get_sales_product()


@GLOBAL_ORDER_BLUEPRINT.route('/getOrders', methods=['GET'])
def getActiveOrders():
    """
    Route that gets a store id and a company id and returns all the active orders. It returns the products of the
    order, the date, and the total to pay


    Method:
    * GET

    Parameters:
    * store_id (optional)
    * company_id (optional)

    Returns:
    * A JSON containing the requested information or an exception
    """
    return c.get_active_orders()