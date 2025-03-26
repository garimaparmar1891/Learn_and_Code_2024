from cart.cart_api_handler import CartAPIHandler

class CartOrderProcessor:
    def place_order(self, user_id):
        response = CartAPIHandler.send_post_request("order/place", {"userId": user_id})
        print("Order placed successfully!" if response else "Order placement failed.")
