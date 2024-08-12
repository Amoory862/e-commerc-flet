import re
from typing import Optional

class Validator:
    @staticmethod
    def validate_email(value: Optional[str]) -> Optional[str]:
        if value is None or not value.strip():
            return 'Email is required.'

        # Regular expression for email validation
        email_reg_exp = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$')
        
        if not email_reg_exp.match(value):
            return 'Invalid email address.'

        return None

    @staticmethod
    def validate_password(value: Optional[str]) -> Optional[str]:
        if value is None or not value.strip():
            return 'Password is required.'

        # Check for minimum password length
        if len(value) < 6:
            return 'Password must be at least 6 characters long.'

        # Check for uppercase letters
        if not re.search(r'[A-Z]', value):
            return 'Password must contain at least one uppercase letter.'

        # Check for numbers
        if not re.search(r'[0-9]', value):
            return 'Password must contain at least one number.'

        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            return 'Password must contain at least one special character.'

        return None

    @staticmethod
    def validate_phone_number(value: Optional[str]) -> Optional[str]:
        if value is None or not value.strip():
            return 'Phone number is required.'

        # Regular expression for phone number validation (assuming a 10-digit US phone number format)
        phone_reg_exp = re.compile(r'^\d{10}$')
        
        if not phone_reg_exp.match(value):
            return 'Invalid phone number format (10 digits required).'

        return None

# Example usage
if __name__ == '__main__':
    print(Validator.validate_email('example@example.com'))  # Output: None
    print(Validator.validate_password('Password1!'))       # Output: None
    print(Validator.validate_phone_number('1234567890'))   # Output: None
