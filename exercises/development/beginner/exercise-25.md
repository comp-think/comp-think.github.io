## Development - Beginner, exercise 25

### Text
Write down a small function in Python that in input a string `s` and a number `n` and returns the character at index `n` in the string `s` if it exists, otherwise it returns `None`.

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
    if n < len(s):
        return s[n]
    else:
        return None


# Tests
print(test_f("ciao", 4, None))
print(test_f("ciao", 0, "c"))
print(test_f("ciao", 2, "a"))
print(test_f("ciao", 7, None))
``` 

### Additional material
The runnable [Python file](exercise_25.py) is available online.
