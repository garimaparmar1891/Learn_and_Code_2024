from authentication.auth import Auth

class SessionManager:
    def __init__(self, auth: Auth):
        self.auth = auth

    def handle_session(self):
        while True:
            choice = input("\n1. Signup\n2. Login\n3. Exit\nChoose an option: ").strip()

            if choice == "1":
                user = self.auth.signup_manager.signup()
            elif choice == "2":
                user = self.auth.login_manager.login()
            elif choice == "3":
                return None
            else:
                print("Invalid choice. Please try again.")
                continue

            if user is not None:
                return user  # Return user data on successful login/signup
