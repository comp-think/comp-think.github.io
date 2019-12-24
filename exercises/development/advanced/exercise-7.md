## Development - Advanced, exercise 7

### Text
The *Rabin–Karp algorithm* is a very efficient approach, used for detecting plagiarism, that allows one to find whether a particular pattern string is contained in another input string. Instead of comparing character by character the pattern with the string, it computes the hash value of the pattern and compares it with the hash value of each substring of length equal to pattern. The hash value is calculated by means of an hash function that assigns a number to a particular string, so as to make number comparisons instead of character comparisons, which are less efficient. Of course, multiple executions of the hash function on the same string returns always the same number.

In practice, starting from the beginning of the input string, the algorithm compare the hash value of the pattern with the hash value of the *k* characters of the input string starting from the first one, where *k* is the length of the pattern string. If the two values do not match, then it compares the hash value of the pattern with the hash value of the *k* characters of the input string from the second one. And so on, until either it found a match or no matches were found.

Write a function in Python – `def rabin_karp(input, pattern)` – which implements the Rabin–Karp algorithm technique and returns True when a match is found, or False otherwise. The hash value can be calculated by means of the Python built-in function `def hash(s)`, which takes a string in input and returns an integer representing the hash value of the input string.

### Solution
```python
# Test case for the function
def test_rabin_karp(s, p, expected):
    result = rabin_karp(s, p)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def rabin_karp(input, pattern):
    pattern_hash = hash(pattern)
    pattern_length = len(pattern)
    for idx in range(len(input) - pattern_length + 1):
        s_hash = hash(input[idx:idx + pattern_length])
        if pattern_hash == s_hash:
            return True
    return False


# Tests
print(test_rabin_karp("This is a simple string", "a si", True))
print(test_rabin_karp("This is a simple string", "solo", False))
print(test_rabin_karp("This is a simple string", "simple s", True))
``` 

### Additional material
The runnable [Python file](exercise_7.py) is available online.
