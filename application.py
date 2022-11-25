"""
    Configuracion e inicializacion de la aplicacion y registro de los blueprints
    Autores: David Rodriguez Fragoso, Eduardo Rodriguez, Erick Hernandez Silva
    Creado en: 18/10/2022
    Ultimo cambio: 07/11/2022
"""
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Configuracion del backend
load_dotenv()
application = Flask(__name__)
cors = CORS(application)
from flask_mail import Mail
mail = Mail()
# Ruta de testing
@application.route("/")
def hello_there():
    return "General Kenobi", 200


# Registro de blueprints
from Global.Routes.Store import GLOBAL_STORE_BLUEPRINT
from Global.Routes.Order import GLOBAL_ORDER_BLUEPRINT
from Global.Routes.NUC import GLOBAL_NUC_BLUEPRINT
from Global.Routes.Company import GLOBAL_COMPANY_BLUEPRINT
from Global.Routes.Product import GLOBAL_PRODUCT_BLUEPRINT
from Global.Routes.User import GLOBAL_USER_BLUEPRINT
from Global.Routes.Ticket import GLOBAL_TICKET_BLUEPRINT
application.register_blueprint(GLOBAL_STORE_BLUEPRINT, url_prefix='/store')
application.register_blueprint(GLOBAL_ORDER_BLUEPRINT, url_prefix='/order')
application.register_blueprint(GLOBAL_NUC_BLUEPRINT, url_prefix='/nuc')
application.register_blueprint(GLOBAL_COMPANY_BLUEPRINT, url_prefix='/company')
application.register_blueprint(GLOBAL_PRODUCT_BLUEPRINT, url_prefix='/product')
application.register_blueprint(GLOBAL_USER_BLUEPRINT, url_prefix='/user')
application.register_blueprint(GLOBAL_TICKET_BLUEPRINT, url_prefix='/ticket')


application.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
application.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
application.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')
application.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
application.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail.init_app(application)
# Configuraciones de la app

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True, port = os.environ.get('FLASK_PORT'))


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
