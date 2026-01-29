"""Module contains functions to perform statistical operations."""

import math
from typing import List


def mean(values: List[float]) -> float:
    """Finds the mean of the list of values.

    Args:
        values: List of values for which the mean to be found.

    Returns:
        Mean of the list.
    """
    return sum(values) / len(values)


def variance(values: List[float]) -> float:
    """Finds the variance of the list of values.

    Args:
        values: List of values for which the variance to be found.

    Returns:
        Variance of the list.
    """
    mu = mean(values)
    return sum((list_1 - mu) ** 2 for list_1 in values) / len(values)


def standard_deviation(values: List[float]) -> float:
    """Finds the standard deviation of the list of values.

    Args:
        values: List of values for which the standard Deviation to be found.

    Returns:
        Standard deviation of the list of values.
    """
    return math.sqrt(variance(values))


def covariance(list_1: List[float], list_2: List[float]) -> float:
    """Finds the covariance between two list of values.

    Args:
        list_1: First list of values.
        list_2: Second list of values between which the covariance to be found.

    Returns:
        Covariance between the two list of values.
    """
    mx, my = mean(list_1), mean(list_2)
    return sum((a - mx) * (b - my) for a, b in zip(list_1, list_2)) / len(list_1)


def correlation(list_1: List[float], list_2: List[float]) -> float:
    """Finds the correlation between two list of values.

    Args:
        list_1: First list of values.
        list_2: Second list of values between which the correlation to be found.

    Returns:
        Correlated value of the two list.
    """
    return covariance(list_1, list_2) / (standard_deviation(list_1) * standard_deviation(list_2))
