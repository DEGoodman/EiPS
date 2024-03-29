import abc, sys, re, operator, string, time


## Constraints
# - larger problem decomposed in `abstract things` for the problem domain
# - each abstract thing is described by wjat operations the things of that
#     abstraction can do
# - concrete things are then bound to the abstractions (mechanisms vary)
# - the rest of the application uses the things, not by what they are,
#     but by what they do in the abstract

#
# The abstract things
#
class IDataStorage(metaclass=abc.ABCMeta):
    """Models the contents of the file"""

    @abc.abstractmethod
    def words(self):
        """Returns the words in storage"""
        pass


class IStopWordFilter(metaclass=abc.ABCMeta):
    """Models the stop word filter"""

    @abc.abstractmethod
    def is_stop_word(self):
        """Checks whether the given word is a stop word"""
        pass


class IWordFrequencyCounter(metaclass=abc.ABCMeta):
    """ " Keeps the word frequency data"""

    @abc.abstractmethod
    def increment_count(self, word):
        """ " Increments the count for the given word"""
        pass

    @abc.abstractmethod
    def sorted(self):
        """Returns the words and their frequencies, sorted by frequency"""
        pass


#
# The concrete things
#
class DataStorageManager:
    _data = ""

    def __init__(self, path_to_file):
        with open(path_to_file) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()
        self._data = "".join(self._data).split()

    def words(self):
        return self._data


class StopWordManager:
    _stop_words = []

    def __init__(self):
        with open("../static/stop_words.txt") as f:
            self._stop_words = f.read().split(",")
        self._stop_words.extend(list(string.ascii_lowercase))

    def is_stop_word(self, word):
        return word in self._stop_words


class WordFrequencyManager:
    _word_freqs = {}

    def increment_count(self, word):
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def sorted(self):
        return sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )


#
# The wiring between abstract things and concrete things
#
IDataStorage.register(subclass=DataStorageManager)
IStopWordFilter.register(subclass=StopWordManager)
IWordFrequencyCounter.register(subclass=WordFrequencyManager)


#
# The application object
#
class WordFrequencyController:
    def __init__(self, path_to_file):
        self._storage = DataStorageManager(path_to_file)
        self._stop_word_manager = StopWordManager()
        self._word_freq_counter = WordFrequencyManager()

    def run(self):
        for w in self._storage.words():
            if not self._stop_word_manager.is_stop_word(w):
                self._word_freq_counter.increment_count(w)

        word_freqs = self._word_freq_counter.sorted()
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
