from flask import request, jsonify
from http import HTTPStatus
from .service import OrderService

class OrderController:
    @staticmethod
    def place_order():
        data = request.json
        user_id = data.get("userId")
        if not user_id:
            return jsonify({"error": "User ID is required"}), HTTPStatus.BAD_REQUEST
        response, status = OrderService.place_order(user_id)
        return jsonify(response), HTTPStatus(status)

    @staticmethod
    def order_history():
        user_id = request.args.get("userId")
        if not user_id:
            return jsonify({"error": "Missing userId"}), HTTPStatus.BAD_REQUEST
        response, status = OrderService.order_history(user_id)
        return jsonify(response), HTTPStatus(status)
