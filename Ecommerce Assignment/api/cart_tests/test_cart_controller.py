import unittest
from unittest.mock import patch
from flask import Flask, request
from http import HTTPStatus
from cart.controller import CartController

app = Flask(__name__)

class TestCartController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch("cart.controller.CartService.add_product_to_cart", return_value=({"message": "Added"}, HTTPStatus.OK))
    def test_add_product_to_cart_success(self, mock_add_product):
        with app.test_request_context(json={"userId": 1, "product": "Apple", "quantity": 2}):
            response, status = CartController.add_product_to_cart(request.json)
            self.assertEqual(status, HTTPStatus.OK)

    def test_add_product_to_cart_missing_fields(self):
        with app.test_request_context(json={"userId": 1, "quantity": 2}):
            response, status = CartController.add_product_to_cart(request.json)
            self.assertEqual(status, HTTPStatus.BAD_REQUEST)

    @patch("cart.controller.CartService.get_cart", return_value=({"items": []}, HTTPStatus.OK))
    def test_get_cart_success(self, mock_get_cart):
        with app.test_request_context():
            response, status = CartController.get_cart(user_id=1)
            self.assertEqual(status, HTTPStatus.OK)

    @patch("cart.controller.CartService.remove_product_from_cart", return_value=({"message": "Removed"}, HTTPStatus.OK))
    def test_remove_product_from_cart_success(self, mock_remove_product):
        with app.test_request_context(json={"userId": 1, "product": "Apple", "quantity": 1}):
            response, status = CartController.remove_product_from_cart(request.json)
            self.assertEqual(status, HTTPStatus.OK)

    def test_remove_product_from_cart_missing_fields(self):
        with app.test_request_context(json={"userId": 1, "quantity": 1}):
            response, status = CartController.remove_product_from_cart(request.json)
            self.assertEqual(status, HTTPStatus.BAD_REQUEST)

if __name__ == "__main__":
    unittest.main()
