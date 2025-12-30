"""Text cleaning functions for the text_processor package."""

import string

from .exceptions import InvalidInputError


def clean_line(line):
    """Clean a line of text by converting to lowercase and removing punctuation.

    Args:
        line: A string to clean.

    Returns:
        The cleaned string with lowercase letters and no punctuation.

    Raises:
        InvalidInputError: If line is not a string.
    """
    if not isinstance(line, str):
        raise InvalidInputError(f"Expected string, got {type(line).__name__}")
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    return line


def write_words_to_file(words, output_file):
    """Write each word to the output file on a separate line.

    Args:
        words: An iterable of words to write.
        output_file: An open file object to write to.
    """
    try:
        for word in words:
            output_file.write(word + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")
