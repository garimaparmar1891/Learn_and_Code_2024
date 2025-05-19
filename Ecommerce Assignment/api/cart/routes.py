from flask import request, jsonify
from . import cart_bp
from .controller import CartController

@cart_bp.route("/cart/add", methods=["POST"])
def add_product_to_cart():
    data = request.json
    return CartController.add_product_to_cart(data)

@cart_bp.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    return CartController.get_cart(user_id)

@cart_bp.route("/cart/remove", methods=["POST"])
def remove_product_from_cart():
    data = request.json
    return CartController.remove_product_from_cart(data)
