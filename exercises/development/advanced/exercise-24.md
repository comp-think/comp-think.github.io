## Development - Advanced, exercise 24

### Text
The **Levenshtein distance** is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

The Levenshtein distance `lev(a, b)` between two strings `a` and `b` is `0` if one or both the strings are empty, and it is equal to `lev(a[1:], b[1:])` if the first characters of both the strings are the same. Otherwise, it is equal to `1` plus the minimum Levenshtein distance between these three cases:

* `lev(a[1:], b)`
* `lev(a, b[1:])`
* `lev(a[1:], b[1:])`

Write a recursive algorithm in Python – `def lev(a, b)` – which takes in input two strings `a` and `b`, and returns the Levenshtein distance.


### Solution
```python
# Test case for the function
def test_lev(a, b, expected):
    result = lev(a, b)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def lev(a, b):
    if a == "" or b == "":
        return 0
    elif a[0] == b[0]:
        return lev(a[1:], b[1:])
    else:
        lev_list = [
            lev(a[1:], b),
            lev(a, b[1:]),
            lev(a[1:], b[1:])
        ]
        lev_list.sort()
        return 1 + lev_list[0]


# Tests
print(test_lev("hello", "hello", 0))
print(test_lev("", "hello", 0))
print(test_lev("hello", "", 0))
print(test_lev("", "", 0))
print(test_lev("hella", "hello", 1))
print(test_lev("this", "hello", 3))
print(test_lev("door", "beard", 3))
``` 

### Additional material
The runnable [Python file](exercise_24.py) is available online.
