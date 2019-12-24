## Development - Beginner, exercise 10

### Text
Write down a small function in Python that takes in input a non-empty string `s` and a positive integer number `n` and returns a new string composed by the last character of the input string repeated `n` times.

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
    return s[len(s) - 1] * n


# Tests
print(test_f("anna", 5, "aaaaa"))
print(test_f("ron", 3, "nnn"))
print(test_f("hermione", 0, ""))
``` 

### Additional material
The runnable [Python file](exercise_10.py) is available online.
