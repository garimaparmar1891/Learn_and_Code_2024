import unittest
from unittest.mock import patch, MagicMock
from session.session_manager import SessionManager
from authentication.auth import Auth

class TestSessionManager(unittest.TestCase):

    @patch("builtins.input", side_effect=["1"])
    def test_handle_session_signup(self, mock_input):
        mock_signup = MagicMock()
        mock_signup.signup.return_value = {"id": 1, "name": "testuser"}
        
        mock_auth = MagicMock(spec=Auth)
        mock_auth.signup = mock_signup
        mock_auth.login = MagicMock()

        session_manager = SessionManager(mock_auth)
        user = session_manager.handle_session()

        self.assertEqual(user, {"id": 1, "name": "testuser"})
        mock_signup.signup.assert_called_once()

    @patch("builtins.input", side_effect=["2"])
    def test_handle_session_login(self, mock_input):
        mock_login = MagicMock()
        mock_login.login.return_value = {"id": 2, "name": "john"}

        mock_auth = MagicMock(spec=Auth)
        mock_auth.login = mock_login
        mock_auth.signup = MagicMock()

        session_manager = SessionManager(mock_auth)
        user = session_manager.handle_session()

        self.assertEqual(user, {"id": 2, "name": "john"})
        mock_login.login.assert_called_once()

    @patch("builtins.input", side_effect=["3"])
    def test_handle_session_exit(self, mock_input):
        mock_auth = MagicMock(spec=Auth)
        session_manager = SessionManager(mock_auth)

        result = session_manager.handle_session()
        self.assertEqual(result, {"status": "exit"})

    @patch("builtins.input", side_effect=["invalid", "2"])
    def test_handle_session_invalid_then_login(self, mock_input):
        mock_login = MagicMock()
        mock_login.login.return_value = {"id": 3, "name": "doe"}

        mock_auth = MagicMock(spec=Auth)
        mock_auth.login = mock_login
        mock_auth.signup = MagicMock()

        session_manager = SessionManager(mock_auth)
        user = session_manager.handle_session()

        self.assertEqual(user, {"id": 3, "name": "doe"})
        self.assertEqual(mock_login.login.call_count, 1)

if __name__ == "__main__":
    unittest.main()
