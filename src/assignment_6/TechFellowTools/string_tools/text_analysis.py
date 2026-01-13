"""Functions to analyse the texts based on words."""

import re
from collections import Counter


def word_frequency(sentence: str) -> dict[str, int]:
    """Find the frequency of words in the given sentence.

    Args:
        sentence: The sentence for which the word frequency to be found.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        Dictionary containing the word and its frequency.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    words = sentence.lower().split()
    return dict(Counter(words))


def find_most_common_word(sentence: str) -> str:
    """Find the most repeated word from the sentence.

    Args:
        sentence: The sentence for which the most common repeated word to be found.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        The most repeated word.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    freq = word_frequency(sentence)
    return max(freq, key=lambda k: freq[k])


def calculate_lexical_diversity(sentence: str) -> float:
    """Calculate the lexical diversity of a given of the sentence.

    Args:
        sentence: The sentence for which the lexical diversity should be identified.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        Lexical diversity of the given sentence.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    words = sentence.split()
    return len(set(words)) / len(words)


def count_sentences(sentence: str) -> int:
    """Count the sentence based on the punctuations.

    Args:
        sentence: The sentence for which the sentence count to be found.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        Count of the sentence.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    return len(re.findall(r"[.!?](?:\s|$)", sentence))


def get_ngram_count(sentence: str, word_count: int = 1) -> dict[str, int]:
    """Calculate the frequency count of n-grams within a given sentence.

    Args:
        sentence: The sentence for which the n-gram frequency to be found.
        word_count: The word count("n" in n-grams), defaults to 1.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        The n-gram frequency of the sentence.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    words = sentence.split()
    ngrams = [" ".join(words[i : i + word_count]) for i in range(len(words) - word_count + 1)]
    return dict(Counter(ngrams))
