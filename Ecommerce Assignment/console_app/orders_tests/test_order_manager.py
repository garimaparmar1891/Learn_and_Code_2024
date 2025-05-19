import unittest
from unittest.mock import patch, MagicMock
from orders.order_manager import OrderManager

class TestOrderManager(unittest.TestCase):

    @patch('orders.order_manager.OrderViewer')
    @patch('orders.order_manager.OrderFetcher')
    def test_view_order_history_displays_orders(self, mock_fetcher_class, mock_viewer_class):
        mock_fetcher = mock_fetcher_class.return_value
        mock_viewer = mock_viewer_class.return_value

        mock_fetcher.get_history.return_value = [{"orderId": 1, "item": "Book"}]

        manager = OrderManager()
        manager.view_order_history(user_id=101)

        mock_fetcher.get_history.assert_called_once_with(101)
        mock_viewer.display.assert_called_once_with([{"orderId": 1, "item": "Book"}])

    @patch('builtins.print')
    @patch('orders.order_manager.OrderAPIHandler.send_post_request')
    def test_place_order_success(self, mock_post, mock_print):
        mock_post.return_value = {
            "message": "Order placed successfully",
            "order_id": 456
        }

        manager = OrderManager()
        manager.place_order(user_id=202)

        mock_post.assert_called_once_with("order/place", {"userId": 202})
        mock_print.assert_called_once_with("\nOrder placed successfully (Order ID: 456)")

    @patch('builtins.print')
    @patch('orders.order_manager.OrderAPIHandler.send_post_request')
    def test_place_order_failure(self, mock_post, mock_print):
        mock_post.return_value = {}

        manager = OrderManager()
        manager.place_order(user_id=303)

        mock_post.assert_called_once_with("order/place", {"userId": 303})
        mock_print.assert_called_once_with("\nFailed to place order.")

if __name__ == '__main__':
    unittest.main()
