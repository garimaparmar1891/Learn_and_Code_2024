import unittest
from unittest.mock import patch, MagicMock
from authentication.auth import Auth

class TestAuth(unittest.TestCase):

    @patch('authentication.auth.UserInputHandler.get_user_choice')
    @patch('authentication.auth.SignupManager')
    @patch('authentication.auth.LoginManager')
    def test_handle_session_signup(self, MockLoginManager, MockSignupManager, mock_get_user_choice):
        mock_get_user_choice.return_value = "1"
        mock_signup_instance = MagicMock()
        MockSignupManager.return_value = mock_signup_instance

        auth_instance = Auth()
        auth_instance.handle_session()

        MockSignupManager.assert_called_once()
        mock_signup_instance.signup.assert_called_once()

    @patch('authentication.auth.UserInputHandler.get_user_choice')
    @patch('authentication.auth.SignupManager')
    @patch('authentication.auth.LoginManager')
    def test_handle_session_login(self, MockLoginManager, MockSignupManager, mock_get_user_choice):
        mock_get_user_choice.return_value = "2" 
        mock_login_instance = MagicMock()
        MockLoginManager.return_value = mock_login_instance

        auth_instance = Auth()
        auth_instance.handle_session()

        MockLoginManager.assert_called_once()
        mock_login_instance.login.assert_called_once()

    @patch('authentication.auth.UserInputHandler.get_user_choice')
    @patch('authentication.auth.SignupManager')
    @patch('authentication.auth.LoginManager')
    def test_handle_session_exit(self, MockLoginManager, MockSignupManager, mock_get_user_choice):
        mock_get_user_choice.return_value = "3"

        auth_instance = Auth()
        result = auth_instance.handle_session()

        mock_get_user_choice.assert_called_once()
        self.assertTrue(result) 

    @patch('authentication.auth.UserInputHandler.get_user_choice')
    @patch('authentication.auth.SignupManager')
    @patch('authentication.auth.LoginManager')
    def test_handle_session_invalid_choice(self, MockLoginManager, MockSignupManager, mock_get_user_choice):
        mock_get_user_choice.side_effect = ["4", "1"]

        auth_instance = Auth()
        auth_instance.handle_session()

        mock_get_user_choice.assert_any_call("\n1. Signup\n2. Login\n3. Exit\nChoose an option: ", ["1", "2", "3"])
        mock_get_user_choice.assert_any_call("\n1. Signup\n2. Login\n3. Exit\nChoose an option: ", ["1", "2", "3"])
        MockSignupManager.assert_called_once()

if __name__ == '__main__':
    unittest.main()
