#! /usr/bin/env python3
"""wcsolution: Count lines, words, and characters in a file.
Can also be run as a script with command-line arguments.
usage as a script: python3 wcsolution.py <filename> [-l] [-w] [-c]"""
import string
import sys
from argparse import ArgumentParser


def main():
    """
    Docstring for main
    """
    parser = ArgumentParser(description="Count lines, words, and characters in a file")
    parser.add_argument("filename", help="File to process")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-c", "--chars", action="store_true", help="Count characters")
    args = parser.parse_args()

    try:
        with open(args.filename, encoding="utf-8") as infile:
            content = infile.read()
            lines = content.splitlines()
            words = [w.strip(string.punctuation) for line in lines
                      for w in line.split() if w.strip(string.punctuation)]
            print(f"File has {len(lines)} lines, {len(words)} words, {len(content)} characters")
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found", file=sys.stderr)
        sys.exit(1)

    if args.lines:
        print(f"Lines: {len(lines)}")
    if args.words:
        print(f"Words: {len(words)}")
    if args.chars:
        print(f"Characters: {len(content)}")
if __name__ == "__main__":
    main()
