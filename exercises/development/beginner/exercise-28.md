## Development - Beginner, exercise 28

### Text
Write down a small function in Python that takes in input a string and a non-negative integer and returns `True` if the character in the input string at the position indicated by the integer is a vowel, otherwise it returns `False`.

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
The runnable [Python file](exercise_28.py) is available online.
