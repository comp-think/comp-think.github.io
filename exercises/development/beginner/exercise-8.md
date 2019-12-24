## Development - Beginner, exercise 8

### Text
Write down a small function in Python that takes in input a string and a number and returns `True` if the division of the number of characters in the input string by the input number does not return any remainder, otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(s, n, expected):
    result = f(s, n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, n):
    return len(s) % n == 0


# Tests
print(test_f("good", 2, True))
print(test_f("hello", 2, False))
print(test_f("", 122, True))
``` 

### Additional material
The runnable [Python file](exercise_8.py) is available online.
