import unittest
from unittest.mock import patch, MagicMock
from utils.check_server import is_server_available, print_server_error
from utils.server_request_handler import ServerRequestHandler
from http import HTTPStatus
from config import API_URL
import requests

class TestServerRequestHandler(unittest.TestCase):

    @patch('requests.get')
    @patch('requests.post')
    def test_send_request(self, mock_post, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_response.json.return_value = {"message": "success"}
        mock_get.return_value = mock_response

        handler = ServerRequestHandler()
        response = handler.send_request('test-endpoint')

        mock_get.assert_called_once_with(f"{API_URL}/test-endpoint")
        self.assertEqual(response, {"message": "success"})

        mock_post.return_value = mock_response
        response_post = handler.send_request('test-endpoint', data={"key": "value"})

        mock_post.assert_called_once_with(f"{API_URL}/test-endpoint", json={"key": "value"})
        self.assertEqual(response_post, {"message": "success"})


if __name__ == '__main__':
    unittest.main()
