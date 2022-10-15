#!/usr/bin/python
import sys, string

# the global list of [word, frequency] pairs
word_freqs = []
# the list of stop words
with open('../static/stop_words.txt') as f:
    stop_words = f.read().split(',')
stop_words.extend(list(string.ascii_lowercase))

# iterate through the file one line at a time
for line in open(sys.argv[1]):
    start_char = None
    i = 0
    for c in line:
        if start_char == None:
            if c.isalnum():
                # we found the start of a word
                start_char = i
            else:
                if not c.isalnum():
                    # we found the end of a word, process it
                    found = False
                    word = line[start_char:i].lower()
                    # ignore stop words
                    if word not in stop_words:
                        pair_index = 0
                        # let's see if it already exists
                        for pair in word_freqs:
                            if word == pair[0]:
                                pair[1] += 1
                                found = True
                                break
                            pair_index += 1
                        if not found:
                            word_freqs.append([word, 1])
                        elif len(word_freqs) > 1:
                            # we may need to reorder
                            for n in reversed(range(pair_index)):
                                if word_freqs[pair_index][1] > \
                                   word_freqs[n][1]:
                                        # swap
                                        word_freqs[n], word_freqs[\
                                            pair_index] = word_freqs[\
                                            pair_index], word_freqs[n]
                                        pair_index = n
                    # let's reset
                    start_char = None
            i += 1

for tf in word_freqs[0:25]:
    print(tf[0], '-', tf[1])
