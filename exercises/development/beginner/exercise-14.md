## Development - Beginner, exercise 14

### Text
Write down a small function in Python that takes in input two numbers and returns `True` if their subtraction is an even number, otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(n1, n2, expected):
    result = f(n1, n2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(n1, n2):
    return (n1 - n2) % 2 == 0


# Tests
print(test_f(2, 1, False))
print(test_f(2, 4, True))
``` 

### Additional material
The runnable [Python file](exercise_14.py) is available online.
