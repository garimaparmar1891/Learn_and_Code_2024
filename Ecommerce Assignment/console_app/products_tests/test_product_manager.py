import unittest
from unittest.mock import patch, MagicMock
from products.product_manager import ProductManager

class TestProductManager(unittest.TestCase):

    @patch('products.product_manager.ProductService.fetch_products')
    @patch('builtins.print')
    def test_browse_products_no_products(self, mock_print, mock_fetch):
        mock_fetch.return_value = []
        manager = ProductManager()
        manager.browse_products(user_id=1, category_id=101)

        mock_fetch.assert_called_once_with(101)
        mock_print.assert_any_call("\nNo products available in this category.")

    @patch('products.product_manager.input', side_effect=['b'])
    @patch('products.product_manager.CartModifier')
    @patch('builtins.print')
    @patch('products.product_manager.ProductService.fetch_products')
    def test_browse_products_user_exits(self, mock_fetch, mock_print, mock_cart, mock_input):
        mock_fetch.return_value = [{'name': 'Phone', 'price': 500}]
        manager = ProductManager()
        manager.browse_products(user_id=1, category_id=101)

        mock_input.assert_called_once()
        mock_cart.return_value.add_to_cart.assert_not_called()

    @patch('products.product_manager.input', side_effect=['phone'])
    @patch('products.product_manager.CartModifier')
    @patch('builtins.print')
    @patch('products.product_manager.ProductService.fetch_products')
    def test_browse_products_add_to_cart(self, mock_fetch, mock_print, mock_cart_class, mock_input):
        mock_cart = mock_cart_class.return_value
        mock_fetch.return_value = [{'name': 'Phone', 'price': 500}]

        manager = ProductManager()
        manager.browse_products(user_id=1, category_id=101)

        mock_cart.add_to_cart.assert_called_once_with(1, 'Phone')

    @patch('products.product_manager.input', side_effect=['invalid', 'b'])
    @patch('products.product_manager.CartModifier')
    @patch('builtins.print')
    @patch('products.product_manager.ProductService.fetch_products')
    def test_browse_products_invalid_choice_then_back(self, mock_fetch, mock_print, mock_cart_class, mock_input):
        mock_fetch.return_value = [{'name': 'Phone', 'price': 500}]
        manager = ProductManager()
        manager.browse_products(user_id=1, category_id=101)

        mock_print.assert_any_call("Invalid product name. Please enter a valid product.")
        mock_cart_class.return_value.add_to_cart.assert_not_called()

if __name__ == '__main__':
    unittest.main()