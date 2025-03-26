from utils.user_input_handler import UserInputHandler
from authentication.signup_manager import SignupManager
from authentication.login_manager import LoginManager

class Auth:
    def __init__(self):
        self.signup_manager = SignupManager()
        self.login_manager = LoginManager()

    def handle_session(self):
        while True:
            choice = UserInputHandler.get_user_choice(
                "\n1. Signup\n2. Login\n3. Exit\nChoose an option: ", ["1", "2", "3"]
            )
            if choice == "1":
                return self.signup_manager.signup()
            elif choice == "2":
                return self.login_manager.login()
            elif choice == "3":
                print("Exiting program...")
                return True
