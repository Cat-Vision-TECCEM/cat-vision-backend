"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
from flask import request
from Global.Classes.User import User


def register():
    try:
        params = {
            'store_or_company_id': request.json.get('store_or_company_id'),
            'username': request.json.get('username'),
            'password': request.json.get('password'),
            'is_admin': request.json.get('is_admin'),
        }
        user = User(params, db=False)
        return f'User {user.username} created successfully', 200
    except Exception as e:
        return str(e), 400


def login():
    try:
        params = {
            'username': request.json.get('username'),
            'password': request.json.get('password'),
        }
        user = User(params)
        return 'Logged in', 200
    except Exception as e:
        return str(e), 200
