import unittest
from unittest.mock import patch
from orders.order_fetcher import OrderFetcher

class TestOrderFetcher(unittest.TestCase):

    @patch('orders.order_fetcher.OrderAPIHandler.send_get_request')
    def test_get_history_successful_response(self, mock_send_get):
        mock_send_get.return_value = [{"orderId": 1, "item": "Laptop"}]

        result = OrderFetcher.get_history(user_id=101)

        mock_send_get.assert_called_once_with("orders/history", {"userId": 101})
        self.assertEqual(result, [{"orderId": 1, "item": "Laptop"}])

    @patch('orders.order_fetcher.OrderAPIHandler.send_get_request')
    def test_get_history_with_error_message(self, mock_send_get):
        mock_send_get.return_value = {"message": "User not found"}

        result = OrderFetcher.get_history(user_id=999)

        mock_send_get.assert_called_once_with("orders/history", {"userId": 999})
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
