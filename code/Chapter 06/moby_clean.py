import string

punct_table = str.maketrans('', '', string.punctuation)

with open('moby_01.txt') as infile, open('moby_01_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned = line.lower().translate(punct_table)
        for word in cleaned.split():
            outfile.write(word + '\n')
