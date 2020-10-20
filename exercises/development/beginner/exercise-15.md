## Development - Beginner, exercise 15

### Text
Write down a small function in Python that takes in input two booleans and returns `True` if both are false, otherwise it returns `False`.

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
The runnable [Python file](exercise_15.py) is available online.
