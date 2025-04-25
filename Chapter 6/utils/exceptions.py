class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class ATMFundsError(Exception):
    pass

class DailyLimitExceededError(Exception):
    pass

class ServerConnectionError(Exception):
    pass

class InvalidMenuChoiceError(Exception):
    pass

class CardBlockedError(Exception):
    def __init__(self, message="Your card is blocked due to multiple incorrect PIN attempts."):
        super().__init__(message)

class InvalidPinError(Exception):
    def __init__(self, attempts_left):
        message = f"Incorrect PIN. Attempts remaining: {attempts_left}"
        super().__init__(message)
