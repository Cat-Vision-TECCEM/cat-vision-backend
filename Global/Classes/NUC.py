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




