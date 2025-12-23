#! /usr/bin/env python3
import sys
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description='Generate a list of prime numbers up to a given limit.')
    parser.add_argument('limit', type=int, help='The upper limit for generating prime numbers.')
    args = parser.parse_args()

    if args.limit < 2:
        print("No prime numbers found.")
        sys.exit(1)

    primes = []
    for num in range(2, args.limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    print("arguments:", args)
    print("Prime numbers up to", args.limit, "are:", primes)
if __name__ == '__main__':
     main()

