from .model import OrderModel

class OrderService:
    @staticmethod
    def place_order(user_id):
        total_amount = OrderModel.get_total_cart_amount(user_id)
        if total_amount is None:
            return {"error": "Cart is empty"}, 400
        order_id, order_date = OrderModel.create_order(user_id, total_amount)
        OrderModel.move_cart_to_order_items(order_id, user_id)
        OrderModel.clear_cart(user_id)
        return {
            "message": "Order placed successfully!",
            "order_id": order_id,
            "total_amount": total_amount,
            "order_date": order_date,
        }, 200

    @staticmethod
    def fetch_order_history(user_id):
        orders = OrderModel.get_order_history(user_id)
        if not orders:
            return {"message": "No orders found"}, 200
        return [
            {
                "order_id": order[0],
                "order_date": order[1],
                "product_name": order[2],
                "quantity": order[3],
                "price": order[4],
            }
            for order in orders
        ], 200
