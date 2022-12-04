"""
    Class that describes a Ticket
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 26/10/2022
    Last update: 26/10/2022
"""
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
        self.username = params['username']

        self.ticket_id = post(
            '''INSERT INTO ticket(company_id, body, status, name) VALUES (%s,%s,%s,%s) RETURNING ticket_id''',
            (self.company_id, self.body, self.status, self.name),
            True
        )
        self.ticket_id = self.ticket_id[0]
        from flask import current_app
        from flask_mail import Mail, Message
        from flask import render_template
        import os
        company = get("""
                SELECT name from public.company where company_id = %s
                """, (self.company_id,), False)
        with current_app.app_context():
            # Obtenemos el sender email para enviar el correo
            MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
            mail = Mail()
            subject = "Nuevo reporte recibido"
            recipients = [os.environ.get('STORE_REQUEST_EMAIL')]
            sender = ('CatVision', MAIL_USERNAME)
            html = render_template("/new_ticket.html", subject=self.name, username=self.username,
                                   company=company[0])
            msg = Message(subject=subject, recipients=recipients, sender=sender, html=html)
            mail.send(msg)

