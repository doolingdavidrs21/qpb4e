#!/usr/bin/env python3
"""wc_claude.py: Count lines, words, and characters in a file.
Similar to the UNIX wc utility.

Usage: python3 wc_claude.py [-l] [-w] [-c] [-L] filename
"""
import sys
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Count lines, words, and characters in a file")
    parser.add_argument("filename", help="File to process")
    parser.add_argument("-l", "--lines", action="store_true", help="Print line count")
    parser.add_argument("-w", "--words", action="store_true", help="Print word count")
    parser.add_argument("-c", "--chars", action="store_true", help="Print character count")
    parser.add_argument("-L", "--max-line-length", action="store_true",
                        help="Print length of longest line")
    args = parser.parse_args()

    try:
        with open(args.filename, encoding="utf-8") as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found", file=sys.stderr)
        sys.exit(1)

    # Calculate stats
    lines = content.splitlines(keepends=True)  # Keep newlines for accurate char count
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = len(content)
    longest_len = max((len(line.rstrip('\n\r')) for line in lines), default=0)

    # Determine what to show
    show_all = not any([args.lines, args.words, args.chars, args.max_line_length])

    # Build output
    output_parts = []
    if show_all or args.lines:
        output_parts.append(f"{line_count:>7}")
    if show_all or args.words:
        output_parts.append(f"{word_count:>7}")
    if show_all or args.chars:
        output_parts.append(f"{char_count:>7}")
    if args.max_line_length:
        output_parts.append(f"{longest_len:>7}")

    output_parts.append(args.filename)
    print(" ".join(output_parts))


if __name__ == "__main__":
    main()
