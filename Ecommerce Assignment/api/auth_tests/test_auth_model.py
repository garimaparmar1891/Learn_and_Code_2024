import unittest
from unittest.mock import patch, MagicMock
from auth.model import UserModel

class TestUserModel(unittest.TestCase):

    @patch("auth.model.get_database_connection")
    def test_user_exists_returns_true_if_user_found(self, mock_get_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (1,)
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        result = UserModel.user_exists("test@example.com")
        self.assertTrue(result)

    @patch("auth.model.get_database_connection")
    def test_user_exists_returns_false_if_user_not_found(self, mock_get_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        result = UserModel.user_exists("missing@example.com")
        self.assertFalse(result)

    @patch("auth.model.get_database_connection")
    @patch("auth.model.bcrypt.hashpw")
    def test_create_user_success(self, mock_hashpw, mock_get_conn):
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        result = UserModel.create_user("John", "john@example.com", "secret", "1234567890", "123 Street")
        self.assertTrue(result)

    @patch("auth.model.get_database_connection")
    def test_get_user_by_email_returns_data(self, mock_get_conn):
        expected_user = (1, "Jane", "hashed_pwd")
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = expected_user
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        result = UserModel.get_user_by_email("jane@example.com")
        self.assertEqual(result, expected_user)

if __name__ == "__main__":
    unittest.main()
