## Development - Beginner, exercise 7

### Text
Write down a small function in Python that takes in input a function and two integers and returns `True` if the result of the execution of the input function using the first integer as its input is equal to the second integer, otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(fn, i1, i2, expected):
    result = f(fn, i1, i2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(fn, i1, i2):
    return fn(i1) == i2


# Tests
def my_f(i):
    return i * 2


print(test_f(my_f, 2, 4, True))
print(test_f(my_f, 2, 5, False))
print(test_f(my_f, 0, 0, True))
``` 

### Additional material
The runnable [Python file](exercise_7.py) is available online.
