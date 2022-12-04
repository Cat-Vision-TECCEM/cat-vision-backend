"""
    Script that handles the received requests
    Authors: Erick Hernandez Silva, David Rodriguez Fragoso
    Created: 26/10/2022
    Last update: 26/10/2022
"""

from flask import request
from Global.Classes.Company import Company


def create_company():
    """
    Controller for the route /create

    Method:
        * POST

    Parameters:
        * name: The name of the company
        * email: Contact email of the company

    Format:
        * JSON

    Returns:
        * An exception or a 200 status
    """

    try:
        params = {
            'name': request.json['name'],
            'email': request.json['email']
        }
        company = Company(params, False)
        return f'Company {company.name} with id {company.company_id} has been created'

    except Exception as e:
        return {'error': str(e)}, 400

def get_companies():
    """
    Controller for the route /get-all

    Method:
        * GET

    Parameters:
        * Not required

    Format:
        * None

    Returns:
        * An exception or a 200 status
    """

    try:
        return Company.get_all()
    except Exception as e:
        return {'error': str(e)}, 400
