## Development - Beginner, exercise 16

### Text
Write down a small function in Python that takes in input a boolean and an integer and returns `True` if the input boolean is `True` and the input integer is an even number, while it returns `False` otherwise.

### Solution
```python
# Test case for the function
def test_f(b1, b2, expected):
    result = f(b1, b2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(b1, b2):
    return not (b1 or b2)


# Tests
print(test_f(True, True, False))
print(test_f(True, False, False))
print(test_f(False, True, False))
print(test_f(False, False, True))
``` 

### Additional material
The runnable [Python file](exercise_16.py) is available online.
