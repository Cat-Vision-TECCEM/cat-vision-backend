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
                # We use this when we want to login comparing passwords
                self.load(params)
            else:
                # We use this when whe are already logged in
                self.obtenerUsuarioActual(params)
        else:
            # We use this when we want to register a new user
            self.register(params)

    def load(self, params):
        """
        Method used to login. This methods gets the user from database and compares passowrd, it also creates
        the JWT used to check sessions.
        :param params:
        :return:
        """
        username = params.get('username')
        password = params.get('password')
        # Obtenemos el JWT KEY desde las variables de entorno
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        user_info = get("""SELECT * from public.company_user WHERE username = %s""", (username,), False)
        if user_info is not None:
            self.user_id = user_info[0]
            self.store_or_company_id = user_info[1]
            self.username = user_info[2]
            self.password = user_info[3]
            self.is_admin = user_info[4]
            self.type = 'company'
        else:
            user_info = get("""SELECT * from public.store_user WHERE username = %s""", (username,), False)
            if user_info is not None:
                self.user_id = user_info[0]
                self.store_or_company_id = user_info[1]
                self.username = user_info[2]
                self.password = user_info[3]
                self.is_admin = user_info[4]
                self.type = 'store'

        if self.user_id is None:
            raise Exception('Cuenta inexistente')

        # We first compare password to login
        if self.password == hashlib.md5(password.encode()).hexdigest():
            # We create the new access token
            self.access_token = jwt.encode(
                {
                    "username": self.username,
                    "timestamp": datetime.datetime.timestamp(
                        datetime.datetime.now() + datetime.timedelta(hours=24))
                },
                JWT_SECRET_KEY, algorithm="HS256"
            )
            # We finally upload the token to database
            if self.type == 'company':
                # Enviamos el token a la base de datos
                post("""UPDATE public.company_user SET access_token= %s WHERE username= %s;""",
                     (self.access_token, self.username))
            else:
                # Enviamos el token a la base de datos
                post("""UPDATE public.store_user SET access_token= %s WHERE username= %s;""",
                     (self.access_token, self.username))
        else:
            # Raise an exception if password is wrong
            raise Exception('Wrong password')


    def register(self, params):
        """
        Method that creates a new user in database
        :param params:
        :return:
        """
        self.username = params['username']
        self.type = params['type']
        # If user type is a company user
        if self.type == 'company':
            # First we seek for the username to check if the username is not taken already
            user_info = get("""SELECT * from public.company_user WHERE username = %s""", (self.username,), False)
            if user_info is not None:
                raise Exception(f'User {self.username} already exists')

            # If not, we can proceed
            self.password = hashlib.md5(params['password'].encode()).hexdigest()
            self.is_admin = params['is_admin']
            self.access_token = None
            self.reset_token = None
            self.store_or_company_id = params['store_or_company_id']
            self.user_id = post(
                '''INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING company_user_id''',
                (self.store_or_company_id, self.username, self.password, self.is_admin, self.access_token, self.reset_token),
                True
            )

        # If user type is a store user
        elif self.type == 'store':
            # First we seek for the username to check if the username is not taken already
            user_info = get("""SELECT * from public.store_user WHERE username = %s""", (self.username,), False)
            if user_info is not None:
                raise Exception(f'User {self.username} already exists')

            # If not, we can proceed
            self.password = hashlib.md5(params['password'].encode()).hexdigest()
            self.is_admin = params['is_admin']
            self.access_token = None
            self.reset_token = None
            self.store_or_company_id = params['store_or_company_id']
            self.user_id = post(
                '''INSERT INTO public.store_user(store_id, username, password, is_admin, access_token, reset_token) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING store_user_id''',
                (self.store_or_company_id, self.username, self.password, self.is_admin, self.access_token,
                 self.reset_token),
                True
            )


    def obtenerUsuarioActual(self, params):
        self.user_id = params[0]
        self.store_or_company_id = params[1]
        self.username = params[2]
        self.password = params[3]
        self.is_admin = params[4]
        self.access_token = params[5]
        self.reset_token = params[6]
        self.type = params[7]
