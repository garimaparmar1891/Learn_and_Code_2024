from utils.user_input_handler import UserInputHandler
from utils.server_request_handler import ServerRequestHandler

class LoginManager:
    def login(self):
        response_data = None

        if ServerRequestHandler.check_server():
            credentials = self.get_login_fields()
            if credentials:
                response_data = ServerRequestHandler.send_request("login", credentials)
                if response_data:
                    print(f"\nWelcome {response_data['userName']} !!")

        return response_data

    @staticmethod
    def get_login_fields():
        return {
            "email": UserInputHandler.get_required_input("Enter Email: "),
            "password": UserInputHandler.get_required_input("Enter Password: ")
        }
