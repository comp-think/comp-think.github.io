## Development - Beginner, exercise 24

### Text
Write down a small function in Python that takes in input two positive integers and returns the result of the division of the smaller one over the greater one.

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
    if i1 < i2:
        return i1 / i2
    else:
        return i2 / i1


# Tests
print(test_f(2, 4, 0.5))
print(test_f(4, 2, 0.5))
print(test_f(4, 4, 1))
``` 

### Additional material
The runnable [Python file](exercise_24.py) is available online.
