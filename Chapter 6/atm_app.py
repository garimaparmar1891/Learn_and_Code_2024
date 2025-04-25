from services.auth_service import AuthService
from services.transaction_service import TransactionService
from utils.console_io import ConsoleIO
from utils.menu_handler import MenuHandler
from utils.exceptions import CardBlockedError, InvalidPinError
import sys

class ATMApp:
    def __init__(self):
        self.auth_service = AuthService()
        self.transaction_service = TransactionService(self.auth_service)
        self.menu_handler = MenuHandler(self.transaction_service)

    def run(self):
        try:
            while True:
                if self.auth_service.is_card_blocked():
                    raise CardBlockedError("Your card is blocked due to multiple incorrect PIN attempts.")

                cardPin = ConsoleIO.get_input("Enter your PIN: ")
                if self.auth_service.validate_pin(cardPin):
                    self.menu_handler.show_menu()

        except InvalidPinError as e:
            ConsoleIO.display_message(str(e))
            self.run()

        except CardBlockedError as e:
            ConsoleIO.display_message(str(e))

        except ValueError as e:
            ConsoleIO.display_message(str(e))
            self.run()

        except KeyboardInterrupt:
            ConsoleIO.display_message("\nExiting application due to keyboard interruption.")
            sys.exit()

        except Exception as e:
            ConsoleIO.display_message(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    ATMApp().run()
