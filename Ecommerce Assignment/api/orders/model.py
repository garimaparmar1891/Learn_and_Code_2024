from database import get_database_connection
from datetime import datetime

class OrderModel:
    @staticmethod
    def get_total_cart_amount(user_id):
        query = OrderModel._get_total_cart_amount_query()
        return OrderModel._execute_fetch_one(query, (user_id,))

    @staticmethod
    def create_order(user_id, total_amount):
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_order_query = OrderModel._get_insert_order_query()

        conn = get_database_connection()
        cursor = conn.cursor()
       
        cursor.execute(insert_order_query, (user_id, total_amount, order_date))
        cursor.execute("SELECT @@IDENTITY")
        order_id = cursor.fetchone()[0]
        if not order_id:
            return None, None
        conn.commit()
        
        cursor.close()
        conn.close()
        return order_id, order_date   

    @staticmethod
    def move_cart_to_order_items(order_id, user_id):
        insert_items_query = OrderModel._get_move_cart_items_query()
        update_stock_query = OrderModel._get_update_product_quantity_query()

        conn = get_database_connection()
        cursor = conn.cursor()
        
        cursor.execute(insert_items_query, (order_id, user_id))
        cursor.execute(update_stock_query, (user_id,))
        conn.commit()

        cursor.close()
        conn.close()
            
    @staticmethod
    def clear_cart(user_id):
        query = "DELETE FROM Cart WHERE user_id = ?"
        OrderModel._execute_commit(query, (user_id,))

    @staticmethod
    def get_order_history(user_id):
        query = OrderModel._get_order_history_query()
        return OrderModel._execute_fetch_all(query, (user_id,))

    @staticmethod
    def _get_total_cart_amount_query():
        return """
            SELECT SUM(c.quantity * p.price)
            FROM Cart c
            JOIN Products p ON c.product_id = p.id
            WHERE c.user_id = ?
        """

    @staticmethod
    def _get_insert_order_query():
        return "INSERT INTO Orders (user_id, total_amount, order_date) VALUES (?, ?, ?)"

    @staticmethod
    def _get_move_cart_items_query():
        return """
            INSERT INTO order_details (order_id, product_id, quantity, price)
            SELECT ?, c.product_id, c.quantity, p.price
            FROM Cart c
            JOIN Products p ON c.product_id = p.id
            WHERE c.user_id = ?
        """

    @staticmethod
    def _get_update_product_quantity_query():
        return """
            UPDATE Products
            SET quantity_available = quantity_available - c.quantity
            FROM Products p
            JOIN Cart c ON p.id = c.product_id
            WHERE c.user_id = ?
        """

    @staticmethod
    def _get_order_history_query():
        return """
            SELECT o.id AS order_id, o.order_date, 
                   p.name AS product_name, d.quantity, p.price
            FROM orders o
            JOIN order_details d ON o.id = d.order_id
            JOIN products p ON d.product_id = p.id
            WHERE o.user_id = ?
            ORDER BY o.order_date DESC
        """
    
    @staticmethod
    def _execute_fetch_one(query, params):
        conn = get_database_connection()
        cursor = conn.cursor()
     
        cursor.execute(query, params)
        result = cursor.fetchone()[0]
    
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def _execute_fetch_all(query, params):
        conn = get_database_connection()
        cursor = conn.cursor()
       
        cursor.execute(query, params)
        result = cursor.fetchall()
    
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def _execute_commit(query, params):
        conn = get_database_connection()
        cursor = conn.cursor()
      
        cursor.execute(query, params)
        conn.commit()
        
        cursor.close()
        conn.close()     
