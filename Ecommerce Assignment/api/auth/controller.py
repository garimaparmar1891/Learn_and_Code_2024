from flask import request, jsonify
from http import HTTPStatus
from .service import AuthService 

class AuthController:
    @staticmethod
    def user_signup():
        user_details = request.json
        response, status = AuthService.register_user(user_details)
        return jsonify(response), HTTPStatus(status)

    @staticmethod
    def user_login():
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), HTTPStatus.BAD_REQUEST

        response, status = AuthService.authenticate_user(email, password)
        return jsonify(response), HTTPStatus(status)
