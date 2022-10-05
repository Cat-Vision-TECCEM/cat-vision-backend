from flask import Blueprint, jsonify

example = Blueprint("example", __name__, url_prefix="/example")


@example.route("/", methods=['GET'])
def test():
    return "Welcome, example", 200