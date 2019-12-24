## Development - Beginner, exercise 9

### Text
Write down a small function in Python that takes in input two strings and returns a set of all the characters they have in common.

### Solution
```python
# Test case for the function
def test_f(s1, s2, expected):
    result = f(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()

    for c in s1:
        if c in s2:
            result.add(c)

    return result


# Tests
print(test_f("anna", "elsa", {"a"}))
print(test_f("ron", "hermione", {"r", "o", "n"}))
print(test_f("", "hello", set()))
print(test_f("dad", "mum", set()))
``` 

### Additional material
The runnable [Python file](exercise_9.py) is available online.
