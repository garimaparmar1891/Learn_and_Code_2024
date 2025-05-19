from flask import jsonify
from http import HTTPStatus
from .service import CartService

class CartController:
    @staticmethod
    def add_product_to_cart(data):
        user_id = data.get("userId")
        product_name = data.get("product")
        quantity = data.get("quantity")

        if not all([user_id, product_name, quantity]):
            return jsonify({"error": "Missing required fields"}), HTTPStatus.BAD_REQUEST

        response, status = CartService.add_product_to_cart(user_id, product_name, quantity)
        return jsonify(response), HTTPStatus(status)

    @staticmethod
    def get_cart(user_id):
        response, status = CartService.get_cart(user_id)
        return jsonify(response), HTTPStatus(status)

    @staticmethod
    def remove_product_from_cart(data):
        user_id = data.get("userId")
        product_name = data.get("product")
        quantity_to_remove = int(data.get("quantity", 0))

        if not all([user_id, product_name, quantity_to_remove]):
            return jsonify({"error": "Missing required fields"}), HTTPStatus.BAD_REQUEST

        response, status = CartService.remove_product_from_cart(user_id, product_name, quantity_to_remove)
        return jsonify(response), HTTPStatus(status)
