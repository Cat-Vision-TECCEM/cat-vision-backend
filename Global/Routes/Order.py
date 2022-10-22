"""

"""

from urllib import request
from flask import Blueprint
from Global.Controllers import Order as c

GLOBAL_ORDER_BLUEPRINT = Blueprint('GLOBAL_ORDER_BLUEPRINT', __name__)


@GLOBAL_ORDER_BLUEPRINT.route('/create', methods=['POST'])
def create_ordern():
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


@GLOBAL_ORDER_BLUEPRINT.route('/getOrders', methods=['GET'])
def getStoreProducts():
    """
    Route to get all active orders

    Method:
    * GET

    Parameters:
    * name: name of the store
    * state: state where the store is located
    * street: street where the store is located
    * number: street number where the store is located
    * city: city where store is located
    * password: login password

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    return c.get_store_products()


@GLOBAL_ORDER_BLUEPRINT.route('/getAllStores', methods=['GET'])
def getAllStores():
    """
    Route used to load all the stores from the databse

    Method:
    * GET

    Parameters:
    * Not required

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    return c.get_all_stores()

@GLOBAL_ORDER_BLUEPRINT.route('/getAllProducts', methods=['GET'])
def getAllProducts():
    """
    Route used to get

    Method:
    * GET

    Parameters:
    * Not required

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    return c.get_all_products()


"""
estadisticas para todos
- los mas comprandos
- los menos comprados

estadísticas por tienda
- los productos


estadisticas gobales, estado
la tiendita que mas compra
la tiendita que menos compra

-------------------

Ruta que devuelva todas las tienditas 
- toda la informacion

Ruta que devuelve los pedidos ordenados en orden descendente para 

Ruta para crear pedido 

IMPORTANTE

RUTA PARA ESTADISTICAS DE LA TIENDA
- los productos de la tienda separados en agotados, existentes
- los productos 3 productos mas comprados en un intervalo de fechas 
- grafica de linea con el historico de compras con intervalos de temporalidad de 1 mes


BASE DEDATOS
QUITAR CANTIDAD
"""
