#!/usr/bin/env python
import sys, string, time
import numpy as np

## Constraints
# - Main data type: array - a fixed-size collection of elements.
# - No explicit iteration; instead, an array is accessed by high-level,
#   declarative operations
# - Computation unfolds as searcg, selection, and transformation of fixed-
#   size data.

# runtime calc
start_time = time.time()

# Example input: "Hello  World!"
characters = np.array([" "] + list(open(sys.argv[1]).read()) + [" "])
# Result: array([' ', 'H', 'e', 'l', 'l', 'o', ' ', ' ',
#                'W', 'o', 'r', 'l', 'd', '!', ' '], dtype='<U1')

# Normalize
characters[~np.char.isalpha(characters)] = " "
characters = np.char.lower(characters)
# Result: array([' ', 'h', 'e', 'l', 'l', 'o', ' ', ' ',
#                'w', 'o', 'r', 'l', 'd', ' ', ' '], dtype='<U1')

### Split the words by finding the indices of spaces
sp = np.where(characters == " ")
# Result: (array([0, 6, 7, 13, 14], dtype=int64),)
# A little trick: let's double each index, and then take pairs
sp2 = np.repeat(sp, 2)
# Result: array([ 0, 0, 6, 6, 7, 7, 13, 13, 14, 14], dtype=int64)
# Get the pairs as a 2D matrix, skip the first and the last
w_ranges = np.reshape(sp2[1:-1], (-1, 2))
# Result: array([[ 0, 6],
#                [ 6, 7],
#                [ 7, 13],
#                [13, 14]], dtype=int64)
# Remove the indexing to the spaces themselves
w_ranges = w_ranges[np.where(w_ranges[:, 1] - w_ranges[:, 0] > 2)]
# Result: array([[ 0, 6],
#                [ 7, 13]], dtypes=int64)

# Voila! Words are in between spaces, given as pairs of indices
words = list(map(lambda r: characters[r[0] : r[1]], w_ranges))
# Result: [array([' ', 'h', 'e', 'l', 'l', 'o'], dtype='<U1'),
#          array([' ', 'w', 'o', 'r', 'l', 'd'], dtype='<U1')]
# let's recode the characters as strings
swords = np.array(list(map(lambda w: "".join(w).strip(), words)))
# Result: array(['hello', 'world'], dtype='<U5')

# Next, let's remove stop words
stop_words = np.array(list(set(open("../static/stop_words.txt").read().split(","))))
ns_words = swords[~np.isin(swords, stop_words)]

### Finally, count to word occurrences
uniq, counts = np.unique(ns_words, axis=0, return_counts=True)
wf_sorted = sorted(zip(uniq, counts), key=lambda t: t[1], reverse=True)

for w, c in wf_sorted[:25]:
    print(w, "-", c)

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))
