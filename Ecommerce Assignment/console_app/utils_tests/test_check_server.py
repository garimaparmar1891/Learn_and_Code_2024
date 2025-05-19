import unittest
from unittest.mock import patch, MagicMock
from utils import check_server
from http import HTTPStatus
from config import API_URL

class TestCheckServer(unittest.TestCase):

    @patch("utils.check_server.requests.get")
    def test_is_server_available_true(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_get.return_value = mock_response

        result = check_server.is_server_available()
        self.assertTrue(result)
        mock_get.assert_called_once_with(f"{API_URL}/health")

    @patch("utils.check_server.requests.get")
    def test_is_server_available_false_due_to_status(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        mock_get.return_value = mock_response

        result = check_server.is_server_available()
        self.assertFalse(result)
        mock_get.assert_called_once_with(f"{API_URL}/health")

    @patch("builtins.print")
    def test_print_server_error(self, mock_print):
        check_server.print_server_error()
        mock_print.assert_called_once_with("Error: Unable to connect to the server. Please try again later.")

if __name__ == "__main__":
    unittest.main()
