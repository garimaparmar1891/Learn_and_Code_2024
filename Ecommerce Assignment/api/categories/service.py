from .model import CategoryModel

class CategoryService:
    @staticmethod
    def fetch_categories():
        categories = CategoryModel.get_all_categories()

        if not categories:
            return {"message": "No categories found"}, 200

        return {
            str(row[0]): {"name": row[1]} for row in categories
        }, 200
