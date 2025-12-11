"""This module contains functions for:
- Classify a number as Positive, Negative or Zero
- to fid the factorial of a number
"""


def classify_number(number: int):
    """Classify the number as Positive, Negative or Zero.

    Args:
        number (int): Number to be classified

    Returns:
        string: Whether the number is Positive, Negative or Zero
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def factorial(n: int):
    """Calculate the factorial of a number.

    Args:
        n (int): Number to calculate factorial for

    Returns:
        int: Factorial of the number
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(
        "Number classification:",
        classify_number(int(input("Enter a number to classify:\n"))),
    )

    print(
        "Factorial:", factorial(int(input("Enter a number to calculate factorial:\n")))
    )
