from typing import List
from products import Product


class Store:
    def __init__(self, initial_products=None):
        if initial_products is None:
            initial_products = []
        self.products = initial_products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the store")
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in the store")

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: dict[Product, int]) -> float:
        total_cost = 0.0

        # Validate the shopping list
        for product, quantity in shopping_list.items():
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"Invalid quantity for {product.name}: {quantity}")

        # Process each purchase
        for product, quantity in shopping_list.items():
            if product not in self.products:
                raise ValueError(f"{product.name} is not available in the store")

            try:
                cost = product.buy(quantity)
                total_cost += cost
            except Exception as e:
                raise Exception(f"Failed to purchase {quantity} units of {product.name}: {str(e)}")

        return total_cost
