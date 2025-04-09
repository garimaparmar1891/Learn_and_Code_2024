from database import get_database_connection

class ProductModel:
    @staticmethod
    def get_products_by_category(category_id):
        conn = get_database_connection()
        cursor = conn.cursor()
      
        cursor.execute(
            "SELECT name, price, quantity_available FROM Products WHERE category_id = ?",
            (category_id,),
        )
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result
