from urllib import request
from flask import Blueprint
from Global.Controllers import User as c

GLOBAL_USER_BLUEPRINT = Blueprint('GLOBAL_USER_BLUEPRINT', __name__)


@GLOBAL_USER_BLUEPRINT.route('/create', methods=['POST'])
def register():
    return c.register()

@GLOBAL_USER_BLUEPRINT.route('/login', methods=['POST'])
def login():
    return c.login()

@GLOBAL_USER_BLUEPRINT.route('/recover-password', methods=['POST'])
def recover_password():
    return c.recover_password()