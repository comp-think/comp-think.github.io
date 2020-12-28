## Development - Beginner, exercise 16

### Text
Write down a small function in Python that takes in input a boolean and an integer and returns `True` if the input boolean is `True` and the input integer is an even number, while it returns `False` otherwise.

### Solution
```python
# Test case for the function
def test_f(b, n, expected):
    result = f(b, n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(b, n):
    return b and n % 2 == 0


# Tests
print(test_f(True, 3, False))
print(test_f(True, 4, True))
print(test_f(False, 3, False))
print(test_f(False, 4, False))
``` 

### Additional material
The runnable [Python file](exercise_16.py) is available online.
