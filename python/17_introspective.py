import sys, re, operator, string, inspect, time

## Constraints
# - The problem is decomposed using some form of abstraction
# - The abstractions have access to information about themselves and others,
#     although they cannot modify that information


def read_stop_words():
    """This function can only be called from a function
    named extract_words"""
    # Meta-level data: inspect.stack()
    if inspect.stack()[1][3] != "extract_words":
        return None

    with open("../static/stop_words.txt") as f:
        stop_words = f.read().split(",")
    stop_words.extend(list(string.ascii_lowercase))
    return stop_words


def extract_words(path_to_file):
    # Meta-level data: locals()
    with open(locals()["path_to_file"]) as f:
        str_data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    stop_words = read_stop_words()
    return [w for w in word_list if not w in stop_words]


def frequencies(word_list):
    # Meta-level data: locals()
    word_freqs = {}
    for w in locals()["word_list"]:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    # Meta-level data: locals()
    return sorted(
        # accesses arguments passed to a function via an introspective runtime structure 'locals()'
        locals()["word_freq"].items(),
        key=operator.itemgetter(1),
        reverse=True,
    )


def main():
    word_freqs = sort(frequencies(extract_words(sys.argv[1])))
    for (w, c) in word_freqs[0:25]:
        print(w, "-", c)


# runtime calc
start_time = time.time()

#
# The main function
#
if __name__ == "__main__":
    main()

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))
