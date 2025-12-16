"""Module contains methods to analyse the JSON file to extract the prime numbers and its square."""

import json
import math
import random
from pathlib import Path
from typing import Any, Dict, List, Set

PATH = Path("") / "src" / "assignment_5" / "data.json"


def is_prime(number: int) -> bool:
    """Checks if the number is prime.

    Args:
        number: The number to be checked for prime.

    Returns:
        True if the number is prime, False if the number is not prime.
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def read_json() -> List[Dict[str, Any]]:
    """Reads the json file and converts it to list of dictionaries.

    Returns:
        Returns list of dictionaries.
    """
    with open(PATH.absolute(), "r") as file:
        data = json.load(file)
    return data


def list_with_square_of_primes(data: List[Dict[str, Any]]) -> List[int]:
    """Extracts the square of numbers whose value is prime.

    Args:
        data: JSON data with dictionary having value as keys.

    Returns:
        List of square of prime numbers from the JSON.
    """
    return [dictionary["value"] ** 2 for dictionary in data if is_prime(dictionary["value"])]


def set_with_unique_squared_values(squared_list: List[int]) -> Set[int]:
    """Extracts unique square numbers from the list of square numbers.

    Args:
        squared_list: List of square numbers with duplicate values.

    Returns:
        Set of squared numbers from the list.
    """
    return {num for num in squared_list}


if __name__ == "__main__":
    if not PATH.exists():
        data = [{"id": i, "value": random.randint(1, 100)} for i in range(1, 10001)]
        with open(PATH.absolute(), "w") as json_file:
            json.dump(data, json_file)

    json_data = read_json()
    square_of_primes = list_with_square_of_primes(json_data)
    unique_square_of_primes = set_with_unique_squared_values(square_of_primes)
    print(square_of_primes)
    print(unique_square_of_primes)
