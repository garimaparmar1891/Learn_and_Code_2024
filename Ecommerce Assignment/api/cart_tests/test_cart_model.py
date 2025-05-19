import unittest
from unittest.mock import patch
from http import HTTPStatus
from cart.model import CartModel

class TestCartModel(unittest.TestCase):

    @patch("cart.model.CartModel._execute_select_query")
    def test_get_product_id_found(self, mock_execute_select_query):
        mock_execute_select_query.return_value = [(1,)]
        product_id = CartModel.get_product_id("Apple")
        self.assertEqual(product_id, (1,))

    @patch("cart.model.CartModel._execute_select_query")
    def test_get_product_id_not_found(self, mock_execute_select_query):
        mock_execute_select_query.return_value = []
        product_id = CartModel.get_product_id("Apple")
        self.assertIsNone(product_id)

    @patch("cart.model.CartModel._get_existing_quantity", return_value=None)
    @patch("cart.model.CartModel._insert_new_cart_item", return_value=True)
    def test_add_product_to_cart_new_item(self, mock_insert_new_item, mock_get_existing_quantity):
        user_id = 1
        product_id = 1
        quantity = 2
        
        result = CartModel.add_product_to_cart(user_id, product_id, quantity)
        
        self.assertTrue(mock_insert_new_item.called)
        self.assertEqual(result, True)

    @patch("cart.model.CartModel._get_existing_quantity", return_value=5)
    @patch("cart.model.CartModel._update_cart_quantity", return_value=True)
    def test_add_product_to_cart_existing_item(self, mock_update_cart, mock_get_existing_quantity):
        user_id = 1
        product_id = 1
        quantity = 3
        
        result = CartModel.add_product_to_cart(user_id, product_id, quantity)
        
        self.assertTrue(mock_update_cart.called)
        self.assertEqual(result, True)

    @patch("cart.model.CartModel._get_existing_quantity", return_value=5)
    @patch("cart.model.CartModel._execute_commit_query", return_value=True)
    def test_remove_product_from_cart_completely(self, mock_execute_commit, mock_get_existing_quantity):
        user_id = 1
        product_id = 1
        quantity_to_remove = 5
        
        response, status = CartModel.remove_product_from_cart(user_id, product_id, quantity_to_remove)
        
        self.assertEqual(status, HTTPStatus.OK)
        self.assertEqual(response["message"], "Product removed from cart completely!")

    @patch("cart.model.CartModel._get_existing_quantity", return_value=3)
    @patch("cart.model.CartModel._execute_commit_query", return_value=True)
    def test_remove_product_from_cart_partial(self, mock_execute_commit, mock_get_existing_quantity):
        user_id = 1
        product_id = 1
        quantity_to_remove = 2
        
        response, status = CartModel.remove_product_from_cart(user_id, product_id, quantity_to_remove)
        
        self.assertEqual(status, HTTPStatus.OK)
        self.assertEqual(response["message"], "Updated cart: 1 items left")

    @patch("cart.model.CartModel._get_existing_quantity", return_value=None)
    def test_remove_product_from_cart_not_found(self, mock_get_existing_quantity):
        user_id = 1
        product_id = 1
        quantity_to_remove = 1
        
        response, status = CartModel.remove_product_from_cart(user_id, product_id, quantity_to_remove)
        
        self.assertEqual(status, HTTPStatus.NOT_FOUND)
        self.assertEqual(response["error"], "Product not found in cart")

if __name__ == "__main__":
    unittest.main()
