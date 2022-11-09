"""
* Código que permite codificar y decodificar tokens jwt
* Autor: Erick Hernández Silva
* Fecha de creación: 03/11/2022
* Última a actualización: 03/11/2022
"""

from Global.Classes.User import User
from Global.Utils.db import get, post

import os
from datetime import datetime, timedelta
from functools import wraps

import jwt


def token_valid(request):
    def check(record):
        # Primero verificamos que el usuario no esté suspendido.
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        now = datetime.now()
        target_timestamp = datetime.timestamp(now + timedelta(hours=24))
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms="HS256")
        exp_timestamp = decoded_token['timestamp']
        correo = decoded_token['username']
        # Comprobamos si la sesión sigue activa o ya caducó
        if target_timestamp > exp_timestamp > datetime.timestamp(now):
            # Si aun no caduca, generamos un access token nuevo
            access_token = jwt.encode({"correo": correo, "timestamp": datetime.timestamp(
                datetime.now() + timedelta(hours=24))},
                                      JWT_SECRET_KEY, algorithm="HS256")
            # Actualizamos el token en la DB"""
            # cursor.execute("""UPDATE usuario SET access_token= %s WHERE access_token = %s""",
            # (access_token, token))
        elif exp_timestamp < datetime.timestamp(now):
            # Borramos el token ya que la sesión ya caducó
            post("""UPDATE usuario SET access_token= %s WHERE access_token = %s""", (None, token))
            raise Exception('Sesión expirada')

    token = request.headers.get('Authorization', None)
    if token is not None:
        token = token.split()[1]
        record = get("""SELECT * from public.company_user WHERE access_token = %s """, (token,), False)
        if record is not None:
            check(record)
        else:
            record = get("""SELECT * from public.store_user WHERE access_token = %s """, (token,), False)
            if record is not None:
                check(record)
            else:
                raise Exception('Usuario inexistente o token expirado')

    else:
        raise Exception('El token no fue proporcionado')


def getCurrentUser(request):
    """
    Método que obtiene el usuario actual gracias al Auth Token recibido.
    :param request: AUTH token con split.
    :return:
    """
    token = request.headers.get('Authorization', None)
    record = get("""SELECT * from public.company_user WHERE access_token = %s """, (token,), False)
    if record is not None:
        return User(record.append('company'), True, True)
    else:
        record = get("""SELECT * from public.store_user WHERE access_token = %s """, (token,), False)
        if record is not None:
            return User(record.append('store'), True, True)
        else:
            raise Exception('Current user error')


def getToken(request):
    """
    Método que sirve para obtener el token de autentificación de la request y lo regresa solito
    :param request: request de flask
    :return: el token partido, es decir sin el texto "bearer"
    """
    token = request.headers.get('Authorization', None)
    return token.split()[1]


def company_user_permission(request):
    token = request.headers.get('Authorization', None)
    record = get("""SELECT * from public.company_user WHERE access_token = %s """, (token,), False)
    if record is not None:
        return True
    else:
        record = get("""SELECT * from public.store_user WHERE access_token = %s """, (token,), False)
        if record is not None:
            raise Exception('You do not have access to this.')
        else:
            raise Exception('You do not have access to this.')
