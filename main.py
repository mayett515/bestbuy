import store
import products


def start(best_buy):
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option: ")

        if choice == "1":
            print("\nAvailable Products:")
            for i, product in enumerate(best_buy.get_all_products()):
                print(f"{i + 1}. {product.show()}")

        elif choice == "2":
            print(f"\nTotal amount in store: {best_buy.get_total_quantity()} items")

        elif choice == "3":
            active_products = best_buy.get_all_products()
            if not active_products:
                print("No active products available.")
                continue

            print("\nAvailable Products:")
            for i, product in enumerate(active_products):
                print(f"{i + 1}. {product.show()}")

            order_list = {}
            while True:
                try:
                    choice = input("Enter the number of the product to add to cart (or 'done' to finish): ")
                    if choice.lower() == 'done':
                        break

                    index = int(choice) - 1
                    if index < 0 or index >= len(active_products):
                        raise ValueError

                    product = active_products[index]
                    quantity = int(input(f"How many {product.name} would you like? "))

                    if quantity <= 0:
                        raise ValueError

                    order_list[product] = quantity

                except ValueError:
                    print("Invalid input. Please enter a valid product number or 'done' to finish.")

            if not order_list:
                print("No items added to cart. Order cancelled.")
                continue

            try:
                total_cost = best_buy.order(order_list)
                print(f"\nOrder successful! Total cost: ${total_cost:.2f}")

                # Show updated inventory
                print("\nUpdated Inventory:")
                for product in best_buy.get_all_products():
                    print(product.show())

            except Exception as e:
                print(f"\nOrder failed: {str(e)}")

        elif choice == "4":
            print("Thank you for shopping at Best Buy!")
            break

        else:
            print("Invalid option. Please choose again.")


# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

promotion = products.PercentageDiscount("good sale", 10)
product_list[0].promotion = promotion
best_buy = store.Store(product_list)

# Start the application
start(best_buy)
