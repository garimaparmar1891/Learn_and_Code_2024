import requests
from config import API_URL
from utils import print_server_error
from products import ProductManager

class CategoryManager:
    def __init__(self):
        self.fetcher = CategoryFetcher()
        self.viewer = CategoryViewer()
        self.product_manager = ProductManager()

    def browse_categories(self, user_id):
        categories = self.fetcher.get_categories()
        if not categories:
            print("\nNo categories available.")
            return

        self.viewer.display(categories)
        category_id = UserInputHandler.get_category_selection(categories)

        if category_id is not None:
            self.product_manager.browse_products(user_id, category_id)


class CategoryFetcher:
    @staticmethod
    def get_categories():
        return CategoryAPIHandler.get_request("categories")


class CategoryViewer:
    @staticmethod
    def display(categories):
        print("\nAvailable Categories:")
        for category_id, details in categories.items():
            print(f"{category_id}. {details['name']}")


class UserInputHandler:
    @staticmethod
    def get_category_selection(categories):
        while True:
            choice = input("Select a category ID (or 'B' to go back): ").strip()
            if choice.lower() == "b":
                return None
            if choice in categories:
                return choice
            print("Invalid category ID. Try again.")


class CategoryAPIHandler:
    @staticmethod
    def get_request(endpoint):
        try:
            response = requests.get(f"{API_URL}/{endpoint}")
            if response.status_code == 200:
                return response.json()
            print(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException:
            print_server_error()
        return {}
