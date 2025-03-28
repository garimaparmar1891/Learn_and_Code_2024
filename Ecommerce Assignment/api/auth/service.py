import bcrypt
from .model import UserModel

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
