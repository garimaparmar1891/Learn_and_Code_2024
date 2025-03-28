from database import get_database_connection
import bcrypt

class UserModel:
    @staticmethod
    def get_user_by_email(email):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, name, password FROM Users WHERE email = ?", (email,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def user_exists(email):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM Users WHERE email = ?", (email,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_user(name, email, password, phone, address):
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Users (name, email, password, phone, address) VALUES (?, ?, ?, ?, ?)",
                (name, email, hashed_password, phone, address)
            )
            conn.commit()
            return True
        except Exception as e:
            print("Error inserting user:", e)
            return False
        finally:
            cursor.close()
            conn.close()
