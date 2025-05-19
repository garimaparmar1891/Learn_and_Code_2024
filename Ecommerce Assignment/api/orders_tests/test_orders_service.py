import unittest
from unittest.mock import patch
from http import HTTPStatus
from orders.service import OrderService

class TestOrderService(unittest.TestCase):
    
    @patch("orders.model.OrderModel.get_total_cart_amount")
    @patch("orders.model.OrderModel.create_order")
    @patch("orders.model.OrderModel.move_cart_to_order_items")
    @patch("orders.model.OrderModel.clear_cart")
    def test_place_order_success(self, mock_clear_cart, mock_move_cart, mock_create_order, mock_get_total_cart_amount):
        user_id = 1
        total_amount = 100.0
        order_id = 1
        order_date = "2025-05-01 12:00:00"
        
        mock_get_total_cart_amount.return_value = total_amount
        mock_create_order.return_value = (order_id, order_date)

        response, status = OrderService.place_order(user_id)

        self.assertEqual(status, HTTPStatus.OK)
        self.assertEqual(response["message"], "Order placed successfully!")
        self.assertEqual(response["order_id"], order_id)
        self.assertEqual(response["total_amount"], total_amount)
        self.assertEqual(response["order_date"], order_date)

        mock_move_cart.assert_called_once_with(order_id, user_id)
        mock_clear_cart.assert_called_once_with(user_id)

    @patch("orders.model.OrderModel.get_total_cart_amount")
    @patch("orders.model.OrderModel.create_order")
    def test_place_order_cart_empty(self, mock_create_order, mock_get_total_cart_amount):
        user_id = 1
        
        mock_get_total_cart_amount.return_value = None

        response, status = OrderService.place_order(user_id)

        self.assertEqual(status, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response["error"], "Cart is empty")
        
    @patch("orders.model.OrderModel.get_total_cart_amount")
    @patch("orders.model.OrderModel.create_order")
    def test_place_order_failure(self, mock_create_order, mock_get_total_cart_amount):
        user_id = 1
        total_amount = 100.0
        
        mock_get_total_cart_amount.return_value = total_amount
        mock_create_order.return_value = (None, None)

        response, status = OrderService.place_order(user_id)

        self.assertEqual(status, HTTPStatus.INTERNAL_SERVER_ERROR)
        self.assertEqual(response["error"], "Failed to place order")
        
    @patch("orders.model.OrderModel.get_order_history")
    def test_order_history_success(self, mock_get_order_history):
        user_id = 1
        
        mock_get_order_history.return_value = [
            (1, "2025-05-01 12:00:00", "Apple", 2, 10.0) 
        ]
        
        response, status = OrderService.order_history(user_id)
        
        self.assertEqual(status, HTTPStatus.OK)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]["order_id"], 1)
        self.assertEqual(response[0]["order_date"], "2025-05-01 12:00:00")
        self.assertEqual(response[0]["product_name"], "Apple")
        self.assertEqual(response[0]["quantity"], 2)
        self.assertEqual(response[0]["price"], 10.0)

    @patch("orders.model.OrderModel.get_order_history")
    def test_order_history_no_orders(self, mock_get_order_history):
        user_id = 1
        
        mock_get_order_history.return_value = []

        response, status = OrderService.order_history(user_id)
        
        self.assertEqual(status, HTTPStatus.OK)

if __name__ == "__main__":
    unittest.main()
