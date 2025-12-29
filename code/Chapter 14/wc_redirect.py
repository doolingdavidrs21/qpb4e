#!/usr/bin/env python3
# File: wc_redirect.py
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""
import sys
import argparse


def main():
    # initialze counts
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0
    longest_line = 0

    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("-c", "--chars",
                  action="store_true", dest="chars", default=False,
                  help="display number of characters")
    parser.add_argument("-w", "--words",
                  action="store_true", dest="words", default=False,
                  help="display number of words")
    parser.add_argument("-l", "--lines",
                  action="store_true", dest="lines", default=False,
                  help="display number of lines")
    parser.add_argument("-L", "--longest",
                  action="store_true", dest="longest", default=False,
                  help="display longest line length")
    parser.add_argument("file", nargs='?', type=argparse.FileType('r'), #A
                        default=sys.stdin,   #B
                        help="read data from this file")
    args = parser.parse_args()

    with  args.file  as infile:
        for line in infile.readlines():   #C
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
            if len(line) > longest_line:
                longest_line = len(line)

    default_args = any([getattr(args, _) for _ in ('chars', 'words', 'lines', 'longest')])

    if not default_args:
        args.chars = args.lines = args.words = True

    if args.lines:
        print(f"{line_count:3}", end=" ")
    if args.words:
        print(f"{word_count:4}", end=" ")
    if args.chars:
        print(f"{char_count:4}", end=" ")
    if args.longest:
        print(f'{longest_line}', end=" ")
    if args.file.name != '<stdin>':      #D
        print(f'{args.file.name}', end=" ")
    print()

if __name__ == '__main__':
    main()