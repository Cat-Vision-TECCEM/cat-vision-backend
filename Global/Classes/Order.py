from Global.Utils.db import post, get


class Order:
    def __init__(self, params, load=True):
        self.id = None
        self.company_id = None
        self.store_id = None
        self.products = None
        self.datetime = None
        self.status = None

        self.load(params) if load else self.create(params)

    def load(self, params):
        self.id = params['id']

        try:

            self.id, self.company_id, self.store_id, self.products, self.datetime, self.status = get(
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

    @classmethod
    def get_sales_product(self, params):
        company_id = params.get('COMPANY_ID')
        start_month = params['start_month']
        start_year = params['start_year']
        end_month = params.get('end_month')
        end_year = params.get('end_year')
        process = None

        def process_products(productos, company = True):
            if company:
                pass
            else:
                pass
        # Comprobamos si recibimos la fecha de termina
        if end_year is not None:
            tupla = (f'{start_year}-{start_month}-01', f'{end_year}-{end_month}-01')
        else:
            import datetime
            tupla = (str(datetime.date(int(start_year), int(start_month), 1)), str(datetime.date.today()))
        try:
            if company_id is None:
                tupla = ('2022-10-01', '2022-10-31')
                sales = get('''SELECT products, total FROM public.order WHERE datetime BETWEEN %s AND %s ''', tupla)
                print(sales)
            else:
                sales = get('''SELECT products, total FROM public.order WHERE datetime BETWEEN %s AND %s AND company_id = %s''',
                            tupla + (company_id,))
            return '"('
        except Exception as e:
            return e

        return sales
