## Development - Beginner, exercise 20

### Text
Write down a small function in Python that takes in input a string, an integer, and a boolean, and returns the character of the string at the index specified by the input integer if the input boolean is True, otherwise it returns the last character in the input string.

### Solution
```python
# Test case for the function
def test_f(s, i, b, expected):
    result = f(s, i, b)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, i, b):
    if b:
        return s[i]
    else:
        return s[-1]


# Tests
print(test_f("hello", 0, True, "h"))
print(test_f("hello", 0, False, "o"))
print(test_f("hello", 2, True, "l"))
print(test_f("hello", 2, False, "o"))
``` 

### Additional material
The runnable [Python file](exercise_20.py) is available online.
