from datetime import datetime
import locale
from babel.numbers import format_currency # type: ignore

class TFormatter:
    @staticmethod
    def format_date(date=None):
        """Formats a datetime object into a readable date format."""
        if date is None:
            date = datetime.now()
        return date.strftime('%d-%b-%Y')  # Customize the date format as needed

    @staticmethod
    def format_currency(amount, locale_str='en_US', currency_symbol='$'):
        """Formats a float value into a currency string."""
        return format_currency(amount, currency_symbol, locale=locale_str)  # Customize the currency locale and symbol as needed

    @staticmethod
    def format_phone_number(phone_number):
        """Formats a phone number into a specific format for US phone numbers."""
        if len(phone_number) == 10:
            return f'({phone_number[:3]}) {phone_number[3:6]} {phone_number[6:]}'
        elif len(phone_number) == 11:
            return f'({phone_number[:4]}) {phone_number[4:7]} {phone_number[7:]}'
        return phone_number

    @staticmethod
    def international_format_phone_number(phone_number):
        """Formats an international phone number by adding a country code and grouping digits."""
        # Remove any non-digit characters from the phone number
        digits_only = ''.join(filter(str.isdigit, phone_number))
        
        # Handle the case where no digits are present
        if not digits_only:
            return phone_number
        
        # Extract the country code (assuming country code is always the first 1-3 digits)
        country_code = f'+{digits_only[:3]}' if len(digits_only) > 3 else f'+{digits_only}'
        digits_only = digits_only[len(country_code) - 1:]  # Adjust substring after country code

        # Format the remaining digits with a space separator
        formatted_number = f'{country_code} '
        for i in range(0, len(digits_only), 3):
            formatted_number += digits_only[i:i+3] + ' '

        return formatted_number.strip()

# Example usage
print(TFormatter.format_date())  # Example date format
print(TFormatter.format_currency(1234.56))  # Example currency format
print(TFormatter.format_phone_number('1234567890'))  # Example US phone number format
print(TFormatter.international_format_phone_number('+14155552671'))  # Example international phone number format
