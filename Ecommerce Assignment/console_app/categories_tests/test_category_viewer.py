import unittest
from unittest.mock import patch
from categories.category_viewer import CategoryViewer

class TestCategoryViewer(unittest.TestCase):

    @patch('builtins.print')
    def test_display_categories(self, mock_print):
        categories = {
            1: {'name': 'Electronics'},
            2: {'name': 'Clothing'},
            3: {'name': 'Books'}
        }

        CategoryViewer.display(categories)

        mock_print.assert_any_call("\nAvailable Categories:")
        mock_print.assert_any_call("1. Electronics")
        mock_print.assert_any_call("2. Clothing")
        mock_print.assert_any_call("3. Books")

    @patch('builtins.print')
    def test_display_empty_categories(self, mock_print):
        categories = {}

        CategoryViewer.display(categories)

        mock_print.assert_called_once_with("\nAvailable Categories:")

    @patch('builtins.print')
    def test_display_single_category(self, mock_print):
        categories = {
            1: {'name': 'Electronics'}
        }

        CategoryViewer.display(categories)

        mock_print.assert_any_call("\nAvailable Categories:")
        mock_print.assert_any_call("1. Electronics")

if __name__ == '__main__':
    unittest.main()
