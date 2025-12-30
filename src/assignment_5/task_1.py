"""Function to analyse the JSON file to extract the prime numbers & their square."""

import json
import math
import random
from pathlib import Path
from typing import Any

from src.assignment_3.task_4 import json_analyzer

PATH = Path("") / "src" / "assignment_5" / "data.json"


def is_prime(number: int) -> bool:
    """Check if the number is prime.

    Args:
        number: The number to be checked for prime.

    Returns:
        True if the number is prime, False if the number is not prime.
    """
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, math.isqrt(number) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def get_square_of_primes(data: list[dict[str, Any]]) -> list[int]:
    """Extract the square of numbers whose "value" is prime.

    Args:
        data: JSON data.

    Returns:
        List of square of prime numbers from the JSON.
    """
    return list(
        map(
            lambda d: d["value"] ** 2,
            filter(lambda d: "value" in d and is_prime(d["value"]), data),
        )
    )


def filter_unique_values(squared_list: list[int]) -> set[int]:
    """Extract unique square numbers from the list of square numbers.

    Args:
        squared_list: List of square numbers with duplicate values.

    Returns:
        set of squared numbers from the list.
    """
    return set(squared_list)


def seed_json() -> None:
    """Seed JSON value to the provided path."""
    if not PATH.exists() or PATH.stat().st_size == 0:
        data = [{"id": i, "value": random.randint(1, 100)} for i in range(1, 10001)]
        with open(PATH.absolute(), "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)


if __name__ == "__main__":
    seed_json()

    json_data = json_analyzer(str(PATH.absolute()))
    square_of_primes = get_square_of_primes(json_data)
    unique_square_of_primes = filter_unique_values(square_of_primes)
    print(square_of_primes)
    print(unique_square_of_primes)
