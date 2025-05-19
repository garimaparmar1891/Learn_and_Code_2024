from categories.category_api_handler import CategoryAPIHandler

class CategoryFetcher:
    @staticmethod
    def get_categories():
        return CategoryAPIHandler.get_request("categories")
