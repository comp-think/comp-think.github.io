## Development - Advanced, exercise 5

### Text
The *MostFreqKHashing* is a string hashing technique that takes as input a string *s* and an integer *k* and returns the most frequent *k* characters from the input string *s*.

Write the Python function `def k_hash(s, k)` which implements the *MostFreqKHashing* hashing technique and returns the set of the most frequent `k` characters. In case multiple characters have the same frequency, get the one that occurs first in `s`.

### Solution
```python
# Test case for the function
def test_k_hash(s, k, expected):
    result = k_hash(s, k)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def k_hash(s, k):
    result = set()

    d = dict()

    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1

    for idx in range(k):
        cur_best = None
        cur_char = None
        for k, v in d.items():
            if cur_best is None or v > cur_best:
                cur_best = v
                cur_char = k

        if cur_char is not None:
            result.add(cur_char)
            del d[cur_char]

    return result


# Tests
print(test_k_hash("What is the use of a book without pictures or conversations?", 3, {" ", "o", "t"}))
print(test_k_hash("old pond"
                  "frog leaps in"
                  "water's sound", 2, {" ", "o"}))
print(test_k_hash("It is an ancient Mariner,"
                  "And he stoppeth one of three."
                  "'By thy long grey beard and glittering eye,"
                  "Now wherefore stopp'st thou me?", 5, {" ", "e", "t", "n", "r"}))
``` 

### Additional material
The runnable [Python file](exercise_5.py) is available online.
