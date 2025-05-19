import unittest
from unittest.mock import patch, MagicMock
from categories.category_manager import CategoryManager

class TestCategoryManager(unittest.TestCase):

    @patch("categories.category_manager.ProductManager")
    @patch("categories.category_manager.UserInputHandler")
    @patch("categories.category_manager.CategoryViewer")
    @patch("categories.category_manager.CategoryFetcher")
    def test_browse_categories_success(self, mock_fetcher, mock_viewer, mock_input_handler, mock_product_manager):
        mock_fetcher().get_categories.return_value = [{"id": 1, "name": "Electronics"}]
        mock_input_handler.get_category_selection.return_value = 1

        category_manager = CategoryManager()

        category_manager.browse_categories(user_id=123)

        mock_viewer().display.assert_called_once_with([{"id": 1, "name": "Electronics"}])
        mock_input_handler.get_category_selection.assert_called_once_with([{"id": 1, "name": "Electronics"}])
        mock_product_manager().browse_products.assert_called_once_with(123, 1)

    @patch("categories.category_manager.ProductManager")
    @patch("categories.category_manager.UserInputHandler")
    @patch("categories.category_manager.CategoryViewer")
    @patch("categories.category_manager.CategoryFetcher")
    @patch("builtins.print")
    def test_browse_categories_empty_list(self, mock_print, mock_fetcher, mock_viewer, mock_input_handler, mock_product_manager):
        mock_fetcher().get_categories.return_value = []

        category_manager = CategoryManager()

        category_manager.browse_categories(user_id=456)

        mock_print.assert_called_once_with("\nNo categories available.")
        mock_viewer().display.assert_not_called()
        mock_input_handler.get_category_selection.assert_not_called()
        mock_product_manager().browse_products.assert_not_called()

    @patch("categories.category_manager.ProductManager")
    @patch("categories.category_manager.UserInputHandler")
    @patch("categories.category_manager.CategoryViewer")
    @patch("categories.category_manager.CategoryFetcher")
    def test_browse_categories_user_cancels_selection(self, mock_fetcher, mock_viewer, mock_input_handler, mock_product_manager):
        mock_fetcher().get_categories.return_value = [{"id": 1, "name": "Books"}]
        mock_input_handler.get_category_selection.return_value = None

        category_manager = CategoryManager()

        category_manager.browse_categories(user_id=789)

        mock_viewer().display.assert_called_once()
        mock_input_handler.get_category_selection.assert_called_once()
        mock_product_manager().browse_products.assert_not_called()


if __name__ == "__main__":
    unittest.main()
