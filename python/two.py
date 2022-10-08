#!/usr/bin/env python
import sys, re, operator, string

#
# The all-important data stack
#
stack = []

#
# The heap. Maps names to data (i.e. variables)
#
heap = []

#
# The new "words" (procedures) of our program
#
def read_file():
    """
    Takes a path to a file on the stack and places the entire
    contents of the file back on the stack.
    """
    # TODO: implement
    pass

def filter_chars():
    """
    Takes data on the stack and places back a copy with all
    nonalphanumeric chars replaced by a white space.
    """
    # TODO: implement
    pass

def scan():
    """
    Takes a string on the stack and scans for words, placing
    the list of words back on the stack    
    """
    # TODO: implement
    pass

def remove_stop_words():
    """
    Takes a list of words on the stack and removes stop words.
    """
    # TODO: implement
    pass

def frequencies():
    """
    Takes a list of words and returns a dictionary associating
    words with frequencies of occurrence.
    """
    # TODO: implement
    pass

def sort():
    """
    Not in "style", left as exercise
    """
    # TODO: implement
    pass

## The main function
#
