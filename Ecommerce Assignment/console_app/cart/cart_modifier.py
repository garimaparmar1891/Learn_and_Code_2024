from cart.cart_api_handler import CartAPIHandler
from utils.user_input_handler import UserInputHandler

class CartModifier:
    def add_to_cart(self, user_id, product_name):
        quantity = self._get_quantity_for_action("add")
        if not quantity:
            return

        payload = {"userId": user_id, "product": product_name, "quantity": quantity}
        success = CartAPIHandler.send_post_request("cart/add", payload)
        self._print_add_result(success, product_name, quantity)

    def remove_cart_item(self, user_id):
        product_name = UserInputHandler.get_required_input("\nEnter the product name to remove: ")
        quantity = self._get_quantity_for_action("remove")
        if not quantity:
            return

        payload = {"userId": user_id, "product": product_name, "quantity": quantity}
        success = CartAPIHandler.send_post_request("cart/remove", payload)
        self._print_remove_result(success, product_name, quantity)

    @staticmethod
    def _get_quantity_for_action(action):
        prompt = "Enter the quantity to {}: ".format(action)
        return UserInputHandler.get_valid_quantity(prompt)

    @staticmethod
    def _print_add_result(success, product_name, quantity):
        message = (
            f"{quantity} x {product_name} added to cart successfully!"
            if success else f"Failed to add {product_name} to cart."
        )
        print(message)

    @staticmethod
    def _print_remove_result(success, product_name, quantity):
        message = (
            f"Successfully removed {quantity} x {product_name} from your cart!"
            if success else "Failed to remove the item. Please try again."
        )
        print(message)
