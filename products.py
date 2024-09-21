class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Product name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to buy must be a positive integer")

        if not self.is_active():
            raise Exception("Product is not active")

        if self.quantity < quantity:
            raise Exception("Not enough stock available")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

