"""
* Clase que representa a un usuario. Sirve para guardar los datos y portafolios del usuario en un JSON.
* Se realizan todos los cálculos necesarios dentro del __init__.
* Autor: Erick Hernández Silva
* Fecha de creación: 28/02/2022
* Última a actualización: 20/03/2022
"""
import datetime
import json
import os
import hashlib

import jwt

from Global.Utils.db import post, get


class Usuario():
    def __init__(self, params, db=True, current=False):
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



    def crearDesdeDb(self, data):
        """
        Carga un objeto con datos obtenidos desde la db
        :param params:
        :return:
        """
        # Obtenemos el JWT KEY desde las variables de entorno
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        # Obtenemos el correo y el password enviados por el cliente
        correo = data[0]
        password = data[1]
        # Obtenemos la tupla del usuario
        params = get("""SELECT * from usuario WHERE correo = %s""", (correo,), False)
        # Verificamos que el usuario exista
        if params is not None:
            self.id = params[0]
            self.correo = params[1]
            self.password = params[2]
            # Comparamos las contraseñas, si coinciden, entonces terminamos de crear el objeto
            if self.password == hashlib.md5(password.encode()).hexdigest():
                self.nombre = params[3]
                self.apellidos = params[4]
                self.fecha_nac = params[5]
                self.genero = params[6]
                self.pais = params[7]
                self.estado = params[8]
                self.foto = params[9]
                self.experiencia = params[10]
                self.created_on = params[11]
                self.authenticated = params[12]
                self.admin = params[13]
                self.is_active = params[14]
                # Verificamos que el usuario no esté desactivado
                if self.is_active:
                    self.reset_token = params[15]
                    self.moneda = params[16]
                    self.portafolio_activo = params[17]
                    self.acceso = params[18]
                    # Obtenemos todos los portafolios
                    portafolios = get("""SELECT * from portafolio WHERE usuario= %s AND cerrado_en = NULL;""",
                                      (self.id,))
                    self.portafolios = self.gen_port(portafolios)
                    # Generamos el token de acceso
                    access_token = jwt.encode({"correo": self.correo, "timestamp": datetime.datetime.timestamp(
                        datetime.datetime.now() + datetime.timedelta(hours=24))},
                                              JWT_SECRET_KEY, algorithm="HS256")
                    # Enviamos el token a la base de datos
                    post("""UPDATE usuario SET access_token= %s WHERE correo= %s;""",
                         (access_token, correo))
                    self.access_token = access_token
                else:
                    raise Exception("Cuenta desactivada")
            else:
                raise Exception("Contraseña inválida")
        else:
            raise Exception("Usuario inexistente")

    def crearNuevoUsuario(self, params):
        """
        Método que crea un usuario nuevo en la base de datos a partir datos enviados en params
        :param params:
        :return:
        """
        user = get("""SELECT * from usuario WHERE correo = %s""", (params[0],), False)
        if user is None:
            self.correo = params[0]
            self.passw = params[1]
            self.nombre = params[2]
            self.apellidos = params[3]
            self.fecha_nacimiento = params[4]
            self.genero = params[5]
            self.pais_residencia = params[6]
            self.estado_residencia = params[7]
            self.foto = params[8]
            self.experiencia = 0
            self.creado_en = datetime.datetime.now()
            self.authenticated = params[9]
            self.administrator = params[10]
            self.active = params[11]
            self.reset_token = None
            self.access_token = None
            self.moneda = 'mxn'
            self.acceso = params[12]
            self.portafolio_activo = None
            user_id = post("""INSERT INTO usuario(correo, passw, nombre, apellidos, fecha_nacimiento,\
                                   genero, pais_residencia,estado_residencia, foto, \
                                   authenticated, administrator, active, acceso) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  RETURNING id;""", (
                self.correo, self.passw, self.nombre, self.apellidos, self.fecha_nacimiento, self.genero,
                self.pais_residencia, self.estado_residencia, self.foto,
                self.authenticated, self.administrator,
                self.active, self.acceso), True)
            self.id = user_id[0]

            # Crear el primer portafolio
            id_portafolio = post("""INSERT INTO portafolio (usuario, nombre, tiempo, descripcion, real, status)
                    VALUES (%s, %s, %s, %s, %s, %s) returning id""", (user_id, 'Mi primer portafolio', 'auto',
                                                         'Este es mi primer portafolio', True, 'activo'), True)

            # Actualizamos el portafolio activo del usuario
            self.portafolio_activo = str(id_portafolio[0])

            # Actualizamos usuario con el ID del portafolio activo
            post("""UPDATE usuario SET portafolio_activo= %s WHERE usuario = %s""", (self.portafolio_activo, self.id))


            from flask import current_app
            from flask_mail import Mail, Message
            from flask import render_template
            with current_app.app_context():
                # Obtenemos el sender email para enviar el correo
                MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
                mail = Mail()
                subject = "Te damos la bienvenida"
                recipients = [self.correo]
                sender = ('Finzak', MAIL_USERNAME)
                html = render_template("/welcome.html", name=self.nombre)
                msg = Message(subject=subject, recipients=recipients, sender=sender, html=html)
                mail.send(msg)
        else:
            raise Exception("Usuario ya existente")

    def obtenerUsuarioActual(self, params):
        self.id = params[0]
        self.correo = params[1]
        self.password = params[2]
        self.nombre = params[3]
        self.apellidos = params[4]
        self.fecha_nac = params[5]
        self.genero = params[6]
        self.pais = params[7]
        self.estado = params[8]
        self.foto = params[9]
        self.experiencia = params[10]
        self.created_on = params[11]
        self.authenticated = params[12]
        self.admin = params[13]
        self.is_active = params[14]
        self.reset_token = params[15]
        self.access_token = params[16]
        self.moneda = params[17]
        self.acceso = params[18]
        self.portafolio_activo = params[19]

        # Obtenemos todos los portafolios
        portafolios = get("""SELECT * from portafolio WHERE usuario= %s AND cerrado_en is %s;""",
                          (self.id, None))
        self.portafolios = self.gen_port(portafolios)

    def obtenerAccessToken(self):
        """
        Método que regresa el access_token del objeto actual
        :return:
        """
        # Regresamos el access_token
        return {"access_token": self.access_token}, 200




    @classmethod
    def obtenerPerfil(cls, token):
        """
        Método de clase que busca en la base de datos la información pública del usuario activo con su
        token de acceso y la regresa como un diccionario.
        :param token: token de acceso del usuario
        :return:
        """
        # Obtenemos de la base de datos la tupla
        record = get("""SELECT * from usuario WHERE access_token = %s """, (token,), False)
        if record is None:
            raise Exception("Token inválido")
        # Regresamos los datos del usuario en formato JSON
        usuario = {
            "id": record[0],
            "correo": record[1],
            "nombre": record[3],
            "apellidos": record[4],
            "fecha_nacimiento": record[5],
            "genero": record[6],
            "pais_residencia": record[7],
            "estado_residencia": record[8],
            "foto": record[9],
            "experiencia": record[10],
            "creado_en": record[11],
            "administrator": record[13],
            "moneda": record[17],
            "acceso": json.loads(record[18])
        }
        return usuario

    @classmethod
    def cerrar_sesion(cls, access_token):
        """
        Método que cierra la sesión de un usuario con el access_token dado.
        :param access_token: token de acceso del usuario
        :return:
        """
        try:
            post("""UPDATE usuario SET access_token= %s WHERE access_token = %s;""",
                 (None, access_token))
            return {'msg': "Sesión cerrada"}
        except Exception as e:
            return {'msg': str(e)}

    @classmethod
    def solicitarCambioPassw(cls, correo):
        """
        Método de clase que solicita el cambio de contraseña de un correo electronico dado y envía el
        correo electrónico correspondiente
        :param correo: correo electrónico solicitado
        :return:
        """
        # TODO hacer que primero se verifique la exitencia del correo en la DB
        import os
        from flask import current_app, render_template
        from flask_mail import Mail, Message
        with current_app.app_context():
            # Obtenemos el sender email para enviar el correo
            MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
            # Obtenemos el link al cual se redirigirá el usuario al dar clic al boton del template
            BASE_LINK_TO_REESTABLISH_PASSWORD = os.environ.get("BASE_LINK_TO_REESTABLISH_PASSWORD")
            # Obtenemos de la configuración de la app el tiempo que tardará en expirar el token
            TIME_TO_RESET_PASSWORD = float(os.environ.get("TIME_TO_RESET_PASSWORD"))
            # Obtenemos de la configuración la llave de encripción
            JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
            # Generamos el token
            token = jwt.encode(
                {
                    "correo": correo,
                    "timestamp": datetime.datetime.timestamp(
                        datetime.datetime.now() + datetime.timedelta(minutes=TIME_TO_RESET_PASSWORD)
                    )
                },
                JWT_SECRET_KEY, algorithm="HS256")
            # Guardamos en la base de datos
            post("""UPDATE usuario SET reset_token = %s WHERE correo = %s""", (token, correo))
            # Generamos el email
            mail = Mail()
            msg = Message()
            msg.subject = "Restablece tu contraseña"
            msg.recipients = [correo]
            msg.sender = ("Finzak", MAIL_USERNAME)
            msg.body = "Has solicitado reestablecer tu contraseña."
            link = BASE_LINK_TO_REESTABLISH_PASSWORD % (token,)
            msg.html = render_template('/request_password_email.html', link=link)
            mail.send(msg)
            return {'msg': 'Cambio solicitado'}

    @classmethod
    def cambiarPasswCorreo(cls, reset_token, password):
        """
        Método de clase que recibe un token de reset y una contraseña para buscar el usuario correspondiente y
        actualizar su contraseña.
        :param reset_token: token necesario para reestablecer la contraseña
        :param password: contraseña nueva deseada por el usuario
        :return:
        """
        # Buscamos en la base de datos
        record = get("""SELECT * from usuario WHERE reset_token = %s """, (reset_token,), False)
        # Si se encontró el usuario
        if record is not None:
            # Obtenemos la llave de encripción
            JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
            # Obtenemos el timestamp actual
            now_timestamp = datetime.datetime.timestamp(datetime.datetime.now())
            # Desenciptamos el token anterior
            decoded_token = jwt.decode(reset_token, JWT_SECRET_KEY, algorithms="HS256")
            # Guardamos el timestamp de expiración y el correo electrónico del usuario
            exp_timestamp = decoded_token['timestamp']
            correo = decoded_token['correo']
            # Corroboramos que el token no esté expirado
            if exp_timestamp > now_timestamp:
                # Hasheamos la nueva contraseña
                import hashlib
                passw = hashlib.md5(password.encode()).hexdigest()
                # Guardamos los cambios en la base de datos
                post("""UPDATE usuario SET reset_token= %s, 
                    passw = %s, access_token = %s WHERE correo = %s""", (None, passw, None, correo))
                return {"msg": "Contraseña actualizada"}, 200
            else:
                return {"msg": "Enlace expirado"}, 401
        else:
            return {"msg": "Token invalido."}, 404




