"""Word processing and statistics functions for the text_processor package."""

from .cleaning import clean_line, write_words_to_file
from .exceptions import InvalidInputError, InvalidValueError


def count_word_occurrences(words):
    """Count the occurrences of each word in an iterable.

    Args:
        words: An iterable of words to count.

    Returns:
        A dictionary mapping words to their occurrence counts.

    Raises:
        InvalidInputError: If words is not iterable.
    """
    if not hasattr(words, '__iter__'):
        raise InvalidInputError("Input must be iterable")

    word_counts = {}
    for word in words:
        try:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        except TypeError:
            # Skip unhashable items (e.g., lists)
            pass
    return word_counts


def print_common_words(word_counts, n):
    """Print the n most common words.

    Args:
        word_counts: A dictionary mapping words to counts.
        n: Number of words to display.

    Raises:
        InvalidValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise InvalidValueError("n must be a positive integer")

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"{n} most common words:")
    for word, count in sorted_word_counts[:n]:
        print(f"{word}: {count}")


def print_least_common_words(word_counts, n):
    """Print the n least common words.

    Args:
        word_counts: A dictionary mapping words to counts.
        n: Number of words to display.

    Raises:
        InvalidValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise InvalidValueError("n must be a positive integer")

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"{n} least common words:")
    for word, count in sorted_word_counts[-n:]:
        print(f"{word}: {count}")


def process_file(input_file_path, output_file_path):
    """Process an input file: clean text and write words to output file.

    Args:
        input_file_path: Path to the input text file.
        output_file_path: Path to the output file.
    """
    try:
        with open(input_file_path, 'r') as input_file:
            with open(output_file_path, 'w') as output_file:
                for line in input_file:
                    cleaned_line = clean_line(line)
                    words = cleaned_line.split()
                    write_words_to_file(words, output_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found")
    except PermissionError:
        print(f"Error: Permission denied accessing files")
    except IOError as e:
        print(f"Error reading or writing file: {e}")
