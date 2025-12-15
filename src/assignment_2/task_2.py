"""This module contains functions to swap variables using different methods."""

from typing import (
    Any,
    Tuple,
)


def swap_variable_using_third_variable(a: Any, b: Any) -> Tuple[Any, Any]:
    """Swap variable using third temporary variable.

    Args:
        a : Variable 1
        b : Variable 2

    Returns:
        Tuple[Any, Any]: swapped variables
    """
    temp = a
    a = b
    b = temp
    return a, b


def swap_variable_without_third_variable(
    a: int | float, b: int | float
) -> Tuple[int | float, int | float]:
    """Swap variable without using third temporary variable for numeric values alone.

    Args:
        a(int | float) : Variable 1
        b(int | float) : Variable 2

    Raises:
        TypeError: when the variable is not numeric

    Returns:
        Tuple[int | float, int | float]: swapped variables
    """
    try:
        a = a + b
        b = a - b
        a = a - b
    except TypeError:
        raise TypeError("Both variables must be either int or float for this method.")
    else:
        return a, b


def swap_variable_using_tuple_unpacking(a: Any, b: Any) -> Tuple[Any, Any]:
    """Swap variable without using third temporary variable.

    Args:
        a : Variable 1
        b : Variable 2

    Returns:
        Tuple[Any, Any]: swapped variables
    """
    a, b = b, a
    return a, b


if __name__ == "__main__":
    x: int | float = 5
    y: int | float = 10
    x, y = swap_variable_without_third_variable(x, y)
    print(f"After swapping using without third variable: x = {x}, y = {y}")

    a = "asd"
    b = "qwe"

    a, b = swap_variable_using_tuple_unpacking(a, b)
    print(f"After swapping using tuple unpacking: a = {a} , b = {b} ")
    while True:
        a, b = input("Enter two values to swap separated by space: ").split()
        try:
            a, b = swap_variable_using_tuple_unpacking(a, b)
            print(f"After swapping without third variable: a = {a} , b = {b} ")
            flag = int(input("Do you want to continue? (1 for Yes / 0 for No): "))
            if flag == 0:
                break
        except TypeError as e:
            print(e, "Please enter numeric values.")
    # this part is to show that error is thrown for non numeric values
    # try:
    #     swap_variable_without_third_variable(a, b)
    # except TypeError as e:
    #     print(e)
