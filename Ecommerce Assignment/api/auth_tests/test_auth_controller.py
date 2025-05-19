import unittest
from unittest.mock import patch
from http import HTTPStatus
from flask import Flask
from auth.controller import AuthController

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/signup', view_func=AuthController.user_signup, methods=['POST'])
        self.app.add_url_rule('/login', view_func=AuthController.user_login, methods=['POST'])
        self.client = self.app.test_client()

    @patch("auth.controller.AuthService.register_user", return_value=({"message": "User registered successfully"}, HTTPStatus.CREATED))
    def test_user_signup_success_message(self, _):
        response = self.client.post('/signup', json={
            "name": "John",
            "email": "john@example.com",
            "password": "secret",
            "phone_number": "1234567890",
            "address": "Street 1"
        })
        self.assertIn("message", response.get_json())

    @patch("auth.controller.AuthService.authenticate_user", return_value=({"userId": 1, "userName": "John"}, HTTPStatus.OK))
    def test_user_login_success_status(self, _):
        response = self.client.post('/login', json={
            "email": "john@example.com",
            "password": "secret"
        })
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @patch("auth.controller.AuthService.authenticate_user", return_value=({"userId": 1, "userName": "John"}, HTTPStatus.OK))
    def test_user_login_success_response_has_user_id(self, _):
        response = self.client.post('/login', json={
            "email": "john@example.com",
            "password": "secret"
        })
        self.assertIn("userId", response.get_json())

    def test_user_login_missing_email_error(self):
        response = self.client.post('/login', json={
            "password": "secret"
        })
        self.assertIn("error", response.get_json())

    def test_user_login_missing_password_error(self):
        response = self.client.post('/login', json={
            "email": "john@example.com"
        })
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main()
