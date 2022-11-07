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
            return str(e), 400

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

            return str(e), 400

    @classmethod
    def get_sales_product(self, params):
        store_id = params.get('store_id')
        start_month = params['start_month']
        start_year = params['start_year']
        end_month = params.get('end_month')
        end_year = params.get('end_year')
        process = None

        def process_products(orders):
            orders = orders
            res_part_1 = {}
            res_part_totals = {
                'total_earns': 0,
                'totals_products': {}
            }

            for order in orders:
                res_part_1[order[0]] = {
                    'total': order[2]
                }
                res_part_totals['total_earns'] += order[2]
                orders_products = order[1].split('@')
                res = json.loads(orders_products.pop(0))

                for i in range(len(list(res.keys()))):
                    res_part_totals['totals_products'][list(res.keys())[i]] = res_part_totals['totals_products'].get(list(res.keys())[i],0) + list(res.values())[i]


                for products in orders_products:
                    temp_dict = json.loads(products)
                    keys = list(temp_dict.keys())
                    values = list(temp_dict.values())
                    for i in range(len(keys)):
                        res[keys[i]] = res.get(keys[i], 0) + values[i]
                        res_part_totals['totals_products'][keys[i]] = res_part_totals['totals_products'].get(keys[i], 0) + values[i]

                res_part_1[order[0]]['totals'] = res

            res_part_1[0] = res_part_totals
            from flask import jsonify
            return res_part_1


        # Comprobamos si recibimos la fecha de termina
        if end_year is not None:
            tupla = (f'{start_year}-{start_month}-01', f'{end_year}-{end_month}-01')
        else:
            import datetime
            tupla = (str(datetime.date(int(start_year), int(start_month), 1)),
                     str(datetime.date.today() + timedelta(days=1)))
        try:
            if store_id is None:
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
                                WHERE datetime BETWEEN %s AND %s AND company_id = %s GROUP BY 1''', tupla+(store_id,))
                process = process_products(sales)

            return process
        except Exception as e:
            return str(e), 400

    @classmethod
    def get_active_orders(cls, params):
        store_id = params['store_id']
        company_id = params['company_id']
        ordenes = []
        if store_id is not None:
            try:
                result = get('''SELECT products, datetime, total FROM public.order WHERE company_id = %s AND store_id = %s AND status = 'active' ''', (company_id, store_id))
            except Exception as e:
                return str(e), 400
        else:
            try:
                result = get('''SELECT products, datetime, total FROM public.order WHERE company_id = %s and status = 'active' ''', company_id)
            except Exception as e:
                return str(e), 400
            print(result)
        for orden in result:
            res_dict = {
                'products': orden[0],
                'date': orden[1],
                'total': orden[2]
            }
            ordenes.append(res_dict)
        return {
            'ordenes': ordenes
        }


