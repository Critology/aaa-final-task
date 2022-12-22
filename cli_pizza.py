import click
from time_decorator import log
from pizza_classes import PizzaBase, Margherita, Hawaiian, Pepperoni, Size

MENU = {
    "Margherita": Margherita(),
    "Pepperoni": Pepperoni(),
    "Hawaiian": Hawaiian()
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
    "is_delivered",
    default=False,
    is_flag=True,
    help="Do you want to deliver your order?",
)
@click.option("--size", default="L", help="What size do you want?")
@click.argument("pizza", nargs=1)
def order(pizza: str, size: str, is_delivered: bool):
    """Bakes and deliveres pizza if needed."""

    if pizza not in MENU.keys():
        print("We dont have such pizza\n"f'Choose between: {", ".join(MENU.keys())}')
        return
    try:
        Size[size].value
    except KeyError:
        print("We dont have such pizza size.\nTry L or XL")
        return
    bake(MENU[pizza])
    if is_delivered:
        delivery(MENU[pizza])
    else:
        print("Enjoy your pizza.")


@cli.command()
def menu():
    """Returns menu"""
    for pizza in MENU.values():
        print(f"{pizza}: includes {', '.join(pizza.ingredients.keys())}")


if __name__ == "__main__":
    status = cli()
