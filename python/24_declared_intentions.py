import sys, re, operator, string, inspect, time

## Constraints
# - Existence of a type enforcer
# - functions declare what type of arguments they expect
# - if callers send arguments of unexpected types, type errors are raised and function isn't executed

# start runtime calc
start_time = time.time()

#
# Decorator for enforcing types of arguments in method calls
#
class AcceptTypes:
    def __init__(self, *args):
        self._args = args

    def __call__(self, f):
        def wrapped_f(*args):
            for i in range(len(self._args)):
                if type(args[i]) != self._args[i]:
                    raise TypeError(
                        "Expecting %s got %s" % (str(self._args[i]), str(type(args[i])))
                    )
            return f(*args)

        return wrapped_f


#
# The functions
#
@AcceptTypes(str)
def extract_words(path_to_file):
    with open(path_to_file) as f:
        str_data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    with open("../static/stop_words.txt") as f:
        stop_words = f.read().split(",")
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in stop_words]


@AcceptTypes(list)
def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


@AcceptTypes(dict)
def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


word_freqs = sort(frequencies(extract_words(sys.argv[1])))
for (w, c) in word_freqs[0:25]:
    print(w, "-", c)

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))
