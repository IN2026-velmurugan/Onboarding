"""Tests for string transformation functions in TechFellowTools string_tools module."""

import pytest
from src.assignment_6.TechFellowTools.string_tools.string_transformations import (
    convert_camel_to_snake,
    remove_punctuation,
    reverse_words,
)


@pytest.mark.parametrize(
    "word, expected_output",
    [
        ("hello world", "olleh dlrow"),
        ("Python", "nohtyP"),
        (" hello world ", "olleh dlrow"),
    ],
)
def test__reverse_word__valid_input__returns_reversed_word(word, expected_output):
    answer = reverse_words(word)

    assert expected_output == answer


def test__reverse_word__empty_string__raises_value_error():
    word = "   "
    with pytest.raises(ValueError):
        reverse_words(word)


def test__convert_camel_to_snake__empty_string__raises_value_error():
    word = ""
    with pytest.raises(ValueError):
        convert_camel_to_snake(word)


@pytest.mark.parametrize(
    "word, expected_output",
    [
        ("camelCase", "camel_case"),
        ("snakecase", "snakecase"),
    ],
)
def test__convert_camel_to_snake__valid_input__returns_snake_case(word, expected_output):
    answer = convert_camel_to_snake(word)

    assert expected_output == answer


def test__remove_punctuation__empty_string__raises_value_error():
    word = "   "
    with pytest.raises(ValueError):
        remove_punctuation(word)


@pytest.mark.parametrize(
    "word, expected_output",
    [
        ("Hello, world!", "Hello world"),
        ("No punctuation", "No punctuation"),
        ("!!!???", ""),
    ],
)
def test__remove_punctuation__valid_input__returns_string_without_punctuation(
    word, expected_output
):
    answer = remove_punctuation(word)

    assert expected_output == answer
