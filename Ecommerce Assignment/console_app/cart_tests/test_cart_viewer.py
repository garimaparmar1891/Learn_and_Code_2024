import unittest
from unittest.mock import patch
from cart.cart_viewer import CartViewer
from cart.cart_api_handler import CartAPIHandler

class TestCartViewer(unittest.TestCase):

    @patch.object(CartAPIHandler, 'send_get_request', return_value={"cart": [
        {"product": "Laptop", "quantity": 2, "price": 799.99, "added_at": "2025-05-01T14:00:00"},
        {"product": "Mouse", "quantity": 1, "price": 25.99, "added_at": "2025-05-01T15:00:00"}
    ]})
    def test_fetch_cart_success(self, mock_send_get_request):
        cart_viewer = CartViewer()
        user_id = 123

        cart_items = cart_viewer.fetch_cart(user_id)

        self.assertEqual(len(cart_items), 2)
        self.assertEqual(cart_items[0]['product'], "Laptop")
        self.assertEqual(cart_items[1]['product'], "Mouse")
        mock_send_get_request.assert_called_with(f"cart/{user_id}")

    @patch.object(CartAPIHandler, 'send_get_request', return_value=None)
    def test_fetch_cart_empty(self, mock_send_get_request):
        cart_viewer = CartViewer()
        user_id = 123

        cart_items = cart_viewer.fetch_cart(user_id)

        self.assertEqual(cart_items, [])
        mock_send_get_request.assert_called_with(f"cart/{user_id}")

    @patch('builtins.print')
    def test_display_cart(self, mock_print):
        cart_viewer = CartViewer()
        cart_items = [
            {"product": "Laptop", "quantity": 2, "price": 799.99, "added_at": "2025-05-01T14:00:00"},
            {"product": "Mouse", "quantity": 1, "price": 25.99, "added_at": "2025-05-01T15:00:00"}
        ]

        cart_viewer.display_cart(cart_items)

        mock_print.assert_any_call("\nYour Cart:")
        mock_print.assert_any_call("- Laptop (Qty: 2) (Total Price: $1599.98) Added on: 2025-05-01T14:00:00")
        mock_print.assert_any_call("- Mouse (Qty: 1) (Total Price: $25.99) Added on: 2025-05-01T15:00:00")

if __name__ == '__main__':
    unittest.main()
