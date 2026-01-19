import pytest
from src.assignment_6.TechFellowTools.data_tools.data_cleaning import (
    cast_to_float,
    clip_outliers,
    is_float,
    normalize_whitespace,
    remove_duplicates,
    remove_nulls,
)


@pytest.mark.parametrize(
    "value",
    [
        ("12.34"),
        ("10"),
        ("-5.6"),
    ],
)
def test__is_float__valid_float_string__returns_true(value):
    assert is_float(value) is True


@pytest.mark.parametrize(
    "value",
    [
        ("abc"),
        (""),
    ],
)
def test__is_float__invalid_float_string__returns_false(value):
    assert is_float(value) is False


@pytest.mark.parametrize(
    "data, expected_output",
    [
        ([1, None, 2, None, 3], [1, 2, 3]),
        (["a", "b", "c"], ["a", "b", "c"]),
        ([], []),
    ],
)
def test__remove_nulls__list_with_nulls__returns_list_without_nulls(data, expected_output):
    answer = remove_nulls(data)

    assert expected_output == answer


@pytest.mark.parametrize(
    "data, expected_output",
    [
        ([1, 2, 2, 4, 3], [1, 2, 4, 3]),
        (["a", "b", "a"], ["a", "b"]),
        ([], []),
    ],
)
def test__remove_duplicates__list_with_duplicates__returns_list_without_duplicates(
    data, expected_output
):
    answer = remove_duplicates(data)

    assert expected_output == answer


@pytest.mark.parametrize(
    "sentence, expected_output",
    [
        ("Hello\tWorld\nTest   ", "Hello World Test"),
        ("Hello World", "Hello World"),
        ("", ""),
    ],
)
def test__normalize_whitespace__string_with_extra_whitespaces__returns_normalized_string(
    sentence, expected_output
):
    answer = normalize_whitespace(sentence)

    assert expected_output == answer


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (["1.2", "3", "4.5"], [1.2, 3.0, 4.5]),
        (["1.2", "abc", "3"], [1.2, 3.0]),
        ([], []),
    ],
)
def test__cast_to_float__list_of_float_strings__returns_list_of_floats(input, expected_output):
    answer = cast_to_float(input)

    assert expected_output == answer


@pytest.mark.parametrize(
    "data, lower_bound, upper_bound, expected_output",
    [
        ([1.0, 2.5, 5.0], 2.0, 5.0, [2.5, 5.0]),
        ([1.0, 10.0], 2.0, 5.0, []),
        ([], 0, 1, []),
    ],
)
def test__clip_outliers__list_with_outliers__returns_list_without_outliers(
    data, lower_bound, upper_bound, expected_output
):
    answer = clip_outliers(data, lower_bound, upper_bound)

    assert expected_output == answer
