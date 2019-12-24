## Development - Beginner, exercise 5

### Text
Write down a small function in Python that takes in input a string `s` and a non-negative number `n` lesser than the length of the string, and return `True` if the character of `s` in position `n` is a vowel, otherwise it returns `False`.

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
def f(s, n):
    return s[n] in "aeiou"


# Tests
print(test_f("hello", 1, True))
print(test_f("hello", 3, False))
``` 

### Additional material
The runnable [Python file](exercise_5.py) is available online.
