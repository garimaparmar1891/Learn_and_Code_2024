import unittest
from unittest.mock import patch, MagicMock
from cart.cart_api_handler import CartAPIHandler
from config import API_URL
import requests

class TestCartAPIHandler(unittest.TestCase):

    @patch('requests.get')
    def test_send_get_request_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"item": "apple", "quantity": 2}
        mock_get.return_value = mock_response

        result = CartAPIHandler.send_get_request("cart/items")

        mock_get.assert_called_once_with(f"{API_URL}/cart/items")
        self.assertEqual(result, {"item": "apple", "quantity": 2})


    @patch('requests.post')
    def test_send_post_request_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Item added to cart"}
        mock_post.return_value = mock_response

        payload = {"item_id": 1, "quantity": 2}

        result = CartAPIHandler.send_post_request("cart/add", payload)

        mock_post.assert_called_once_with(f"{API_URL}/cart/add", json=payload)
        self.assertEqual(result, {"message": "Item added to cart"})

    @patch('requests.post')
    def test_send_post_request_invalid_status_code(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"message": "Error occurred"}
        mock_post.return_value = mock_response

        payload = {"item_id": 1, "quantity": 2}

        result = CartAPIHandler.send_post_request("cart/add", payload)

        mock_post.assert_called_once_with(f"{API_URL}/cart/add", json=payload)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
