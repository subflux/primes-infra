#!/usr/bin/python

import sys
import argparse
import numpy

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Include verbose output.",
                    action="store_true")
parser.add_argument("Number",
                    help="The number of primes you wish to calculate.",
                    nargs=1)

# Display the full help message if user hasn't supplied any arguments.
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

verbose = args.verbose

# Convert the list to a string with spaces
number_of_primes = int(args.Number[0])

if verbose:
    print "Number of primes to calculate: " + number_of_primes

# Implementation
for x in range(number_of_primes):
    print(x)
