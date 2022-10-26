from datetime import timedelta

from Global.Utils.db import post, get

"""
    Script that handles the received requests
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 24/10/2022
"""


class NUC:
    def __init__(self, params, load=True):
        self.id = None
        self.company_id = None
        self.store_id = None
        self.products = None
        self.datetime = None
        self.status = None

    @classmethod
    def update_store_items(cls, info):
        try:
            store_id = info['store_id']
            info.pop('store_id')
            products = get('''
            select sp.store_product_id, sp.product_id, sp.in_stock, pr.sku from public.store_product sp
            left join product pr on pr.product_id = sp.product_id where store_id = %s
            ''', (store_id,))
            detected_products = list(info.keys())
            database_products = []
            database_ids_products = []
            for product in products:
                if product[3] in detected_products and not product[2]:
                    post('''
                    UPDATE public.store_product SET in_stock= %s WHERE 
                    store_product_id = %s
                    ''', (True, product[0]))
                elif product[3] not in detected_products and product[2] :
                    post('''
                    UPDATE public.store_product SET in_stock= %s WHERE 
                    store_product_id = %s
                    ''', (False, product[0]))
                database_products.append(product[3])
                database_ids_products.append(product[1])

            i = 0
            for product in detected_products:
                if product not in database_products:
                    product_id = get('''
                    SELECT product_id FROM public.product WHERE sku = %s ''',
                                     (detected_products[i],))
                    post('''
                    INSERT INTO public.store_product(product_id, store_id, in_stock) VALUES (%s, %s, %s)
                    ''', (product_id[0][0], store_id, True))
                i += 1
            return 'Completed', 200
        except Exception as e:
            return str(e)


