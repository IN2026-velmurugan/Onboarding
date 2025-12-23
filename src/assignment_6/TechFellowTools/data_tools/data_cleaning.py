"""Functions to perform data cleaning on list or string."""

from typing import Any


def is_float(value: str) -> bool:
    """Check if the string is float.

    Args:
        value: String to be checked.

    Returns:
        True if the string is float, False if not.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def remove_nulls(data: list[Any]) -> list[Any]:
    """Remove the None value from the list.

    Args:
        data: list in which the None values to be removed.

    Returns:
        Data without None values.
    """
    return list(filter(lambda x: x is not None, data))


def remove_duplicates(data: list[Any]) -> list[Any]:
    """Remove the duplicate element from the list.

    Args:
        data: list in which the duplicates should be removed.

    Returns:
        List without duplicates.
    """
    return list(dict.fromkeys(data))


def normalize_whitespace(sentence: str) -> str:
    """Normalize the string by replacing the "tab" and "newline" characters to space.

    Args:
        text: The string to be normalized.

    Returns:
        The normalized string.
    """
    return " ".join(sentence.split())


def cast_to_float(values: list[str]) -> list[float]:
    """Convert the list of string to list of float.

    Args:
        values: The list to be converted.

    Returns:
        The converted list.
    """
    return [float(value) for value in values if is_float(value)]


def clip_outliers(values: list[float], min_val: float, max_val: float):
    """Clip the values that are out of range.

    Args:
        values: Values to be clipped.
        min_val: Lower bound.
        max_val: Upper bound.

    Returns:
        List of clipped values.
    """
    return list(filter(lambda x: min_val <= x <= max_val, values))
