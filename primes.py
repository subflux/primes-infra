#!/usr/bin/python

import sys
import argparse
import numpy

parser = argparse.ArgumentParser()
# parser.add_argument("-l", "--board", help="The code of the board you wish to search, eg `sa`.")
# parser.add_argument("-m", "--modified", help="Cards modified, in trello parlance 'edited', in the past {MODIFIED} days.")
parser.add_argument("-v", "--verbose", help="Include verbose output.",
                    action="store_true")
# parser.add_argument("-y", "--year", help="Searches for cards opened in the past 365 days.",
#                    action="store_true")
parser.add_argument("Number",  help="The number of primes you wish to calculate.", nargs=1)

if len(sys.argv) == 1:
  parser.print_help(sys.stderr)
  sys.exit(1)

args= parser.parse_args()

verbose= args.verbose

# if args.modified is not None:
#     if verbose: 
#         print "searching for cards modified 'edited' in the past " + args.modified + " days."
#     search_command=  search_command + " edited:" + args.modified 


# if args.year:
#     if verbose: 
#         print "searching for -365 days"
#     search_command= search_command + " created:365"

# Convert the list to a string with spaces
number_of_primes= int(args.Number[0])

if verbose:
  print "Number of primes to calculate: " + number_of_primes

# Implementation
for x in range(number_of_primes):
  print(x)
