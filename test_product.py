import pytest
from products import Product
import store


def test_create_normal_product():
    product = Product("Apple", 1.99, 10)
    assert product.name == "Apple"
    assert product.price == 1.99
    assert product.quantity == 10
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", 1.99, 10)

    with pytest.raises(ValueError):
        Product("Apple", -1.99, 10)

    with pytest.raises(ValueError):
        Product("Apple", 1.99, -1)


def test_product_becomes_inactive_at_zero_quantity():
    product = Product("Apple", 1.99, 1)
    product.set_quantity(0)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_correct_output():
    product = Product("Apple", 1.99, 10)
    total_price = product.buy(2)
    assert total_price == 3.98
    assert product.quantity == 8


def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("Apple", 1.99, 5)
    with pytest.raises(Exception):
        product.buy(6)




