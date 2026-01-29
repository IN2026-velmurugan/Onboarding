"""Tests for matrix operations in TechFellowTools math_tools module."""

import pytest
from src.assignment_6.TechFellowTools.math_tools.matrix_operations import (
    add_matrices,
    determinant_2x2,
    inverse_2x2,
    mul_matrices,
    transpose,
)


def test__add_matrices__valid_input_matrix__returns_added_matrix():
    matrix_a = [[1.0, 2.0], [3.0, 4.0]]
    matrix_b = [[5.0, 6.0], [7.0, 8.0]]
    matrix_c = [[6.0, 8.0], [10.0, 12.0]]

    result = add_matrices(matrix_a, matrix_b)
    assert matrix_c == result


@pytest.mark.parametrize(
    "input",
    [
        ([[1, 2]], [[1, 2], [3, 4]]),
        ([[1, 2, 3]], [[1, 2]]),
    ],
)
def test__add_matrices__invalid_inputs__raised_value_error(input):
    with pytest.raises(ValueError):
        add_matrices(*input)


@pytest.mark.parametrize(
    "matrix_a, matrix_b, result",
    [
        ([[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]], [[19.0, 22.0], [43.0, 50.0]]),
        (
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
            [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]],
            [[58.0, 64.0], [139.0, 154.0]],
        ),
    ],
)
def test__mul_matrices__valid_input__returns_multiplied_matrix(matrix_a, matrix_b, result):
    answer = mul_matrices(matrix_a, matrix_b)

    assert result == answer


@pytest.mark.parametrize(
    "matrix_a, matrix_b",
    [
        ([[1.0, 2.0], [3.0]], [[1.0, 2.0], [3.0, 4.0]]),
        ([[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0]]),
        ([[1.0, 2.0]], [[1.0, 2.0]]),
    ],
)
def test__mul_matrices__invalid_inputs__raised_value_error(matrix_a, matrix_b):
    with pytest.raises(ValueError):
        mul_matrices(matrix_a, matrix_b)


@pytest.mark.parametrize(
    "matrix, result",
    [
        ([[1.0, 2.0], [3.0, 4.0]], [[1.0, 3.0], [2.0, 4.0]]),
        ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]),
        ([[1.0, 2.0, 3.0]], [[1.0], [2.0], [3.0]]),
    ],
)
def test__transpose__valid_input__returns_transposed_matrix(matrix, result):
    answer = transpose(matrix)

    assert result == answer


@pytest.mark.parametrize(
    "matrix, result",
    [
        ([[1.0, 2.0], [2.0, 4.0]], 0.0),
        ([[1.0, 2.0], [3.0, 4.0]], -2.0),
    ],
)
def test__determinant_2x2__valid_input__returns_determinant(matrix, result):
    answer = determinant_2x2(matrix)

    assert result == answer


def test__determinant_2x2__invalid_input__raised_value_error():
    matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    with pytest.raises(ValueError):
        determinant_2x2(matrix)


@pytest.mark.parametrize(
    "matrix, result",
    [
        ([[4.0, 7.0], [2.0, 6.0]], [[0.6, -0.7], [-0.2, 0.4]]),
        ([[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]]),
    ],
)
def test__inverse_2x2__valid_input__returns_inverse_matrix(matrix, result):
    answer = inverse_2x2(matrix)

    assert result == answer


def test__inverse_2x2__singular_matrix__raised_value_error():
    matrix = [[1.0, 2.0], [2.0, 4.0]]
    with pytest.raises(ValueError):
        inverse_2x2(matrix)
