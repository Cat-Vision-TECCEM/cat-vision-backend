"""
    Class that describes the functions of a company user
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
import datetime
import hashlib
import os
from time import time
import jwt
from threading import Thread

from flask import current_app, render_template
from flask_mail import Mail, Message
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
        self.email = None
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
            self.email = user_info[5]
        else:
            user_info = get("""SELECT * from public.store_user WHERE username = %s""", (username,), False)
            if user_info is not None:
                self.user_id = user_info[0]
                self.store_or_company_id = user_info[1]
                self.username = user_info[2]
                self.password = user_info[3]
                self.is_admin = user_info[4]
                self.type = 'store'
                self.email = user_info[5]

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
                raise Exception(f'User {self.username} is already taken.')

            # If not, we can proceed
            self.password = hashlib.md5(params['password'].encode()).hexdigest()
            self.is_admin = params['is_admin']
            self.access_token = None
            self.reset_token = None
            self.store_or_company_id = params['store_or_company_id']
            self.email = params['email']
            # CHECK FIRST FOR MAXIMUM USER
            if self.is_admin:
                # Checking maximum admins
                current_users_query = get("""select count(*) from public.company_user where company_id=%s and is_admin=%s""",
                                     (self.store_or_company_id, True))
                maximum_users_query = get("""select admin_number, pl.name from public.permission_level pl, public.company c
                where c.permission_level = pl.id and c.company_id=%s""", (self.store_or_company_id,))
                current_admins = current_users_query[0][0]
                maximum_admins = maximum_users_query[0][0]
                plan_name = maximum_users_query[0][1]
                if current_admins >= maximum_admins:
                    raise Exception(
                        f'Your company has reached the limit of admins accounts for your current plan {plan_name}. \n'
                        f'Limit of admins is {maximum_admins}, you have {current_admins}'
                    )
            else:
                # Checking maximum normal users
                current_users_query = get("""select count(*) from public.company_user where company_id=%s and is_admin=%s""",
                                     (self.store_or_company_id, False))
                maximum_users_query = get("""select user_number, pl.name from public.permission_level pl, public.company c
                                where c.permission_level = pl.id and c.company_id=%s""", (self.store_or_company_id,))
                current_users = current_users_query[0][0]
                maximum_users = maximum_users_query[0][0]
                plan_name = maximum_users_query[0][1]
                if current_users >= maximum_users:
                    raise Exception(
                        f'Your company has reached the limit of users accounts for your current plan "{plan_name}". \n'
                        f'Limit of users is {maximum_users}, you have {current_users}'
                    )

            self.user_id = post(
                '''INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token, 
                email) 
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING company_user_id''',
                (self.store_or_company_id, self.username, self.password, self.is_admin, self.access_token,
                 self.reset_token, self.email),
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
            self.email = params['email']
            self.user_id = post(
                '''INSERT INTO public.store_user(store_id, username, password, is_admin, access_token, reset_token, email) 
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING store_user_id''',
                (self.store_or_company_id, self.username, self.password, self.is_admin, self.access_token,
                 self.reset_token, self.email),
                True
            )

        with current_app.app_context():
            # Obtenemos el sender email para enviar el correo
            MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
            mail = Mail()
            subject = "Your CatVision account has been created"
            recipients = [params['email']]
            sender = ('CatVision', MAIL_USERNAME)
            html = render_template("/welcome.html",
                                   username=self.username)
            msg = Message(subject=subject, recipients=recipients, sender=sender, html=html)
            mail.send(msg)


    def obtenerUsuarioActual(self, params):
        self.user_id = params[0]
        self.store_or_company_id = params[1]
        self.username = params[2]
        self.password = params[3]
        self.is_admin = params[4]
        self.access_token = params[5]
        self.reset_token = params[6]
        self.type = params[7]

    @staticmethod
    def recover_password(params):
        """
        Method that searches an user in the database and generates a JWT to recover its password.
        :param params:
        :return:
        """
        token = jwt.encode({'reset_password': params['email'], 'exp': time() + 500},
                           key=os.environ.get('JWT_SECRET_KEY'),
                           algorithm="HS256")

        user_info = get("""SELECT * from public.store_user WHERE email = %s""", (params['email'],), False)
        if user_info is not None:
            post("""UPDATE public.store_user SET reset_token = %s WHERE email = %s""", (token, params['email']))

        else:
            user_info = get("""SELECT * from public.company_user WHERE email = %s""", (params['email'],), False)
            if user_info is not None:
                post("""UPDATE public.company_user SET reset_token = %s WHERE email = %s""", (token, params['email']))

        if user_info is None:
            raise Exception('Cuenta inexistente')

        with current_app.app_context():
            # Obtenemos el sender email para enviar el correo
            MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
            mail = Mail()
            subject = "Recover your password"
            recipients = [params['email']]
            sender = ('CatVision', MAIL_USERNAME)
            html = render_template("/recover_password.html",
                                   url=os.environ.get('ACTION_URL_PASSWORD_RECOVERY'),
                                   token=token)
            msg = Message(subject=subject, recipients=recipients, sender=sender, html=html)
            mail.send(msg)
            return {'success': f'Password recovery email sent.'}, 200

    @staticmethod
    def reset_password(params):
        passsword = hashlib.md5(params['password'].encode()).hexdigest()
        token = params['token']
        # We look for the user in both user types
        user_info = get("""SELECT * from public.store_user WHERE reset_token = %s""", (token,), False)
        if user_info is not None:
            post("""UPDATE public.store_user SET reset_token = %s, password = %s WHERE reset_token = %s""",
                 ('', passsword, token))

        else:
            user_info = get("""SELECT * from public.company_user WHERE reset_token = %s""", (token,), False)
            if user_info is not None:
                post("""UPDATE public.company_user SET reset_token = %s, password = %s WHERE reset_token = %s""",
                     ('', passsword, token))

        if user_info is None:
            raise Exception('Cuenta inexistente o token inválido')

        return f'Password updated.'




