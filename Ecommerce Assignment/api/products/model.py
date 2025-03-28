from database import get_database_connection

class ProductModel:
    @staticmethod
    def get_products_by_category(category_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT name, price, quantity_available FROM Products WHERE category_id = ?",
                (category_id,),
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
