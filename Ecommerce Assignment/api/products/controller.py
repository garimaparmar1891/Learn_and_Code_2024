from flask import jsonify
from .service import ProductService

class ProductController:
    @staticmethod
    def get_products_by_category(category_id):
        response, status = ProductService.fetch_products_by_category(category_id)
        return jsonify(response), status
