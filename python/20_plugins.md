# What's this?

`20_plugins.py` was added largely for the sake of completion, and I didn't want to implement it
as written because it's a more complicated style to set up.

See: https://github.com/crista/exercises-in-programming-style/tree/master/20-plugins

```
20-plugins/
|--plugins-src
    |--compile.sh
    |--frequencies1.py
    |--frequencies2.py
    |--words1.py
    |--words2.py
|--plugins
    |--frequencies1.pyc
    |--frequencies2.pyc
    |--words1.pyc
    |--words2.pyc
|--config.ini
|--tf-20.py
```

config.ini:
```
[Plugins]
;; Options: plugins/words1.pyc, plugins/words2.pyc
words = plugins/words1.pyc
;; Options: plugins/frequencies1.pyc, plugins/frequencies2.pyc
frequencies = plugins/frequencies1.pyc
```

tf-20.py:
```python
#!/usr/bin/env python
import sys, configparser, importlib.machinery

def load_plugins():
    config = configparser.ConfigParser()
    config.read("config.ini")
    words_plugin = config.get("Plugins", "words")
    frequencies_plugin = config.get("Plugins", "frequencies")
    global tfwords, tffreqs
    tfwords = importlib.machinery.SourcelessFileLoader('tfwords', words_plugin).load_module()
    tffreqs = importlib.machinery.SourcelessFileLoader('tffreqs', frequencies_plugin).load_module()

load_plugins()
word_freqs = tffreqs.top25(tfwords.extract_words(sys.argv[1]))

for (w, c) in word_freqs:
    print(w, '-', c)
```
