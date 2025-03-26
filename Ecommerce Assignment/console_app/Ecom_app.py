from authentication.auth import Auth
from session.session_manager import SessionManager
from categories.category_manager import CategoryManager
from cart.cart_manager import CartManager
from orders.order_manager import OrderManager
from products.product_manager import ProductManager
from user_menu.user_menu import UserMenu  

class ECommerceApp:
    def __init__(self):
        self.auth = Auth()
        self.session = SessionManager(self.auth)
        self.category_manager = CategoryManager()
        self.product_manager = ProductManager()
        self.cart_manager = CartManager()
        self.order_manager = OrderManager()
        self.user_menu = UserMenu(self.category_manager, self.cart_manager, self.order_manager)
        self.user_id = None

    def run(self):
        print("Welcome to Console E-Commerce!")

        while True:
            if not self.user_id:  # Ensure valid user_id before proceeding
                session_data = self.session.handle_session()
                if not session_data:  # User choose to exit
                    print("Exiting program...")
                    break
                
                if isinstance(session_data, dict) and "userId" in session_data:
                    self.user_id = session_data["userId"]
                else:
                    print("Invalid login response. Exiting...")
                    break

            logged_out = self.user_menu.display_menu(self.user_id)

            if logged_out:
                print("\nYou have logged out. Returning to Login/Signup Menu...\n")
                self.user_id = None  # Reset for next session

if __name__ == "__main__":
    app = ECommerceApp()
    app.run()
