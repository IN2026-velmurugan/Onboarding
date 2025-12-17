"""Module contains the functions for performing the string transformations."""


def reverse_words(text: str) -> str:
    """Reverses the words in the sentence.

    Args:
        text: The sentence for which the words need to be reversed.

    Returns:
        The reversed sentence.
    """
    return " ".join(word[::-1] for word in text.split())


def camel_to_snake(text: str) -> str:
    """Converts the camel case to snake case.

    Args:
        text: The camel case text.

    Returns:
        The snake case text of the given text.
    """
    result = ""
    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result.lstrip("_")


def remove_punctuation(text: str) -> str:
    """Removes the punctuations from the sentence.

    Args:
        text: Sentence for which the punctuations should be removed.

    Returns:
        Sentence with all the punctuations removed.
    """
    return "".join(char for char in text if char.isalnum() or char.isspace())


def title_case(text: str) -> str:
    """Converts the given text to title case.

    Args:
        text: Text for which the case to be converted.

    Returns:
        The title case representation of the given text.
    """
    return " ".join(word.capitalize() for word in text.split())


def compress_string(text: str) -> str:
    """Compresses the string by using the count of repeated character.

    Args:
        text: Text to be compressed.

    Returns:
        The compressed text with the character repeating counts.
    """
    if not text:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(f"{text[i-1]}{count}")
            count = 1
    compressed.append(f"{text[-1]}{count}")
    return "".join(compressed)
