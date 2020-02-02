## Development - Beginner, exercise 11

### Text
Write down a small function in Python that takes in input two strings and returns the set of all the digit characters they do not have in common.

### Solution
```python
# Test case for the function
def test_f(s, n, expected):
    result = f(s, n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()
    for d in "0123456789":
        if (d in s1 and d not in s2) or (d not in s1 and d in s2):
            result.add(d)
    return result


# Tests
print(test_f("alice", "bob", set()))
print(test_f("2 books and 1 pen", "trees and 2 apples", {"1"}))
print(test_f("odd number: 1, 3, 5, 7, 9", "even number: 2, 4, 6, 8", {"1", "2", "3", "4", "5", "6", "7", "8", "9"}))
print(test_f("odd number: 1, 3, 5, 7, 9", "prime number: 1, 2, 3, 5, 7", {"2", "9"}))
``` 

### Additional material
The runnable [Python file](exercise_11.py) is available online.
