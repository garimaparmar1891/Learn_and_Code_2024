import unittest
from unittest.mock import patch
import os
from utils.user_input_handler import UserInputHandler

class TestUserInputHandler(unittest.TestCase):

    @patch('builtins.input', return_value='5')
    @patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w'))
    def test_get_valid_quantity(self, mock_stdout, mock_input):
        quantity = UserInputHandler.get_valid_quantity("Enter quantity: ")
        self.assertEqual(quantity, 5)
        mock_stdout.close()

    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w'))
    def test_get_valid_number(self, mock_stdout, mock_input):
        number = UserInputHandler.get_valid_number("Enter a number: ")
        self.assertEqual(number, 10)
        mock_stdout.close()

    @patch('builtins.input', return_value='Test input')
    @patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w'))
    def test_get_required_input(self, mock_stdout, mock_input):
        field = UserInputHandler.get_required_input("Enter a field: ")
        self.assertEqual(field, 'Test input')
        mock_stdout.close()

    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w'))
    def test_get_user_choice(self, mock_stdout, mock_input):
        valid_choices = ['1', '2', '3']
        choice = UserInputHandler.get_user_choice("Choose an option: ", valid_choices)
        self.assertEqual(choice, '2')
        mock_stdout.close()

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w'))
    def test_get_category_selection(self, mock_stdout, mock_input):
        categories = ['1', '2', '3']
        category = UserInputHandler.get_category_selection(categories)
        self.assertEqual(category, '3')
        mock_stdout.close()

if __name__ == '__main__':
    unittest.main()
