import unittest
from unittest.mock import patch, MagicMock
from authentication.login_manager import LoginManager
from utils.server_request_handler import ServerRequestHandler
from utils.user_input_handler import UserInputHandler

class TestLoginManager(unittest.TestCase):

    @patch('utils.server_request_handler.ServerRequestHandler.check_server')
    @patch('utils.server_request_handler.ServerRequestHandler.send_request')
    @patch('utils.user_input_handler.UserInputHandler.get_required_input')
    def test_login_success(self, mock_get_required_input, mock_send_request, mock_check_server):
        mock_check_server.return_value = True 
        mock_get_required_input.side_effect = ["test@example.com", "password123"] 
        mock_send_request.return_value = {"userName": "testuser", "email": "test@example.com"} 

        login_manager = LoginManager()
        response = login_manager.login()

        mock_check_server.assert_called_once()
        mock_send_request.assert_called_once_with("login", {"email": "test@example.com", "password": "password123"})
        self.assertEqual(response, {"userName": "testuser", "email": "test@example.com"})

    @patch('utils.server_request_handler.ServerRequestHandler.check_server')
    @patch('utils.server_request_handler.ServerRequestHandler.send_request')
    @patch('utils.user_input_handler.UserInputHandler.get_required_input')
    def test_login_failure_due_to_server_unavailable(self, mock_get_required_input, mock_send_request, mock_check_server):
        mock_check_server.return_value = False 

        login_manager = LoginManager()
        response = login_manager.login()

        mock_check_server.assert_called_once()
        mock_send_request.assert_not_called()
        self.assertIsNone(response)

    @patch('utils.server_request_handler.ServerRequestHandler.check_server')
    @patch('utils.server_request_handler.ServerRequestHandler.send_request')
    @patch('utils.user_input_handler.UserInputHandler.get_required_input')
    def test_login_failure_due_to_invalid_credentials(self, mock_get_required_input, mock_send_request, mock_check_server):
        mock_check_server.return_value = True
        mock_get_required_input.side_effect = ["test@example.com", "wrongpassword"] 
        mock_send_request.return_value = None

        login_manager = LoginManager()
        response = login_manager.login()

        mock_check_server.assert_called_once()
        mock_send_request.assert_called_once_with("login", {"email": "test@example.com", "password": "wrongpassword"})
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
