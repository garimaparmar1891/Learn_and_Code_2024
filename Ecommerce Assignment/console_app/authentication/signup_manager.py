from utils.user_input_handler import UserInputHandler
from utils.server_request_handler import ServerRequestHandler

class SignupManager:
    def signup(self):
        if not ServerRequestHandler.check_server():
            return False

        user_data = self.get_signup_fields()
        if not user_data:
            return None

        response = ServerRequestHandler.send_request("signup", user_data)
        if response:
            print("\nUser Registered Successfully! Please log in.\n")
            return None
        return None
    
    @staticmethod
    def get_signup_fields():
        return {
            "name": UserInputHandler.get_required_input("Enter Name: "),
            "email": UserInputHandler.get_required_input("Enter Email: "),
            "password": UserInputHandler.get_required_input("Enter Password: "),
            "phone_number": UserInputHandler.get_required_input("Enter Phone: "),
            "address": UserInputHandler.get_required_input("Enter Address: ")
        }
