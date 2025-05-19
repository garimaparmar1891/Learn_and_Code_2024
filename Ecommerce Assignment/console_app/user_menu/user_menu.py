from user_menu.menu_manager import MenuManager

class UserMenu:
    def __init__(self, category_manager, cart_manager, order_manager):
        self.category_manager = category_manager
        self.cart_manager = cart_manager
        self.order_manager = order_manager

    def display_menu(self, user_id):
        while True:
            choice = MenuManager.display_user_menu()  
            match choice:
                case "1":
                    self.category_manager.browse_categories(user_id)
                case "2":
                    self.cart_manager.view_cart(user_id)
                case "3":
                    self.order_manager.view_order_history(user_id)
                case "4":
                    return True 
                case _:
                    print("Invalid choice. Try again.")
