"""This file has a few functions to do things with numbers."""


@staticmethod
def add_two(one, two):
    """Adds two values together and returns it."""
    return one + two


@staticmethod
def add_three(one, two, three):
    """Adds three values together and returns it."""
    return one + two + three


if __name__ == "__main__":
    print(add_two(5, 6))
    print(add_three(5, 6, 7))
