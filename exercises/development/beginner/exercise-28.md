## Development - Beginner, exercise 28

### Text
Write down a small function in Python that takes in input a string and a non-negative integer and returns `True` if the character in the input string at the position indicated by the integer is a vowel, otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(s, i, expected):
    result = f(s, i)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, i):
    if i < len(s):
        return s[i] in "aeiou"
    else:
        return False


# Tests
print(test_f("ciao", 2, True))
print(test_f("ciao", 0, False))
print(test_f("ciao", 1, True))
print(test_f("ciao", 7, False))
``` 

### Additional material
The runnable [Python file](exercise_28.py) is available online.
