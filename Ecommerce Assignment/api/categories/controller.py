from flask import jsonify
from .service import CategoryService

class CategoryController:
    @staticmethod
    def get_categories():
        response, status = CategoryService.fetch_categories()
        return jsonify(response), status
