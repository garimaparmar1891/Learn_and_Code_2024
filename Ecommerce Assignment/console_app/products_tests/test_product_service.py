import unittest
from unittest.mock import patch, MagicMock
from products.product_service import ProductService
import requests 

class TestProductService(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_products_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Product A", "price": 10.0},
            {"name": "Product B", "price": 20.0}
        ]
        mock_get.return_value = mock_response

        products = ProductService.fetch_products(1)

        self.assertEqual(len(products), 2)
        self.assertEqual(products[0]['name'], "Product A")
        self.assertEqual(products[1]['price'], 20.0)

    @patch('requests.get')
    def test_fetch_products_no_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        products = ProductService.fetch_products(1)

        self.assertEqual(products, [])

    @patch('requests.get')
    def test_fetch_products_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        products = ProductService.fetch_products(1)

        self.assertEqual(products, [])

    @patch('requests.get')
    @patch('builtins.print')
    def test_fetch_products_request_exception(self, mock_print, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        products = ProductService.fetch_products(1)

        mock_print.assert_called_once_with("\nError: Unable to fetch products. Please try again later.")
        self.assertEqual(products, [])

if __name__ == '__main__':
    unittest.main()
