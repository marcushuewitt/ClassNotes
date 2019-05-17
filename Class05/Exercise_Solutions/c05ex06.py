"""
Author:         Tim Smith
Description:    Solution to Class04 Ex4
"""
import sys

for i in sys.argv:  # loop through all command line arguments given
    if i[0] == "-":  # check if the first character of the argument is -
        print(i)  # if so, print it.
