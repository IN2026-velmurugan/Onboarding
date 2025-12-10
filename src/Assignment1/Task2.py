"""Task 2.

This module contains functions for:
- filtering the primes from a list of numbers
- inverting key value pairs in a dictionary
"""

import math
from typing import Any, Dict, List


def filter_primes(numbers: List[int]):
    """_summary_.

    Args:
        numbers (List[int]): _description_

    Returns:
        _type_: _description_
    """
    primes: List[int] = []
    for num in numbers:
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def invert_dict(input_dict: Dict[Any, Any]):
    """_summary_.

    dictionary where each unique value in the input becomes a key in
    the output that maps to a list of corresponding keys from the input.

    Args:
        input_dict (Dict[Any, Any]): Dictionary input

    Returns:
        Dict[Any, Any]: Dictionary with unique values from the input as keys
    """
    inverted_dict: Dict[Any, Any] = {}
    for key, value in input_dict.items():
        if value not in inverted_dict.keys():
            inverted_dict[value] = key
    return inverted_dict


print("Filtered Primes:", filter_primes([10, 15, 3, 7, 19, 20, 23, 24, 29]))

sample_dict = {"a": 1, "b": 2, "c": 3, "d": 2}
print("Inverted dictionary:", invert_dict(sample_dict))
