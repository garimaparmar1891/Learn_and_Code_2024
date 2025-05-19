import unittest
from unittest.mock import patch, MagicMock
from authentication.signup_manager import SignupManager
from utils.server_request_handler import ServerRequestHandler
from utils.user_input_handler import UserInputHandler

class TestSignupManager(unittest.TestCase):

    @patch('utils.server_request_handler.ServerRequestHandler.check_server')
    @patch('utils.server_request_handler.ServerRequestHandler.send_request')
    @patch('utils.user_input_handler.UserInputHandler.get_required_input')
    def test_signup_success(self, mock_get_required_input, mock_send_request, mock_check_server):
        mock_check_server.return_value = True
        mock_get_required_input.side_effect = [
            "John Doe", "john.doe@example.com", "password123", "1234567890", "1234 Elm Street"
        ]
        mock_send_request.return_value = {"status": "success"}

        signup_manager = SignupManager()
        response = signup_manager.signup()

        mock_check_server.assert_called_once()
        mock_send_request.assert_called_once_with("signup", {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone_number": "1234567890",
            "address": "1234 Elm Street"
        })
        self.assertIsNone(response)

    @patch('utils.server_request_handler.ServerRequestHandler.check_server')
    @patch('utils.server_request_handler.ServerRequestHandler.send_request')
    @patch('utils.user_input_handler.UserInputHandler.get_required_input')
    def test_signup_failure_due_to_server_unavailable(self, mock_get_required_input, mock_send_request, mock_check_server):
        mock_check_server.return_value = False
       
        signup_manager = SignupManager()
        response = signup_manager.signup()

        mock_check_server.assert_called_once()
        mock_send_request.assert_not_called()
        self.assertIsNone(response)

    @patch('utils.server_request_handler.ServerRequestHandler.check_server')
    @patch('utils.server_request_handler.ServerRequestHandler.send_request')
    @patch('utils.user_input_handler.UserInputHandler.get_required_input')
    def test_signup_failure_due_to_invalid_response(self, mock_get_required_input, mock_send_request, mock_check_server):
        mock_check_server.return_value = True
        mock_get_required_input.side_effect = [
            "John Doe", "john.doe@example.com", "password123", "1234567890", "1234 Elm Street"
        ]
        mock_send_request.return_value = None

        signup_manager = SignupManager()
        response = signup_manager.signup()

        mock_check_server.assert_called_once()
        mock_send_request.assert_called_once_with("signup", {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone_number": "1234567890",
            "address": "1234 Elm Street"
        })
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
