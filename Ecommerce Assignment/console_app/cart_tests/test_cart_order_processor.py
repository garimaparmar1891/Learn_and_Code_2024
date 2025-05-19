import unittest
from unittest.mock import patch
from cart.cart_order_processor import CartOrderProcessor
from cart.cart_api_handler import CartAPIHandler

class TestCartOrderProcessor(unittest.TestCase):

    @patch.object(CartAPIHandler, 'send_post_request', return_value=True)
    def test_place_order_success(self, mock_send_post_request):

        cart_order_processor = CartOrderProcessor()
        user_id = 123
        
        with patch('builtins.print') as mock_print:
            cart_order_processor.place_order(user_id)
            
            mock_send_post_request.assert_called_with("order/place", {"userId": user_id})
            
            mock_print.assert_called_with("Order placed successfully!")

    @patch.object(CartAPIHandler, 'send_post_request', return_value=False)
    def test_place_order_failure(self, mock_send_post_request):

        cart_order_processor = CartOrderProcessor()
        user_id = 123
        
        with patch('builtins.print') as mock_print:
            cart_order_processor.place_order(user_id)
            
            mock_send_post_request.assert_called_with("order/place", {"userId": user_id})
            
            mock_print.assert_called_with("Order placement failed.")

if __name__ == '__main__':
    unittest.main()
