from .model import CartModel

class CartService:
    @staticmethod
    def add_to_cart(user_id, product_name, quantity):
        product = CartModel.get_product_id(product_name)
        if not product:
            return {"error": "Product not found"}, 404

        product_id = product[0]
        success = CartModel.add_or_update_cart(user_id, product_id, quantity)
        return ({"message": "Product added to cart successfully!"}, 200) if success else ({"error": "Failed to add product to cart"}, 500)

    @staticmethod
    def view_cart(user_id):
        cart_items = CartModel.get_cart_items(user_id)
        if not cart_items:
            return {"message": "Your cart is empty"}, 200

        cart_list = [
            {"product": item[0], "quantity": item[1], "price": item[2], "added_at": item[3]}
            for item in cart_items
        ]
        return {"cart": cart_list}, 200

    @staticmethod
    def remove_from_cart(user_id, product_name, quantity_to_remove):
        product = CartModel.get_product_id(product_name)
        if not product:
            return {"error": "Product not found"}, 404

        product_id = product[0]
        return CartModel.remove_from_cart(user_id, product_id, quantity_to_remove)
