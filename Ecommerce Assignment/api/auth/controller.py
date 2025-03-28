from .service import AuthService

class AuthController:
    @staticmethod
    def user_signup(user_details):
        return AuthService.register_user(user_details)

    @staticmethod
    def user_login(email, password):
        return AuthService.authenticate_user(email, password)
