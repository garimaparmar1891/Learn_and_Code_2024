import unittest
from unittest.mock import patch, MagicMock
from products.model import ProductModel
from decimal import Decimal

class ProductModelTestCase(unittest.TestCase):

    @patch("products.model.get_database_connection")
    def test_get_products_by_category(self, mock_get_db_conn):
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            ("Product A", Decimal("10.0"), 100),
            ("Laptop", Decimal("1299.99"), 24)
        ]

        category_id = 1
        result = ProductModel.get_products_by_category(category_id)

        self.assertEqual(result[0], ("Product A", Decimal("10.0"), 100))
        self.assertEqual(result[1], ("Laptop", Decimal("1299.99"), 24))

        mock_cursor.execute.assert_called_once_with(
            "SELECT name, price, quantity_available FROM Products WHERE category_id = ?",
            (category_id,)
        )
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
