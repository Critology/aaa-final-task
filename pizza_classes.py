from enum import Enum


class Size(Enum):

    L = 1
    XL = 2


class PizzaBase:
    """Pizza base class sets and returns size and ingridients"""

    def __init__(self, size: str = "L") -> None:
        self._size = size
        ingredients = {}
        ingredients["tomato sauce"] = 200 * Size[self._size].value
        ingredients["mozzarella"] = 200 * Size[self._size].value
        self._ingredients = ingredients

    @property
    def size(self) -> str:
        return self._size

    @property
    def ingredients(self) -> dict:
        """dict() method."""
        return self._ingredients

    @size.setter
    def size(self, new_size: str) -> None:
        """This weird setter checkup is how it is made in EAFP, lol."""
        try:
            self._size = Size[new_size]
            if self._size != new_size:
                for key, value in self._ingredients.items():
                    if new_size == 'L':
                        self._ingredients[key] = int(value / 2)
                    if new_size == 'XL':
                        self._ingredients[key] = value * 2
        except KeyError:
            raise KeyError("Try L or XL")

    def __hash__(self) -> int:
        return hash((self.ingredients, self._size))

    def __eq__(self, other) -> bool:
        """Better type of checkup."""
        if isinstance(other, PizzaBase):
            return self.ingredients == other.ingredients
        raise TypeError("Compare pizza and pizza.")

    def __repr__(self) -> str:
        return self.__class__.__name__


class Margherita(PizzaBase):
    """Margo class"""

    def __init__(self, size: str = 'L') -> None:
        super().__init__(size)
        self._ingredients["tomatoes"] = 250 * Size[self._size].value


class Pepperoni(PizzaBase):
    """Pepe class"""

    def __init__(self, size: str = 'L') -> None:
        super().__init__(size)
        self._ingredients["pepperoni"] = 250 * Size[self._size].value


class Hawaiian(PizzaBase):
    """Hawaiii class"""

    def __init__(self, size: str = 'L') -> None:
        super().__init__(size)
        self._ingredients["pineapples"] = 250 * Size[self._size].value
        self._ingredients["chicken"] = 250 * Size[self._size].value
