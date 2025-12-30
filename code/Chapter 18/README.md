# Text Processor Package

A Python package for cleaning text and analyzing word frequencies.

## Package Structure

```
text_processor/
├── __init__.py       # Package initialization and exports
├── cleaning.py       # Text cleaning functions
├── processing.py     # Word counting and statistics
└── exceptions.py     # Custom exception classes
```

## Modules

### `exceptions.py`
Custom exceptions for error handling:
- `TextProcessingError` - Base exception class
- `InvalidInputError` - Raised when input is of invalid type
- `InvalidValueError` - Raised when a value is invalid

### `cleaning.py`
Functions for cleaning and preparing text:
- `clean_line(line)` - Convert to lowercase and remove punctuation
- `write_words_to_file(words, output_file)` - Write words to file, one per line

### `processing.py`
Functions for word counting and analysis:
- `count_word_occurrences(words)` - Count word frequencies, returns a dict
- `print_common_words(word_counts, n)` - Display n most common words
- `print_least_common_words(word_counts, n)` - Display n least common words
- `process_file(input_file_path, output_file_path)` - Process entire file

## Usage

### Import the package
```python
# Import specific functions
from text_processor import clean_line, count_word_occurrences

# Import everything
from text_processor import *
```

### Clean text
```python
from text_processor import clean_line

text = "Hello, World!"
cleaned = clean_line(text)
print(cleaned)  # "hello world"
```

### Process a file
```python
from text_processor import process_file

process_file("input.txt", "output.txt")
```

### Count word frequencies
```python
from text_processor import count_word_occurrences, print_common_words

words = ["the", "quick", "brown", "fox", "the", "lazy", "dog", "the"]
counts = count_word_occurrences(words)
print_common_words(counts, 3)
```

## Running the Demo

```bash
python main.py
```

This will:
1. Process `moby_01.txt` and clean the text
2. Write cleaned words to `moby_cleaned.txt`
3. Count word frequencies
4. Display the 5 most and 5 least common words
