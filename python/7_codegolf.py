#!/usr/bin/env python
import collections, re, sys, time

## Constraints
# - as few lines as possible

# runtime calc
start_time = time.time()

stops = open('../static/stop_words.txt').read().split(',')
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
counts = collections.Counter(w for w in words if w not in stops)
for (w, c) in counts.most_common(25):
    print(w, '-', c)

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))





