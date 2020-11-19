## Development - Advanced, exercise 3

### Text
In information retrieval, the *term frequency–inverse document frequency* (or *tf-idf*) is a numerical statistic that is intended to reflect how important a word is to a document in a corpus. It is based on two functions:

* the *term frequency*, *tf(t, d)*, which counts the number of times a term *t* occurs in document *d*;
* the *inverse document frequency*, *idf(t, d_list)*, which measures whether a term *t* is common or rare across all the documents in a list *d_list*, calculated as the logarithm of the division between the total number of documents in the list and the number of documents that contains the term *t*. 

Thus, the *tf-idf* of a term *t* in a document *d* included in a collection of document *d_list* is simply the multiplication between its term frequency and its inverse document frequency.

Write the Python function `tfidf(t, d, d_list)` which takes as input a string `t` representing a term, a string `d` representing a document, and a list of strings `d_list` representing a collection of documents which includes also `d`, and that returns the *tf-idf* of the input term according to the document in that document list. As a simplification, all the input strings are composed only by lowercase English alphabetic characters with no punctuation. The logarithm function is available in Python within the module `math` (`from math import log`) and has the following signature: `def log(n)` – e.g. `log(3)` calculates the logarithm of the number 3.

### Solution
```python
from math import log


# Test case for the function
def test_tfidf(t, d, d_list, expected):
    result = tfidf(t, d, d_list)
    if expected == round(result, 2):
        return True
    else:
        return False


# Code of the function
def tfidf(t, d, d_list):
    return tf(t, d) * idf(t, d_list)


def tf(t, d):
    r = 0
    for term in d.split():
        if t == term:
            r += 1
    return r


def idf(t, d_list):
    d_with_t = 0
    for d in d_list:
        if t in d.split():
            d_with_t += 1
    return log(len(d_list) / d_with_t)


# Tests
d1 = "snow in my shoe abandoned sparrow's nest"
d2 = "whitecaps on the bay a broken signboard banging in the April wind"
d3 = "lily out of the water out of itself bass picking bugs off the moon"
d4 = "an aging willow its image unsteady in the flowing stream"
d5 = "just friends he watches my gauze dress blowing on the line"
d6 = "little spider will you outlive me"
d7 = "meteor shower a gentle wave wets our sandals"
d_list = [d1, d2, d3, d4, d5, d6, d7]

print(test_tfidf("a", d2, d_list, 1.25))
print(test_tfidf("out", d1, d_list, 0.0))
print(test_tfidf("out", d3, d_list, 3.89))
``` 

### Additional material
The runnable [Python file](exercise_3.py) is available online.
