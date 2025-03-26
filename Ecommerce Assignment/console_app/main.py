from auth import Auth
from session import SessionManager
from categories import CategoryManager
from cart import CartManager
from orders import OrderManager
from products import ProductManager
from user_menu import UserMenu  

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
            if self.user_id is None:
                self.user_id = self.session.handle_session()

                if self.user_id is None: 
                    print("Exiting program...")
                    break

            if isinstance(self.user_id, dict): 
                user_id = self.user_id.get("userId")
                logged_out = self.user_menu.display_menu(user_id)

                if logged_out: 
                    print("\nYou have logged out. Returning to Login/Signup Menu...\n")
                    self.user_id = None  


if __name__ == "__main__":
    app = ECommerceApp()
    app.run()
