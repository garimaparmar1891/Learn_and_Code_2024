from flask import Blueprint, request, jsonify
from .service import OrderService

orders_bp = Blueprint("orders", __name__)

class OrderController:
    @staticmethod
    @orders_bp.route("/order/place", methods=["POST"])
    def place_order():
        data = request.json
        user_id = data.get("userId")
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400
        response, status = OrderService.place_order(user_id)
        return jsonify(response), status

    @staticmethod
    @orders_bp.route("/orders/history", methods=["GET"])
    def order_history():
        user_id = request.args.get("userId")
        if not user_id:
            return jsonify({"error": "Missing userId"}), 400
        response, status = OrderService.fetch_order_history(user_id)
        return jsonify(response), status
