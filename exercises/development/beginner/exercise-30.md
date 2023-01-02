## Development - Beginner, exercise 30

### Text
Write down a small function in Python that takes in input two integers and returns `0` if they are equal, `-1` if the first is divisible by the second (i.e. the rest of the division is `0`), `1` if the second is divisible by the first (i.e. the rest of the division is `0`), otherwise it returns `None`.

### Solution
```python
def test_f(x, y, expected):
    result = f(x, y)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(x, y):
    if x == y:
        return 0
    elif x % y == 0:
        return -1
    elif y % x == 0:
        return 1
    else: 
        return None


# Tests
print(test_f(5, 5, 0))
print(test_f(5, 10, 1))
print(test_f(10, 5, -1))
print(test_f(5, 7, None))
``` 

### Additional material
The runnable [Python file](exercise_30.py) is available online.
