## Development - Beginner, exercise 3

### Text
Write down a small function in Python that checks if two integers `i1` and `i2` are both even, and in that case returns `True` – otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(i1, i2, expected):
    result = f(i1, i2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(i1, i2):
    return (i1 % 2) + (i2 % 2) == 0


# Tests
print(test_f(1, 3, False))
print(test_f(2, 3, False))
print(test_f(2, 4, True))
print(test_f(1, 4, False))
``` 

### Additional material
The runnable [Python file](exercise_3.py) is available online.
