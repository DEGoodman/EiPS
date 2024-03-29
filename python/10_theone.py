import sys, re, operator, string, time


## Constraints
# - Existence of an abstraction to which values can be converted.
# - This abstraction provides operations to:
#     1 wrap around values so that they become the abstraction
#     2 bind itself fto functions, to establish sequences of functions
#     3 unwrap the value, to examine the final result
# - Larger problem is solved as a pipeline of functions bound together,
#     with unwrapping happening at the end
# - Particularly for The One style, the bind operation simply
#    calls the given function, giving it the value that it holds,
#    and holds on to the returned value.

#
# The One class for this example
#


class TFTheOne:
    def __init__(self, v):
        self._value = v

    def bind(self, func):
        self._value = func(self._value)
        return self

    def printme(self):
        print(self._value)


#
# The functions
#
def read_file(path_to_file):
    with open(path_to_file) as f:
        data = f.read()
    return data


def filter_chars(str_data):
    pattern = re.compile("[\W_]+")
    return pattern.sub(" ", str_data)


def normalize(str_data):
    return str_data.lower()


def scan(str_data):
    return str_data.split()


def remove_stop_words(word_list):
    with open("../static/stop_words.txt") as f:
        stop_words = f.read().split(",")
        # add single-letter words
        stop_words.extend(list(string.ascii_lowercase))
        return [w for w in word_list if not w in stop_words]


def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


def top25_frqs(word_freqs):
    top25 = ""
    for tf in word_freqs[0:25]:
        top25 += str(tf[0]) + " - " + str(tf[1]) + "\n"
    return top25


#
# The main function
#
TFTheOne(sys.argv[1]).bind(read_file).bind(filter_chars).bind(normalize).bind(
    scan
).bind(remove_stop_words).bind(frequencies).bind(sort).bind(top25_frqs).printme()

# runtime calc
start_time = time.time()

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))
