"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 07/11/2022
    Last update: 07/11/2022
"""
from flask import request
from Global.Classes.Ticket import Ticket


def create_ticket():
    """
    Controller for the route /create

    Method:
    * POST

    Parameters:
    * company_id: id of the company that created the ticket
    * body: content of the ticket
    * status: status of the ticket
    * name: name of the client

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """

    try:
        params = {
            'company_id': request.json.get('company_id'),
            'body': request.json.get('body'),
            'status': request.json.get('status'),
            'name': request.json.get('subject'),
            'username': request.json.get('username')
        }
        ticket = Ticket(params, False)
        return {'success': f'Ticket created with the ticket id: {ticket.ticket_id}'}, 200
    except Exception as e:
        return {'error': str(e)}, 400


def get_ticket():
    """
    Controller for the route /get

    Method:
    * GET

    Parameters:
    * ticket_id: id of the desired ticket

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """

    try:
        ticket_id = request.args.get('ticket_id')
        ticket = Ticket(ticket_id)
        return ticket.load(ticket_id)
    except Exception as e:
        return str(e), 200

