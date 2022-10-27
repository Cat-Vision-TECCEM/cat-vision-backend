"""
    Class that describes a product
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 26/10/2022
    Last update: 26/10/2022
"""
from Global.Utils.db import post, get
from json import load
from venv import create


class Product:

    def __init__(self, params, load =True):
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

        self.company_id = params['id']
        self.sku = params['sku']
        self.name = params['name']
        self.selling_price = params['selling_price']
        self.image = params['image']

        try:
            self.product_id = post('''INSERT INTO product(company_id,sku,name,selling_price,image) VALUES(%s,%s,%s,%s) 
            RETURNING product_id''', (self.company_id, self.sku, self.name, self.selling_price, self.image), True)
        except Exception as e:
            return e

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

