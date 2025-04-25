from utils.exceptions import CardBlockedError, InvalidPinError

class AuthService:
    def __init__(self):
        self.correct_pin = "1891"
        self.pin_attempts = 0
        self.card_blocked = False

    def validate_pin(self, cardPin):
        try:
            if self.card_blocked:
                raise CardBlockedError()

            if not self._is_pin_correct(cardPin):
                self._handle_failed_attempt()
                raise InvalidPinError(3 - self.pin_attempts)

            self._reset_attempts()
            return True

        except (CardBlockedError, InvalidPinError) as e:
            print(e)
            return False
        except Exception as e:
            print(f"Unexpected error during PIN validation: {e}")
            return False

    def _is_pin_correct(self, cardPin):
        return cardPin == self.correct_pin

    def _handle_failed_attempt(self):
        self.pin_attempts += 1
        if self.pin_attempts >= 3:
            self.card_blocked = True

    def _reset_attempts(self):
        self.pin_attempts = 0

    def is_card_blocked(self):
        return self.card_blocked
