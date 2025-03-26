from orders.order_fetcher import OrderFetcher
from orders.order_viewer import OrderViewer
from orders.order_api_handler import OrderAPIHandler

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
