## Development - Beginner, exercise 13

### Text
Write down a small function in Python that takes in input a string and a boolean and return a list of the *vowel* characters (i.e. those matching with any of the following ones: `"a"`, `"e"`, `"i"`, `"o"`, `"u"`) in the input string if the input boolean is `True`, otherwise (i.e. the input boolean is `False`) it returns a list of the characters that are *not* vowels.

### Solution
```python
# Test case for the function
def test_f(s, b, expected):
    result = f(s, b)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, b):
    result = list()

    for c in s:
        if b and c in "aeiou":
            result.append(c)
        elif not b and c not in "aeiou":
            result.append(c)

    return result


# Tests
print(test_f("john doe", True, ["o", "o", "e"]))
print(test_f("john doe", False, ["j", "h", "n", " ", "d"]))
``` 

### Additional material
The runnable [Python file](exercise_13.py) is available online.
