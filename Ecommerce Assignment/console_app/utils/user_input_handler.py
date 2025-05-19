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

    @staticmethod
    def get_category_selection(categories):
        while True:
            choice = input("Select a category ID (or 'B' to go back): ").strip()
            if choice.lower() == "b":
                return None
            if choice in categories:
                return choice
            print("Invalid category ID. Try again.")

