from .model import CartModel
from http import HTTPStatus
from .cartDTO import cartDTO

class CartService:
    @staticmethod
    def add_to_cart(user_id, product_name, quantity):
        product = CartModel.get_product_id(product_name)
        if not product:
            return {"error": "Product not found"}, HTTPStatus.NOT_FOUND

        product_id = product[0]
        success = CartModel.add_to_cart(user_id, product_id, quantity)
        return (
            {"message": "Product added to cart successfully!"}, HTTPStatus.OK
        ) if success else (
            {"error": "Failed to add product to cart"}, HTTPStatus.INTERNAL_SERVER_ERROR
        )

    @staticmethod
    def view_cart(user_id):
        cart_items = CartModel.get_cart_items(user_id)
        if not cart_items:
            return {"message": "Your cart is empty"}, HTTPStatus.OK

        cart_list = [cartDTO(*item).to_dict() for item in cart_items]

        return {"cart": cart_list}, HTTPStatus.OK

    @staticmethod
    def remove_from_cart(user_id, product_name, quantity_to_remove):
        product = CartModel.get_product_id(product_name)
        if not product:
            return {"error": "Product not found"}, HTTPStatus.NOT_FOUND

        product_id = product[0]
        return CartModel.remove_from_cart(user_id, product_id, quantity_to_remove)
