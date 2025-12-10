"""Task 1.

This module contains functions for:
- reverse the words in a sentence
- find roots of a quadratic equation
- evaluate boolean conditions
"""

import math


# Task 1
def reverse_words(sentence=""):
    """_summary_.

    method to reverse the sentence words.

    Args:
        sentence (string to be displayed, optional): _description_. Defaults to "".

    Returns:
        _string_: _words arranged in reverse order_
    """
    result = ""
    for item in sentence.split(" "):
        result = item + " " + result
    return result


def solve_quad(a: float, b: float, c: float):
    """_summary_.

    to find the roots of the quadratic expression aX^2 + bX + c.

    Args:
        a (float): a in expression
        b (float): b in expression
        c (float): c in expression

    Returns:
        tuple : roots for the given quadratic equation
    """
    dis = math.sqrt(b**2 - 4 * a * c)
    root1 = (-b + dis) / (2 * a)
    root2 = (-b - dis) / (2 * a)
    return (root1, root2)


def evaluate_conditions(a: bool, b: bool, c: bool):
    """_summary_.

    To evaluate the boolean expression

    Args:
        a (bool): a
        b (bool): b
        c (bool): c

    Returns:
        bool: True if at least any 2 of the input is true
    """
    return (a and b) or (b and c) or (c and a)


print("Reversed words:", reverse_words(input("Enter a Sentence\n")))

print("Quadratic roots:", solve_quad(1, -5, 6))

print("Conditions evaluation:", evaluate_conditions(True, False, True))
