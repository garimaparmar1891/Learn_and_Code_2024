from flask import jsonify
from .service import CartService

class CartController:
    @staticmethod
    def add_product_to_cart(data):
        user_id = data.get("userId")
        product_name = data.get("product")
        quantity = data.get("quantity")

        if not all([user_id, product_name, quantity]):
            return jsonify({"error": "Missing required fields"}), 400

        response, status = CartService.add_to_cart(user_id, product_name, quantity)
        return jsonify(response), status

    @staticmethod
    def get_cart(user_id):
        response, status = CartService.view_cart(user_id)
        return jsonify(response), status

    @staticmethod
    def remove_product_from_cart(data):
        user_id = data.get("userId")
        product_name = data.get("product")
        quantity_to_remove = int(data.get("quantity", 0))

        if not all([user_id, product_name, quantity_to_remove]):
            return jsonify({"error": "Missing required fields"}), 400

        response, status = CartService.remove_from_cart(user_id, product_name, quantity_to_remove)
        return jsonify(response), status
