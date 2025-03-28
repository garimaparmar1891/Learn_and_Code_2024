from cart.cart_api_handler import CartAPIHandler
from utils.user_input_handler import UserInputHandler

class CartModifier:
    def add_to_cart(self, user_id, product_name):
        quantity = UserInputHandler.get_valid_quantity()
        if quantity:
            response = CartAPIHandler.send_post_request("cart/add", {
                "userId": user_id, 
                "product": product_name, 
                "quantity": quantity
            })
            print(f"{quantity} x {product_name} added to cart successfully!" if response else f"Failed to add {product_name} to cart.")

    def remove_cart_item(self, user_id):
        product_name = UserInputHandler.get_required_input("\nEnter the product name to remove: ")
        quantity = UserInputHandler.get_valid_quantity("Enter the quantity to remove: ")
        response = CartAPIHandler.send_post_request("cart/remove", {
            "userId": user_id, 
            "product": product_name, 
            "quantity": quantity
        })
        print(f"Successfully removed {quantity} x {product_name} from your cart!" if response else "Failed to remove the item. Please try again.")
