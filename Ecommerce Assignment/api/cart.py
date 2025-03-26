from flask import Blueprint, request, jsonify
from database import get_database_connection

cart_bp = Blueprint("cart", __name__)

class CartModel:
    @staticmethod
    def get_cart_items(user_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT p.name, c.quantity, p.price, c.added_at
                FROM Cart c
                JOIN Products p ON c.product_id = p.id 
                WHERE c.user_id = ?
                """,
                (user_id,),
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_product_id(product_name):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM Products WHERE name = ?", (product_name,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def add_or_update_cart(user_id, product_id, quantity):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT quantity FROM Cart WHERE user_id = ? AND product_id = ?",
                (user_id, product_id),
            )
            existing_item = cursor.fetchone()

            if existing_item:
                cursor.execute(
                    "UPDATE Cart SET quantity = quantity + ? WHERE user_id = ? AND product_id = ?",
                    (quantity, user_id, product_id),
                )
            else:
                cursor.execute(
                    "INSERT INTO Cart (user_id, product_id, quantity) VALUES (?, ?, ?)",
                    (user_id, product_id, quantity),
                )
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def remove_from_cart(user_id, product_id, quantity_to_remove):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT quantity FROM Cart WHERE user_id = ? AND product_id = ?",
                (user_id, product_id),
            )
            existing_item = cursor.fetchone()

            if not existing_item:
                return {"error": "Product not found in cart"}, 404

            current_quantity = existing_item[0]

            if quantity_to_remove >= current_quantity:
                cursor.execute(
                    "DELETE FROM Cart WHERE user_id = ? AND product_id = ?",
                    (user_id, product_id),
                )
                message = "Product removed from cart completely!"
            else:
                cursor.execute(
                    "UPDATE Cart SET quantity = quantity - ? WHERE user_id = ? AND product_id = ?",
                    (quantity_to_remove, user_id, product_id),
                )
                message = f"Updated cart: {current_quantity - quantity_to_remove} items left"

            conn.commit()
            return {"message": message}, 200
        except:
            return {"error": "Internal server error"}, 500
        finally:
            cursor.close()
            conn.close()

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

class CartController:
    @staticmethod
    @cart_bp.route("/cart/add", methods=["POST"])
    def add_product_to_cart():
        data = request.json
        user_id = data.get("userId")
        product_name = data.get("product")
        quantity = data.get("quantity")

        if not all([user_id, product_name, quantity]):
            return jsonify({"error": "Missing required fields"}), 400

        response, status = CartService.add_to_cart(user_id, product_name, quantity)
        return jsonify(response), status

    @staticmethod
    @cart_bp.route("/cart/<int:user_id>", methods=["GET"])
    def get_cart(user_id):
        response, status = CartService.view_cart(user_id)
        return jsonify(response), status

    @staticmethod
    @cart_bp.route("/cart/remove", methods=["POST"])
    def remove_product_from_cart():
        data = request.json
        user_id = data.get("userId")
        product_name = data.get("product")
        quantity_to_remove = int(data.get("quantity", 0))

        if not all([user_id, product_name, quantity_to_remove]):
            return jsonify({"error": "Missing required fields"}), 400

        response, status = CartService.remove_from_cart(user_id, product_name, quantity_to_remove)
        return jsonify(response), status
