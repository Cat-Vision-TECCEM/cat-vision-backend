"""
    Class that describes the functions of a company user
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
import datetime
import hashlib
import os

import jwt

from Global.Utils.db import get, post


class User:

    def __init__(self, params, db=True, current=False):
        self.user_id = None
        self.store_or_company_id = None
        self.username = None
        self.password = None
        self.is_admin = None
        self.access_token = None
        self.reset_token = None
        self.type = None
        if db:
            if not current:
                # Params es una lista que contiene únicamente el ID del usuario  a cargar
                self.crearDesdeDb(params)
            else:
                # Si es un usuario actual, sin contraseña
                self.obtenerUsuarioActual(params)
        else:
            # Params es una lista con todos los atributos para crear un nuevo usuario en la DB.
            self.crearNuevoUsuario(params)

    def crearDesdeDb(self, params):
        username = params.get('username')
        password = params.get('password')
        # Obtenemos el JWT KEY desde las variables de entorno
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        user_info = get("""SELECT * from public.company_user WHERE correo = %s""", (username,), False)
        if user_info is not None:
            self.user_id = user_info[0]
            self.store_or_company_id = [1]
            self.username = [2]
            self.password = [3]
            self.is_admin = [4]
            self.type = 'company'
        else:
            user_info = get("""SELECT * from public.store_user WHERE correo = %s""", (username,), False)
            if user_info is not None:
                self.user_id = user_info[0]
                self.store_or_company_id = [1]
                self.username = [2]
                self.password = [3]
                self.is_admin = [4]
                self.type = 'store'

        if self.user_id is None:
            raise Exception('Cuenta inexistente')

        # Compare passwords
        if self.password == hashlib.md5(password.encode()).hexdigest():
            self.access_token = jwt.encode(
                {
                    "username": self.username,
                    "timestamp": datetime.datetime.timestamp(
                        datetime.datetime.now() + datetime.timedelta(hours=24))},
                JWT_SECRET_KEY, algorithm="HS256"
            )
            if self.type == 'company':
                # Enviamos el token a la base de datos
                post("""UPDATE public.company_user SET access_token= %s WHERE username= %s;""",
                     (self.access_token, self.username))
            else:
                # Enviamos el token a la base de datos
                post("""UPDATE public.store_user SET access_token= %s WHERE username= %s;""",
                     (self.access_token, self.username))
        else:
            raise Exception('Wrong password')

    def obtenerUsuarioActual(self, params):
        self.user_id = params['user_id']
        self.store_or_company_id = params['store_or_company_id']
        self.username = params['username']
        self.password = params['password']
        self.is_admin = params['is_admin']
        self.access_token = params['access_token']
        self.reset_token = params['reset_token']
        self.type = params['type']

    def crearNuevoUsuario(self, params):
        self.username = params['username']
        self.type = params['type']
        if self.type == 'company':
            user_info = get("""SELECT * from public.company_user WHERE username = %s""", (self.username,), False)
            if user_info is not None:
                raise Exception(f'User {self.username} already exists')
            self.password = hashlib.md5(params['password'].encode()).hexdigest()
            self.is_admin = params['is_admin']
            self.access_token = None
            self.reset_token = None
            self.store_or_company_id = params['company_id']
            self.user_id = post(
                '''INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING company_user_id''',
                (self.store_or_company_id, self.username, self.password, self.is_admin, self.access_token, self.reset_token),
                True
            )

        elif self.type == 'store':
            user_info = get("""SELECT * from public.store_user WHERE username = %s""", (self.username,), False)
            if user_info is not None:
                raise Exception(f'User {self.username} already exists')
            self.password = hashlib.md5(params['password'].encode()).hexdigest()
            self.is_admin = params['is_admin']
            self.access_token = None
            self.reset_token = None
            self.store_or_company_id = params['company_id']
            self.user_id = post(
                '''INSERT INTO public.store_user(store_id, username, password, is_admin, access_token, reset_token) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING store_user_id''',
                (self.store_or_company_id, self.username, self.password, self.is_admin, self.access_token,
                 self.reset_token),
                True
            )

