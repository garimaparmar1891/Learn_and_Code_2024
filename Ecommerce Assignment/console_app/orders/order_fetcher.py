from orders.order_api_handler import OrderAPIHandler

class OrderFetcher:
    @staticmethod
    def get_history(user_id):
        response = OrderAPIHandler.send_get_request("orders/history", {"userId": user_id})
        return response if response and "message" not in response else []
