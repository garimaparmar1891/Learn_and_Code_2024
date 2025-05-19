import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from orders.model import OrderModel

class TestOrderModel(unittest.TestCase):

    @patch('orders.model.get_database_connection')
    def test_get_total_cart_amount_returns_correct_sum(self, mock_get_conn):
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [150.0]

        # Act
        result = OrderModel.get_total_cart_amount(user_id=1)

        # Assert
        self.assertEqual(result, 150.0)
        mock_cursor.execute.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('orders.model.get_database_connection')
    def test_create_order_returns_order_id_and_date(self, mock_get_conn):
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [101]  # Simulate inserted order ID

        # Act
        order_id, order_date = OrderModel.create_order(user_id=2, total_amount=99.99)

        # Assert
        self.assertEqual(order_id, 101)
        self.assertIsNotNone(order_date)
        self.assertIsInstance(order_date, str)
        mock_cursor.execute.assert_any_call("SELECT @@IDENTITY")
        mock_conn.commit.assert_called_once()

    @patch('orders.model.get_database_connection')
    def test_clear_cart_executes_delete_query(self, mock_get_conn):
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Act
        OrderModel.clear_cart(user_id=3)

        # Assert
        mock_cursor.execute.assert_called_once_with("DELETE FROM Cart WHERE user_id = ?", (3,))
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
