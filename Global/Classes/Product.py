"""
    Class that describes a Product
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 26/10/2022
    Last update: 26/10/2022
"""
from Global.Utils.db import post, get
from json import load
from venv import create
from Global.Utils.s3 import S3_Instance


class Product:

    def __init__(self, params, load=True):
        self.product_id = None
        self.company_id = None
        self.sku = None
        self.name = None
        self.selling_price = None
        self.image = None

        self.load(params) if load else self.create(params)

    def create(self, params):

        """
        Method that creates a new product into the database using params

        Parameters:
        * comapny_id: id of the company
        * sku: sku of the product
        * name: name of the product
        * selling_price: price of the product
        * image: url of the image of the product

        Returns:

        """

        self.company_id = params['company_id']
        self.sku = params['sku']
        self.name = params['name']
        self.selling_price = params['selling_price']
        self.image = params['image']

        # First we check the limit of products
        created_products = get('SELECT COUNT(*) FROM product WHERE company_id = %s', (self.company_id,))
        created_products = created_products[0][0]
        maximum_products = get("""select product_number, pl.name from public.permission_level pl, public.company c
            where c.permission_level = pl.id and c.company_id=%s """, (self.company_id,))
        plan_name = maximum_products[0][1]
        maximum_products = maximum_products[0][0]
        if created_products >= maximum_products:
            raise Exception(
                f'Your company has reached the limit of registered products for your current plan {plan_name}. \n'
                f'Limit of products is {maximum_products}, you have {created_products}'
            )
        else:
            # We have to upload the image to the S3 Bucket
            self.image = S3_Instance().upload_image(self.image)
            self.product_id = post(
                '''INSERT INTO product(company_id,sku,name,selling_price,image) 
                VALUES(%s,%s,%s,%s,%s) RETURNING product_id''',
                (self.company_id, self.sku, self.name, self.selling_price, self.image),
             True)


    def load(self, params):
        """
        Method that loads a product from the database using params

        Parameters:
        * id: id of the product

        Returns:

        """

        self.product_id = params['product_id']

        try:
            self.company_id, self.sku, self.name, self.selling_price, self.image = get(
                '''SELECT * FROM product WHERE product_id = %s''', (self.product_id,), True
            )
        except Exception as e:
            return e

    @classmethod
    def obtener_producto(cls,product_id):

        try:
            producto = get('''SELECT * FROM product WHERE product_id = %s''', (product_id,), False)
            return {
                'producto': producto
            }
        except Exception as e:
            return e

    @staticmethod
    def get_products(company_id):
        products = get('''
            SELECT product_id, company_id, sku, name, selling_price, image
            FROM public.product WHERE company_id=%s;
            ''', (company_id,))
        product_list = []
        for product in products:
            product_list.append(
                {
                    'id': product[0],
                    'sku': product[2],
                    'name': product[3],
                    'price': product[4],
                    'image': product[5]
                }
            )

        return product_list, 200
