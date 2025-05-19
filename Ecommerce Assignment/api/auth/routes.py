from . import auth_bp
from .controller import AuthController

@auth_bp.route("/signup", methods=["POST"])
def signup_route():
    return AuthController.user_signup()

@auth_bp.route("/login", methods=["POST"])
def login_route():
    return AuthController.user_login()
