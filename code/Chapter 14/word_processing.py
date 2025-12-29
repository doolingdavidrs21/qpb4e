
import string

def clean_line(line):
    if not isinstance(line, str):
        raise TypeError(f"Expected string, got {type(line).__name__}")
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    return line

def write_words_to_file(words, output_file):
    try:
        for word in words:
            output_file.write(word + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")

def count_word_occurrences(words):
    if not hasattr(words, '__iter__'):
        raise TypeError("Input must be iterable")

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
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"{n} most common words:")
    for word, count in sorted_word_counts[:n]:
        print(f"{word}: {count}")

def print_least_common_words(word_counts, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"{n} least common words:")
    for word, count in sorted_word_counts[-n:]:
        print(f"{word}: {count}")

def process_file(input_file_path, output_file_path):
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