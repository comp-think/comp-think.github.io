## Development - Beginner, exercise 19

### Text
Write down a small function in Python that takes in input two strings and returns a set containing the characters that are not contained in both the strings.

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

    for c in s1 + s2:
        if not (c in s1 and c in s2):
            result.add(c)

    return result


# Tests
print(test_f("", "", set()))
print(test_f("hello", "hello", set()))
print(test_f("hello", "", {"h", "e", "l", "o"}))
print(test_f("", "hello", {"h", "e", "l", "o"}))
print(test_f("hello", "hi", {"i", "e", "l", "o"}))
``` 

### Additional material
The runnable [Python file](exercise_19.py) is available online.
