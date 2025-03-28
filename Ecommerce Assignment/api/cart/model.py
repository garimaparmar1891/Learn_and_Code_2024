from database import get_database_connection

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
