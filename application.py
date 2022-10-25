"""
    Configuracion e inicializacion de la aplicacion y registro de los blueprints
    Autores: David Rodriguez Fragoso, Eduardo Rodriguez, Erick Hernandez Silva
    Creado en: 18/10/2022
    Ultimo cambio: 18/10/2022
"""
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Configuracion del backend
load_dotenv()
application = Flask(__name__)
cors = CORS(application)

# Ruta de testing
@application.route("/")
def hello_there():
    return "General Kenobi", 200

# Registro de blueprints
from Global.Routes.Store import GLOBAL_STORE_BLUEPRINT
from Global.Routes.Order import GLOBAL_ORDER_BLUEPRINT
from Global.Routes.NUC import GLOBAL_NUC_BLUEPRINT
application.register_blueprint(GLOBAL_STORE_BLUEPRINT, url_prefix='/store')
application.register_blueprint(GLOBAL_ORDER_BLUEPRINT, url_prefix='/order')
application.register_blueprint(GLOBAL_NUC_BLUEPRINT, url_prefix='/nuc')
# Configuraciones de la app

if __name__ == "__main__":
    application.run(debug=True, port = os.environ.get('FLASK_PORT'))

#TODO:
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

DB 

Añadir la columna status de la orden
va a tener "fulfilled" o "active"
"""
