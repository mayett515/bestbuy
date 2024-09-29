# In this implementation, we've created an abstract Promotion class and three concrete promotion classes:
#
# We defined the Promotion class as abstract since there isn't a generic promotion.
# Each concrete promotion (PercentageDiscount, SecondItemHalfPrice, and BuyTwoGetOneFree) implements the apply_promotion method.
# We updated the Product class to include a promotion attribute with getter/setter methods.
# The show method now displays the current promotion if one exists.
# The buy method applies the promotion if one is set, otherwise uses the regular price calculation.
# Best practices followed:
#
# Using inheritance and polymorphism for flexible promotion handling.
# Implementing the Open/Closed Principle by allowing new promotions without modifying existing code.
# Using type hints for better code readability and maintainability.
# Providing clear error messages for invalid operations.
# Maintaining existing validation logic while adding new features.
# This design allows for easy addition of new promotion types in the future without modifying the existing codebase, demonstrating the power of object-oriented programming principles [1][2][3][4].