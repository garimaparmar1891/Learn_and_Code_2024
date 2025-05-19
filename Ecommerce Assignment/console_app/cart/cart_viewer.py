from cart.cart_api_handler import CartAPIHandler

class CartViewer:
    def fetch_cart(self, user_id):
        response = CartAPIHandler.send_get_request(f"cart/{user_id}")
        return response.get("cart", []) if response else []

    def display_cart(self, cart_items):
        print("\nYour Cart:")
        for item in cart_items:
            total_price = float(item['quantity']) * float(item['price'])
            print(f"- {item['product']} (Qty: {item['quantity']}) (Total Price: ${total_price:.2f}) Added on: {item['added_at']}")
