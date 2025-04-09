from http import HTTPStatus
from .model import CategoryModel

class CategoryService:
    @staticmethod
    def fetch_categories():
        categories = CategoryModel.get_all_categories()

        if not categories:
            return {"message": "No categories found"}, HTTPStatus.OK

        return {
            str(row[0]): {"name": row[1]} for row in categories
        }, HTTPStatus.OK
