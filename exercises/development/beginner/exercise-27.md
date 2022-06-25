## Development - Beginner, exercise 27

### Text
Write down a small function in Python that takes in input an integer and returns `True` if it is divisible by 2, otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(i, expected):
    result = f(i)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(i):
    return i % 2 == 0


# Tests
print(test_f(2, True))
print(test_f(3, False))
print(test_f(0, True))
print(test_f(7, False))
print(test_f(108, True))
``` 

### Additional material
The runnable [Python file](exercise_27.py) is available online.
