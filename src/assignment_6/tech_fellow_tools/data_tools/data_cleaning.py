"""Module having the functions to perform data cleaning on List or string."""

from typing import Any, List


def remove_nulls(data: List[Any]) -> List[Any]:
    """Removes the None value from the list.

    Args:
        data: List in which the None to be removed.

    Returns:
        The data with all the "None" removed.
    """
    return [item for item in data if item is not None]


def remove_duplicates(data: List[Any]) -> List[Any]:
    """Removes the duplicate element from the list.

    Args:
        data: List in which the duplicates should be removed.

    Returns:
        List with duplicate elements removed.
    """
    return list(dict.fromkeys(data))


def normalize_whitespace(text: str) -> str:
    """Normalizes the space by replacing the "tab" and "newline" characters to space.

    Args:
        text: The string to be normalized.

    Returns:
        The normalized string.
    """
    return " ".join(text.split())


def cast_to_float(values: List[str]) -> List[float]:
    """Converts the list of string to list of float.

    Args:
        values: The list to be converted.

    Returns:
        The converted list.
    """
    return [float(v) for v in values if v.replace(".", "", 1).isdigit()]


def clip_outliers(values: List[float], min_val: float, max_val: float):
    """To clip the values that are out of range.

    Args:
        values: Values to be clipped.
        min_val: Lower bound.
        max_val: Upper bound.

    Returns:
        List containing the list with clipped value.
    """
    return [min(max(v, min_val), max_val) for v in values]
