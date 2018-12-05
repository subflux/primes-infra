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

print "Number of primes to calculate: " + str(number_of_primes)

# Implementation

# A logical flaw here was to assume that the data structure
# should be filled to "number of primes". Given that we're
# setting a fraction of these as "not primes", we need
# a much larger range of integers to test. Let's just
# speculatively initialise the array.
# We can be smarter about how we decide how many integers
# to run our iterators through.
speculative_largest_prime = 1000000

# This is addressible as 0-((number_of_primes+2)-1)
a = np.ones(speculative_largest_prime + 1, dtype=np.int64)

if verbose:
    print a

print "Trying an incrementor"
for x in range(2,a.size-1):

    iteration_increment = x
    current_int = x

    if verbose:
        print "Integer is: " + str(x)
        print "Increment is: " + str(x)

    # Until we hit the end of our list...
    while current_int <= a.size-1:
        # Move to next incremental int
        if verbose:
            print "current_int: " + str(current_int)
        # current_int is a prime, so next one, and all
        # following the same incrementor, are not.
        current_int = current_int + iteration_increment
        # in case we increment outside the end of the list
        if current_int <= a.size-1:
            # flag as NOT PRIME
            a[current_int] = 0

# How about stopping running the iterator once we've
# identified enough primes?

primes_seen = 1
print "Iterating through the structure."

# Iterate through the whole data structure
for this_integer in range(2,a.size-1):
    if a[this_integer] == 1:
        # Look at the next element of the array.
        #  Maybe numpy has way of making this faster, and only
        #  looking at the next array already identified as a prime?
        print "Prime " + str(primes_seen) + ": " + str(this_integer)
        if primes_seen == number_of_primes:
            sys.exit(0)
        primes_seen = primes_seen + 1
    this_integer = this_integer + 1;

# Append to the array in chunks?
