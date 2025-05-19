import unittest
from unittest.mock import patch, MagicMock
from http import HTTPStatus
from categories.category_api_handler import CategoryAPIHandler
from config import API_URL


class TestCategoryAPIHandler(unittest.TestCase):

    @patch("requests.get")
    def test_get_request_success(self, mock_get):
        expected_data = {"id": 1, "name": "Electronics"}
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        result = CategoryAPIHandler.get_request("categories/electronics")

        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(f"{API_URL}/categories/electronics")

    @patch("builtins.print")
    @patch("requests.get")
    def test_get_request_failure(self, mock_get, mock_print):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Category not found"
        mock_get.return_value = mock_response

        result = CategoryAPIHandler.get_request("categories/nonexistent")

        self.assertEqual(result, {})
        mock_print.assert_called_once_with("Error: 404 - Category not found")
        mock_get.assert_called_once_with(f"{API_URL}/categories/nonexistent")


if __name__ == '__main__':
    unittest.main()
