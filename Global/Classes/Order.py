from datetime import timedelta

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

        def process_products(orders, company = True):
            orders = orders[0]

            if company:
                for order in orders:
                    pass

            else:
                pass


        # Comprobamos si recibimos la fecha de termina
        if end_year is not None:
            tupla = (f'{start_year}-{start_month}-01', f'{end_year}-{end_month}-01')
        else:
            import datetime
            tupla = (str(datetime.date(int(start_year), int(start_month), 1)),
                     str(datetime.date.today() + timedelta(days=1)))
        try:
            if company_id is None:
                #sales = get('''SELECT products, total, datetime FROM public.order WHERE datetime BETWEEN %s AND %s ''', tupla)
                sales = get('''SELECT DATE_PART('month',datetime::date) AS mes, string_agg(products::text, '@'), 
                SUM(total) AS productos FROM public.order 
                WHERE datetime BETWEEN %s AND %s GROUP BY 1''', tupla)
                process = process_products(sales)
                print(sales)
            else:
                #sales = get('''SELECT products, total, datetime FROM public.order WHERE datetime BETWEEN %s AND %s AND company_id = %s''',
                            #tupla + (company_id,))
                sales = get('''SELECT DATE_PART('month',datetime::date) AS mes, string_agg(products::text, '@'), 
                                SUM(total) AS productos FROM public.order 
                                WHERE datetime BETWEEN %s AND %s AND company_id = %s GROUP BY 1''', tupla+(company_id,))
                process = process_products(sales, False)

            return 'a'
        except Exception as e:
            return e
