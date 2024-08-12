from typing import List, Optional

# Assuming CartModel is a data class with an attribute 'items' being a list of ItemModel
class CartModel:
    def __init__(self, items: List['ItemModel']):
        self.items = items

class ItemModel:
    def __init__(self, price: Optional[float]):
        self.price = price

class PricingCalculator:
    @staticmethod
    def calculate_total_price(product_price: float, location: str) -> float:
        tax_rate = PricingCalculator.get_tax_rate_for_location(location)
        tax_amount = product_price * tax_rate

        shipping_cost = PricingCalculator.get_shipping_cost(location)

        total_price = product_price + tax_amount + shipping_cost
        return total_price

    @staticmethod
    def calculate_shipping_cost(product_price: float, location: str) -> str:
        shipping_cost = PricingCalculator.get_shipping_cost(location)
        return f"{shipping_cost:.2f}"

    @staticmethod
    def calculate_tax(product_price: float, location: str) -> str:
        tax_rate = PricingCalculator.get_tax_rate_for_location(location)
        tax_amount = product_price * tax_rate
        return f"{tax_amount:.2f}"

    @staticmethod
    def get_tax_rate_for_location(location: str) -> float:
        # Lookup the tax rate for the given location from a tax rate database or API.
        # Return the appropriate tax rate.
        return 0.15  # Example tax rate of 10%

    @staticmethod
    def get_shipping_cost(location: str) -> float:
        # Lookup the shipping cost for the given location using a shipping rate API.
        # Calculate the shipping cost based on various factors like distance, weight, etc.
        return 9.00  # Example shipping cost of $9

    @staticmethod
    def calculate_cart_total(cart: CartModel) -> float:
        return sum(item.price or 0 for item in cart.items)

# Example usage
cart_items = [ItemModel(10.00), ItemModel(20.00), ItemModel(None)]
cart = CartModel(cart_items)
total_price = PricingCalculator.calculate_total_price(30.00, 'SA')
shipping_cost = PricingCalculator.calculate_shipping_cost(30.00, 'SA')
tax_amount = PricingCalculator.calculate_tax(30.00, 'SA')
cart_total = PricingCalculator.calculate_cart_total(cart)



print(f"Total Price: ${total_price:.2f}")
print(f"Shipping Cost: ${shipping_cost}")
print(f"Tax Amount: ${tax_amount}")
print(f"Cart Total: ${cart_total:.2f}")
