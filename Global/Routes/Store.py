"""

"""

from urllib import request
from flask import Blueprint
from Global.Controllers import Store as c

GLOBAL_STORE_BLUEPRINT = Blueprint('GLOBAL_STORE_BLUEPRINT', __name__)


@GLOBAL_STORE_BLUEPRINT.route('/create', methods=['POST'])
def createStore():
    """
    Route used to create a new store in the databse

    Method:
    * POST

    Parameters:
    * name: name of the store
    * state: state where the store is located
    * street: street where the store is located
    * number: street number where the store is located
    * city: city where store is located
    * password: login password

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.create_store()


@GLOBAL_STORE_BLUEPRINT.route('/getProducts', methods=['GET'])
def getStoreProducts():
    """
    Route used to create a new store in the databse

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


@GLOBAL_STORE_BLUEPRINT.route('/getAllStores', methods=['GET'])
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

@GLOBAL_STORE_BLUEPRINT.route('/getAllProducts', methods=['GET'])
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
