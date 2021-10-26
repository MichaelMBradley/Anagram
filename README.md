# Anagram

Using primes to do various fun things with words.
When a script is run, it will repeatedly prompt for input text and will output anagrams until `*` is entered to end execution.
The wildcard character is `?`.

## Files

* `pureanagram.py` searches for perfect anagrams of an input word
* `scrabble.py` outputs words that can be formed by any number of letters from the input string (including wildcards!)
* `sentence.py` outputs sequences of words that can be formed from the input (e.g. `abc -> "ab c", "a bc"`)
  * Would not recommend running this one with larger word lists or input words much longer than 10 characters (it's fairly inefficient)
* `crossword.py` outputs words that fit a given sequence of wildcards and fixed characters (e.g. `D?N???U? -> DINOSAUR`)

## Words

While there are more word lists available on the internet that will work with this code (words can be capitalized, but must be seperated by newline), I have only included two with this code (plus the ability to find their intersection).
Be careful with how you select a word list as a larger list will have every word you might want to use, but it will also have many strings you may not consider words.
Alternatively, a smaller word list will be of high quality but may lack some common words.

* `words_alpha.txt` is sourced from [dwyl/english-words](https://github.com/dwyl/english-words), which was in turn sourced from InfoChimp
* `corncob_lowercase.txt` is sourced from [mieliestronk.com/wordlist.html](http://www.mieliestronk.com/wordlist.html)

## TODO

* finish writing test cases
* complete documentation
* implement custom errors (specifically wrt `sentence.py line 22`)
* make `sentence.py` run faster while I'm at it
* add more experiments?
* replace wildcard character?
