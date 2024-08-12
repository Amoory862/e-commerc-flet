class TFormatException(Exception):
    """Custom exception class to handle various format-related errors."""

    def __init__(self, message='An unexpected format error occurred. Please check your input.'):
        self.message = message
        super().__init__(self.message)

    @classmethod
    def from_message(cls, message):
        """Create a format exception from a specific error message."""
        return cls(message)

    @classmethod
    def from_code(cls, code):
        """Create a format exception from a specific error code."""
        messages = {
            'invalid-email-format': 'The email address format is invalid. Please enter a valid email.',
            'invalid-phone-number-format': 'The provided phone number format is invalid. Please enter a valid number.',
            'invalid-date-format': 'The date format is invalid. Please enter a valid date.',
            'invalid-url-format': 'The URL format is invalid. Please enter a valid URL.',
            'invalid-credit-card-format': 'The credit card format is invalid. Please enter a valid credit card number.',
            'invalid-numeric-format': 'The input should be a valid numeric format.',
            # Add more cases as needed...
        }
        return cls(messages.get(code, 'An unexpected format error occurred. Please check your input.'))
