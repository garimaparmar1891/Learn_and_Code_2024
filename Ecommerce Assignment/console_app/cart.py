import requests
from config import API_URL
from user_menu import UserMenu

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
            choice = UserInputHandler.get_user_choice("\nOptions:\n1. Remove Item\n2. Place Order\n3. Go Back\nChoose an option: ", options.keys())
            if choice == "3":
                return
            options[choice](user_id)

class CartViewer:
    def fetch_cart(self, user_id):
        response = CartAPIHandler.send_get_request(f"cart/{user_id}")
        return response.get("cart", []) if response else []

    def display_cart(self, cart_items):
        print("\nYour Cart:")
        for item in cart_items:
            total_price = float(item['quantity']) * float(item['price'])
            print(f"- {item['product']} (Qty: {item['quantity']}) (Total Price: ${total_price:.2f}) Added on: {item['added_at']}")

class CartModifier:
    def add_to_cart(self, user_id, product_name):
        quantity = UserInputHandler.get_valid_quantity()
        if quantity:
            response = CartAPIHandler.send_post_request("cart/add", {"userId": user_id, "product": product_name, "quantity": quantity})
            print(f"{quantity} x {product_name} added to cart successfully!" if response else f"Failed to add {product_name} to cart.")

    def remove_cart_item(self, user_id):
        product_name = UserInputHandler.get_required_input("\nEnter the product name to remove: ")
        quantity = UserInputHandler.get_valid_quantity("Enter the quantity to remove: ")
        response = CartAPIHandler.send_post_request("cart/remove", {"userId": user_id, "product": product_name, "quantity": quantity})
        print(f"Successfully removed {quantity} x {product_name} from your cart!" if response else "Failed to remove the item. Please try again.")

class CartOrderProcessor:
    def place_order(self, user_id):
        response = CartAPIHandler.send_post_request("order/place", {"userId": user_id})
        print("Order placed successfully!" if response else "Order placement failed.")


class UserInputHandler:
    @staticmethod
    def get_valid_quantity(prompt="Enter quantity: "):
        while True:
            quantity = UserInputHandler.get_valid_number(prompt)
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero.")

    @staticmethod
    def get_valid_number(prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_required_input(prompt):
        while True:
            field = input(prompt).strip()
            if field:
                return field
            print("This field is required. Please enter a value.")

    @staticmethod
    def get_user_choice(prompt, valid_choices):
        while True:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice
            print("Invalid choice. Please try again.")


class CartAPIHandler:
    @staticmethod
    def send_get_request(endpoint):
        try:
            return requests.get(f"{API_URL}/{endpoint}").json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}

    @staticmethod
    def send_post_request(endpoint, payload):
        try:
            response = requests.post(f"{API_URL}/{endpoint}", json=payload)
            return response.json() if response.status_code == 200 else None
        except requests.exceptions.RequestException:
            print("Error: Unable to connect to the server.")
            return None
        