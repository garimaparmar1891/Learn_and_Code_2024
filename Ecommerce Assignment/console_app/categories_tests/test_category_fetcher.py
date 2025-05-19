import unittest
from unittest.mock import patch
from categories.category_fetcher import CategoryFetcher

class TestCategoryFetcher(unittest.TestCase):

    @patch('categories.category_fetcher.CategoryAPIHandler.get_request')
    def test_get_categories_success(self, mock_get_request):
        mock_get_request.return_value = [{'id': 1, 'name': 'Electronics'}, {'id': 2, 'name': 'Clothing'}]
        
        categories = CategoryFetcher.get_categories()

        mock_get_request.assert_called_once_with('categories')

        self.assertEqual(len(categories), 2)
        self.assertEqual(categories[0]['name'], 'Electronics')
        self.assertEqual(categories[1]['name'], 'Clothing')

    @patch('categories.category_fetcher.CategoryAPIHandler.get_request')
    def test_get_categories_empty_response(self, mock_get_request):
        mock_get_request.return_value = []

        categories = CategoryFetcher.get_categories()

        mock_get_request.assert_called_once_with('categories')

        self.assertEqual(categories, [])

    @patch('categories.category_fetcher.CategoryAPIHandler.get_request')
    def test_get_categories_api_error(self, mock_get_request):
        mock_get_request.return_value = {}

        categories = CategoryFetcher.get_categories()

        mock_get_request.assert_called_once_with('categories')

        self.assertEqual(categories, {})

if __name__ == '__main__':
    unittest.main()
