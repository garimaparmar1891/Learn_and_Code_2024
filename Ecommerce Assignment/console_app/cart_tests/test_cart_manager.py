import unittest
from unittest.mock import patch, MagicMock
from cart.cart_manager import CartManager

class TestCartManager(unittest.TestCase):

    @patch('cart.cart_manager.CartViewer')
    def test_view_cart_with_invalid_user_id(self, mock_cart_viewer):
        manager = CartManager()
        with patch.object(manager, '_handle_invalid_user') as mock_handle_invalid:
            manager.view_cart(None)

            mock_handle_invalid.assert_called_once()

    @patch('cart.cart_manager.CartViewer')
    def test_view_cart_with_empty_cart(self, mock_cart_viewer):
        mock_viewer = mock_cart_viewer.return_value
        mock_viewer.fetch_cart.return_value = []

        manager = CartManager()
        with patch.object(manager, '_handle_empty_cart') as mock_handle_empty:
            manager.view_cart(1)

            mock_viewer.fetch_cart.assert_called_once_with(1)
            mock_handle_empty.assert_called_once()

    @patch('cart.cart_manager.UserInputHandler')
    @patch('cart.cart_manager.CartOrderProcessor')
    @patch('cart.cart_manager.CartModifier')
    @patch('cart.cart_manager.CartViewer')
    def test_view_cart_with_valid_user_and_items(self, mock_viewer_cls, mock_modifier_cls, mock_processor_cls, mock_input_handler):
        mock_viewer = mock_viewer_cls.return_value
        mock_viewer.fetch_cart.return_value = [{'product': 'Book', 'quantity': 1, 'price': 10}]
        mock_input_handler.get_user_choice.side_effect = ["3"]

        manager = CartManager()

        manager.view_cart(1)

        mock_viewer.fetch_cart.assert_called_once_with(1)
        mock_viewer.display_cart.assert_called_once()
        mock_input_handler.get_user_choice.assert_called_once()


if __name__ == '__main__':
    unittest.main()
