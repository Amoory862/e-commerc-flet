from enum import Enum

# Switch of Custom Brand-Text-Size Widget
class TextSizes(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

class OrderStatus(Enum):
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'

class PaymentMethods(Enum):
    PAYPAL = 'paypal'
    GOOGLE_PAY = 'googlePay'
    APPLE_PAY = 'applePay'
    VISA = 'visa'
    MASTERCARD = 'masterCard'
    CREDIT_CARD = 'creditCard'
    PAYSTACK = 'paystack'
    RAZOR_PAY = 'razorPay'
    PAYTM = 'paytm'
