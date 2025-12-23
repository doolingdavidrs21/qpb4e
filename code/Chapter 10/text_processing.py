
import string
def clean_line(line):
    # Convert the line to lowercase
    line = line.lower()

    # Remove punctuation from the line
    line = line.translate(str.maketrans('', '', string.punctuation))

    return line

def write_words_to_file(words, output_file):
    # Write each word to the output file
    for word in words:
        output_file.write(word + '\n')

def count_word_occurrences(words):
    # Count the occurrences of each word using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def print_common_words(word_counts, n):
    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the n most common words and their occurrences
    print(f"{n} most common words:")
    for word, count in sorted_word_counts[:n]:
        print(f"{word}: {count}")

def print_least_common_words(word_counts, n):
    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the n least common words and their occurrences
    print(f"{n} least common words:")
    for word, count in sorted_word_counts[-n:]:
        print(f"{word}: {count}")

def process_file(input_file_path, output_file_path):
    # Open the input file for reading
    with open(input_file_path, 'r') as input_file:
        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Iterate over each line in the input file
            for line in input_file:
                # Clean the line
                cleaned_line = clean_line(line)

                # Split the line into words
                words = cleaned_line.split()

                # Write the words to the output file
                write_words_to_file(words, output_file)
