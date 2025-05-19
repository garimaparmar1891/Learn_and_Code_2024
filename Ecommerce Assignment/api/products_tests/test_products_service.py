import unittest
from unittest.mock import patch
from http import HTTPStatus
from products.service import ProductService 
from decimal import Decimal


class TestProductService(unittest.TestCase):

    @patch("products.service.ProductModel.get_products_by_category")
    def test_fetch_products_by_category_with_products(self, mock_get_products):
        mock_get_products.return_value = [
            ("Smartphone", Decimal("699.99"), 50),
            ("Laptop", Decimal("1299.99"), 24)
        ]

        expected_output = [
            {
                "name": "Smartphone",
                "price": Decimal("699.99"),
                "quantity_available": 50
            },
            {
                "name": "Laptop",
                "price": Decimal("1299.99"),
                "quantity_available": 24
            }
        ]

        result, status = ProductService.fetch_products_by_category(1)

        self.assertEqual(result, expected_output)
        self.assertEqual(status, HTTPStatus.OK)
        mock_get_products.assert_called_once_with(1)

    @patch("products.service.ProductModel.get_products_by_category")
    def test_fetch_products_by_category_no_products(self, mock_get_products):
        mock_get_products.return_value = []

        result, status = ProductService.fetch_products_by_category(999)

        self.assertEqual(result, {"message": "No products found in this category"})
        self.assertEqual(status, HTTPStatus.OK)
        mock_get_products.assert_called_once_with(999)

if __name__ == "__main__":
    unittest.main()
