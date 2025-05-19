import unittest
import bcrypt
from unittest.mock import patch
from http import HTTPStatus
from auth.service import AuthService

class TestAuthService(unittest.TestCase):

    @patch("auth.service.UserModel.user_exists", return_value=True)
    def test_register_user_already_exists_returns_bad_request(self, _):
        user_details = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "securepassword",
            "phone_number": "1234567890",
            "address": "123 Main St"
        }
        _, status = AuthService.register_user(user_details)
        self.assertEqual(status, HTTPStatus.BAD_REQUEST)

    @patch("auth.service.UserModel.user_exists", return_value=False)
    @patch("auth.service.UserModel.create_user", return_value=True)
    def test_register_user_success_returns_created_status(self, *_):
        user_details = {
            "name": "New User",
            "email": "new@example.com",
            "password": "securepassword",
            "phone_number": "0987654321",
            "address": "456 Side St"
        }
        response, status = AuthService.register_user(user_details)
        self.assertEqual(status, HTTPStatus.CREATED)

    @patch("auth.service.UserModel.user_exists", return_value=False)
    @patch("auth.service.UserModel.create_user", return_value=False)
    def test_register_user_failure_returns_error(self, *_):
        user_details = {
            "name": "Fail User",
            "email": "fail@example.com",
            "password": "securepassword",
            "phone_number": "0000000000",
            "address": "789 Nowhere"
        }
        response, status = AuthService.register_user(user_details)
        self.assertIn("error", response)

    @patch("auth.service.UserModel.get_user_by_email", return_value=None)
    def test_authenticate_user_invalid_email_error(self, _):
        response, status = AuthService.authenticate_user("fake@example.com", "wrongpassword")
        self.assertIn("error", response)

    @patch("auth.service.UserModel.get_user_by_email", return_value=(1, "Valid User", bcrypt.hashpw(b"password123", bcrypt.gensalt()).decode()))
    def test_authenticate_user_success_status(self, _):
        response, status = AuthService.authenticate_user("valid@example.com", "password123")
        self.assertEqual(status, HTTPStatus.OK)

    @patch("auth.service.UserModel.get_user_by_email", return_value=(1, "Valid User", bcrypt.hashpw(b"password123", bcrypt.gensalt()).decode()))
    def test_authenticate_user_success_response_contains_user_id(self, _):
        response, status = AuthService.authenticate_user("valid@example.com", "password123")
        self.assertIn("userId", response)

    @patch("auth.service.UserModel.get_user_by_email", return_value=(1, "Valid User", bcrypt.hashpw(b"password123", bcrypt.gensalt()).decode()))
    def test_authenticate_user_success_response_contains_user_name(self, _):
        response, status = AuthService.authenticate_user("valid@example.com", "password123")
        self.assertIn("userName", response)

    @patch("auth.service.UserModel.get_user_by_email", return_value=(2, "Another User", bcrypt.hashpw(b"correctpassword", bcrypt.gensalt()).decode()))
    def test_authenticate_user_wrong_password_status(self, _):
        response, status = AuthService.authenticate_user("user@example.com", "wrongpassword")
        self.assertEqual(status, HTTPStatus.UNAUTHORIZED)

if __name__ == "__main__":
    unittest.main()
