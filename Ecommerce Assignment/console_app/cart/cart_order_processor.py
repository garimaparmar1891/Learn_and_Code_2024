from cart.cart_api_handler import CartAPIHandler

class CartOrderProcessor:
    def place_order(self, user_id):
        response = CartAPIHandler.send_post_request("order/place", {"userId": user_id})
        self._print_order_result(response)

    @staticmethod
    def _print_order_result(success):
        message = "Order placed successfully!" if success else "Order placement failed."
        print(message)
