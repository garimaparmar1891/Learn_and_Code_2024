from database import get_database_connection

class CategoryModel:
    @staticmethod
    def get_categories():
        conn = get_database_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name FROM categories")
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result
