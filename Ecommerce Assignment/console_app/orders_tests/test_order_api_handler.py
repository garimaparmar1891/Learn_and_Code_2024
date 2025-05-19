import unittest
from unittest.mock import patch, MagicMock
from http import HTTPStatus
import requests
from orders.order_api_handler import OrderAPIHandler
from config import API_URL

class TestOrderAPIHandler(unittest.TestCase):

    @patch('requests.get')
    def test_send_get_request_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_response.json.return_value = {"order_id": 1}
        mock_get.return_value = mock_response

        result = OrderAPIHandler.send_get_request("orders/1")

        mock_get.assert_called_once_with(f"{API_URL}/orders/1", params=None)
        self.assertEqual(result, {"order_id": 1})

    @patch('requests.get')
    def test_send_get_request_failure_status_code(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.NOT_FOUND
        mock_get.return_value = mock_response

        result = OrderAPIHandler.send_get_request("orders/invalid")

        mock_get.assert_called_once_with(f"{API_URL}/orders/invalid", params=None)
        self.assertEqual(result, [])
 
    @patch('orders.order_api_handler.print_server_error')
    @patch('requests.post')
    def test_send_post_request_exception(self, mock_post, mock_print_error):
        mock_post.side_effect = requests.exceptions.RequestException

        result = OrderAPIHandler.send_post_request("orders", data={"item": "book"})

        mock_post.assert_called_once_with(f"{API_URL}/orders", json={"item": "book"})
        mock_print_error.assert_called_once()
        self.assertEqual(result, {"error": "Request failed"})

if __name__ == "__main__":
    unittest.main()
