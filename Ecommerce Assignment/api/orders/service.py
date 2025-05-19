from http import HTTPStatus
from .model import OrderModel
from .ordersDTO import OrderResponseDTO, OrderHistoryDTO

class OrderService:
    @staticmethod
    def place_order(user_id):
        total_amount = OrderModel.get_total_cart_amount(user_id)
        if total_amount is None:
            return {"error": "Cart is empty"}, HTTPStatus.BAD_REQUEST

        order_id, order_date = OrderModel.create_order(user_id, total_amount)
        if not order_id:
            return {"error": "Failed to place order"}, HTTPStatus.INTERNAL_SERVER_ERROR

        OrderModel.move_cart_to_order_items(order_id, user_id)
        OrderModel.clear_cart(user_id)

        response_dto = OrderResponseDTO(
            message="Order placed successfully!",
            order_id=order_id,
            total_amount=total_amount,
            order_date=order_date
        )
        return response_dto.__dict__, HTTPStatus.OK

    @staticmethod
    def order_history(user_id):
        orders = OrderModel.get_order_history(user_id)
        if not orders:
            return {"message": "No orders found"}, HTTPStatus.OK

        history_dto = [
            OrderHistoryDTO(
                order_id=order[0],
                order_date=order[1],
                product_name=order[2],
                quantity=order[3],
                price=order[4]
            ).__dict__
            for order in orders
        ]
        return history_dto, HTTPStatus.OK
