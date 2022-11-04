"""
* Código que permite codificar y decodificar tokens jwt
* Autor: Erick Hernández Silva
* Fecha de creación: 03/11/2022
* Última a actualización: 03/11/2022
"""

from Global.Classes.Usuario import Usuario
from Global.Utils.db import get, post

def getCurrentUser(request):
    """
    Método que obtiene el usuario actual gracias al Auth Token recibido.
    :param token: AUTH token con split.
    :return:
    """
    token = request.headers.get('Authorization', None)
    record = get("""SELECT * from usuario WHERE access_token = %s """, (token,), False)
    if record is not None:
        if record[14]:
            return Usuario(record,True, True)
        else:
            raise Exception("Usuario bloqueado")

def getToken(request):
    """
    Método que sirve para obtener el token de autentificación de la request y lo regresa solito
    :param request: request de flask
    :return: el token partido, es decir sin el texto "bearer"
    """
    token = request.headers.get('Authorization', None)
    return token.split()[1]
