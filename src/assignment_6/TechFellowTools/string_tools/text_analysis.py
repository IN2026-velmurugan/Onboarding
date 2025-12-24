"""Functions to analyse the texts based on words."""

from collections import Counter


def word_frequency(sentence: str) -> dict[str, int]:
    """Find the frequency of words in the given sentence.

    Args:
        sentence: The sentence for which the word frequency to be found.

    Returns:
        Dictionary containing the word and its frequency.
    """
    words = sentence.lower().split()
    return dict(Counter(words))


def most_common_word(sentence: str) -> str:
    """Find the most repeated word from the sentence.

    Args:
        sentence: The sentence for which the most common repeated word to be found.

    Returns:
        The most repeated word.
    """
    freq = word_frequency(sentence)
    return max(freq, key=lambda k: freq[k])


def lexical_diversity(sentence: str) -> float:
    """Calculate the lexical diversity of a given of the sentence.

    Args:
        sentence: The sentence for which the lexical diversity should be identified.

    Returns:
        Lexical diversity of the given sentence.
    """
    words = sentence.split()
    return len(set(words)) / len(words)


def count_sentences(sentence: str) -> int:
    """Count the sentence based on the punctuations.

    Args:
        sentence: The sentence for which the sentence count to be found.

    Returns:
        Count of the sentence.
    """
    return sum(sentence.count(p) for p in ".!?")


def ngram_frequency(sentence: str, word_count: int) -> dict[str, int]:
    """Calculate the frequency count of n-grams within a given sentence.

    Args:
        sentence: The sentence for which the n-gram frequency to be found.
        word_count: The word count("n" in n-grams).

    Returns:
        The n-gram frequency of the sentence.
    """
    words = sentence.split()
    ngrams = [" ".join(words[i : i + word_count]) for i in range(len(words) - word_count + 1)]
    return dict(Counter(ngrams))
