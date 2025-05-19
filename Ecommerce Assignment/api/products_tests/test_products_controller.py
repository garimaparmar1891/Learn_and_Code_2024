import unittest
from unittest.mock import patch
from flask import Flask
from products.controller import ProductController

class ProductControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch("products.controller.ProductService.fetch_products_by_category")
    def test_get_products_by_category(self, mock_fetch_products):
        mock_fetch_products.return_value = ({"products": [{"id": 1, "name": "Test Product"}]}, 200)

        response, status = ProductController.get_products_by_category(1)

        self.assertEqual(status, 200)
        self.assertEqual(response.json, {"products": [{"id": 1, "name": "Test Product"}]})

if __name__ == "__main__":
    unittest.main()
