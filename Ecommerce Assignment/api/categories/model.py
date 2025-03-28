from database import get_database_connection

class CategoryModel:
    @staticmethod
    def get_all_categories():
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, name FROM categories")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
