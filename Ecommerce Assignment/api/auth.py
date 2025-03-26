from flask import Blueprint, request, jsonify
import bcrypt
from database import get_database_connection

auth_bp = Blueprint("auth", __name__)

class AuthController:
    @staticmethod
    @auth_bp.route("/signup", methods=["POST"])
    def user_signup():
        user_details = request.json
        response, status = AuthService.register_user(user_details)
        return jsonify(response), status

    @staticmethod
    @auth_bp.route("/login", methods=["POST"])
    def user_login():
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        response, status = AuthService.authenticate_user(email, password)
        return jsonify(response), status


class AuthService:
    @staticmethod
    def register_user(user_details):
        if UserModel.user_exists(user_details["email"]):
            return {"error": "User already exists. Please log in."}, 400

        success = UserModel.create_user(
            user_details["name"], user_details["email"],
            user_details["password"], user_details["phone_number"],
            user_details["address"]
        )

        if success:
            return {"message": "User registered successfully. Please login."}, 201
        return {"error": "User registration failed"}, 500

    @staticmethod
    def authenticate_user(email, password):
        user = UserModel.get_user_by_email(email)

        if not user:
            return {"error": "Invalid email or password"}, 401

        user_id, user_name, stored_hash = user

        if not bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")):
            return {"error": "Invalid email or password"}, 401

        return {"userId": user_id, "userName": user_name}, 200


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
