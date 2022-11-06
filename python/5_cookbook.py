#!/usr/bin/env python
import sys, string, time

## Constraints
# - No long jumps.
# - Complexity of Control flow tamed by dividn the large problem into
#   smaller units using procedural abstraction.
# - Procedures may share state in the form of global variables.
# - The larger problem is solved by aolying the procedures, one after the
#   other, that change, or add to, the shared state.

# runtime calc
start_time = time.time()

# The shared mutable data
data = []
words = []
word_freqs = []

#
# The procedures
#
def read_file(path_to_file):
    """
    Takes a path to a file and assigns the entire
    contents of the file to the global variable data
    """
    global data
    with open(path_to_file) as f:
        data = data + list(f.read())

def filter_chars_and_normalize():
    """
    Replaces all alphanumeric chars in data with while space
    """
    global data
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = ' '
        else:
            data[i] = data[i].lower()

def scan():
    """
    Scans data for words, filling the global variable words
    """
    global data
    global words
    data_str = ''.join(data)
    words = words + data_str.split()

def remove_stop_words():
    global words
    with open('../static/stop_words.txt') as f:
        stop_words = f.read().split(',')
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)

def frequencies():
    """
    Creates a list of pairs associating
    words with frequencies
    """
    global words
    global word_freqs
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])

def sort():
    """
    Sorts word_freqs by frequency
    """
    global word_freqs
    word_freqs.sort(key=lambda x: x[1], reverse=True)

#
# The main functions
#
read_file(sys.argv[1])
filter_chars_and_normalize()
scan()
remove_stop_words()
frequencies()
sort()

for tf in word_freqs[0:25]:
    print(tf[0], '-', tf[1])

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))