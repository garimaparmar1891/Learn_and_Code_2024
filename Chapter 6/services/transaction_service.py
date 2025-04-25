import random
from utils.console_io import ConsoleIO
from utils.exceptions import (
    InvalidAmountError,
    InsufficientFundsError,
    ATMFundsError,
    DailyLimitExceededError,
    ServerConnectionError
)

class TransactionService:
    def __init__(self, auth_service):
        self.auth_service = auth_service
        self.account_balance = 5000
        self.atm_balance = 10000
        self.daily_limit = 3000
        self.daily_withdrawn = 0

    def withdraw_cash(self):
        try:
            self._simulate_server_connection()
            amount = self._get_valid_amount()
            self._validate_withdrawal(amount)
            self._process_withdrawal(amount)
            self._print_receipt(amount)
        except Exception as e:
            self._handle_withdrawal_error(e)

    def deposit_cash(self):
        try:
            amount = int(ConsoleIO.get_input("Enter amount to deposit: "))
            if amount <= 0:
                raise InvalidAmountError("Amount must be greater than 0.")
            self.account_balance += amount
            self.atm_balance += amount
            ConsoleIO.display_message(f"${amount} deposited successfully.")
        except Exception as e:
            self._handle_deposit_error(e)

    def check_balance(self):
        ConsoleIO.display_message(f"Your current balance is: ${self.account_balance}")

    def _simulate_server_connection(self):
        if random.choice([True, False, False, False]):
            raise ServerConnectionError("Server connection failed. Please try again later.")

    def _get_valid_amount(self):
        try:
            user_input = ConsoleIO.get_input("Enter amount to withdraw: ")
            amount = int(user_input)
            return amount
        except ValueError:
            raise InvalidAmountError("Invalid input. Please enter a valid numeric amount.")

    def _validate_withdrawal(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than 0.")
        if amount > self.account_balance:
            raise InsufficientFundsError("Insufficient funds in your account.")
        if amount > self.atm_balance:
            raise ATMFundsError("ATM does not have enough cash.")
        if self.daily_withdrawn + amount > self.daily_limit:
            raise DailyLimitExceededError("Daily withdrawal limit exceeded.")

    def _process_withdrawal(self, amount):
        self.account_balance -= amount
        self.atm_balance -= amount
        self.daily_withdrawn += amount

    def _print_receipt(self, amount):
        ConsoleIO.display_message(f"Please collect your cash: ${amount}")

    def _handle_withdrawal_error(self, error):
        if isinstance(error, (InvalidAmountError, InsufficientFundsError, ATMFundsError, DailyLimitExceededError, ServerConnectionError)):
            ConsoleIO.display_message(f"Transaction failed: {error}")
        else:
            ConsoleIO.display_message(f"Unexpected error occurred: {error}")

    def _handle_deposit_error(self, error):
        if isinstance(error, InvalidAmountError):
            ConsoleIO.display_message(f"Deposit failed: {error}")
        elif isinstance(error, ValueError):
            ConsoleIO.display_message("Invalid input. Please enter a valid number.")
        else:
            ConsoleIO.display_message(f"An error occurred during deposit: {error}")
