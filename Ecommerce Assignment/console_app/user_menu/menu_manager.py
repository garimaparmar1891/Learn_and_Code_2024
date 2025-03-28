class MenuManager:
    @staticmethod
    def display_user_menu():
        print("\n1. Browse Categories")
        print("2. View Cart")
        print("3. View Order History")
        print("4. Logout")
        return input("Choose an option: ").strip()
