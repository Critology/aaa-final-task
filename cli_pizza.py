import click
from time_decorator import log
from pizza_classes import PizzaBase, Margherita, Hawaiian, Pepperoni

MENU = {
    "Margherita": Margherita(),
    "Pepperoni": Pepperoni(),
    "Hawaiian": Hawaiian()
}

SIZES = {
    "L": 1,
    "XL": 2
}


@log("Made in _ minutes.")
def bake(pizza: PizzaBase) -> None:
    pass


@log("Delivered in _ minutes.")
def delivery(pizza: PizzaBase) -> None:
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--delivery",
    "is_delivery_needed",
    default=False,
    is_flag=True,
    help="Do you want to deliver your order?",
)
@click.option("--size", default="L", help="What size do you want?")
@click.argument("pizza", nargs=1)
def order(pizza: str, size: str, is_delivery_needed: bool):
    """Bakes and deliveres pizza if needed."""

    if pizza not in MENU.keys():
        print("We dont have such pizza\n"f'Choose between: {", ".join(MENU.keys())}')
        return
    if size not in SIZES.keys():
        print("We dont have such pizza size.\nTry L or XL")
        return
    bake(MENU[pizza])
    if is_delivery_needed:
        delivery(MENU[pizza])
    print("Enjoy your pizza.")


@cli.command()
def menu():
    """Returns menu"""
    for pizza in MENU.values():
        print(f"{pizza}: includes {', '.join(pizza.ingredients.keys())}")


if __name__ == "__main__":
    status = cli()
