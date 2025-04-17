from . import orders_bp 
from .controller import OrderController

@orders_bp.route("/order/place", methods=["POST"])
def place_order():
    return OrderController.place_order()

@orders_bp.route("/orders/history", methods=["GET"])
def order_history():
    return OrderController.order_history()
