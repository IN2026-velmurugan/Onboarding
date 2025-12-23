"""Functions to perform statistical operations."""

import math

Values = float | int

def mean(values: list[Values]) -> Values:
    """Calculate the mean of the list of values.

    Args:
        values: list of values for which the mean to be found.

    Returns:
        Mean of the list.
    """
    return sum(values) / len(values)


def variance(values: list[Values]) -> Values:
    """Calculate the variance of the list of values.

    Args:
        values: list of values for which the variance to be found.

    Returns:
        Variance of the list.
    """
    mu = mean(values)
    return sum((list_a - mu) ** 2 for list_a in values) / len(values)


def standard_deviation(values: list[Values]) -> Values:
    """Calculate the standard deviation of the list of values.

    Args:
        values: list of values for which the standard Deviation to be found.

    Returns:
        Standard deviation of the list.
    """
    return math.sqrt(variance(values))


def covariance(list_a: list[Values], list_b: list[Values]) -> Values:
    """Calculate the covariance between two list of values.

    Args:
        list_a: First list of values.
        list_b: Second list of values between which the covariance to be found.

    Returns:
        Covariance between the two list.
    """
    mx, my = mean(list_a), mean(list_b)
    return sum((a - mx) * (b - my) for a, b in zip(list_a, list_b)) / len(list_a)


def correlation(list_a: list[Values], list_b: list[Values]) -> Values:
    """Calculate the correlation between two list of values.

    Args:
        list_a: First list of values.
        list_b: Second list of values between which the correlation to be found.

    Returns:
        Correlated value of the two list.
    """
    return covariance(list_a, list_b) / (standard_deviation(list_a) * standard_deviation(list_b))
