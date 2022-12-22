import pytest
from pizza_classes import Margherita, Hawaiian, Pepperoni


@pytest.mark.parametrize(
    "pizza_class, name",
    [
        (Margherita, "Margherita"),
        (Pepperoni, "Pepperoni"),
        (Hawaiian, "Hawaiian"),
    ],
)
def test_pizza_default(pizza_class, name: str):
    assert str(pizza_class()) == name
    assert pizza_class().size == "L"


@pytest.mark.parametrize(
    "pizza_class, amount",
    [
        (Margherita, 200),
        (Pepperoni, 200),
        (Hawaiian, 200),
    ],
)
def test_size_switch(pizza_class, amount: str):
    pizza = pizza_class()
    pizza.size = "XL"
    assert pizza.ingredients["mozzarella"] == amount * 2
    pizza.size = "L"
    assert pizza.ingredients["mozzarella"] == amount


def test_size_comparison():
    assert Margherita(size="L") != Margherita(size="XL")
    assert Margherita() != Hawaiian() != Pepperoni()


def test_ingredients():
    ingredients = {}
    ingredients["tomatoes"] = 250
    ingredients["tomato sauce"] = 200
    ingredients["mozzarella"] = 200
    assert Margherita().ingredients == ingredients


def test_wrong_size():
    with pytest.raises(KeyError):
        Margherita(size="S")
