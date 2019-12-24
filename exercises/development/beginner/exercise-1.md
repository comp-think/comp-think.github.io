## Development - Beginner, exercise 1

### Text
Write down a small function in Python that takes in input a string and returns the same string repeated twice (e.g. if the string `"mouse"` is used as input, the function will return `"mousemouse"`).

### Solution
```python
# Test case for the function
def test_f(string, expected):
    result = f(string)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(string):
    return string + string


# Tests
print(test_f("mouse", "mousemouse"))
print(test_f("let me ", "let me let me "))
print(test_f("", ""))
``` 

### Additional material
The runnable [Python file](exercise_1.py) is available online.
