import json
from datetime import timedelta

from Global.Utils.db import post, get


class Ticket:

    def __init__(self, params, load=True):

        self.ticket_id = None
        self.company_id = None
        self.body = None
        self.status = None
        self.name = None

        self.load(params) if load else self.create(params)

    def load(self, params):
        self.ticket_id = params['ticket_id']

        try:
            self.ticket_id, self.company_id, self.body, self.status, self.name = get(
                '''SELECT * FROM ticket WHERE ticket_id = %s''',
                (self.ticket_id,),
                False
            )
        except Exception as e:
            return str(e), 400

    def create(self, params):
        self.company_id = params['company_id']
        self.body = params['body']
        self.status = params['status']
        self.name = params['name']

        try:
            self.ticket_id = post(
                '''INSERT INTO ticket(company_id, body, status, name) VALUES (%s,%s,%s,%s) RETURNING ticket_id''',
                (self.company_id, self.body, self.status, self.name),
                True
            )
        except Exception as e:
            return str(e), 400
