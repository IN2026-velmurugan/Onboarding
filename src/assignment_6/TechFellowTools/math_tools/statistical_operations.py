"""Functions to perform statistical operations."""

import math


def mean(values: list[float | int]) -> float | int:
    """Calculate the mean of the list of values.

    Args:
        values: List of values for which the mean to be found.

    Raises:
        ValueError: When the input list is empty.

    Returns:
        Mean of the list.
    """
    if not values:
        raise ValueError("Input list must not be empty")

    return sum(values) / len(values)


def variance(values: list[float | int]) -> float | int:
    """Calculate the sample variance of the list of values.

    Args:
        values: List of values for which the variance to be found.

    Raises:
        ValueError: When the input list is empty or has less than 2 values.

    Returns:
        Sample variance of the list.
    """
    if not values:
        raise ValueError("Input list must not be empty")

    if len(values) < 2:
        raise ValueError("Sample variance requires at least 2 values")

    mu = mean(values)
    return sum((value - mu) ** 2 for value in values) / (len(values) - 1)


def standard_deviation(values: list[float | int]) -> float | int:
    """Calculate the sample standard deviation of the list of values.

    Args:
        values: List of values for which the standard Deviation to be found.

    Raises:
        ValueError: When the input list is empty or has less than 2 values.

    Returns:
        Sample standard deviation of the list.
    """
    if not values:
        raise ValueError("Input list must not be empty")

    return math.sqrt(variance(values))


def covariance(list_a: list[float | int], list_b: list[float | int]) -> float | int:
    """Calculate the sample covariance between two list of values.

    Args:
        list_a: First list of values.
        list_b: Second list of values between which the covariance to be found.

    Raises:
        ValueError: When the input list is empty, have different lengths,
                    or have less than 2 values.

    Returns:
        Sample covariance between the two list.
    """
    if not list_a or not list_b:
        raise ValueError("Input list must not be empty")

    if len(list_a) != len(list_b):
        raise ValueError("Input lists must have the same length")

    if len(list_a) < 2:
        raise ValueError("Sample covariance requires at least 2 values")

    mx, my = mean(list_a), mean(list_b)
    return sum((a - mx) * (b - my) for a, b in zip(list_a, list_b)) / (len(list_a) - 1)


def correlation(list_a: list[float | int], list_b: list[float | int]) -> float | int:
    """Calculate the correlation between two list of values.

    Args:
        list_a: First list of values.
        list_b: Second list of values between which the correlation to be found.

    Raises:
        ValueError: When the input list is empty, have different lengths,
                    have less than 2 values, or have zero variance.

    Returns:
        Correlated value of the two list.
    """
    if not list_a or not list_b:
        raise ValueError("Input list must not be empty")

    if len(list_a) != len(list_b):
        raise ValueError("Input lists must have the same length")

    if len(list_a) < 2:
        raise ValueError("Correlation requires at least 2 values")

    std_a = standard_deviation(list_a)
    std_b = standard_deviation(list_b)

    if std_a == 0 or std_b == 0:
        raise ValueError("Cannot calculate correlation: one or both lists have zero variance")

    result = covariance(list_a, list_b) / (std_a * std_b)
    return result
