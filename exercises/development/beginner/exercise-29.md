## Development - Beginner, exercise 29

### Text
Write down a small function in Python that takes in input two strings and returns `True` if they are identical, `False` if they are not identical but contains the same number of characters, otherwise it returns the shorter one.

### Solution
```python
# Test case for the function
def test_f(s, t, expected):
    result = f(s, t)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, t):
    if s == t:
        return True
    elif len(s) == len(t):
        return False
    elif len(s) < len(t):
        return s
    else:
        return t


# Tests
print(test_f("ciao", "ciao", True))
print(test_f("ciao", "oaic", False))
print(test_f("ciao", "me", "me"))
print(test_f("me", "ciao", "me"))
``` 

### Additional material
The runnable [Python file](exercise_29.py) is available online.
