class TExceptions(Exception):
    """Exception class for handling various errors."""
    
    def __init__(self, message="An unexpected error occurred. Please try again."):
        self.message = message
        super().__init__(self.message)

    @classmethod
    def from_code(cls, code):
        """Create an authentication exception from a Firebase authentication exception code."""
        messages = {
            'email-already-in-use': 'The email address is already registered. Please use a different email.',
            'invalid-email': 'The email address provided is invalid. Please enter a valid email.',
            'weak-password': 'The password is too weak. Please choose a stronger password.',
            'user-disabled': 'This user account has been disabled. Please contact support for assistance.',
            'user-not-found': 'Invalid login details. User not found.',
            'wrong-password': 'Incorrect password. Please check your password and try again.',
            'INVALID_LOGIN_CREDENTIALS': 'Invalid login credentials. Please double-check your information.',
            'too-many-requests': 'Too many requests. Please try again later.',
            'invalid-argument': 'Invalid argument provided to the authentication method.',
            'invalid-password': 'Incorrect password. Please try again.',
            'invalid-phone-number': 'The provided phone number is invalid.',
            'operation-not-allowed': 'The sign-in provider is disabled for your Firebase project.',
            'session-cookie-expired': 'The Firebase session cookie has expired. Please sign in again.',
            'uid-already-exists': 'The provided user ID is already in use by another user.',
            'sign_in_failed': 'Sign-in failed. Please try again.',
            'network-request-failed': 'Network request failed. Please check your internet connection.',
            'internal-error': 'Internal error. Please try again later.',
            'invalid-verification-code': 'Invalid verification code. Please enter a valid code.',
            'invalid-verification-id': 'Invalid verification ID. Please request a new verification code.',
            'quota-exceeded': 'Quota exceeded. Please try again later.',
        }
        return cls(messages.get(code, "An unexpected error occurred. Please try again."))
