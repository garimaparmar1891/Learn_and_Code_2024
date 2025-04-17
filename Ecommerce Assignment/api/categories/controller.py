from flask import jsonify
from .service import CategoryService

class CategoryController:
    @staticmethod
    def get_categories():
        response, status = CategoryService.get_categories()
        return jsonify(response), status
