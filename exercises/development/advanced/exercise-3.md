## Development - Advanced, exercise 3

### Text
In information retrieval, the *term frequency–inverse document frequency* (or *tf-idf*) is a numerical statistic that is intended to reflect how important a word is to a document in a corpus. It is based on two functions:

* the *term frequency*, *tf(t, d)*, which counts the number of times a term *t* occurs in document *d*;
* the *inverse document frequency*, *idf(t, d_list)*, which measures whether a term *t* is common or rare across all the documents in a list *d_list*, calculated as the logarithm of the division between the total number of documents in the list and the number of documents that contains the term *t*. 

Thus, the *tf-idf* of a term *t* in a document *d* included in a collection of document *d_list* is simply the multiplication between its term frequency and its inverse document frequency.

Write the Python function `tfidf(t, d, d_list)` which takes as input a string `t` representing a term, a string `d` representing a document, and a list of strings `d_list` representing a collection of documents which includes also `d`, and that returns the *tf-idf* of the input term according to the document in that document list. As a simplification, all the input strings are composed only by lowercase English alphabetic characters with no punctuation. The logarithm function is available in Python within the module `math` (`from math import log`) and has the following signature: `def log(n)` – e.g. `log(3)` calculates the logarithm of the number 3.

### Solution
```python
# Test case for the function
def test_hamming_distance(s1, s2, expected):
    result = hamming_distance(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def hamming_distance(s1, s2):
    if len(s1) < len(s2):
        return s1
    elif len(s1) > len(s2):
        return s2
    else:
        result = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                result = result + 1
        return result


# Tests
print(test_hamming_distance("Silvio", "Peroni", 6))
print(test_hamming_distance("Silvio", "Silvia", 1))
print(test_hamming_distance("Silvio", "Giovanni", "Silvio"))
print(test_hamming_distance("Silvio", "John", "John"))
``` 

### Additional material
The runnable [Python file](exercise_3.py) is available online.
