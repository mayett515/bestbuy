from abc import ABC, abstractmethod
from typing import Optional

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        pass

class PercentageDiscount(Promotion):
    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        self.percentage = percentage / 100
    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        original_price = product.price * quantity
        discount_amount = original_price * self.percentage
        return original_price - discount_amount

class SecondItemHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        if quantity < 2:
            return product.price * quantity

        full_price_items = (quantity // 2) + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        if quantity < 3:
            return product.price * quantity

        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price








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
        self._promotion: Optional[Promotion] = None


    @property
    def promotion(self) -> Optional[Promotion]:
        return self._promotion

    @promotion.setter
    def promotion(self, promo: Optional[Promotion]):
        self._promotion = promo

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
        if self.promotion:
            promotion_name = self.promotion.name
            return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity} and current promotion {promotion_name}"
        else:
            return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to buy must be a positive integer")

        if not self.is_active():
            raise Exception("Product is not active")

        if self.quantity < quantity:
            raise Exception("Not enough stock available")
        if self.promotion:

            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)  # Calls Parent.__init__
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot purchase {quantity} units of {self.name}. Maximum allowed is {self.maximum}.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):

        pass

    def get_quantity(self) -> float:
        return 0.0

    def buy(self, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to buy must be a positive integer")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        return total_price