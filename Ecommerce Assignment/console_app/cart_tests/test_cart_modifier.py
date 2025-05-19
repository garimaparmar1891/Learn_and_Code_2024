import unittest
from unittest.mock import patch
from cart.cart_modifier import CartModifier
from cart.cart_api_handler import CartAPIHandler
from utils.user_input_handler import UserInputHandler

class TestCartModifier(unittest.TestCase):

    @patch.object(CartAPIHandler, 'send_post_request', return_value=True)
    @patch.object(UserInputHandler, 'get_valid_quantity', return_value=5)
    @patch('builtins.print')
    def test_add_to_cart_success(self, mock_print, mock_get_quantity, mock_send_post_request):
        cart_modifier = CartModifier()
        user_id = 1
        product_name = "Apple"

        cart_modifier.add_to_cart(user_id, product_name)

        mock_send_post_request.assert_called_with(
            "cart/add", {"userId": user_id, "product": product_name, "quantity": 5}
        )

    @patch.object(CartAPIHandler, 'send_post_request', return_value=False)
    @patch.object(UserInputHandler, 'get_valid_quantity', return_value=3)
    @patch('builtins.print')
    def test_add_to_cart_failure(self, mock_print, mock_get_quantity, mock_send_post_request):
        cart_modifier = CartModifier()
        user_id = 1
        product_name = "Banana"

        cart_modifier.add_to_cart(user_id, product_name)

        mock_send_post_request.assert_called_with(
            "cart/add", {"userId": user_id, "product": product_name, "quantity": 3}
        )

    @patch.object(CartAPIHandler, 'send_post_request', return_value=True)
    @patch.object(UserInputHandler, 'get_required_input', return_value="Apple")
    @patch.object(UserInputHandler, 'get_valid_quantity', return_value=2)
    @patch('builtins.print')
    def test_remove_cart_item_success(self, mock_print, mock_get_quantity, mock_get_product, mock_send_post_request):
        cart_modifier = CartModifier()
        user_id = 1
        product_name = "Apple"
        quantity = 2

        cart_modifier.remove_cart_item(user_id)

        mock_send_post_request.assert_called_with(
            "cart/remove", {"userId": user_id, "product": product_name, "quantity": quantity}
        )

        mock_print.assert_called_once()

if __name__ == '__main__':
    unittest.main()
