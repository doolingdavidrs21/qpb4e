"""Main script demonstrating the text_processor package."""

from text_processor import (
    process_file,
    count_word_occurrences,
    print_common_words,
    print_least_common_words,
)


def main():
    """Demonstrate all modules in the text_processor package."""
    input_file = "moby_01.txt"
    output_file = "moby_cleaned.txt"

    # Step 1: Process the input file (clean and write words)
    print(f"Processing '{input_file}'...")
    process_file(input_file, output_file)
    print(f"Cleaned text written to '{output_file}'\n")

    # Step 2: Read the cleaned words and count occurrences
    with open(output_file, 'r') as f:
        words = [line.strip() for line in f if line.strip()]

    word_counts = count_word_occurrences(words)
    print(f"Total unique words: {len(word_counts)}\n")

    # Step 3: Display word statistics
    print_common_words(word_counts, 5)
    print()
    print_least_common_words(word_counts, 5)


if __name__ == "__main__":
    main()
