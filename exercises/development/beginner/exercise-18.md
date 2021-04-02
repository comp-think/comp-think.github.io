## Development - Beginner, exercise 18

### Text
Write down a small function in Python that takes in input two boolean values and implements the *xor* operation, which returns `True` only when one of the input boolean is `True` and the other is `False`, and returns `False` otherwise.

### Solution
```python
# Test case for the function
def test_f(n1, n2, b, expected):
    result = f(n1, n2, b)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(n1, n2, b):
    if b:
        return n1 * n2
    else:
        return n1 // n2


# Tests
print(test_f(2, 3, True, 6))
print(test_f(2, 3, False, 0))
print(test_f(3, 3, True, 9))
print(test_f(3, 3, False, 1))
``` 

### Additional material
The runnable [Python file](exercise_18.py) is available online.
