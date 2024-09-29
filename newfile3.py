class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)  # Initialize with quantity 0

    def set_quantity(self, quantity):
        # Ignore any attempt to set a non-zero quantity
        pass

    def get_quantity(self) -> float:
        return 0.0  # Always return 0

    def buy(self, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to buy must be a positive integer")
        if quantity != 1:
            raise ValueError(f"Cannot purchase {quantity} units of {self.name}. Only single purchases allowed.")

        # Since it's a non-stocked product, we don't need to check availability
        total_price = self.price * 1
        return total_price


# Usage example
windows_license = NonStockedProduct("Microsoft Windows License", 199.99)
print(windows_license.get_quantity())  # Output: 0.0
try:
    windows_license.set_quantity(10)
except Exception as e:
    print(e)  # No exception raised, but quantity remains 0

print(windows_license.get_quantity())  # Still outputs: 0.0

try:
    windows_license.buy(2)
except ValueError as e:
    print(e)  # Output: Cannot purchase 2 units of Microsoft Windows License. Only single purchases allowed.

cost = windows_license.buy(1)
print(f"Purchased 1 unit of {windows_license.name} for ${cost:.2f}")