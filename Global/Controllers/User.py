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
    try:
        admin_permission(request)
        keep_in_your_garden(request,request.json.get('store_or_company_id'))
        params = {
            'store_or_company_id': request.json.get('store_or_company_id'),
            'username': request.json.get('username'),
            'password': request.json.get('password'),
            'is_admin': request.json.get('is_admin'),
            'type': request.json.get('type')
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
        return {
            'token': user.access_token,
            'type'  : user.type,
            'is_admin': user.is_admin
               }, 200
    except Exception as e:
        return str(e), 200
