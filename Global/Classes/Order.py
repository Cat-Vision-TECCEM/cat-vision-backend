import json
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
        self.total = None

        self.load(params) if load else self.create(params)

    def load(self, params):
        self.id = params['id']

        try:

            self.id, self.company_id, self.store_id, self.products, self.datetime, self.status, self.total = get(
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
        self.total = params['total']

        try:

            self.id = post(
                '''INSERT INTO public.order(company_id, store_id, products,total) VALUES (%s, %s, %s,%s) RETURNING order_id''',
                (self.company_id, self.store_id, json.dumps(self.products), self.total),
                True
            )

        except Exception as e:

            return e

    @classmethod
    def get_sales_product(self, params):
        company_id = params.get('company_id')
        start_month = params['start_month']
        start_year = params['start_year']
        end_month = params.get('end_month')
        end_year = params.get('end_year')
        process = None

        def process_products(orders, company = True):
            orders = orders
            res_part_1 = {}
            if company:
                for order in orders:
                    res_part_1[order[0]] = {
                        'total': order[2]
                    }
                    orders_products = order[1].split('@')

                    res = json.loads(orders_products.pop(0))
                    for products in orders_products:
                        temp_dict = json.loads(products)
                        keys = list(temp_dict.keys())
                        values = list(temp_dict.values())
                        for i in range(len(keys)):
                            res[keys[i]] = res.get(keys[i], 0) + values[i]
                    res_part_1[order[0]]['totals'] = res

                return res_part_1


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
                return process
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
