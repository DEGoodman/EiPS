import sys, re, operator, string, time
from abc import ABCMeta


## Constraints
# - The larger problem is decomposed into _things_ that make sense
#   for the problem domain.
# - Each _thing_ is a capsule of data that exposes procedures to the
#   the rest of the world.
# - Data is never accessed directly, only through these procedures.
# - Capsules can reappropriate procedues defined in other capsules.


class TFExercise:
    _metaclass_ = ABCMeta

    def info(self):
        return self.__class__.__name__


class DataStorageManager(TFExercise):
    """Models the contents of the file"""

    def __init__(self, path_to_file):
        with open(path_to_file) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def words(self):
        """Returns the list words in storage"""
        return self._data.split()

    def info(self):
        return (
            super(DataStorageManager, self).info()
            + ": My\
            major data structure is a "
            + self._data.__class__.__name__
        )


class StopWordManager(TFExercise):
    """Models the stop word filter"""

    def __init__(self):
        with open("../static/stop_words.txt") as f:
            self._stop_words = f.read().split(",")
        # add single-letter words
        self._stop_words.extend(list(string.ascii_lowercase))

    def is_stop_word(self, word):
        return word in self._stop_words

    def info(self):
        return (
            super(StopWordManager, self).info()
            + ": My major\
            data structure is a "
            + self._stop_words.__class__.__name__
        )


class WordFrequencyManager(TFExercise):
    """Keeps the word frequency data"""

    def __init__(self):
        self._word_freqs = {}

    def increment_count(self, word):
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def sorted(self):
        return sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )

    def info(self):
        return (
            super(WordFrequencyManager, self).info()
            + ": My\
            major data structure is a "
            + self._word_freqs.__class__.__name__
        )


class WordFrequencyController(TFExercise):
    def __init__(self, path_to_file):
        self._storage_manager = DataStorageManager(path_to_file)
        self._stop_word_manager = StopWordManager()
        self._word_freq_manager = WordFrequencyManager()

    def run(self):
        for w in self._storage_manager.words():
            if not self._stop_word_manager.is_stop_word(w):
                self._word_freq_manager.increment_count(w)

        word_freqs = self._word_freq_manager.sorted()
        for (w, c) in word_freqs[0:25]:
            print(w, "-", c)


# runtime calc
start_time = time.time()

#
# The main function
#

WordFrequencyController(sys.argv[1]).run()

# final runtime calc
print("--- %s seconds ---" % (time.time() - start_time))
