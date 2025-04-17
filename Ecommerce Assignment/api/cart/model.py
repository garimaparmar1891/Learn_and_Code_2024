from database import get_database_connection
from http import HTTPStatus 

class CartModel:
    @staticmethod
    def get_product_id(product_name):
        query = "SELECT id FROM Products WHERE name = ?"
        result = CartModel._execute_select_query(query, (product_name,))
        return result[0] if result else None

    @staticmethod
    def add_product_to_cart(user_id, product_id, quantity):
        existing_quantity = CartModel._get_existing_quantity(user_id, product_id)

        if existing_quantity is not None:
            return CartModel._update_cart_quantity(user_id, product_id, quantity)
        else:
            return CartModel._insert_new_cart_item(user_id, product_id, quantity)

    @staticmethod
    def get_cart_items(user_id):
        query = """
            SELECT p.name, c.quantity, p.price, c.added_at
            FROM Cart c
            JOIN Products p ON c.product_id = p.id 
            WHERE c.user_id = ?
        """
        return CartModel._execute_select_query(query, (user_id,))

    @staticmethod
    def remove_product_from_cart(user_id, product_id, quantity_to_remove):
        existing_quantity = CartModel._get_existing_quantity(user_id, product_id)

        if existing_quantity is None:
            return {"error": "Product not found in cart"}, HTTPStatus.NOT_FOUND

        if quantity_to_remove >= existing_quantity:
            query = "DELETE FROM Cart WHERE user_id = ? AND product_id = ?"
            params = (user_id, product_id)
            message = "Product removed from cart completely!"
        else:
            query = "UPDATE Cart SET quantity = quantity - ? WHERE user_id = ? AND product_id = ?"
            params = (quantity_to_remove, user_id, product_id)
            message = f"Updated cart: {existing_quantity - quantity_to_remove} items left"

        success = CartModel._execute_commit_query(query, params)
        return ({"message": message}, HTTPStatus.OK) if success else ({"error": "Internal server error"}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @staticmethod
    def _execute_select_query(query, params):
        conn = get_database_connection()
        cursor = conn.cursor()
       
        cursor.execute(query, params)
        result = cursor.fetchall()
    
        cursor.close()
        conn.close()
        return result
    
    @staticmethod
    def _get_existing_quantity(user_id, product_id):
        query = "SELECT quantity FROM Cart WHERE user_id = ? AND product_id = ?"
        result = CartModel._execute_select_query(query, (user_id, product_id))
        return result[0][0] if result else None 
    
    @staticmethod
    def _update_cart_quantity(user_id, product_id, quantity):
        query = "UPDATE Cart SET quantity = quantity + ? WHERE user_id = ? AND product_id = ?"
        params = (quantity, user_id, product_id)
        return CartModel._execute_commit_query(query, params)

    @staticmethod
    def _insert_new_cart_item(user_id, product_id, quantity):
        query = "INSERT INTO Cart (user_id, product_id, quantity) VALUES (?, ?, ?)"
        params = (user_id, product_id, quantity)
        return CartModel._execute_commit_query(query, params)

    @staticmethod
    def _execute_commit_query(query, params):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close() 
   