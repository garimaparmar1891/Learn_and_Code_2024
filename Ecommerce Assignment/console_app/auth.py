import requests
from config import API_URL
from utils import is_server_available, print_server_error

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

class SignupManager:
    def signup(self):
        if not ServerRequestHandler.check_server():
            return False

        user_data = UserInputHandler.get_signup_data()
        if not user_data:
            return None

        response = ServerRequestHandler.send_request("signup", user_data)
        if response:
            print("\nUser Registered Successfully! Please log in.\n")
            return None
        return None

class LoginManager:
    def login(self):
        if not ServerRequestHandler.check_server():
            return False

        credentials = UserInputHandler.get_login_credentials()
        if not credentials:
            return None

        response_data = ServerRequestHandler.send_request("login", credentials)
        if response_data:
            print(f"\nWelcome {response_data['userName']} !!")
            return response_data
        else:
            return None

class UserInputHandler:
    @staticmethod
    def get_signup_data():
        return {
            "name": UserInputHandler.get_required_input("Enter Name: "),
            "email": UserInputHandler.get_required_input("Enter Email: "),
            "password": UserInputHandler.get_required_input("Enter Password: "),
            "phone_number": UserInputHandler.get_required_input("Enter Phone: "),
            "address": UserInputHandler.get_required_input("Enter Address: ")
        }

    @staticmethod
    def get_login_credentials():
        return {
            "email": UserInputHandler.get_required_input("Enter Email: "),
            "password": UserInputHandler.get_required_input("Enter Password: ")
        }

    @staticmethod
    def get_required_input(prompt):
        while True:
            field = input(prompt).strip()
            if field:
                return field
            print("This field is required. Please enter a value.")

    @staticmethod
    def get_user_choice(prompt, valid_choices):
        while True:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice
            print("Invalid choice. Please try again.")

class ServerRequestHandler:
    @staticmethod
    def check_server():
        if not is_server_available():
            print_server_error()
            return False
        return True

    @staticmethod
    def send_request(endpoint, data=None):
        try:
            url = f"{API_URL}/{endpoint}"
            response = requests.post(url, json=data) if data else requests.get(url)
            response_data = response.json()

            if response.status_code in [200, 201]:
                return response_data
            else:
                print(f"Error: {response_data.get('error', 'Invalid request')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect to the server. {e}")
            return None
