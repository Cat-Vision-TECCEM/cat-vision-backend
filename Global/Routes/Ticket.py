"""
    Routes created for the Ticket
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import Ticket as c

GLOBAL_TICKET_BLUEPRINT = Blueprint('GLOBAL_TICKET_BLUEPRINT', __name__)


@GLOBAL_TICKET_BLUEPRINT.route('/create', methods=['POST'])
def create_ticket():
    """
    Route used to create a new ticket in the databse

    Method:
    * POST

    Parameters:
    * company_id: numeric id of the company
    * body: content of the ticket
    * status: status of the ticket
    * name: name of the client

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.create_ticket()


@GLOBAL_TICKET_BLUEPRINT.route('/get', methods=['GET'])
def get_ticket():
    """
    Route used to get the information of a ticket given the ticket_id

    Method:
    * POST

    Parameters:
    * ticket_id: id of the ticket

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    return c.get_ticket()
