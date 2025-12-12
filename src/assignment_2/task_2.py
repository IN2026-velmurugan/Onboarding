from typing import (  # noqa: D100 - Missing docstring in public module (auto-generated noqa)
    Any,
    Tuple,
)


def swap_variable_using_third_variable(a: Any, b: Any) -> Tuple[Any, Any]:
    """To swap variable using third temporary variable.

    Args:
        a(Any) : Variable 1
        b(Any) : Variable 2

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
    """To swap variable without using third temporary variable for numeric values alone.

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
    """To swap variable without using third temporary variable.

    Args:
        a(Any) : Variable 1
        b(Any) : Variable 2

    Returns:
        Tuple[Any, Any]: swapped variables
    """
    a, b = b, a
    return a, b


if __name__ == "__main__":
    x = 5
    y = 10
    swap_variable_without_third_variable(x, y)
    print(f"After swapping using without third variable: x = {x}, y = {y}")

    a = "asd"
    b = "qwe"

    swap_variable_using_tuple_unpacking(a, b)
    print("After swapping using tuple unpacking: a ={a} , b ={b} ")
    try:
        swap_variable_without_third_variable(a, b)
    except TypeError as e:
        print(e)
