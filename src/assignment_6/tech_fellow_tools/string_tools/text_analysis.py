"""Module contains the functions to analyse the texts based on words."""

from collections import Counter
from typing import Dict


def word_frequency(text: str) -> Dict[str, int]:
    """Finds the frequency of words in the given text.

    Args:
        text: The text for which the word frequency to be found.

    Returns:
        Dictionary containing the word and its frequency.
    """
    words = text.lower().split()
    return dict(Counter(words))


def most_common_word(text: str) -> str:
    """Finds the most repeated word from the text.

    Args:
        text: The text for which the word that occurs frequently to be found.

    Returns:
        The most repeated word.
    """
    freq = word_frequency(text)
    return max(freq, key=freq.get)  # type: ignore


def lexical_diversity(text: str) -> float:
    """This Python function calculates the lexical diversity of a given of the text.

    Args:
        text: The text for which the lexical diversity should be identified.

    Returns:
        Lexical diversity of the given text.
    """
    words = text.split()
    return len(set(words)) / len(words)


def count_sentences(text: str) -> int:
    """Counts the sentence based on the punctuations.

    Args:
        text: The text for which the sentence count to be found.

    Returns:
        Count of the sentence.
    """
    return sum(text.count(p) for p in ".!?")


def ngram_frequency(text: str, n: int) -> Dict[str, int]:
    """Calculates and returns the frequency count of n-grams within a given text.

    Args:
        text: The text for which the n-gram frequency to be found.
        n: The word count.

    Returns:
        The anagram frequency of the text.
    """
    words = text.split()
    ngrams = [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]
    return dict(Counter(ngrams))
