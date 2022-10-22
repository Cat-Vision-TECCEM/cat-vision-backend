from Global.Utils.db import post, get


class Order:
    def __init__(self, params, load=True):
        self.id = None
        self.company_id = None
        self.store_id = None
        self.products = None
        self.datetime = None

        self.load(params) if load else self.create(params)

    def load(self, params):
        self.id = params['id']

        try:

            self.id, self.company_id, self.store_id, self.products, self.datetime = get(
                '''SELECT * FROM order WHERE order_id = %s ''',
                (self.id,),
                False
            )

        except Exception as e:
            return e

    def create(self, params):

        self.company_id = params['company_id']
        self.store_id = params['store_id']
        self.products = params['products']

        try:

            self.id = post(
                '''INSERT INTO order(company_id, store_id, products) VALUES (%s, %s, %s) RETURNING order_id''',
                (self.company_id, self.store_id, self.products),
                True
            )

        except Exception as e:

            return e
        