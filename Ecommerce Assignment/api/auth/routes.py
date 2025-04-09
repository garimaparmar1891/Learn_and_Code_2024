from flask import request, jsonify
from http import HTTPStatus
from . import auth_bp
from .controller import AuthController

@auth_bp.route("/signup", methods=["POST"])
def user_signup():
    user_details = request.json
    response, status = AuthController.user_signup(user_details)
    return jsonify(response), HTTPStatus(status)

@auth_bp.route("/login", methods=["POST"])
def user_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), HTTPStatus.BAD_REQUEST

    response, status = AuthController.user_login(email, password)
    return jsonify(response), HTTPStatus(status)
