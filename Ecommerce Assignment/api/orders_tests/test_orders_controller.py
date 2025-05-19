import unittest
from unittest.mock import patch
from http import HTTPStatus
from app import create_app

class OrderControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch("orders.controller.OrderService.place_order")
    def test_place_order_success(self, mock_place_order):
        mock_place_order.return_value = ({"message": "Order placed successfully"}, HTTPStatus.CREATED)

        response = self.app.post("/order/place", json={"userId": 1})
        data = response.get_json()

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(data["message"], "Order placed successfully")

    def test_place_order_missing_user_id(self):
        response = self.app.post("/order/place", json={})
        data = response.get_json()

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(data["error"], "User ID is required")

    @patch("orders.controller.OrderService.order_history")
    def test_order_history_success(self, mock_order_history):
        mock_order_history.return_value = ({"orders": [{"order_id": 1, "status": "delivered"}]}, HTTPStatus.OK)

        response = self.app.get("/orders/history", query_string={"userId": 1})
        data = response.get_json()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn("orders", data)
        self.assertEqual(data["orders"][0]["order_id"], 1)

    def test_order_history_missing_user_id(self):
        response = self.app.get("/orders/history")
        data = response.get_json()

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(data["error"], "Missing userId")

if __name__ == "__main__":
    unittest.main()
