import unittest
from unittest.mock import patch
from collections import defaultdict
from orders.order_viewer import OrderViewer

class TestOrderViewer(unittest.TestCase):

    @patch('builtins.print')
    def test_display_no_orders(self, mock_print):
        OrderViewer.display([])

        mock_print.assert_called_once_with("\nNo Past Orders !!")

    @patch('builtins.print')
    def test_display_with_orders(self, mock_print):
        orders = [
            {"order_id": 1, "order_date": "2025-05-10", "product_name": "Product A", "quantity": 2, "price": 10.0},
            {"order_id": 1, "order_date": "2025-05-10", "product_name": "Product B", "quantity": 1, "price": 20.0},
            {"order_id": 2, "order_date": "2025-05-09", "product_name": "Product C", "quantity": 3, "price": 15.0}
        ]

        OrderViewer.display(orders)

        mock_print.assert_any_call("\nYour Order History:")
        mock_print.assert_any_call("\nDate: 2025-05-10 - Total: $40.00")
        mock_print.assert_any_call("  - Product A (Qty: 2, Price: $20.00)")
        mock_print.assert_any_call("  - Product B (Qty: 1, Price: $20.00)")
        mock_print.assert_any_call("\nDate: 2025-05-09 - Total: $45.00")
        mock_print.assert_any_call("  - Product C (Qty: 3, Price: $45.00)")

    @patch('builtins.print')
    def test_group_orders_by_id(self, mock_print):
        orders = [
            {"order_id": 1, "order_date": "2025-05-10", "product_name": "Product A", "quantity": 2, "price": 10.0},
            {"order_id": 1, "order_date": "2025-05-10", "product_name": "Product B", "quantity": 1, "price": 20.0},
            {"order_id": 2, "order_date": "2025-05-09", "product_name": "Product C", "quantity": 3, "price": 15.0}
        ]

        grouped_orders = OrderViewer._group_orders_by_id(orders)

        self.assertEqual(len(grouped_orders), 2)
        self.assertEqual(len(grouped_orders[1]), 2)
        self.assertEqual(len(grouped_orders[2]), 1)

    def test_calculate_order_total(self):
        items = [
            {"price": 10.0, "quantity": 2},
            {"price": 20.0, "quantity": 1},
        ]
        total = OrderViewer._calculate_order_total(items)

        self.assertEqual(total, 40.0)

if __name__ == '__main__':
    unittest.main()
