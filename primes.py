#!/usr/bin/python

import sys
import argparse
import numpy as np

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

print "Trying a range."
a = np.arange(2,number_of_primes)
print a

# This is addressible as 0-((number_of_primes+2)-1)
a = np.ones(number_of_primes + 2, dtype=np.int64)
print a

print "Iterating through the array."
for x in range(2,(number_of_primes + 2) - 1):
    print "Integer is: " + str(x)
    print a[x]

print "Trying an iterator"
for x in range(2,(number_of_primes + 2) - 1):
    iteration_increment = x
    current_int = x

    print "Integer is: " + str(x)
    print "Increment is: " + str(x)

    # Until we hit the end of our list...
    while current_int <= (number_of_primes + 2) - 1:
        # Move to next incremental int
        print "current_int: " + str(current_int)
        # current_int is a prime, so next one, and all
        # following the same incrementor, are not.
        current_int = current_int + iteration_increment
        # in case we increment outside the end of the list
        if current_int <= (number_of_primes + 2) - 1:
            # flag as NOT PRIME
            a[current_int] = 0
            print a[current_int]

print "Iterating through the structure."
primes_seen = 0

for x in range(2,(number_of_primes + 2) - 1):
# Iterate through the whole data structure
    if a[x] == 1:
        primes_seen = primes_seen + 1
        print "Prime " + str(primes_seen) + ": " + str(x)

# Append to the array in chunks?
