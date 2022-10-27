from flask import Blueprint
from Global.Controllers import Product as c

GLOBAL_ORDER_BLUEPRINT = Blueprint('GLOBAL_ORDER_BLUEPRINT', __name__)


@GLOBAL_ORDER_BLUEPRINT.route('/create', methods=['POST'])
def create_product():
    """
    Route used to create a new product in the databse

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