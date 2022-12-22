from time import perf_counter
from random import randint
from pizza_classes import PizzaBase


def log(text: str = "Time of executing _"):
    """Replaces _ in your text with time of function executing"""

    def inner(func):

        def wrapper_timer(pizza: PizzaBase):
            start_time = perf_counter()
            value = func(pizza)
            end_time = perf_counter()
            run_time = end_time - start_time
            print(
                text.replace("_", f"{int(run_time + randint(4, 7))}")
            )
            return value

        return wrapper_timer

    return inner
