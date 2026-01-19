import pytest
from src.assignment_6.TechFellowTools.string_tools.text_analysis import (
    calculate_lexical_diversity,
    count_sentences,
    find_most_common_word,
    get_ngram_count,
    word_frequency,
)


@pytest.mark.parametrize(
    "text, expected_output",
    [
        ("hello world hello", {"hello": 2, "world": 1}),
        (
            "The quick brown fox jumps over the lazy dog",
            {
                "the": 2,
                "quick": 1,
                "brown": 1,
                "fox": 1,
                "jumps": 1,
                "over": 1,
                "lazy": 1,
                "dog": 1,
            },
        ),
        ("test test! TEST", {"test": 2, "test!": 1}),
    ],
)
def test__word_frequency__valid_input__returns_frequency_dict(text, expected_output):
    answer = word_frequency(text)

    assert expected_output == answer


def test__word_frequency__empty_string__raises_value_error():
    text = ""
    with pytest.raises(ValueError):
        word_frequency(text)


def test__find_most_common_word__no_words__raises_value_error():
    text = "     "
    with pytest.raises(ValueError):
        find_most_common_word(text)


def test__find_most_common_word__valid_input__returns_most_common_word():
    text = "apple banana apple orange banana apple"
    expected_output = "apple"
    answer = find_most_common_word(text)

    assert expected_output == answer


def test__find_most_common_word__tie__returns_first_occurrence():
    text = "apple banana apple banana"
    expected_output = "apple"
    answer = find_most_common_word(text)

    assert expected_output == answer


def test__calculate_lexical_diversity__empty_string__raises_value_error():
    text = ""
    with pytest.raises(ValueError):
        calculate_lexical_diversity(text)


@pytest.mark.parametrize(
    "text, expected_output",
    [
        ("hello world hello", 2 / 3),
        ("The quick brown fox jumps over the lazy dog", 1),
        ("test test test test", 1 / 4),
    ],
)
def test__calculate_lexical_diversity__valid_input__returns_diversity(text, expected_output):
    answer = calculate_lexical_diversity(text)

    assert expected_output == answer


def test__count_sentences__empty_string__raises_value_error():
    text = "   "
    with pytest.raises(ValueError):
        count_sentences(text)


@pytest.mark.parametrize(
    "text, expected_output",
    [
        ("Hello world. How are you?", 2),
        ("This is a test! Is it working? Yes.", 3),
        ("No punctuation here", 0),
        ("Wait... What?! Really!", 3),
    ],
)
def test__count_sentences__valid_input__returns_sentence_count(text, expected_output):
    answer = count_sentences(text)

    assert expected_output == answer


def test__get_ngram_count__empty_string__raises_value_error():
    text = ""
    with pytest.raises(ValueError):
        get_ngram_count(text, 2)


@pytest.mark.parametrize(
    "text, n, expected_output",
    [
        ("hello world hello", 1, {"hello": 2, "world": 1}),
        ("The quick brown fox", 2, {"The quick": 1, "quick brown": 1, "brown fox": 1}),
    ],
)
def test__get_ngram_count__valid_input__returns_ngram_count(text, n, expected_output):
    answer = get_ngram_count(text, n)

    assert expected_output == answer
