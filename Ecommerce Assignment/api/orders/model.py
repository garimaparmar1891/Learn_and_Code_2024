from database import get_database_connection
from datetime import datetime

class OrderModel:
    @staticmethod
    def get_total_cart_amount(user_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT SUM(c.quantity * p.price)
                FROM Cart c
                JOIN Products p ON c.product_id = p.id
                WHERE c.user_id = ?
                """,
                (user_id,)
            )
            return cursor.fetchone()[0]
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_order(user_id, total_amount):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO Orders (user_id, total_amount, order_date) VALUES (?, ?, ?)",
                (user_id, total_amount, order_date),
            )
            cursor.execute("SELECT @@IDENTITY")
            order_id = cursor.fetchone()[0]
            if not order_id:
                return None, None
            conn.commit()
            return order_id, order_date
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def move_cart_to_order_items(order_id, user_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO order_details (order_id, product_id, quantity, price)
                SELECT ?, c.product_id, c.quantity, p.price
                FROM Cart c
                JOIN Products p ON c.product_id = p.id
                WHERE c.user_id = ?
                """,
                (order_id, user_id),
            )
            cursor.execute(
                """
                UPDATE Products
                SET quantity_available = quantity_available - c.quantity
                FROM Products p
                JOIN Cart c ON p.id = c.product_id
                WHERE c.user_id = ?
                """,
                (user_id,)
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def clear_cart(user_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Cart WHERE user_id = ?", (user_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_order_history(user_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT o.id AS order_id, o.order_date, 
                       p.name AS product_name, d.quantity, p.price
                FROM orders o
                JOIN order_details d ON o.id = d.order_id
                JOIN products p ON d.product_id = p.id
                WHERE o.user_id = ?
                ORDER BY o.order_date DESC
                """,
                (user_id,),
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
