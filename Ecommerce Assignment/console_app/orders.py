import requests
from collections import defaultdict
from config import API_URL
from utils import print_server_error

class OrderManager:
    def __init__(self):
        self.fetcher = OrderFetcher()
        self.viewer = OrderViewer()

    def view_order_history(self, user_id):
        orders = self.fetcher.get_history(user_id)
        self.viewer.display(orders)

    def place_order(self, user_id):
        response = OrderAPIHandler.send_post_request("order/place", {"userId": user_id})
        if response and "message" in response:
            print(f"\n{response['message']} (Order ID: {response.get('order_id', 'Unknown')})")
        else:
            print("\nFailed to place order.")


class OrderViewer:
    @staticmethod
    def display(orders):
        if not orders:
            print("\nNo Past Orders !!")
            return

        grouped_orders = defaultdict(list)
        for order in orders:
            grouped_orders[order.get("order_id")].append(order)

        print("\nYour Order History:")
        for order_id, items in grouped_orders.items():
            total_amount = sum(float(item.get("price", 0)) * int(item.get("quantity", 1)) for item in items)
            order_date = items[0].get("order_date", "Unknown Date")

            print(f"\nDate: {order_date} - Total: ${total_amount:.2f}")

            for item in items:
                print(f"  - {item.get('product_name', 'Unknown Product')} "
                      f"(Qty: {item.get('quantity', 1)}, Price: ${float(item.get('price', 0)) * int(item.get('quantity', 1)):.2f})")


class OrderFetcher:
    @staticmethod
    def get_history(user_id):
        response = OrderAPIHandler.send_get_request("orders/history", {"userId": user_id})
        return response if response and "message" not in response else []


class OrderAPIHandler:
    @staticmethod
    def send_get_request(endpoint, params=None):
        try:
            response = requests.get(f"{API_URL}/{endpoint}", params=params)
            return response.json() if response.status_code == 200 else []
        except requests.exceptions.RequestException:
            print_server_error()
            return []

    @staticmethod
    def send_post_request(endpoint, data=None):
        try:
            response = requests.post(f"{API_URL}/{endpoint}", json=data)
            return response.json() if response.status_code in [200, 201] else {"error": "Request failed"}
        except requests.exceptions.RequestException:
            print_server_error()
            return {"error": "Request failed"}
