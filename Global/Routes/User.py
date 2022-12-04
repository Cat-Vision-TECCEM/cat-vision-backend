"""
    Routes created for the User
    Authors: Erick Hernandez Silva
    Created: 24/10/2022
    Last update: 04/12/2022
"""

from flask import Blueprint
from Global.Controllers import User as c

GLOBAL_USER_BLUEPRINT = Blueprint('GLOBAL_USER_BLUEPRINT', __name__)


@GLOBAL_USER_BLUEPRINT.route('/create', methods=['POST'])
def register():
    """
    Route used to create a new user in the database

    Method:
    * POST

    Parameters:
    * store_or_company_id: numeric id of the store or company
    * username: name of the user
    * password: login password of the user
    * is_admin: true if the user is admin, otherwise false
    * type: type of the account: company or store
    * email: email of the user

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.register()

@GLOBAL_USER_BLUEPRINT.route('/login', methods=['POST'])
def login():
    """
    Route used to login to the application

    Method:
    * POST

    Parameters:
    * username: name of the user
    * password: login password of the user

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.login()

@GLOBAL_USER_BLUEPRINT.route('/recover-password', methods=['POST'])
def recover_password():
    """
    Route used to send the user a password recovery email

    Method:
    * POST

    Parameters:
    * email: email of the user

    Format:
    * JSON

    Returns:
    * An exception or a 200 status
    """
    return c.recover_password()

@GLOBAL_USER_BLUEPRINT.route('/reset-password', methods=['GET'])
def reset_password():
    """
    Route used to send the user a password recovery email

    Method:
    * GET

    Parameters:
    * email: email of the user
    * token: token that was sent in the password recovery email
    * password: new password of the user

    Format:
    * QueryParams

    Returns:
    * An exception or a 200 status
    """
    return c.reset_password()