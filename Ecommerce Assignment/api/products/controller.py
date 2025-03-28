from flask import Blueprint, jsonify
from .service import ProductService

products_bp = Blueprint("products", __name__)

class ProductController:
    @staticmethod
    @products_bp.route("/products/<int:category_id>", methods=["GET"])
    def get_products_by_category(category_id):
        response, status = ProductService.fetch_products_by_category(category_id)
        return jsonify(response), status
