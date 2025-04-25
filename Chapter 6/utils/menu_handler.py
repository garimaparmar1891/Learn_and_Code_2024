from utils.console_io import ConsoleIO
from utils.exceptions import InvalidMenuChoiceError
import sys

class MenuHandler:
    def __init__(self, transaction_service):
        self.transaction_service = transaction_service
        self.options = {
            "1": self.transaction_service.withdraw_cash,
            "2": self.transaction_service.deposit_cash,
            "3": self.transaction_service.check_balance,
            "4": self._exit_app
        }

    def show_menu(self):
        while True:
            try:
                ConsoleIO.display_message("\nOptions:\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
                choice = ConsoleIO.get_input("Choose an option: ").strip()

                action = self.options.get(choice)
                if not action:
                    raise InvalidMenuChoiceError(f"'{choice}' is not a valid option.")
                
                action()

            except InvalidMenuChoiceError as e:
                ConsoleIO.display_message(str(e))
            except KeyboardInterrupt:
                ConsoleIO.display_message("\nExiting application due to keyboard interruption.")
                sys.exit()
            except Exception as e:
                ConsoleIO.display_message(f"An error occurred in menu: {e}")

    def _exit_app(self):
        ConsoleIO.display_message("Thank you for using the ATM. Goodbye!")
        sys.exit()
