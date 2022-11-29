from Global.Utils.db import post, get

"""
    Script that handles the received requests
    Authors: Erick Hernandez Silva
    Created: 26/10/2022
    Last update: 26/10/2022
"""


class Company:
    def __init__(self, params, load=True):
        self.company_id = None
        self.name = None
        self.email = None
        self.load(params) if load else self.create(params)

    def load(self, params):
        try:
            self.company_id = params.get('company_id')
            self.name, self.email = get('''
                SELECT name, email FROM public.company WHERE company_id = %s
            ''', (self.company_id,), False)
        except Exception as e:
            return str(e), 400

    def create(self, params):
        """
        Método que crea una nueva compañia en la base de datos
        :param params:
        :return:
        """
        try:
            self.company_id = None
            self.name = params.get('name')
            self.email = params.get('email')

            self.company_id = post('''
                INSERT INTO public.company(name, email) VALUES (%s, %s) RETURNING company_id
            ''', (self.name, self.email), True)[0]

            post(
                '''INSERT INTO product(company_id,sku,name,selling_price,image) 
                VALUES(%s,%s,%s,%s,%s) RETURNING product_id''',
                (self.company_id, "-69", "Unrecognized product", 0, 'https://images.emojiterra.com/google/android-11/512px/2753.png'),
                True)
            return f'Company {self.name} has been created with id {self.company_id}', 200
        except Exception as e:
            return str(e), 400
