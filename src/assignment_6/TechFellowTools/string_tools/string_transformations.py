"""Functions to perform the string transformations."""


def reverse_words(sentence: str) -> str:
    """Reverse the words in the sentence.

    Args:
        sentence: The sentence for which the words need to be reversed.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        The reversed sentence.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    return " ".join(word[::-1] for word in sentence.split())


def convert_camel_to_snake(sentence: str) -> str:
    """Convert the camel case to snake case.

    Args:
        sentence: The camel case sentence.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        The snake case sentence.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    result = ""
    for char in sentence:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result.lstrip("_")


def remove_punctuation(sentence: str) -> str:
    """Remove the punctuations from the sentence.

    Args:
        sentence: Sentence for which the punctuations should be removed.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        Sentence with all the punctuations removed.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    return "".join(
        char
        for char in sentence
        if ord(char) in range(65, 91) or ord(char) in range(97, 123) or char == " "
    )


def convert_to_title_case(sentence: str) -> str:
    """Convert the given sentence to title case.

    Args:
        sentence: Text for which the case to be converted.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        The title case representation of the given sentence.
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    return " ".join(word.capitalize() for word in sentence.split())


def compress_string(sentence: str) -> str:
    """Compress a string using run-length encoding.

    Args:
        sentence: Text to be compressed.

    Raises:
        ValueError: When the input sentence is empty.

    Returns:
        Compressed string (e.g., "aaabb" → "a3b2").
    """
    if not sentence.strip():
        raise ValueError("Sentence must not be empty")

    if not sentence:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(sentence)):
        if sentence[i] == sentence[i - 1]:
            count += 1
        else:
            compressed.append(f"{sentence[i-1]}{count}")
            count = 1
    compressed.append(f"{sentence[-1]}{count}")
    return "".join(compressed)
