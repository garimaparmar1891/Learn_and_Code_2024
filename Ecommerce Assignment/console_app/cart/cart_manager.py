from cart.cart_viewer import CartViewer
from cart.cart_modifier import CartModifier
from cart.cart_order_processor import CartOrderProcessor
from utils.user_input_handler import UserInputHandler

class CartManager:
    def __init__(self):
        self.viewer = CartViewer()
        self.modifier = CartModifier()
        self.order_processor = CartOrderProcessor()

    def view_cart(self, user_id):
        user_id = user_id.get("userId", 0) if isinstance(user_id, dict) else user_id
        if not user_id:
            print("Error: Invalid user ID")
            return

        cart_items = self.viewer.fetch_cart(user_id)
        if not cart_items:
            print("\nYour cart is empty.")
            return

        self.viewer.display_cart(cart_items)
        self.handle_cart_options(user_id)

    def handle_cart_options(self, user_id):
        options = {
            "1": self.modifier.remove_cart_item,
            "2": self.order_processor.place_order,
            "3": lambda _: None,
        }
        while True:
            choice = UserInputHandler.get_user_choice(
                "\nOptions:\n1. Remove Item\n2. Place Order\n3. Go Back\nChoose an option: ", 
                options.keys()
            )
            if choice == "3":
                return
            options[choice](user_id)
