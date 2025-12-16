"""Module contains functions to swap variables using different methods."""

from typing import Any, Tuple


def swap_variables_using_third_variable(variable_1: Any, variable_2: Any) -> Tuple[Any, Any]:
    """Swap variables using third temporary variable.

    Args:
        variable_1 : First variable to be swapped.
        variable_2 : Second variable to be swapped.

    Returns:
        Tuple: Swapped variables.
    """
    temp = variable_1
    variable_1 = variable_2
    variable_2 = temp
    return variable_1, variable_2


def swap_variables_without_third_variable(
    variable_1: int | float, variable_2: int | float
) -> Tuple[int | float, int | float]:
    """Swap variables without using third temporary variable for numeric values alone.

    Args:
        variable_1 : First variable to be swapped.
        variable_2 : Second variable to be swapped.

    Raises:
        TypeError: When the variable is not numeric.

    Returns:
        Tuple: Swapped variables.
    """
    try:
        variable_1 = variable_1 + variable_2
        variable_2 = variable_1 - variable_2
        variable_1 = variable_1 - variable_2
    except TypeError:
        raise TypeError("Both variables must be either int or float for this method.")
    else:
        return variable_1, variable_2


def swap_variables_using_tuple_unpacking(variable_1: Any, variable_2: Any) -> Tuple[Any, Any]:
    """Swap variables without using third temporary variable - tuple unpacking.

    Args:
        variable_1 : First variable to be swapped.
        variable_2 : Second variable to be swapped.

    Returns:
        Tuple: Swapped variables.
    """
    variable_1, variable_2 = variable_2, variable_1
    return variable_1, variable_2


if __name__ == "__main__":
    x: int | float = 5
    y: int | float = 10
    x, y = swap_variables_without_third_variable(x, y)
    print(f"After swapping using without third variable: x = {x}, y = {y}")

    variable_1 = "asd"
    variable_2 = "qwe"

    variable_1, variable_2 = swap_variables_using_tuple_unpacking(variable_1, variable_2)
    print(
        f"After swapping using tuple unpacking: variable_1 = {variable_1} , variable_2 = {variable_2} "
    )
    while True:
        variable_1, variable_2 = input("Enter two values to swap separated by space: ").split()
        try:
            variable_1, variable_2 = swap_variables_using_tuple_unpacking(variable_1, variable_2)
            print(
                f"After swapping without third variable: variable_1 = {variable_1} , variable_2 = {variable_2} "
            )
            flag = int(input("Do you want to continue? (1 for Yes / 0 for No): "))
            if flag == 0:
                break
        except TypeError as e:
            print(e, "Please enter numeric values.")
    # this part is to show that error is thrown for non numeric values
    # try:
    #     swap_variables_without_third_variable(variable_1, variable_2)
    # except TypeError as e:
    #     print(e)
