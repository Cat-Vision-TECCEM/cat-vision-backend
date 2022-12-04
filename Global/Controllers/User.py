"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""

from flask import request
from Global.Classes.User import User
from Global.Utils.sessions import admin_permission, keep_in_your_garden


def register():
    """
    Controller for the route /create

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

    try:
        admin_permission(request)
        keep_in_your_garden(request, request.json.get('store_or_company_id'))
        params = {
            'store_or_company_id': request.json.get('store_or_company_id'),
            'username': request.json.get('username'),
            'password': request.json.get('password'),
            'is_admin': request.json.get('is_admin'),
            'type': request.json.get('type'),
            'email': request.json.get('email')
        }
        user = User(params, db=False)
        return {'success': f'User {user.username} created successfully'}, 200
    except Exception as e:
        return {'error': str(e)}, 400


def login():
    """
    Controller for the route /login

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

    try:
        params = {
            'username': request.json.get('username'),
            'password': request.json.get('password'),
        }
        user = User(params)
        return {
                   'token': user.access_token,
                   'type': user.type,
                   'is_admin': user.is_admin,
                   'store_or_company_id': user.store_or_company_id
               }, 200
    except Exception as e:
        return {'error': str(e)}, 400


def recover_password():
    """
    Controller for the route /recover-password

    Method:
        * POST

    Parameters:
        * email: email of the user

    Format:
        * JSON

    Returns:
        * An exception or a 200 status
    """

    try:
        params = {
            'email': request.json.get('email')
        }
        return User.recover_password(params)

    except Exception as e:
        return {'error': str(e)}, 400

def reset_password():
    """
    Controller for the route /reset-password

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

    try:
        params = {
            'email': request.args.get('email'),
            'token': request.args.get('token'),
            'password': request.args.get('password')
        }
        return User.reset_password(params)
    except Exception as e:
        return {'error': str(e)}, 400
