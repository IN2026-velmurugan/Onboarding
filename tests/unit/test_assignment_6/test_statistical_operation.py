"""Tests for statistical operations in TechFellowTools math_tools module."""

import pytest
from src.assignment_6.TechFellowTools.math_tools.statistical_operations import (
    correlation,
    covariance,
    mean,
    standard_deviation,
    variance,
)


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ([1.0, 2.0, 3.0], 2.0),
        ([10, 20, 30, 40], 25),
    ],
)
def test__mean__valid_input__returns_mean(input, expected_output):
    answer = mean(input)

    assert expected_output == answer


def test__mean__empty_list__raises_value_error():
    with pytest.raises(ValueError):
        mean([])


def test__mean__non_numeric_list__raises_type_error():
    with pytest.raises(TypeError):
        mean([1, "two", 3])  # type: ignore


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ([1.0, 2.0, 3.0], 1.0),
        ([10, 20, 30, 40], 166.6666666666),
    ],
)
def test__variance__valid_input__returns_variance(input, expected_output):
    answer = variance(input)

    assert expected_output == pytest.approx(answer)


def test__variance__empty_list__raises_value_error():
    with pytest.raises(ValueError):
        variance([])


def test__variance__non_numeric_list__raises_type_error():
    with pytest.raises(TypeError):
        variance([1, "two", 3])  # type: ignore


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ([1.0, 2.0, 3.0], 1.0**0.5),
        ([10, 20, 30, 40], (500 / 3) ** 0.5),
    ],
)
def test__standard_deviation__valid_input__returns_standard_deviation(input, expected_output):
    answer = standard_deviation(input)

    assert expected_output == pytest.approx(answer)


def test__standard_deviation__empty_list__raises_value_error():
    with pytest.raises(ValueError):
        standard_deviation([])


def test__standard_deviation__non_numeric_list__raises_type_error():
    with pytest.raises(TypeError):
        standard_deviation([1, "two", 3])  # type: ignore


@pytest.mark.parametrize(
    "data_x, data_y, expected_output",
    [
        ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0], 1.0),
        ([10, 20, 30], [20, 30, 40], 100.0),
    ],
)
def test__covariance__valid_input__returns_covariance(data_x, data_y, expected_output):
    answer = covariance(data_x, data_y)

    assert expected_output == pytest.approx(answer)


def test__covariance__unequal_length_lists__raises_value_error():
    with pytest.raises(ValueError):
        covariance([1, 2, 3], [4, 5])


@pytest.mark.parametrize(
    "data_x, data_y",
    [
        ([], [4, 5, 6]),
        ([1, 2, 3], []),
    ],
)
def test__covariance__empty_lists__raises_value_error(data_x, data_y):
    with pytest.raises(ValueError):
        covariance(data_x, data_y)


def test__covariance__non_numeric_lists__raises_type_error():
    with pytest.raises(TypeError):
        covariance([1, "two", 3], [4, 5, 6])  # type: ignore


@pytest.mark.parametrize(
    "data_x, data_y, result",
    [
        ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0], 1.0),
        ([10, 20, 30], [20, 30, 40], 1.0),
    ],
)
def test__correlation__valid_input__returns_correlation(data_x, data_y, result):
    answer = correlation(data_x, data_y)

    assert result == pytest.approx(answer)


def test__correlation__unequal_length_lists__raises_value_error():
    with pytest.raises(ValueError):
        correlation([1, 2, 3], [4, 5])


def test__correlation__zero_variance__raises_value_error():
    with pytest.raises(ValueError):
        correlation([1, 1, 1], [2, 3, 4])


@pytest.mark.parametrize(
    "data_x, data_y",
    [
        ([], [4, 5, 6]),
        ([1, 2, 3], []),
    ],
)
def test__correlation__empty_lists__raises_value_error(data_x, data_y):
    with pytest.raises(ValueError):
        correlation(data_x, data_y)


def test__correlation__non_numeric_lists__raises_type_error():
    with pytest.raises(TypeError):
        correlation([1, "two", 3], [4, 5, 6])  # type: ignore
