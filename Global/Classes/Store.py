"""
    Class that describes a Store
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
from Global.Utils.db import post, get
from json import load
from venv import create


class Store:

    def __init__(self, params, load=True):
        self.id = None
        self.name = None
        self.state = None
        self.street = None
        self.number = None
        self.city = None
        self.lat = None
        self.lng = None
        self.load(params) if load else self.create(params)

    def create(self, params):

        """
        Method that creates a new store into the database using params

        Parameters:
        * name: name of the store
        * state: state where the store is located
        * street: street where the store is located
        * number: street number where the store is located
        * city: city where store is located
        * lat: latitude of the store location
        * lng: longitude of the store location
        * password: login password

        Returns:

        """

        from hashlib import md5
        self.name = params['name']
        self.state = params['state']
        self.street = params['street']
        self.number = params['number']
        self.city = params['city']
        self.lat = params['lat']
        self.lng = params['lng']
        company_id = params['company_id']


        """self.id = post(
            '''INSERT INTO store(name, state, street, number, city, lat, lng) VALUES (%s, %s, %s, %s, %s, 
            %s, %s) RETURNING store_id''',
            (self.name, self.state, self.street, self.number, self.city, self.lat, self.lng),
            True
        )"""

        from flask import current_app
        from flask_mail import Mail, Message
        from flask import render_template
        import os
        company = get("""
        SELECT name from public.company where company_id = %s
        """, (company_id,), False)
        with current_app.app_context():
            # Obtenemos el sender email para enviar el correo
            MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
            mail = Mail()
            subject = "Solicitud de tienda"
            recipients = [os.environ.get('STORE_REQUEST_EMAIL')]
            sender = ('CatVision', MAIL_USERNAME)
            html = render_template("/new_store.html", name=self.name,
                          state=self.state, street=self.street,
                                   number=self.number, city=self.city, lat=self.lat, lng = self.lng, company = company[0])
            msg = Message(subject=subject, recipients=recipients, sender=sender, html=html)
            mail.send(msg)


    def load(self, params):

        """
        Method that loads a store from the database using params

        Parameters:
        * id: id of the store

        Returns:

        """

        self.id = params['id']

        try:

            self.name, self.state, self.street, self.number, self.city, self.lat, self.lng = get(
                '''SELECT * FROM store WHERE store_id = %s ''',
                (self.id,),
                False
            )

        except Exception as e:
            return e

    @classmethod
    def get_store_products(cls, id):

        """
        Class method that loads the available products in a store

        Parameters:
        * id: id of the store

        Returns:

        """

        result = get(
            ''' SELECT p.name, p.image, sp.in_stock
                FROM store_product sp
                LEFT JOIN product p ON sp.product_id = p.product_id
                WHERE sp.store_id = %s''',
            (id,)
        )
        print(result)
        res_list = []
        for item in result:
            res_dict = {
                'name' : item[0],
                'url' : item[1],
                'stock': item[2]
            }
            res_list.append(res_dict)
        return {
            'products': res_list
        }

    @classmethod
    def get_all(cls):

        """
        Class method that loads the address and the name of all stores from the database

        Parameters:


        Returns:
        * A list with a dictionary containing the store name, address and id

        """

        result = get("""
            SELECT name,state,street,number,city, lat, lng,  store_id FROM store
        """, ())

        stores = []

        for i in result:
            dict = {
                'value': i[0],
                'label': i[0],
                'written_address': i[2] + ' ' + i[3] + ', ' + i[4] + ', ' + i[1],
                'address': {
                    'lat':i[5],
                    'lng':i[6]
                },
                'id': i[7]

            }
            stores.append(dict)
        return {
            'stores': stores
        }
