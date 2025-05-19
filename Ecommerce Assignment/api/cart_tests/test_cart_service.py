import unittest
from unittest.mock import patch
from http import HTTPStatus
from cart.service import CartService

class TestCartService(unittest.TestCase):

    @patch("cart.service.CartModel.get_product_id", return_value=[1])
    @patch("cart.service.CartModel.add_product_to_cart", return_value=True)
    def test_add_product_to_cart_success(self, mock_add_product, mock_get_product):
        user_id = 1
        product_name = "Apple"
        quantity = 2
        
        result, status = CartService.add_product_to_cart(user_id, product_name, quantity)
        
        mock_get_product.assert_called_with(product_name)
        
        mock_add_product.assert_called_with(user_id, 1, quantity)
        
        self.assertEqual(result.get("message"), "Product added to cart successfully!")
        self.assertEqual(status, HTTPStatus.OK)

    @patch("cart.service.CartModel.get_product_id", return_value=None)
    def test_add_product_to_cart_product_not_found(self, mock_get_product):
        user_id = 1
        product_name = "NonExistentProduct"
        quantity = 2
        
        result, status = CartService.add_product_to_cart(user_id, product_name, quantity)
        
        mock_get_product.assert_called_with(product_name)
        
        self.assertEqual(result.get("error"), "Product not found")
        self.assertEqual(status, HTTPStatus.NOT_FOUND)

    @patch("cart.service.CartModel.get_cart_items", return_value=[("Apple", 2, 10.0, "2025-05-01")])
    def test_get_cart_with_items(self, mock_get_cart_items):
        user_id = 1
        
        result, status = CartService.get_cart(user_id)
        
        mock_get_cart_items.assert_called_with(user_id)
        
        self.assertIn("cart", result)
        self.assertEqual(len(result["cart"]), 1)
        self.assertEqual(result["cart"][0]["product"], "Apple")


        self.assertEqual(status, HTTPStatus.OK)

    @patch("cart.service.CartModel.get_cart_items", return_value=[])
    def test_get_cart_empty(self, mock_get_cart_items):
        user_id = 1
        
        result, status = CartService.get_cart(user_id)
        
        mock_get_cart_items.assert_called_with(user_id)
        
        self.assertEqual(result.get("message"), "Your cart is empty")
        self.assertEqual(status, HTTPStatus.OK)

    @patch("cart.service.CartModel.get_product_id", return_value=[1])
    @patch("cart.service.CartModel.remove_product_from_cart", return_value=({"message": "Product removed from cart"}, HTTPStatus.OK))  # Mocking successful removal
    def test_remove_product_from_cart_success(self, mock_remove_product, mock_get_product):
        user_id = 1
        product_name = "Apple"
        quantity = 1
        
        result, status = CartService.remove_product_from_cart(user_id, product_name, quantity)
        
        mock_get_product.assert_called_with(product_name)
        
        mock_remove_product.assert_called_with(user_id, 1, quantity)
        
        self.assertEqual(result.get("message"), "Product removed from cart")
        self.assertEqual(status, HTTPStatus.OK)

    @patch("cart.service.CartModel.get_product_id", return_value=None)
    def test_remove_product_from_cart_product_not_found(self, mock_get_product):
        user_id = 1
        product_name = "NonExistentProduct"
        quantity = 1
        
        result, status = CartService.remove_product_from_cart(user_id, product_name, quantity)
        
        mock_get_product.assert_called_with(product_name)
        
        self.assertEqual(result.get("error"), "Product not found")
        self.assertEqual(status, HTTPStatus.NOT_FOUND)

if __name__ == "__main__":
    unittest.main()
