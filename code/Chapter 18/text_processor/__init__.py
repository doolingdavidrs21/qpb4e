"""Text processor package for cleaning and analyzing text files."""

from .exceptions import TextProcessingError, InvalidInputError, InvalidValueError
from .cleaning import clean_line, write_words_to_file
from .processing import (
    count_word_occurrences,
    print_common_words,
    print_least_common_words,
    process_file,
)

__all__ = [
    # Exceptions
    'TextProcessingError',
    'InvalidInputError',
    'InvalidValueError',
    # Cleaning functions
    'clean_line',
    'write_words_to_file',
    # Processing functions
    'count_word_occurrences',
    'print_common_words',
    'print_least_common_words',
    'process_file',
]
