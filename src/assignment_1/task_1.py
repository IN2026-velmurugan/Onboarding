"""This module contains functions to
reverse the words in a sentence,
find roots of a quadratic equation,
evaluate boolean conditions
"""

import math
from typing import Tuple


def reverse_words(sentence: str = "") -> str:
    """Method to reverse the sentence words.

    Args:
        sentence (str, optional): Sentence to be reversed Defaults to "".

    Returns:
        str: The sentence with words in reverse order.
    """
    return " ".join(sentence.split(" ")[::-1])


def solve_quad(a: float, b: float, c: float) -> Tuple[float, float] | None:
    """Find the roots of the quadratic expression aX^2 + bX + c.

    Args:
        a (float): a in expression
        b (float): b in expression
        c (float): c in expression

    Returns:
        tuple : roots for the given quadratic equation
    """
    if a == 0:
        print("Not a quadratic equation")
        return None
    dis = math.sqrt(b**2 - 4 * a * c)
    if dis < 0:
        print("No Real Roots")
        return None
    root1 = (-b + dis) / (2 * a)
    root2 = (-b - dis) / (2 * a)
    return (root1, root2)


def evaluate_conditions(a: bool, b: bool, c: bool) -> bool:
    """To evaluate the boolean expression.

    Args:
        a (bool): First boolean value.
        b (bool): Second boolean value.
        c (bool): Third boolean value.

    Returns:
        bool: True if at least any 2 of the input is true
    """
    return (a and b) or (b and c) or (c and a)


if __name__ == "__main__":
    print("Reversed words:", reverse_words(input("Enter a Sentence\n")))

    print("Quadratic roots:", solve_quad(1, -5, 6))

    print("Conditions evaluation:", evaluate_conditions(True, False, True))
