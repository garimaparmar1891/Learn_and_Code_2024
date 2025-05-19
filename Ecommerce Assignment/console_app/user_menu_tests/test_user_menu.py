import unittest
from unittest.mock import MagicMock, patch
from user_menu.user_menu import UserMenu

class TestUserMenu(unittest.TestCase):

    @patch("user_menu.menu_manager.MenuManager.display_user_menu", side_effect=["1", "4"])
    def test_display_menu_calls_browse_categories(self, mock_display_menu):
        mock_category_manager = MagicMock()
        mock_cart_manager = MagicMock()
        mock_order_manager = MagicMock()

        user_menu = UserMenu(mock_category_manager, mock_cart_manager, mock_order_manager)
        
        result = user_menu.display_menu(user_id=123)

        mock_category_manager.browse_categories.assert_called_once_with(123)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
