from categories.category_fetcher import CategoryFetcher
from categories.category_viewer import CategoryViewer
from products.product_manager import ProductManager
from utils.user_input_handler import UserInputHandler

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
