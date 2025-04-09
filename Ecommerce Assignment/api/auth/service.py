import bcrypt
from http import HTTPStatus
from .model import UserModel

class AuthService:
    @staticmethod
    def register_user(user_details):
        if UserModel.user_exists(user_details["email"]):
            return {"error": "User already exists. Please log in."}, HTTPStatus.BAD_REQUEST

        success = UserModel.create_user(
            user_details["name"], user_details["email"],
            user_details["password"], user_details["phone_number"],
            user_details["address"]
        )

        if success:
            return {"message": "User registered successfully. Please login."}, HTTPStatus.CREATED
        return {"error": "User registration failed"}, HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def authenticate_user(email, password):
        user = UserModel.get_user_by_email(email)
        if not user:
            return {"error": "Invalid email or password"}, HTTPStatus.UNAUTHORIZED

        user_id, user_name, stored_hash = user

        if not AuthService._verify_password(password, stored_hash):
            return {"error": "Invalid email or password"}, HTTPStatus.UNAUTHORIZED

        return {"userId": user_id, "userName": user_name}, HTTPStatus.OK

    @staticmethod
    def _verify_password(password, stored_hash):
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
